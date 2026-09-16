import os
import sys
from pathlib import Path

# Ensure workspace root is in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import json
import numpy as np
import pandas as pd
from typing import Dict, Any, Optional, Tuple

from src.data.drive_downloader import (
    initialize_dataset_directories,
    prepare_benchmark_dataset,
    is_synthetic_path,
    BENCHMARK_DATASET_METADATA
)
from src.data.cleaner import clean_dataset, clean_column_names
from src.data.splitters import (
    AntiLeakageGroupKFold,
    extract_subnet_mask,
    fit_fold_isolated_pipeline,
    safe_slice
)
from src.data.graph_builder import (
    build_networkx_flow_graph,
    export_to_pyg_tensors
)

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_preparation_pipeline(
    dataset_name: str = "CICIDS2017",
    base_dir: str | Path = ".",
    raw_data_dir: Optional[str | Path] = None,
    prefer_sample: bool = False,
    n_splits: int = 5,
    build_graphs: bool = True,
    *args,
    **kwargs
) -> Dict[str, Any]:
    """Execute complete ingestion, cleaning, anti-leakage splitting, and artifact generation from provided structure."""
    dirs = initialize_dataset_directories(base_dir)
    print(f"\n==========================================")
    print(f"🚀 Launching Prep Pipeline for: {dataset_name}")
    print(f"==========================================")
    
    # 1. Ingestion from provided structure (Zero remote downloads)
    try:
        raw_path = prepare_benchmark_dataset(
            dataset_name, base_dir=base_dir, raw_data_dir=raw_data_dir, prefer_sample=prefer_sample
        )
    except TypeError:
        raw_path = prepare_benchmark_dataset(
            dataset_name, base_dir=base_dir, prefer_sample=prefer_sample
        )
    print(f"📄 Ingesting raw file: {raw_path}...")
    
    if str(raw_path).endswith(".parquet"):
        try:
            df_raw = pd.read_parquet(raw_path)
        except ImportError:
            # Fallback to csv if paired csv exists
            csv_alt = raw_path.with_suffix(".csv")
            if csv_alt.exists():
                df_raw = pd.read_csv(csv_alt)
            else:
                raise
    else:
        # Handles CSV or space/comma separated text files (NSL-KDD)
        try:
            df_raw = pd.read_csv(raw_path)
        except Exception:
            df_raw = pd.read_csv(raw_path, sep=r'\s+|,', engine='python')
            
    print(f"📊 Raw shape: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns.")
    
    # 2. Decontamination & Harmonization
    print("🧹 Executing decontamination suite...")
    df_clean, clean_stats = clean_dataset(df_raw, dataset_name)
    
    # 3. Export Cleaned Data
    processed_file = dirs["processed"] / f"{dataset_name}_cleaned.parquet"
    try:
        df_clean.to_parquet(processed_file, index=False)
        print(f"💾 Cleaned dataset saved to: {processed_file}")
    except (ImportError, Exception) as e:
        processed_file = dirs["processed"] / f"{dataset_name}_cleaned.csv"
        df_clean.to_csv(processed_file, index=False)
        print(f"💾 Cleaned dataset saved (CSV fallback) to: {processed_file}")
    
    # 4. Anti-Leakage Partitioning
    print(f"🛡️ Generating Anti-Leakage {n_splits}-Fold CV Partitions...")
    ip_candidates = ["source_ip", "src_ip", "srcip", "sourceip"]
    src_ip_col = None
    for candidate in ip_candidates:
        if candidate in df_clean.columns:
            src_ip_col = candidate
            break
            
    if src_ip_col:
        subnets = extract_subnet_mask(df_clean[src_ip_col], mask_prefix_len=24)
        print(f"🌐 Extracted {subnets.nunique()} unique subnet blocks from '{src_ip_col}'.")
    else:
        # Fallback to temporal / sequential chunk blocks if IP address column absent
        print("ℹ️ Source IP column not found; creating sequential temporal blocks for group partitioning.")
        subnets = pd.Series(np.arange(len(df_clean)) // (max(len(df_clean) // (n_splits * 4), 1)))
        
    gkf = AntiLeakageGroupKFold(n_splits=n_splits)
    target_col = "is_attack" if "is_attack" in df_clean.columns else df_clean.columns[-1]
    feature_cols = [c for c in df_clean.select_dtypes(include=[np.number]).columns if c != target_col]
    
    X = df_clean[feature_cols].values
    y = df_clean[target_col].values
    
    fold_splits = []
    for fold_idx, (train_idx, val_idx) in enumerate(gkf.split(X, y, groups=subnets)):
        fold_splits.append({
            "fold": fold_idx + 1,
            "train_indices_count": int(len(train_idx)),
            "val_indices_count": int(len(val_idx)),
            "val_attack_ratio": float(np.mean(y[val_idx])) if len(val_idx) > 0 else 0.0
        })
        
    is_synthetic = is_synthetic_path(raw_path)
    data_provenance = "SYNTHETIC_FALLBACK" if is_synthetic else "REAL_DATASET"

    # Save fold assignments metadata
    splits_meta_file = dirs["processed"] / f"{dataset_name}_splits_meta.json"
    with open(splits_meta_file, "w", encoding="utf-8") as f:
        json.dump({
            "dataset": dataset_name,
            "is_synthetic": is_synthetic,
            "data_provenance": data_provenance,
            "raw_source_file": str(raw_path),
            "n_splits": n_splits,
            "feature_cols": feature_cols,
            "target_col": target_col,
            "clean_stats": clean_stats,
            "folds": fold_splits
        }, f, indent=2)
    print(f"📋 Partition metadata serialized to: {splits_meta_file}")
    
    # 5. Graph Representation for GraphIDS
    graph_info = None
    if build_graphs:
        dst_candidates = ["destination_ip", "dst_ip", "dstip", "destip"]
        dst_ip_col = None
        for candidate in dst_candidates:
            if candidate in df_clean.columns:
                dst_ip_col = candidate
                break
                
        if src_ip_col and dst_ip_col:
            print("🕸️ Constructing NetworkX interaction multigraph for GraphIDS...")
            # Use representative sample slice for fast graph compilation
            graph_df = df_clean.head(1000)
            G = build_networkx_flow_graph(
                graph_df,
                src_ip_col=src_ip_col,
                dst_ip_col=dst_ip_col,
                label_col=target_col,
                feature_cols=feature_cols[:4]
            )
            pyg_tensors = export_to_pyg_tensors(G)
            graph_info = {
                "nodes": pyg_tensors["num_nodes"],
                "edges": int(pyg_tensors["edge_index"].shape[1])
            }
            print(f"🕸️ Flow graph compiled: {graph_info['nodes']} nodes, {graph_info['edges']} edges.")
            
    print(f"\n==========================================")
    status_icon = "⚠️" if is_synthetic else "🛡️"
    print(f"{status_icon} Prep Pipeline Completed: {dataset_name} [{data_provenance}]")
    print(f"📁 Output file: {processed_file}")
    print(f"==========================================\n")

    return {
        "dataset_name": dataset_name,
        "is_synthetic": is_synthetic,
        "data_provenance": data_provenance,
        "raw_source_file": str(raw_path),
        "processed_file": str(processed_file),
        "metadata_file": str(splits_meta_file),
        "clean_stats": clean_stats,
        "fold_splits": fold_splits,
        "graph_info": graph_info,
        "raw_shape": (int(df_raw.shape[0]), int(df_raw.shape[1])),
        "cleaned_shape": (int(df_clean.shape[0]), int(df_clean.shape[1]))
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ingest, decontaminate, and partition benchmark datasets.")
    parser.add_argument("--dataset", type=str, default="CICIDS2017", help="Dataset name (CICIDS2017, UNSW-NB15, TON_IoT, CIC-DDoS2019, NSL-KDD)")
    parser.add_argument("--base-dir", type=str, default=".", help="Project base directory")
    parser.add_argument("--prefer-sample", action="store_true", help="Force synthetic sample generation instead of looking for real files")
    parser.add_argument("--n-splits", type=int, default=5, help="Number of cross-validation folds")
    parser.add_argument("--no-graphs", action="store_true", help="Skip PyG flow graph generation")
    args = parser.parse_args()

    result = run_preparation_pipeline(
        dataset_name=args.dataset,
        base_dir=args.base_dir,
        prefer_sample=args.prefer_sample,
        n_splits=args.n_splits,
        build_graphs=not args.no_graphs
    )
    print("Execution Summary:", json.dumps({k: v for k, v in result.items() if k != "clean_stats"}, indent=2))


"""Streaming & Chunked Data Loader for Industrial High-Throughput Track B (N >= 100k).
Manages memory-bounded chunk iteration to prevent Google Colab 12.7GB host RAM exhaustion.
"""
import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Iterator, Tuple, Dict, Any, Optional

from src.data.drive_downloader import (
    initialize_dataset_directories,
    prepare_benchmark_dataset,
    is_synthetic_path
)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

class StreamingChunkLoader:
    """Memory-efficient streaming chunk iterator for large-scale NetFlow partitions."""

    def __init__(
        self,
        filepath: str | Path,
        chunk_size: int = 50000,
        target_col: str = "is_attack",
        feature_cols: Optional[list] = None
    ):
        self.filepath = Path(filepath)
        self.chunk_size = chunk_size
        self.target_col = target_col
        self.feature_cols = feature_cols

    def iter_chunks(self, max_total_records: Optional[int] = None) -> Iterator[Tuple[np.ndarray, np.ndarray]]:
        """Yield (X_chunk, y_chunk) in bounded batches."""
        if not self.filepath.exists():
            raise FileNotFoundError(f"Data file not found: {self.filepath}")

        is_parquet = str(self.filepath).endswith(".parquet")
        total_yielded = 0

        if is_parquet:
            # Chunked parquet reading via pyarrow or pandas batching
            try:
                import pyarrow.parquet as pq  # type: ignore
                parquet_file = pq.ParquetFile(self.filepath)
                for batch in parquet_file.iter_batches(batch_size=self.chunk_size):
                    df_chunk = batch.to_pandas()
                    X_c, y_c = self._extract_features_and_target(df_chunk)
                    
                    if max_total_records and (total_yielded + len(X_c)) > max_total_records:
                        limit = max_total_records - total_yielded
                        yield X_c[:limit], y_c[:limit]
                        break
                    
                    yield X_c, y_c
                    total_yielded += len(X_c)
                    if max_total_records and total_yielded >= max_total_records:
                        break
            except (ImportError, Exception):
                # If pyarrow fails, try reading paired CSV if it exists
                csv_fallback = self.filepath.with_suffix(".csv")
                if csv_fallback.exists():
                    for df_chunk in pd.read_csv(csv_fallback, chunksize=self.chunk_size):
                        X_c, y_c = self._extract_features_and_target(df_chunk)
                        if max_total_records and (total_yielded + len(X_c)) > max_total_records:
                            limit = max_total_records - total_yielded
                            yield X_c[:limit], y_c[:limit]
                            break
                        yield X_c, y_c
                        total_yielded += len(X_c)
                        if max_total_records and total_yielded >= max_total_records:
                            break
                    return
                else:
                    df_full = pd.read_parquet(self.filepath)
                    for start_idx in range(0, len(df_full), self.chunk_size):
                        df_chunk = df_full.iloc[start_idx:start_idx + self.chunk_size]
                        X_c, y_c = self._extract_features_and_target(df_chunk)
                        if max_total_records and (total_yielded + len(X_c)) > max_total_records:
                            limit = max_total_records - total_yielded
                            yield X_c[:limit], y_c[:limit]
                            break
                        yield X_c, y_c
                        total_yielded += len(X_c)
                        if max_total_records and total_yielded >= max_total_records:
                            break
        else:
            # CSV chunked iterator
            for df_chunk in pd.read_csv(self.filepath, chunksize=self.chunk_size):
                X_c, y_c = self._extract_features_and_target(df_chunk)
                if max_total_records and (total_yielded + len(X_c)) > max_total_records:
                    limit = max_total_records - total_yielded
                    yield X_c[:limit], y_c[:limit]
                    break
                yield X_c, y_c
                total_yielded += len(X_c)
                if max_total_records and total_yielded >= max_total_records:
                    break

    def _extract_features_and_target(self, df_chunk: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        target = self.target_col if self.target_col in df_chunk.columns else df_chunk.columns[-1]
        if self.feature_cols:
            features = [c for c in self.feature_cols if c in df_chunk.columns]
        else:
            features = [c for c in df_chunk.select_dtypes(include=[np.number]).columns if c != target]

        X = df_chunk[features].values
        # Harmonize target label to binary 0/1 if string object
        if df_chunk[target].dtype == object:
            y = (~df_chunk[target].astype(str).str.strip().str.upper().isin(["BENIGN", "0", "NORMAL"])).astype(int).values
        else:
            y = pd.to_numeric(df_chunk[target], errors="coerce").fillna(0).astype(int).values

        # Clean NaN and infinite values in features
        X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
        return X, y

def generate_scalable_synthetic_partition(
    output_path: str | Path,
    n_samples: int = 100000,
    n_features: int = 20,
    seed: int = 42
) -> Path:
    """Quickly synthesize large-scale streaming NetFlow benchmark partition for Track B testing."""
    np.random.seed(seed)
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    chunk_size = 50000
    first_chunk = True
    
    for i in range(0, n_samples, chunk_size):
        current_chunk_len = min(chunk_size, n_samples - i)
        X_chunk = np.random.randn(current_chunk_len, n_features).astype(np.float32)
        # Linear separable boundary with 15% attack prevalence
        logits = X_chunk[:, 0] * 1.5 - X_chunk[:, 1] * 0.8 + np.random.randn(current_chunk_len) * 0.5
        y_chunk = (logits > 1.0).astype(int)
        
        chunk_dict = {f"flow_feat_{f}": X_chunk[:, f] for f in range(n_features)}
        chunk_dict["is_attack"] = y_chunk
        df_chunk = pd.DataFrame(chunk_dict)
        
        mode = "w" if first_chunk else "a"
        header = first_chunk
        df_chunk.to_csv(output_file, mode=mode, header=header, index=False)
        first_chunk = False

    print(f"📊 Scalable partition ({n_samples} records) synthesized at: {output_file}")
    return output_file

def resolve_track_b_dataset(
    base_dir: str | Path = ".",
    dataset_name: str = "CICIDS2017",
    target_samples: int = 100000
) -> Tuple[Path, bool]:
    """Resolve the dataset file for Track B streaming benchmark: prefers real data, falls back to synthetic.

    Returns:
        Tuple[Path, bool]: (filepath, is_synthetic)
    """
    root = Path(base_dir)
    dirs = initialize_dataset_directories(root)
    proc_dir = dirs["processed"]
    raw_dir = dirs["raw"]

    # 1. Search for real cleaned files first
    cleaned_candidates = [
        proc_dir / f"{dataset_name}_cleaned.parquet",
        proc_dir / f"{dataset_name}_cleaned.csv",
        raw_dir / f"{dataset_name}.csv",
        raw_dir / f"{dataset_name.lower()}.csv",
    ]

    for cand in cleaned_candidates:
        if cand.exists() and not is_synthetic_path(cand) and cand.stat().st_size > 0:
            print("\n" + "=" * 80)
            print(f"🛡️ [TRACK B STREAMING STATUS: REAL DECONTAMINATED DATA ACTIVE]")
            print(f"📁 Source: {cand.resolve()}")
            print(f"📊 Dataset: {dataset_name} (Authentic Reference Flows)")
            print(f"✅ Streaming benchmark will profile real network traffic.")
            print("=" * 80 + "\n")
            return cand, False

    # 2. Check for real authentic raw dataset files using prepare_benchmark_dataset
    try:
        raw_benchmark_file = prepare_benchmark_dataset(dataset_name, base_dir=base_dir, prefer_sample=False)
        if raw_benchmark_file.exists() and not is_synthetic_path(raw_benchmark_file):
            print("\n" + "=" * 80)
            print(f"🛡️ [TRACK B STREAMING STATUS: REAL AUTHENTIC RAW DATA ACTIVE]")
            print(f"📁 Source: {raw_benchmark_file.resolve()}")
            print(f"📊 Dataset: {dataset_name} (Authentic Reference NetFlows)")
            print(f"✅ Streaming benchmark will profile real network traffic directly.")
            print("=" * 80 + "\n")
            return raw_benchmark_file, False
    except Exception:
        pass

    # 3. If real data not found, use/generate synthetic partition
    synthetic_file = proc_dir / f"track_b_{target_samples // 1000}k_synthetic.csv"
    if not synthetic_file.exists():
        generate_scalable_synthetic_partition(synthetic_file, n_samples=target_samples)

    print("\n" + "=" * 80)
    print(f"⚠️ [TRACK B STREAMING STATUS: SYNTHETIC FALLBACK DATA ACTIVE]")
    print(f"❌ Real dataset not found in '{proc_dir}' or '{raw_dir}'.")
    print(f"📊 Streaming from synthetic partition: {synthetic_file.name}")
    print(f"📌 TO USE REAL DATA: Upload authentic dataset (e.g. into data/raw/MachineLearningCVE/) and run Phase 1.")
    print("=" * 80 + "\n")
    return synthetic_file, True


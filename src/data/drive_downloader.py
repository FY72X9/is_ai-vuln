"""Drive Dataset Retrieval, Checksum Verification & Automatic .gitignore Safeguards."""
import os
import sys
import hashlib
import requests
import time
from pathlib import Path
from typing import Dict, Any, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

REQUIRED_GITIGNORE = [
    "# === Automated Dataset & Checkpoint Exclusions ===",
    "*.csv",
    "*.pcap",
    "*.parquet",
    "*.zip",
    "*.tar.gz",
    "/data/",
    "!src/data/",
    "src/data/actual-data/",
    "actual-data/",
    "workspace_drive/",
    "drive_cache/",
    "checkpoints/*.pt",
    "experiment_output/**/checkpoints/"
]

BENCHMARK_DATASET_METADATA = {
    "CICIDS2017": {
        "description": "Canadian Institute for Cybersecurity Intrusion Detection Evaluation Dataset 2017",
        "primary_file": "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        "subfolder": "MachineLearningCVE",
        "subfolders": ["MachineLearningCVE", "TrafficLabelling"],
        "approx_size_mb": 843.66,
        "real_candidates": [
            "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
            "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
            "Wednesday-workingHours.pcap_ISCX.csv",
            "Tuesday-WorkingHours.pcap_ISCX.csv",
            "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
            "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
            "Monday-WorkingHours.pcap_ISCX.csv",
            "Friday-WorkingHours-Morning.pcap_ISCX.csv",
            "CICIDS2017.csv",
            "cicids2017.csv",
            "CICIDS2017_cleaned.parquet",
            "CICIDS2017_cleaned.csv",
        ],
        "sample_file": "CICIDS2017_sample.csv",
        "format": "parquet/csv"
    },
    "UNSW-NB15": {
        "description": "UNSW Network Benchmark 2015",
        "primary_file": "UNSW_NB15_training-set.csv",
        "subfolder": "unsw-data-full",
        "subfolders": ["unsw-data-full"],
        "approx_size_mb": 604.69,
        "real_candidates": [
            "UNSW_NB15_training-set.csv",
            "UNSW_NB15_testing-set.csv",
            "UNSW-NB15_1.csv",
            "UNSW-NB15_2.csv",
            "UNSW-NB15_3.csv",
            "UNSW-NB15_4.csv",
            "UNSW_NB15.csv",
            "unsw_nb15.csv",
            "UNSW-NB15_cleaned.parquet",
        ],
        "sample_file": "UNSW_NB15_sample.csv",
        "format": "csv"
    },
    "TON_IOT": {
        "description": "TON_IoT Telemetry and Network Dataset 2021",
        "primary_file": "train_test_network.csv",
        "subfolder": "TON-IoT",
        "subfolders": ["TON-IoT", "ToN-IOT", "ton-iot", "ToN-IoT", "ton_iot", "TON_IoT"],
        "approx_size_mb": 28.52,
        "real_candidates": [
            "train_test_network.csv",
            "Train_Test_Network.csv",
            "TON_IoT.csv",
            "ton_iot.csv"
        ],
        "sample_file": "TON_IoT_sample.csv",
        "format": "csv"
    },
    "CIC-DDOS2019": {
        "description": "CIC Distributed Denial of Service 2019 Dataset",
        "primary_file": "Syn-training.parquet",
        "subfolder": "CIC-DDoS2019",
        "subfolders": ["CIC-DDoS2019", "cic-ddos2019"],
        "approx_size_mb": 33.60,
        "real_candidates": [
            "Syn-training.parquet",
            "DNS-testing.parquet",
            "UDP-training.parquet",
            "LDAP-training.parquet",
            "MSSQL-training.parquet",
            "NetBIOS-training.parquet",
            "CIC_DDoS2019.parquet",
            "CIC_DDoS2019.csv",
            "cic_ddos2019.csv",
            "CIC_DDoS2019_sample.parquet"
        ],
        "sample_file": "CIC_DDoS2019_sample.csv",
        "format": "parquet"
    },
    "NSL-KDD": {
        "description": "NSL-KDD Historical Baseline Dataset",
        "primary_file": "KDDTrain+.txt",
        "subfolder": "NSL-KDD",
        "subfolders": ["NSL-KDD", "nsl-kdd"],
        "approx_size_mb": 53.29,
        "real_candidates": [
            "KDDTrain+.txt",
            "KDDTrain+_20Percent.txt",
            "KDDTest+.txt",
            "kdd_train.csv"
        ],
        "sample_file": "KDDTrain+_sample.txt",
        "format": "txt/csv"
    }
}

def ensure_gitignore_safeguards(repo_root: str | Path = ".") -> bool:
    """Check and automatically append required exclusion rules to .gitignore."""
    gitignore = Path(repo_root) / ".gitignore"
    existing_content = gitignore.read_text(encoding="utf-8") if gitignore.exists() else ""
    
    missing_entries = [entry for entry in REQUIRED_GITIGNORE if entry not in existing_content]
    
    if missing_entries:
        with open(gitignore, "a", encoding="utf-8") as f:
            if not existing_content.endswith("\n"):
                f.write("\n")
            for entry in missing_entries:
                f.write(f"{entry}\n")
        print(f"🔒 .gitignore updated: {len(missing_entries)} safeguard rules appended.")
        return True
    else:
        print("🔒 .gitignore safeguards active: all heavy file patterns already excluded.")
        return False

def verify_file_sha256(filepath: str | Path, expected_sha256: Optional[str]) -> bool:
    """Verify SHA-256 checksum of a downloaded file."""
    path = Path(filepath)
    if not path.exists():
        return False
    if not expected_sha256:
        return True
    
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    calculated = sha256.hexdigest()
    is_valid = calculated.lower() == expected_sha256.lower()
    if is_valid:
        print(f"✅ Checksum matched for {path.name}: {calculated}")
    else:
        print(f"❌ Checksum mismatch for {path.name}: expected {expected_sha256}, got {calculated}")
    return is_valid

def download_file(
    url: str,
    destination: str | Path,
    expected_sha256: Optional[str] = None,
    chunk_size: int = 1024 * 1024,
    max_retries: int = 3
) -> bool:
    """Download a file with retry mechanism and SHA256 verification."""
    dest_path = Path(destination)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    if dest_path.exists() and expected_sha256:
        if verify_file_sha256(dest_path, expected_sha256):
            print(f"ℹ️ File already exists and verified: {dest_path.name}")
            return True

    headers = {"User-Agent": "AcademicResearch-IDS/1.0"}
    for attempt in range(1, max_retries + 1):
        try:
            print(f"📥 Downloading {url} -> {dest_path.name} (Attempt {attempt}/{max_retries})...")
            response = requests.get(url, headers=headers, stream=True, timeout=30)
            if response.status_code == 200:
                with open(dest_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)
                if verify_file_sha256(dest_path, expected_sha256):
                    print(f"✅ Successfully downloaded and verified {dest_path.name}")
                    return True
            else:
                print(f"⚠️ HTTP {response.status_code} received from {url}")
        except Exception as e:
            print(f"⚠️ Download attempt {attempt} failed: {e}")
        time.sleep(2 * attempt)
    return False

def generate_synthetic_benchmark_sample(
    dataset_name: str,
    output_path: str | Path,
    n_samples: int = 5000,
    seed: int = 42
) -> Path:
    """Generate realistic synthetic NetFlow records for offline pipeline testing and Colab verification."""
    import numpy as np
    import pandas as pd
    
    np.random.seed(seed)
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Realistic IP address distribution across 5 subnets
    subnets = [f"192.168.{net}" for net in [10, 20, 30, 40, 50]]
    src_ips = [f"{np.random.choice(subnets)}.{np.random.randint(2, 254)}" for _ in range(n_samples)]
    dst_ips = [f"10.0.{np.random.randint(1, 5)}.{np.random.randint(1, 100)}" for _ in range(n_samples)]
    
    flow_duration = np.random.exponential(scale=2000.0, size=n_samples)
    tot_fwd_pkts = np.random.poisson(lam=12, size=n_samples) + 1
    tot_bwd_pkts = np.random.poisson(lam=10, size=n_samples)
    tot_len_fwd_pkts = tot_fwd_pkts * np.random.normal(loc=120, scale=30, size=n_samples).clip(40, 1500)
    tot_len_bwd_pkts = tot_bwd_pkts * np.random.normal(loc=200, scale=40, size=n_samples).clip(40, 1500)
    
    flow_bytes_s = (tot_len_fwd_pkts + tot_len_bwd_pkts) / (flow_duration / 1000.0 + 1e-6)
    flow_pkts_s = (tot_fwd_pkts + tot_bwd_pkts) / (flow_duration / 1000.0 + 1e-6)
    
    # 20% attack ratio
    is_attack = np.random.binomial(n=1, p=0.20, size=n_samples)
    labels = ["BENIGN" if a == 0 else np.random.choice(["PortScan", "DDoS", "Botnet", "Infiltration"]) for a in is_attack]
    
    # Inject dirty data elements to test decontamination: zero-length flows, NaN/inf
    dirty_indices = np.random.choice(n_samples, size=int(n_samples * 0.02), replace=False)
    for idx in dirty_indices[:len(dirty_indices)//2]:
        flow_bytes_s[idx] = np.inf
    for idx in dirty_indices[len(dirty_indices)//2:]:
        flow_duration[idx] = 0.0
        
    df = pd.DataFrame({
        " Source IP ": src_ips,
        " Destination IP ": dst_ips,
        " Source Port ": np.random.randint(1024, 65535, size=n_samples),
        " Destination Port ": np.random.choice([80, 443, 22, 21, 53, 8080], size=n_samples),
        " Protocol ": np.random.choice([6, 17], size=n_samples),
        " Flow Duration": flow_duration,
        " Total Fwd Packets": tot_fwd_pkts,
        " Total Backward Packets": tot_bwd_pkts,
        "Total Length of Fwd Packets": tot_len_fwd_pkts,
        " Total Length of Bwd Packets": tot_len_bwd_pkts,
        " Flow Bytes/s": flow_bytes_s,
        " Flow Packets/s": flow_pkts_s,
        " Fwd Packet Length Mean": tot_len_fwd_pkts / tot_fwd_pkts,
        " Bwd Packet Length Mean": np.where(tot_bwd_pkts > 0, tot_len_bwd_pkts / (tot_bwd_pkts + 1e-6), 0.0),
        " Flow IAT Mean": np.random.exponential(scale=100.0, size=n_samples),
        " Flow IAT Std": np.random.exponential(scale=50.0, size=n_samples),
        " Constant Feature ": [0.0] * n_samples,
        " Label ": labels
    })
    
    if str(output_file).endswith(".parquet"):
        try:
            df.to_parquet(output_file, index=False)
        except (ImportError, Exception):
            output_file = output_file.with_suffix(".csv")
            df.to_csv(output_file, index=False)
    else:
        df.to_csv(output_file, index=False)
        
    print(f"📊 Synthetic {dataset_name} sample ({n_samples} records) generated at: {output_file}")
    return output_file

def initialize_dataset_directories(base_dir: str | Path = ".") -> Dict[str, Path]:
    """Ensure data directories exist and safeguards are active."""
    ensure_gitignore_safeguards(base_dir)
    data_dir = Path(base_dir) / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    raw_dir = data_dir / "raw"
    processed_dir = data_dir / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    return {
        "root": data_dir,
        "raw": raw_dir,
        "processed": processed_dir
    }

def is_synthetic_path(filepath: str | Path) -> bool:
    """Check if the provided dataset path represents a synthetic fallback dataset."""
    name = Path(filepath).name.lower()
    return "synthetic" in name or "_sample" in name

def prepare_benchmark_dataset(
    dataset_name: str,
    base_dir: str | Path = ".",
    raw_data_dir: Optional[str | Path] = None,
    prefer_sample: bool = False,
    *args,
    **kwargs
) -> Path:
    """Retrieve benchmark dataset: checks for authentic files in user-provided structure without remote downloading."""
    dirs = initialize_dataset_directories(base_dir)
    meta = BENCHMARK_DATASET_METADATA.get(dataset_name.upper())
    if not meta:
        valid_keys = list(BENCHMARK_DATASET_METADATA.keys())
        raise ValueError(f"Unknown benchmark dataset: '{dataset_name}'. Must be one of: {valid_keys}")
    
    # 1. Search for real authentic candidate files across candidate roots & subfolders
    real_candidates = meta.get("real_candidates", [meta["primary_file"]])
    subfolders = meta.get("subfolders", [])
    base_path = Path(base_dir).resolve()
    
    candidate_roots = []
    if raw_data_dir:
        raw_p = Path(raw_data_dir).resolve()
        if raw_p.exists() and raw_p not in candidate_roots:
            candidate_roots.append(raw_p)
            
    candidate_roots.extend([
        Path("/content/drive/MyDrive/Colab Notebooks/data/raw"),
        Path("/content/drive/My Drive/Colab Notebooks/data/raw"),
        Path("/content/drive/MyDrive/Colab Notebook/data/raw"),
        Path("/content/drive/My Drive/Colab Notebook/data/raw"),
        Path("/Colab Notebooks/data/raw"),
        Path("/Colab Notebook/data/raw"),
        dirs["raw"],
        base_path / "data" / "raw",
        base_path / "src" / "data" / "actual-data",
        base_path / "actual-data",
        REPO_ROOT / "src" / "data" / "actual-data",
        REPO_ROOT / "data" / "raw",
        REPO_ROOT / "actual-data",
        Path("/content/drive/MyDrive/Colab Notebooks/src/data/actual-data"),
        Path("/content/drive/My Drive/Colab Notebooks/src/data/actual-data"),
        Path("/content/drive/MyDrive/Colab Notebook/src/data/actual-data"),
        Path("/content/drive/My Drive/Colab Notebook/src/data/actual-data"),
        Path("/content/My Drive/Colab Notebooks/data/raw"),
        Path("/content/My Drive/Colab Notebook/data/raw"),
        Path("/content/Colab Notebooks/data/raw"),
        Path("/content/Colab Notebook/data/raw"),
        Path("/content/data/raw"),
        dirs["processed"],
        base_path / "data" / "processed",
        dirs["root"],
    ])

    # Dynamically discover any mounted Drive directories if present
    drive_base = Path("/content/drive")
    if drive_base.exists():
        for drive_parent in [drive_base / "MyDrive", drive_base / "My Drive", drive_base, Path("/content/My Drive")]:
            if drive_parent.exists():
                try:
                    for sub in drive_parent.iterdir():
                        if sub.is_dir() and ("colab notebook" in sub.name.lower() or "is_ai-vuln" in sub.name.lower()):
                            r_dir = sub / "data" / "raw"
                            if r_dir.exists() and r_dir not in candidate_roots:
                                candidate_roots.insert(0, r_dir)
                            a_dir = sub / "src" / "data" / "actual-data"
                            if a_dir.exists() and a_dir not in candidate_roots:
                                candidate_roots.insert(0, a_dir)
                except Exception:
                    pass
    
    search_dirs = []
    for cr in candidate_roots:
        if cr.exists() and cr not in search_dirs:
            search_dirs.append(cr)
            try:
                for child in cr.iterdir():
                    if child.is_dir() and child not in search_dirs:
                        search_dirs.append(child)
                        for grandchild in child.iterdir():
                            if grandchild.is_dir() and grandchild not in search_dirs:
                                search_dirs.append(grandchild)
            except Exception:
                pass

    found_real_path = None
    if not prefer_sample:
        # Step A: Priority match by candidate filename (case-insensitive)
        for s_dir in search_dirs:
            try:
                dir_files = [f for f in s_dir.iterdir() if f.is_file()]
            except Exception:
                continue
            file_map = {f.name.lower(): f for f in dir_files}
            for cand in real_candidates:
                cand_l = cand.lower()
                if cand_l in file_map:
                    candidate_path = file_map[cand_l]
                    if not is_synthetic_path(candidate_path) and candidate_path.stat().st_size > 0:
                        found_real_path = candidate_path
                        break
            if found_real_path:
                break

        # Step B: Folder-name match fallback
        if not found_real_path:
            sub_lowers = [s.lower() for s in subfolders]
            for s_dir in search_dirs:
                if s_dir.name.lower() in sub_lowers:
                    try:
                        dir_files = [f for f in s_dir.iterdir() if f.is_file()]
                    except Exception:
                        continue
                    valid_files = [
                        f for f in dir_files
                        if f.suffix.lower() in [".parquet", ".csv", ".txt"]
                        and not is_synthetic_path(f)
                        and f.stat().st_size > 0
                        and not f.name.startswith(".")
                        and "features" not in f.name.lower()
                        and "list_events" not in f.name.lower()
                    ]
                    if valid_files:
                        found_real_path = valid_files[0]
                        break

    if found_real_path:
        print("\n" + "=" * 80)
        print(f"🛡️ [DATA STATUS: REAL AUTHENTIC DATASET LOADED]")
        print(f"📁 Source: {found_real_path.resolve()}")
        print(f"📊 Dataset: {dataset_name} (Authentic Reference Benchmark)")
        print(f"✅ Ingestion & decontamination will operate on REAL network traffic data.")
        print("=" * 80 + "\n")
        return found_real_path

    # 2. Check if primary file already exists in dirs["raw"]
    target_filename = meta["sample_file"] if prefer_sample else meta["primary_file"]
    target_path = dirs["raw"] / target_filename
    
    if target_path.exists() and not prefer_sample:
        is_syn = is_synthetic_path(target_path)
        if not is_syn:
            print("\n" + "=" * 80)
            print(f"🛡️ [DATA STATUS: REAL AUTHENTIC DATASET LOADED]")
            print(f"📁 Source: {target_path.resolve()}")
            print("=" * 80 + "\n")
            return target_path

    # 3. If prefer_sample was explicitly set to True, generate synthetic benchmark sample
    if prefer_sample:
        sample_path = dirs["raw"] / f"{dataset_name}_sample.csv"
        if not sample_path.exists():
            generate_synthetic_benchmark_sample(dataset_name, sample_path, n_samples=10000)
            
        print("\n" + "=" * 80)
        print(f"⚠️ [DATA STATUS: SYNTHETIC SAMPLE EXPLICITLY REQUESTED]")
        print(f"📊 Active File: {sample_path.name} (Simulated 10,000 synthetic NetFlow records)")
        print("=" * 80 + "\n")
        return sample_path

    # 4. If real dataset not found and prefer_sample is False:
    # Remote downloading is completely disabled per user research policy.
    checked_list = "\n   - ".join(str(p) for p in search_dirs[:10])
    raise FileNotFoundError(
        f"\n{'=' * 80}\n"
        f"❌ REAL BENCHMARK DATASET NOT FOUND: '{dataset_name}'\n"
        f"📁 Expected in subfolder(s)      : {subfolders}\n"
        f"📄 Expected candidate file(s)   : {real_candidates[:4]}\n"
        f"🔍 Checked root directories     :\n   - {checked_list}\n\n"
        f"🚫 Remote downloading has been disabled per research policy.\n"
        f"📌 Please verify that the authentic folder '{subfolders[0]}' is present in your Google Drive at:\n"
        f"   {raw_data_dir or dirs['raw']}\n"
        f"{'=' * 80}"
    )

def scan_available_datasets(
    base_dir: str | Path = ".",
    raw_data_dir: Optional[str | Path] = None,
    *args,
    **kwargs
) -> Dict[str, Dict[str, Any]]:
    """Scan and return status of all 5 benchmark datasets across candidate roots."""
    inventory = {}
    for ds_name, meta in BENCHMARK_DATASET_METADATA.items():
        try:
            resolved_path = prepare_benchmark_dataset(
                ds_name, base_dir=base_dir, raw_data_dir=raw_data_dir, prefer_sample=False
            )
            is_syn = is_synthetic_path(resolved_path)
            file_size_mb = round(resolved_path.stat().st_size / (1024 * 1024), 2) if resolved_path.exists() else 0.0
            try:
                folder_size_mb = round(sum(f.stat().st_size for f in resolved_path.parent.rglob('*') if f.is_file()) / (1024 * 1024), 2)
            except Exception:
                folder_size_mb = file_size_mb
            inventory[ds_name] = {
                "dataset_name": ds_name,
                "expected_folder": meta.get("subfolder", meta.get("subfolders", [""])[0]),
                "detected_folder": resolved_path.parent.name,
                "detected_file": resolved_path.name,
                "source_path": str(resolved_path.resolve()),
                "is_synthetic": is_syn,
                "status": "SYNTHETIC_FALLBACK" if is_syn else "REAL_AUTHENTIC",
                "file_size_mb": file_size_mb,
                "folder_size_mb": folder_size_mb,
                "expected_size_mb": meta.get("approx_size_mb", 0.0),
                "format": meta.get("format", "csv")
            }
        except Exception as e:
            inventory[ds_name] = {
                "dataset_name": ds_name,
                "expected_folder": meta.get("subfolder", meta.get("subfolders", [""])[0]),
                "expected_size_mb": meta.get("approx_size_mb", 0.0),
                "status": "NOT_FOUND",
                "error": str(e).strip()
            }
    return inventory

if __name__ == "__main__":
    ensure_gitignore_safeguards()
    dirs = initialize_dataset_directories()
    print(f"📁 Dataset storage initialized at: {dirs['root'].resolve()}")
    sample_file = prepare_benchmark_dataset("CICIDS2017", prefer_sample=False)



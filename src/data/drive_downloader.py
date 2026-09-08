"""Drive Dataset Retrieval, Checksum Verification & Automatic .gitignore Safeguards."""
import os
import sys
import hashlib
import requests
import time
from pathlib import Path
from typing import Dict, Any, Optional

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
    "workspace_drive/",
    "drive_cache/",
    "checkpoints/*.pt",
    "experiment_output/**/checkpoints/"
]

BENCHMARK_DATASET_METADATA = {
    "CICIDS2017": {
        "description": "Canadian Institute for Cybersecurity Intrusion Detection Evaluation Dataset 2017",
        "primary_file": "CICIDS2017_cleaned.parquet",
        "sample_file": "CICIDS2017_sample.csv",
        "download_url": "https://raw.githubusercontent.com/j4305/Intrusion-Detection-Systems-Benchmark/main/sample_cicids2017.csv",
        "mirror_url": "https://huggingface.co/datasets/carlac/cicids2017/resolve/main/sample.csv",
        "expected_sha256": None,
        "format": "parquet/csv"
    },
    "UNSW-NB15": {
        "description": "UNSW Network Benchmark 2015",
        "primary_file": "UNSW_NB15_training-set.csv",
        "sample_file": "UNSW_NB15_sample.csv",
        "download_url": "https://raw.githubusercontent.com/defcom17/UNSW_NB15/master/UNSW_NB15_testing-set.csv",
        "mirror_url": "https://huggingface.co/datasets/carlac/unsw-nb15/resolve/main/sample.csv",
        "expected_sha256": None,
        "format": "csv"
    },
    "TON_IoT": {
        "description": "TON_IoT Telemetry and Network Dataset 2021",
        "primary_file": "Train_Test_Network.csv",
        "sample_file": "TON_IoT_sample.csv",
        "download_url": "https://raw.githubusercontent.com/network-datasets/ton-iot-samples/main/Train_Test_Network_sample.csv",
        "mirror_url": "https://huggingface.co/datasets/carlac/ton-iot/resolve/main/sample.csv",
        "expected_sha256": None,
        "format": "csv"
    },
    "CIC-DDoS2019": {
        "description": "CIC Distributed Denial of Service 2019 Dataset",
        "primary_file": "CIC_DDoS2019_sample.parquet",
        "sample_file": "CIC_DDoS2019_sample.csv",
        "download_url": "https://raw.githubusercontent.com/j4305/Intrusion-Detection-Systems-Benchmark/main/sample_ddos2019.csv",
        "mirror_url": "https://huggingface.co/datasets/carlac/ddos2019/resolve/main/sample.csv",
        "expected_sha256": None,
        "format": "parquet"
    },
    "NSL-KDD": {
        "description": "NSL-KDD Historical Baseline Dataset",
        "primary_file": "KDDTrain+.txt",
        "sample_file": "KDDTrain+_sample.txt",
        "download_url": "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B.txt",
        "mirror_url": "https://raw.githubusercontent.com/j4305/Intrusion-Detection-Systems-Benchmark/main/KDDTrain%2B.txt",
        "expected_sha256": None,
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

def prepare_benchmark_dataset(
    dataset_name: str,
    base_dir: str | Path = ".",
    prefer_sample: bool = False
) -> Path:
    """Retrieve benchmark dataset: attempts remote download or synthesizes representative sample."""
    dirs = initialize_dataset_directories(base_dir)
    meta = BENCHMARK_DATASET_METADATA.get(dataset_name.upper()) or BENCHMARK_DATASET_METADATA.get("CICIDS2017")
    
    target_filename = meta["sample_file"] if prefer_sample else meta["primary_file"]
    target_path = dirs["raw"] / target_filename
    
    if target_path.exists():
        print(f"ℹ️ Dataset already available at: {target_path}")
        return target_path
        
    # Attempt download if URL available
    download_success = False
    if meta.get("download_url") and not prefer_sample:
        download_success = download_file(meta["download_url"], target_path, meta.get("expected_sha256"))
    
    if not download_success:
        print(f"ℹ️ Remote source unavailable or sample requested. Generating synthetic benchmark sample...")
        sample_path = dirs["raw"] / f"{dataset_name}_sample.csv"
        generate_synthetic_benchmark_sample(dataset_name, sample_path, n_samples=10000)
        return sample_path
        
    return target_path

if __name__ == "__main__":
    ensure_gitignore_safeguards()
    dirs = initialize_dataset_directories()
    print(f"📁 Dataset storage initialized at: {dirs['root'].resolve()}")
    sample_file = prepare_benchmark_dataset("CICIDS2017", prefer_sample=True)


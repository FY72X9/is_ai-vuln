"""Drive Dataset Retrieval, Checksum Verification & Automatic .gitignore Safeguards."""
import os
import sys
import hashlib
import requests
from pathlib import Path
from typing import Dict, Optional

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
        "expected_sha256": None,
        "format": "parquet/csv"
    },
    "UNSW-NB15": {
        "description": "UNSW Network Benchmark 2015",
        "primary_file": "UNSW_NB15_training-set.csv",
        "expected_sha256": None,
        "format": "csv"
    },
    "TON_IoT": {
        "description": "TON_IoT Telemetry and Network Dataset 2021",
        "primary_file": "Train_Test_Network.csv",
        "expected_sha256": None,
        "format": "csv"
    },
    "CIC-DDoS2019": {
        "description": "CIC Distributed Denial of Service 2019 Dataset",
        "primary_file": "CIC_DDoS2019_sample.parquet",
        "expected_sha256": None,
        "format": "parquet"
    },
    "NSL-KDD": {
        "description": "NSL-KDD Historical Baseline Dataset",
        "primary_file": "KDDTrain+.txt",
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

def verify_file_sha256(filepath: str | Path, expected_sha256: str) -> bool:
    """Verify SHA-256 checksum of a downloaded file."""
    path = Path(filepath)
    if not path.exists():
        return False
    
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

if __name__ == "__main__":
    ensure_gitignore_safeguards()
    dirs = initialize_dataset_directories()
    print(f"📁 Dataset storage initialized at: {dirs['root'].resolve()}")

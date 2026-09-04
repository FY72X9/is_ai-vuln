"""Environment initialization and hardware-runtime abstraction for Google Colab and Workstations."""
import os
import sys
import gc
from pathlib import Path

def is_colab() -> bool:
    """Check if the current runtime is Google Colab."""
    try:
        import google.colab
        return True
    except ImportError:
        return False

def setup_environment(base_dir: str = None) -> dict:
    """Initialize storage directories, Google Drive mounting (if Colab), and memory safeguards.

    Returns:
        dict: Configuration dictionary containing paths and environment status.
    """
    in_colab = is_colab()
    
    if in_colab:
        try:
            from google.colab import drive
            drive.mount("/content/drive")
            drive_root = Path("/content/drive/MyDrive/is_ai-vuln")
            drive_root.mkdir(parents=True, exist_ok=True)
            local_cache = Path("/content/data")
            local_cache.mkdir(parents=True, exist_ok=True)
            print(" Google Drive mounted successfully at /content/drive/MyDrive/is_ai-vuln")
        except Exception as e:
            print(f" Warning: Google Drive mount failed: {e}")
            drive_root = Path("./workspace_drive")
            drive_root.mkdir(parents=True, exist_ok=True)
            local_cache = Path("./data")
            local_cache.mkdir(parents=True, exist_ok=True)
    else:
        root = Path(base_dir) if base_dir else Path(".")
        drive_root = root / "workspace_drive"
        local_cache = root / "data"
        drive_root.mkdir(parents=True, exist_ok=True)
        local_cache.mkdir(parents=True, exist_ok=True)
        print(f"ℹ️ Local execution environment initialized. Data cache at: {local_cache.resolve()}")

    output_dir = Path("experiment_output")
    output_dir.mkdir(parents=True, exist_ok=True)

    return {
        "is_colab": in_colab,
        "drive_dir": drive_root,
        "data_dir": local_cache,
        "output_dir": output_dir,
    }

def flush_memory():
    """Trigger Python garbage collection and flush CUDA cache to avoid OOM."""
    gc.collect()
    try:
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
    except ImportError:
        pass

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

def resolve_project_root(candidate_roots: list = None) -> Path:
    """Detect and return the project root directory across Colab and workstation environments."""
    default_candidates = [
        Path("/content/My Drive/Colab Notebooks"),
        Path("/content/drive/My Drive/Colab Notebooks"),
        Path("/content/drive/MyDrive/Colab Notebooks"),
        Path("/content/drive/MyDrive/is_ai-vuln"),
        Path("/content/is_ai-vuln"),
        Path(".").resolve(),
    ]
    if candidate_roots:
        candidates = [Path(p) for p in candidate_roots] + default_candidates
    else:
        candidates = default_candidates

    for candidate in candidates:
        if candidate.exists() and (candidate / "src").exists():
            return candidate.resolve()

    return Path(".").resolve()

def setup_environment(base_dir: str = None) -> dict:
    """Initialize storage directories, Google Drive mounting (if Colab), and memory safeguards.

    Returns:
        dict: Configuration dictionary containing paths and environment status.
    """
    in_colab = is_colab()
    
    if in_colab:
        try:
            from google.colab import drive
            if not Path("/content/drive").exists() and not Path("/content/My Drive").exists():
                drive.mount("/content/drive")
        except Exception as e:
            print(f"⚠️ Warning: Google Drive mount failed or already mounted: {e}")

    project_root = resolve_project_root([base_dir] if base_dir else None)
    os.chdir(str(project_root))
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    data_dir = project_root / "data"
    raw_dir = data_dir / "raw"
    processed_dir = data_dir / "processed"
    output_dir = project_root / "experiment_output"
    checkpoint_dir = project_root / "checkpoints"

    for d in [data_dir, raw_dir, processed_dir, output_dir, checkpoint_dir]:
        d.mkdir(parents=True, exist_ok=True)

    print(f"✅ Environment initialized. Project root: {project_root}")
    print(f"📁 Data directory: {data_dir.resolve()}")
    print(f"💾 Output directory: {output_dir.resolve()}")

    return {
        "is_colab": in_colab,
        "project_root": project_root,
        "data_dir": data_dir,
        "raw_dir": raw_dir,
        "processed_dir": processed_dir,
        "output_dir": output_dir,
        "checkpoint_dir": checkpoint_dir
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


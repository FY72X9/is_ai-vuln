"""State Checkpointing & Fault-Tolerant Autorecovery Pipeline for Google Colab and Workstations."""
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional

class CheckpointManager:
    """Manages experiment state checkpointing, allowing seamless resumption across folds and models."""

    def __init__(self, drive_checkpoint_dir: str | Path, dataset_name: str, track_name: str, total_folds: int = 5):
        self.checkpoint_dir = Path(drive_checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.dataset_name = dataset_name
        self.track_name = track_name
        self.total_folds = total_folds
        self.state_file = self.checkpoint_dir / f"checkpoint_{dataset_name}_{track_name}.json"
        self.state = self._load_or_init()

    def _load_or_init(self) -> Dict[str, Any]:
        """Load state from disk if exists, otherwise initialize clean state schema."""
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    state = json.load(f)
                    print(f"🔄 Checkpoint detected for {self.dataset_name} ({self.track_name}):")
                    print(f"   Completed models: {state.get('completed_models', [])}")
                    print(f"   Current model: {state.get('current_model')} | Completed folds: {state.get('completed_folds', [])}")
                    return state
            except Exception as e:
                print(f"⚠️ Failed to parse existing checkpoint ({e}). Creating backup and starting fresh.")
                backup_file = self.checkpoint_dir / f"checkpoint_{self.dataset_name}_{self.track_name}_{int(time.time())}.bak"
                self.state_file.rename(backup_file)

        return {
            "project": "is_ai-vuln",
            "version": "v4.0",
            "dataset": self.dataset_name,
            "track": self.track_name,
            "status": "IN_PROGRESS",
            "completed_models": [],
            "current_model": None,
            "completed_folds": [],
            "current_fold": 1,
            "last_checkpoint_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "metrics_accumulator": {}
        }

    def should_skip_model(self, model_name: str) -> bool:
        """Check whether all folds for a given model have been completed."""
        return model_name in self.state.get("completed_models", [])

    def should_skip_fold(self, model_name: str, fold_idx: int) -> bool:
        """Check whether a specific fold for a given model has already completed."""
        if self.should_skip_model(model_name):
            return True
        if self.state.get("current_model") == model_name and fold_idx in self.state.get("completed_folds", []):
            return True
        return False

    def record_fold_completion(self, model_name: str, fold_idx: int, fold_metrics: Dict[str, Any]):
        """Record the completion of a fold, update metrics, and persist to disk."""
        self.state["current_model"] = model_name
        if fold_idx not in self.state["completed_folds"]:
            self.state["completed_folds"].append(fold_idx)

        if model_name not in self.state["metrics_accumulator"]:
            self.state["metrics_accumulator"][model_name] = {}
        self.state["metrics_accumulator"][model_name][f"fold_{fold_idx}"] = fold_metrics

        if len(self.state["completed_folds"]) >= self.total_folds:
            if model_name not in self.state["completed_models"]:
                self.state["completed_models"].append(model_name)
            self.state["completed_folds"] = []
            self.state["current_fold"] = 1
            print(f"✅ Model '{model_name}' completed all {self.total_folds} folds.")
        else:
            self.state["current_fold"] = fold_idx + 1

        self.state["last_checkpoint_timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self._persist_state()

    def mark_completed(self):
        """Mark the entire track for this dataset as completed."""
        self.state["status"] = "COMPLETED"
        self.state["last_checkpoint_timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self._persist_state()
        print(f"🏆 All models and folds completed successfully for {self.dataset_name} ({self.track_name}).")

    def reset_state(self, backup: bool = True):
        """Reset the checkpoint state, optionally archiving the current state."""
        if backup and self.state_file.exists():
            backup_file = self.checkpoint_dir / f"checkpoint_{self.dataset_name}_{self.track_name}_{int(time.time())}.bak"
            self.state_file.rename(backup_file)
            print(f"📦 Checkpoint backed up to {backup_file}")
        self.state = self._load_or_init()

    def _persist_state(self):
        """Atomically persist state JSON."""
        temp_file = self.state_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2)
        temp_file.replace(self.state_file)

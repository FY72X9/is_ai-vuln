"""Unified Base Model Interface for Intrusion Detection Models.
Standardizes training, inference, latency profiling, and memory tracking.
"""
import os
import sys
import time
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Tuple, Union
import numpy as np

# Ensure workspace root is in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.utils.environment import flush_memory

class BaseIDSModel(ABC):
    """Abstract Base Class for all benchmarked IDS models."""

    def __init__(self, name: str, task_profile: str = "T1", random_state: int = 42, **kwargs):
        self.name = name
        self.task_profile = task_profile
        self.random_state = random_state
        self.params = kwargs
        self.is_fitted = False
        self.model = None

    @abstractmethod
    def fit(self, X: np.ndarray, y: np.ndarray, **kwargs) -> "BaseIDSModel":
        """Train the model on the provided training partition."""
        pass

    @abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Generate hard binary / multi-class predictions."""
        pass

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Generate prediction probability distributions. Fallback to binary indicator if unsupported."""
        preds = self.predict(X)
        if preds.ndim == 1:
            proba = np.zeros((len(preds), 2), dtype=float)
            for i, p in enumerate(preds):
                idx = int(p > 0)
                proba[i, idx] = 1.0
            return proba
        return preds

    def profile_inference(
        self,
        X_val: np.ndarray,
        warmup_runs: int = 5,
        repeat_runs: int = 20
    ) -> Dict[str, float]:
        """Profile inference latency (ms/flow), throughput (flows/sec), and peak VRAM/RAM."""
        if not self.is_fitted:
            raise RuntimeError(f"Model {self.name} must be fitted before profiling inference.")

        # Subset for profiling if evaluation partition is large
        X_eval = X_val[:min(len(X_val), 2000)]
        n_samples = len(X_eval)

        # Warm-up phase
        for _ in range(warmup_runs):
            _ = self.predict(X_eval[:min(10, n_samples)])

        # Measure PyTorch CUDA peak memory if available
        vram_peak_mb = 0.0
        try:
            import torch  # type: ignore
            if torch.cuda.is_available():
                torch.cuda.reset_peak_memory_stats()
                torch.cuda.synchronize()
        except ImportError:
            pass

        # Time evaluation runs
        latencies = []
        for _ in range(repeat_runs):
            t0 = time.perf_counter()
            _ = self.predict(X_eval)
            try:
                import torch  # type: ignore
                if torch.cuda.is_available():
                    torch.cuda.synchronize()
            except ImportError:
                pass
            t1 = time.perf_counter()
            latencies.append((t1 - t0))

        avg_total_sec = float(np.mean(latencies))
        avg_latency_ms_per_flow = (avg_total_sec / n_samples) * 1000.0
        throughput_flows_sec = n_samples / max(avg_total_sec, 1e-9)

        # Retrieve CUDA peak VRAM
        try:
            import torch  # type: ignore
            if torch.cuda.is_available():
                vram_peak_mb = float(torch.cuda.max_memory_allocated() / (1024 * 1024))
        except ImportError:
            vram_peak_mb = 0.0

        return {
            "latency_ms_per_flow": round(avg_latency_ms_per_flow, 4),
            "throughput_flows_sec": round(throughput_flows_sec, 2),
            "vram_peak_mb": round(vram_peak_mb, 2)
        }

    def cleanup(self) -> None:
        """Release weights and garbage collect GPU/CPU memory."""
        self.model = None
        self.is_fitted = False
        flush_memory()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name='{self.name}', fitted={self.is_fitted})>"

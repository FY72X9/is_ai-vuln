"""Evaluation Metrics and Task-Technology Fit (TTF) Utility Engine.
Computes standard classification metrics, operational efficiency telemetry, and TTF utilities.
"""
import numpy as np
from typing import Dict, Any, Optional
from sklearn.metrics import (
    f1_score,
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score,
    average_precision_score
)

# TTF Task Weight Vectors (Aligned with Master Blueprint v4.0)
TTF_WEIGHTS = {
    "T1": {"f1": 0.25, "latency": 0.45, "vram": 0.25, "generalization": 0.05},  # Line-Rate Edge
    "T2": {"f1": 0.35, "latency": 0.05, "vram": 0.10, "generalization": 0.50},  # Zero-Day Few-Shot
    "T3": {"f1": 0.40, "latency": 0.20, "vram": 0.10, "generalization": 0.30}   # Multi-Host Tracking
}

def evaluate_classification_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: Optional[np.ndarray] = None
) -> Dict[str, float]:
    """Calculate comprehensive classification metrics."""
    metrics = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_weighted": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        "precision_macro": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(y_true, y_pred, average="macro", zero_division=0))
    }

    if y_prob is not None:
        try:
            # Check binary vs multi-class
            if y_prob.ndim == 2 and y_prob.shape[1] == 2:
                metrics["roc_auc"] = float(roc_auc_score(y_true, y_prob[:, 1]))
                metrics["pr_auc"] = float(average_precision_score(y_true, y_prob[:, 1]))
            elif y_prob.ndim == 1:
                metrics["roc_auc"] = float(roc_auc_score(y_true, y_prob))
                metrics["pr_auc"] = float(average_precision_score(y_true, y_prob))
            elif y_prob.ndim == 2 and y_prob.shape[1] > 2:
                metrics["roc_auc"] = float(roc_auc_score(y_true, y_prob, multi_class="ovr"))
        except Exception:
            metrics["roc_auc"] = 0.5
            metrics["pr_auc"] = 0.5

    return metrics

def evaluate_fold_run(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: Optional[np.ndarray] = None,
    profile_info: Optional[Dict[str, float]] = None
) -> Dict[str, float]:
    """Combine classification metrics with inference profiling into standard telemetry record."""
    summary = evaluate_classification_metrics(y_true, y_pred, y_prob)
    if profile_info:
        summary.update(profile_info)
    else:
        summary.update({
            "latency_ms_per_flow": 0.0,
            "throughput_flows_sec": 0.0,
            "vram_peak_mb": 0.0
        })
    return summary

def calculate_ttf_utility(
    f1_score: float,
    latency_ms: float,
    min_benchmark_latency_ms: float,
    vram_mb: float,
    min_benchmark_vram_mb: float,
    unseen_generalization_ratio: float = 1.0,
    task: str = "T1"
) -> float:
    """Compute formal Task-Technology Fit utility score according to Blueprint v4.0.

    TTF = w_1 * F1 + w_2 * (min_lat / lat) + w_3 * (min_vram / vram) + w_4 * (F1_unseen / F1_seen)
    """
    weights = TTF_WEIGHTS.get(task.upper(), TTF_WEIGHTS["T1"])
    
    # Inverted latency and memory terms (bounded to [0, 1])
    lat_term = min(1.0, (min_benchmark_latency_ms + 1e-6) / (latency_ms + 1e-6))
    mem_term = min(1.0, (min_benchmark_vram_mb + 1.0) / (vram_mb + 1.0))
    gen_term = min(1.0, max(0.0, unseen_generalization_ratio))
    
    ttf = (
        weights["f1"] * f1_score +
        weights["latency"] * lat_term +
        weights["vram"] * mem_term +
        weights["generalization"] * gen_term
    )
    return round(float(ttf), 4)

"""Adversarial Robustness Injection & Architectural Component Ablation Engine.
Evaluates perturbation degradation slopes and hyperparameter grid sweeps.
"""
import os
import sys
import numpy as np
from pathlib import Path
from typing import Dict, Any, List, Tuple, Callable

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

def inject_gaussian_noise(
    X: np.ndarray,
    sigma: float = 0.05,
    seed: int = 42
) -> np.ndarray:
    """Inject zero-mean Gaussian perturbation scaled by feature standard deviations."""
    if sigma <= 0.0:
        return X.copy()
    rng = np.random.RandomState(seed)
    feat_stds = np.std(X, axis=0, keepdims=True) + 1e-6
    noise = rng.normal(loc=0.0, scale=sigma, size=X.shape) * feat_stds
    return X + noise

def inject_feature_corruption(
    X: np.ndarray,
    dropout_ratio: float = 0.20,
    seed: int = 42
) -> np.ndarray:
    """Randomly mask out a fraction of features (zero dropout)."""
    if dropout_ratio <= 0.0:
        return X.copy()
    rng = np.random.RandomState(seed)
    mask = rng.binomial(n=1, p=(1.0 - dropout_ratio), size=X.shape)
    return X * mask

def evaluate_robustness_degradation_slope(
    model,
    X_val: np.ndarray,
    y_val: np.ndarray,
    noise_levels: List[float] = [0.0, 0.02, 0.05, 0.10, 0.20],
    metric_fn: Callable = None
) -> Dict[str, Any]:
    """Profile performance decay curve under increasing Gaussian noise injection."""
    from sklearn.metrics import f1_score
    if metric_fn is None:
        metric_fn = lambda yt, yp: f1_score(yt, yp, average="macro", zero_division=0)

    scores = []
    for sigma in noise_levels:
        X_noisy = inject_gaussian_noise(X_val, sigma=sigma)
        preds = model.predict(X_noisy)
        score = float(metric_fn(y_val, preds))
        scores.append(score)

    # Compute degradation slope via linear regression
    sigmas = np.array(noise_levels)
    sc = np.array(scores)
    # Slope: delta F1 / delta sigma
    slope, intercept = np.polyfit(sigmas, sc, 1)

    return {
        "noise_levels": noise_levels,
        "scores": [round(s, 4) for s in scores],
        "degradation_slope": round(float(slope), 4),
        "baseline_score": round(float(scores[0]), 4),
        "worst_score": round(float(scores[-1]), 4),
        "relative_drop_pct": round(float((scores[0] - scores[-1]) / max(scores[0], 1e-6) * 100.0), 2)
    }

def run_component_ablation_sweep(
    model_class,
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    param_grid: Dict[str, list]
) -> List[Dict[str, Any]]:
    """Execute grid ablation on architectural dimensions (e.g. depth L vs width d)."""
    import itertools
    from sklearn.metrics import f1_score

    keys = list(param_grid.keys())
    combinations = list(itertools.product(*[param_grid[k] for k in keys]))
    results = []

    for combo in combinations:
        params = dict(zip(keys, combo))
        model = model_class(**params)
        model.fit(X_train, y_train)
        preds = model.predict(X_val)
        f1 = float(f1_score(y_val, preds, average="macro", zero_division=0))
        
        entry = dict(params)
        entry["f1_macro"] = round(f1, 4)
        results.append(entry)
        model.cleanup()

    return results

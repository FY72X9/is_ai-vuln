"""Non-Parametric Statistical Significance Engine: Friedman Test & Nemenyi CD Analysis.
Standardized according to Demsar (2006) for multi-classifier benchmarking across multiple datasets.
"""
import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats
from typing import Dict, Any, Tuple, List, Optional
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.visualization.publication_styler import set_publication_style, save_publication_figure

# Two-tailed Nemenyi Studentized Range critical values (q_alpha for alpha=0.05)
# Indexed by number of classifiers k from 2 to 10
NEMENYI_Q_ALPHA_005 = {
    2: 1.960,
    3: 2.343,
    4: 2.569,
    5: 2.728,
    6: 2.850,
    7: 2.949,
    8: 3.031,
    9: 3.102,
    10: 3.164
}

def compute_friedman_test(
    performance_matrix: np.ndarray,
    model_names: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Calculate the Friedman non-parametric test across N datasets and k models.

    Args:
        performance_matrix: Shape (N_datasets, k_models), higher values indicate superior performance.
        model_names: Optional list of k model names.

    Returns:
        Dictionary with chi2 statistic, Iman-Davenport F statistic, p-values, and average ranks.
    """
    N, k = performance_matrix.shape
    if k < 2 or N < 2:
        raise ValueError(f"Friedman test requires at least 2 models and 2 datasets. Got N={N}, k={k}")

    # Rank each row (1 = highest performance)
    ranks = np.zeros_like(performance_matrix, dtype=float)
    for i in range(N):
        # Invert so highest score gets rank 1
        ranks[i] = stats.rankdata(-performance_matrix[i], method="average")

    avg_ranks = np.mean(ranks, axis=0)

    # Standard Friedman chi-square statistic
    ss_ranks = np.sum(avg_ranks ** 2)
    chi2_f = (12.0 * N / (k * (k + 1))) * (ss_ranks - (k * (k + 1) ** 2) / 4.0)
    p_chi2 = float(1.0 - stats.chi2.cdf(chi2_f, df=k - 1))

    # Iman-Davenport F-statistic adjustment (less conservative)
    f_f = ((N - 1) * chi2_f) / (N * (k - 1) - chi2_f + 1e-9)
    p_f = float(1.0 - stats.f.cdf(f_f, k - 1, (k - 1) * (N - 1)))

    ranks_dict = {
        (model_names[j] if model_names else f"Model_{j+1}"): round(float(avg_ranks[j]), 4)
        for j in range(k)
    }

    return {
        "N_datasets": int(N),
        "k_models": int(k),
        "chi2_stat": round(float(chi2_f), 4),
        "p_value_chi2": p_chi2,
        "iman_davenport_f": round(float(f_f), 4),
        "p_value_f": p_f,
        "null_hypothesis_rejected": bool(p_f < 0.05),
        "average_ranks": ranks_dict,
        "raw_ranks": ranks
    }

def compute_nemenyi_critical_difference(k: int, N: int, alpha: float = 0.05) -> float:
    """Compute Nemenyi Critical Difference (CD) threshold."""
    q_alpha = NEMENYI_Q_ALPHA_005.get(k, 3.031)
    cd = q_alpha * np.sqrt((k * (k + 1)) / (6.0 * N))
    return round(float(cd), 4)

def plot_critical_difference_diagram(
    avg_ranks: Dict[str, float],
    cd: float,
    output_filepath: Optional[str | Path] = None,
    title: str = "Nemenyi Critical Difference (CD) Diagram (alpha=0.05)"
) -> plt.Figure:
    """Generate publication-standard horizontal Critical Difference (CD) rank diagram."""
    set_publication_style(is_double_column=True)
    
    sorted_models = sorted(avg_ranks.items(), key=lambda x: x[1])
    names = [x[0] for x in sorted_models]
    ranks = [x[1] for x in sorted_models]
    k = len(names)

    fig, ax = plt.subplots(figsize=(7.0, 3.2))
    
    # Draw horizontal axis from 1 to k
    ax.set_xlim(0.5, k + 0.5)
    ax.set_ylim(-0.5, k * 0.4 + 0.8)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.set_xticks(range(1, k + 1))
    ax.set_xlabel("Average Rank (Lower indicates superior performance across benchmarks)")
    ax.set_title(title, pad=15)

    # Plot CD threshold bar in top-left
    ax.plot([1.0, 1.0 + cd], [k * 0.4 + 0.4, k * 0.4 + 0.4], color="firebrick", lw=3.0)
    ax.text(1.0 + cd / 2.0, k * 0.4 + 0.55, f"CD = {cd:.2f}", ha="center", color="firebrick", fontweight="bold", fontsize=8)

    # Plot model rank points and vertical drop lines
    y_levels = np.linspace(0.1, k * 0.4, k)
    for i, (name, rank) in enumerate(zip(names, ranks)):
        y_pos = y_levels[i]
        ax.plot([rank, rank], [0, y_pos], color="gray", linestyle=":", lw=1.0)
        ax.plot(rank, 0, marker="o", markersize=6, color="navy")
        ax.plot(rank, y_pos, marker="s", markersize=4, color="darkslateblue")
        ax.text(rank + 0.08, y_pos - 0.04, f"{name} ({rank:.2f})", fontsize=8, va="center")

    if output_filepath:
        save_publication_figure(fig, output_filepath)
        
    return fig

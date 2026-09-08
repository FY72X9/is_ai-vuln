"""Evaluation package: classification metrics, latency/memory profiling, TTF utility, statistical tests, and robustness."""
from src.evaluation.metrics import (
    evaluate_classification_metrics,
    evaluate_fold_run,
    calculate_ttf_utility,
    TTF_WEIGHTS
)
from src.evaluation.statistical_tests import (
    compute_friedman_test,
    compute_nemenyi_critical_difference,
    plot_critical_difference_diagram
)
from src.evaluation.robustness import (
    inject_gaussian_noise,
    inject_feature_corruption,
    evaluate_robustness_degradation_slope,
    run_component_ablation_sweep
)

__all__ = [
    "evaluate_classification_metrics",
    "evaluate_fold_run",
    "calculate_ttf_utility",
    "TTF_WEIGHTS",
    "compute_friedman_test",
    "compute_nemenyi_critical_difference",
    "plot_critical_difference_diagram",
    "inject_gaussian_noise",
    "inject_feature_corruption",
    "evaluate_robustness_degradation_slope",
    "run_component_ablation_sweep"
]

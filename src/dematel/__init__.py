"""DEMATEL package: Axiomatic priors, empirical modulation, fuzzy synthesis, CFCS, and Monte Carlo proof."""
from src.dematel.axiomatic_priors import (
    construct_axiomatic_prior_matrix,
    DEMATEL_FACTORS,
    FACTOR_LABELS
)
from src.dematel.empirical_mapper import (
    generate_mock_telemetry_matrix,
    compute_empirical_nmi_matrix
)
from src.dematel.fuzzy_engine import (
    synthesize_triangular_fuzzy_matrix,
    normalize_fuzzy_matrices,
    compute_total_relation_matrix,
    cfcs_defuzzify,
    compute_prominence_and_relation,
    run_closed_loop_fuzzy_dematel
)
from src.dematel.causal_validation import (
    run_monte_carlo_sensitivity_proof,
    run_causal_triangulation,
    plot_causal_network_digraph
)

__all__ = [
    "construct_axiomatic_prior_matrix",
    "DEMATEL_FACTORS",
    "FACTOR_LABELS",
    "generate_mock_telemetry_matrix",
    "compute_empirical_nmi_matrix",
    "synthesize_triangular_fuzzy_matrix",
    "normalize_fuzzy_matrices",
    "compute_total_relation_matrix",
    "cfcs_defuzzify",
    "compute_prominence_and_relation",
    "run_closed_loop_fuzzy_dematel",
    "run_monte_carlo_sensitivity_proof",
    "run_causal_triangulation",
    "plot_causal_network_digraph"
]

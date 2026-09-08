"""Closed-Loop Fuzzy DEMATEL Computational Engine.
Implements TFN synthesis, fuzzy normalization, total relation matrix inversion, and CFCS defuzzification.
"""
import numpy as np
from typing import Dict, Any, Tuple, Optional
from src.dematel.axiomatic_priors import construct_axiomatic_prior_matrix, DEMATEL_FACTORS, FACTOR_LABELS

def synthesize_triangular_fuzzy_matrix(
    W_theory: np.ndarray,
    W_empirical: np.ndarray,
    Var_empirical: np.ndarray,
    beta: float = 0.50,
    n_folds: int = 5
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Synthesize triangular fuzzy numbers (l_ij, m_ij, u_ij) combining theory and telemetry."""
    n = W_theory.shape[0]
    L = np.zeros((n, n), dtype=float)
    M = np.zeros((n, n), dtype=float)
    U = np.zeros((n, n), dtype=float)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            m = beta * W_theory[i, j] + (1.0 - beta) * W_empirical[i, j]
            # Half-width bound based on 95% confidence spread
            sigma = np.sqrt(max(Var_empirical[i, j], 1e-6))
            spread = 1.96 * (sigma / np.sqrt(n_folds))
            spread = max(0.04, min(spread, 0.20))  # Reasonable physical bounds
            
            l = max(0.0, m - spread)
            u = min(1.0, m + spread)
            
            L[i, j] = l
            M[i, j] = m
            U[i, j] = u

    return L, M, U

def normalize_fuzzy_matrices(
    L: np.ndarray, M: np.ndarray, U: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Normalize fuzzy matrix by the maximum row sum of upper bounds."""
    row_sums_u = np.sum(U, axis=1)
    s = float(np.max(row_sums_u))
    s = max(s, 1.0)
    return L / s, M / s, U / s, s

def compute_total_relation_matrix(
    X_L: np.ndarray, X_M: np.ndarray, X_U: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute total relation fuzzy matrices T = X(I - X)^-1."""
    n = X_M.shape[0]
    I = np.eye(n, dtype=float)
    
    T_L = np.dot(X_L, np.linalg.inv(I - X_L))
    T_M = np.dot(X_M, np.linalg.inv(I - X_M))
    T_U = np.dot(X_U, np.linalg.inv(I - X_U))
    
    return T_L, T_M, T_U

def cfcs_defuzzify(
    T_L: np.ndarray, T_M: np.ndarray, T_U: np.ndarray
) -> np.ndarray:
    """Converting Fuzzy data into Crisp Scores (CFCS) defuzzification algorithm (Opricovic & Tzeng 2003)."""
    n = T_M.shape[0]
    T_crisp = np.zeros((n, n), dtype=float)

    min_l = np.min(T_L)
    max_u = np.max(T_U)
    delta = max_u - min_l
    if delta < 1e-9:
        return T_M.copy()

    # Step 1: Normalization
    x_l = (T_L - min_l) / delta
    x_m = (T_M - min_l) / delta
    x_u = (T_U - min_l) / delta

    # Step 2: Compute lower and upper normalized crisp scores
    x_ls = x_m / (1.0 + x_m - x_l + 1e-9)
    x_us = x_u / (1.0 + x_u - x_m + 1e-9)

    # Step 3: Compute total normalized crisp score
    x_total = (x_ls * (1.0 - x_ls) + x_us * x_us) / (1.0 - x_ls + x_us + 1e-9)

    # Step 4: Compute final crisp values
    T_crisp = min_l + x_total * delta
    # Zero out diagonal self-relations
    np.fill_diagonal(T_crisp, 0.0)

    return T_crisp

def compute_prominence_and_relation(
    T_crisp: np.ndarray
) -> Dict[str, Any]:
    """Compute D (row sum), R (col sum), Prominence (D+R), and Relation (D-R)."""
    n = T_crisp.shape[0]
    D = np.sum(T_crisp, axis=1)  # Influence exerted
    R = np.sum(T_crisp, axis=0)  # Influence received

    prominence = D + R
    relation = D - R

    # Threshold alpha for causal network digraph
    alpha = float(np.mean(T_crisp) + 0.5 * np.std(T_crisp))
    adjacency = (T_crisp >= alpha).astype(int)

    results = []
    for i in range(n):
        factor_key = f"F{i+1}"
        results.append({
            "factor_id": factor_key,
            "factor_name": DEMATEL_FACTORS[i],
            "short_label": FACTOR_LABELS[factor_key],
            "D": round(float(D[i]), 4),
            "R": round(float(R[i]), 4),
            "D_plus_R": round(float(prominence[i]), 4),
            "D_minus_R": round(float(relation[i]), 4),
            "classification": "Cause" if relation[i] > 0 else "Effect"
        })

    return {
        "T_crisp": T_crisp,
        "D": D,
        "R": R,
        "prominence": prominence,
        "relation": relation,
        "alpha_threshold": round(alpha, 4),
        "adjacency_matrix": adjacency,
        "summary_table": results
    }

def run_closed_loop_fuzzy_dematel(
    W_theory: Optional[np.ndarray] = None,
    W_empirical: Optional[np.ndarray] = None,
    Var_empirical: Optional[np.ndarray] = None,
    beta: float = 0.50
) -> Dict[str, Any]:
    """Execute complete autonomous Fuzzy DEMATEL causal simulation pipeline."""
    if W_theory is None:
        W_theory = construct_axiomatic_prior_matrix()
    if W_empirical is None or Var_empirical is None:
        from src.dematel.empirical_mapper import generate_mock_telemetry_matrix, compute_empirical_nmi_matrix
        telemetry = generate_mock_telemetry_matrix()
        W_empirical, Var_empirical = compute_empirical_nmi_matrix(telemetry)

    L, M, U = synthesize_triangular_fuzzy_matrix(W_theory, W_empirical, Var_empirical, beta=beta)
    X_L, X_M, X_U, s = normalize_fuzzy_matrices(L, M, U)
    T_L, T_M, T_U = compute_total_relation_matrix(X_L, X_M, X_U)
    T_crisp = cfcs_defuzzify(T_L, T_M, T_U)
    causal_results = compute_prominence_and_relation(T_crisp)

    causal_results["fuzzy_bounds"] = {"L": L, "M": M, "U": U}
    causal_results["normalization_factor"] = s
    return causal_results

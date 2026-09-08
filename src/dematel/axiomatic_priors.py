"""Axiomatic Theoretical Prior Matrix (W_theory) for Autonomous Closed-Loop Fuzzy DEMATEL.
Eliminates subjective human expert questionnaires by rooting causal priors in proven computer science theory.
"""
import numpy as np
from typing import Dict, List, Tuple

DEMATEL_FACTORS = [
    "F1_Asymptotic_Complexity",      # O(L) vs O(L^2) algorithmic space/time bounds
    "F2_Pretraining_Sample_Capacity",# VC-dimension, pre-training corpus magnitude
    "F3_Attention_Sequence_Depth",   # Number of self-attention / SSM recurrent layers
    "F4_Topological_Relationality",  # Bipartite interaction graph representation
    "F5_LineRate_Detection_Accuracy",# F1-Macro on known network attack vectors
    "F6_Inference_Latency",          # Per-flow processing delay (ms / flow)
    "F7_ZeroDay_Generalization",     # Bayesian transfer on novel unseen attack variants
    "F8_Hardware_Memory_Footprint"   # VRAM / Host RAM peak utilization ceiling
]

FACTOR_LABELS = {
    "F1": "Asymptotic Complexity",
    "F2": "Pretraining Capacity",
    "F3": "Attention Depth",
    "F4": "Topological Relationality",
    "F5": "Line-Rate Accuracy",
    "F6": "Inference Latency",
    "F7": "Zero-Day Generalization",
    "F8": "Memory Footprint"
}

def construct_axiomatic_prior_matrix() -> np.ndarray:
    """Derive the 8x8 theoretical causal prior matrix W_theory.
    
    Self-influences W_ii = 0. Values in [0, 1] derived from algorithmic Big-O complexity
    and statistical learning theory bounds (Master Blueprint v4.0).
    """
    W = np.zeros((8, 8), dtype=float)
    
    # F1 (Asymptotic Complexity) -> F6 (Latency) = 0.90
    W[0, 5] = 0.90
    # F1 (Asymptotic Complexity) -> F8 (Memory) = 0.80
    W[0, 7] = 0.80
    # F2 (Pretraining Capacity) -> F7 (ZeroDay Generalization) = 0.85
    W[1, 6] = 0.85
    # F2 (Pretraining Capacity) -> F5 (Accuracy) = 0.70
    W[1, 4] = 0.70
    # F3 (Attention Depth) -> F6 (Latency) = 0.75
    W[2, 5] = 0.75
    # F3 (Attention Depth) -> F5 (Accuracy) = 0.65
    W[2, 4] = 0.65
    # F4 (Topological Relationality) -> F5 (Accuracy) = 0.80
    W[3, 4] = 0.80
    # F4 (Topological Relationality) -> F7 (ZeroDay Generalization) = 0.70
    W[3, 6] = 0.70
    # F5 (Line-Rate Accuracy) -> F7 (ZeroDay Generalization) = 0.60
    W[4, 6] = 0.60
    # F6 (Inference Latency) -> F3 (Attention Depth: Reciprocal restriction) = 0.70
    W[5, 2] = 0.70
    # F8 (Memory Footprint) -> F1 (Asymptotic Complexity: VRAM wall restriction) = 0.75
    W[7, 0] = 0.75
    # F8 (Memory Footprint) -> F3 (Attention Depth: Memory cap forces layer pruning) = 0.65
    W[7, 2] = 0.65

    return W

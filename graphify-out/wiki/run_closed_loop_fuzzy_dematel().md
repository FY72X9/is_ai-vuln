# run_closed_loop_fuzzy_dematel()

> God node · 11 connections · [D:\Codes\research_banks\is_ai-vuln\src\dematel\fuzzy_engine.py](file:///D:/Codes/research_banks/is_ai-vuln/src/dematel/fuzzy_engine.py#L134)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as run_closed_loop_fuzzy_dematel()
    participant P1 as run_tests()
    participant P2 as StreamingChunkLoader
    participant P3 as Comprehensive Full-Pipeline Verification Test Suite. Verifies streaming data loa
    participant P4 as run_monte_carlo_sensitivity_proof()
    participant P5 as normalize_fuzzy_matrices()
    participant P6 as compute_total_relation_matrix()
    participant P7 as cfcs_defuzzify()
    participant P8 as _calculate_kendalls_w()
    participant P9 as .cleanup()
    participant P10 as test_all_models()
    participant P11 as run_component_ablation_sweep()
    participant P12 as flush_memory()
    participant P13 as .fit()
    participant P14 as evaluate_robustness_degradation_slope()
    participant P15 as run_causal_triangulation()
    participant P16 as .iter_chunks()
    participant P17 as inject_gaussian_noise()
    participant P18 as get_model()
    participant P19 as generate_mock_telemetry_matrix()
    participant P20 as generate_scalable_synthetic_partition()
    participant P21 as compute_friedman_test()
    participant P22 as compute_nemenyi_critical_difference()
    participant P23 as export_benchmark_to_latex()
    participant P24 as compute_empirical_nmi_matrix()
    participant P25 as synthesize_triangular_fuzzy_matrix()
    participant P26 as compute_prominence_and_relation()
    participant P27 as construct_axiomatic_prior_matrix()
    P0->>+ P1: calls
    P1-->>- P0: return
    P1->>+ P0: calls
    P0-->>- P1: return
    P1->>+ P2: calls
    P2-->>- P1: return
    P2->>+ P1: calls
    P1-->>- P2: return
    P2->>+ P3: uses
    P3-->>- P2: return
    P1->>+ P4: calls
    P4-->>- P1: return
    P4->>+ P1: calls
    P1-->>- P4: return
    P4->>+ P5: calls
    P5-->>- P4: return
    P4->>+ P6: calls
    P6-->>- P4: return
    P4->>+ P7: calls
    P7-->>- P4: return
    P4->>+ P8: calls
    P8-->>- P4: return
    P1->>+ P9: calls
    P9-->>- P1: return
    P9->>+ P1: calls
    P1-->>- P9: return
    P9->>+ P10: calls
    P10-->>- P9: return
    P9->>+ P11: calls
    P11-->>- P9: return
    P9->>+ P12: calls
    P12-->>- P9: return
    P1->>+ P13: calls
    P13-->>- P1: return
    P1->>+ P14: calls
    P14-->>- P1: return
    P1->>+ P15: calls
    P15-->>- P1: return
    P1->>+ P16: calls
    P16-->>- P1: return
    P1->>+ P17: calls
    P17-->>- P1: return
    P1->>+ P18: calls
    P18-->>- P1: return
    P1->>+ P19: calls
    P19-->>- P1: return
    P1->>+ P20: calls
    P20-->>- P1: return
    P1->>+ P21: calls
    P21-->>- P1: return
    P1->>+ P22: calls
    P22-->>- P1: return
    P1->>+ P23: calls
    P23-->>- P1: return
    P0->>+ P5: calls
    P5-->>- P0: return
    P0->>+ P6: calls
    P6-->>- P0: return
    P0->>+ P7: calls
    P7-->>- P0: return
    P0->>+ P19: calls
    P19-->>- P0: return
    P0->>+ P24: calls
    P24-->>- P0: return
    P0->>+ P25: calls
    P25-->>- P0: return
    P0->>+ P26: calls
    P26-->>- P0: return
    P0->>+ P27: calls
    P27-->>- P0: return
```

## Connections by Relation

### calls
- [[run_tests()]] `INFERRED`
- [[normalize_fuzzy_matrices()]] `EXTRACTED`
- [[compute_total_relation_matrix()]] `EXTRACTED`
- [[cfcs_defuzzify()]] `EXTRACTED`
- [[generate_mock_telemetry_matrix()]] `INFERRED`
- [[compute_empirical_nmi_matrix()]] `INFERRED`
- [[synthesize_triangular_fuzzy_matrix()]] `EXTRACTED`
- [[compute_prominence_and_relation()]] `EXTRACTED`
- [[construct_axiomatic_prior_matrix()]] `INFERRED`

### contains
- [[fuzzy_engine.py]] `EXTRACTED`

### rationale_for
- [[Execute complete autonomous Fuzzy DEMATEL causal simulation pipeline.]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
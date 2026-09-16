# run_tests()

> God node · 16 connections · [D:\Codes\research_banks\is_ai-vuln\scratch\test_full_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_full_pipeline.py#L36)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as run_tests()
    participant P1 as run_closed_loop_fuzzy_dematel()
    participant P2 as generate_mock_telemetry_matrix()
    participant P3 as extract_empirical_telemetry_from_experiments()
    participant P4 as normalize_fuzzy_matrices()
    participant P5 as run_monte_carlo_sensitivity_proof()
    participant P6 as compute_total_relation_matrix()
    participant P7 as cfcs_defuzzify()
    participant P8 as compute_empirical_nmi_matrix()
    participant P9 as synthesize_triangular_fuzzy_matrix()
    participant P10 as compute_prominence_and_relation()
    participant P11 as construct_axiomatic_prior_matrix()
    participant P12 as StreamingChunkLoader
    participant P13 as .cleanup()
    participant P14 as .fit()
    participant P15 as evaluate_robustness_degradation_slope()
    participant P16 as run_causal_triangulation()
    participant P17 as generate_scalable_synthetic_partition()
    participant P18 as .iter_chunks()
    participant P19 as inject_gaussian_noise()
    participant P20 as get_model()
    participant P21 as compute_friedman_test()
    participant P22 as compute_nemenyi_critical_difference()
    participant P23 as export_benchmark_to_latex()
    P0->>+ P1: calls
    P1-->>- P0: return
    P1->>+ P0: calls
    P0-->>- P1: return
    P1->>+ P2: calls
    P2-->>- P1: return
    P2->>+ P0: calls
    P0-->>- P2: return
    P2->>+ P1: calls
    P1-->>- P2: return
    P2->>+ P3: calls
    P3-->>- P2: return
    P1->>+ P4: calls
    P4-->>- P1: return
    P4->>+ P1: calls
    P1-->>- P4: return
    P4->>+ P5: calls
    P5-->>- P4: return
    P1->>+ P6: calls
    P6-->>- P1: return
    P6->>+ P1: calls
    P1-->>- P6: return
    P6->>+ P5: calls
    P5-->>- P6: return
    P1->>+ P7: calls
    P7-->>- P1: return
    P7->>+ P1: calls
    P1-->>- P7: return
    P7->>+ P5: calls
    P5-->>- P7: return
    P1->>+ P8: calls
    P8-->>- P1: return
    P1->>+ P9: calls
    P9-->>- P1: return
    P1->>+ P10: calls
    P10-->>- P1: return
    P1->>+ P11: calls
    P11-->>- P1: return
    P0->>+ P12: calls
    P12-->>- P0: return
    P0->>+ P5: calls
    P5-->>- P0: return
    P0->>+ P13: calls
    P13-->>- P0: return
    P0->>+ P14: calls
    P14-->>- P0: return
    P0->>+ P15: calls
    P15-->>- P0: return
    P0->>+ P2: calls
    P2-->>- P0: return
    P0->>+ P16: calls
    P16-->>- P0: return
    P0->>+ P17: calls
    P17-->>- P0: return
    P0->>+ P18: calls
    P18-->>- P0: return
    P0->>+ P19: calls
    P19-->>- P0: return
    P0->>+ P20: calls
    P20-->>- P0: return
    P0->>+ P21: calls
    P21-->>- P0: return
    P0->>+ P22: calls
    P22-->>- P0: return
    P0->>+ P23: calls
    P23-->>- P0: return
```

## Connections by Relation

### calls
- [[run_closed_loop_fuzzy_dematel()]] `INFERRED`
- [[StreamingChunkLoader]] `INFERRED`
- [[run_monte_carlo_sensitivity_proof()]] `INFERRED`
- [[.cleanup()]] `INFERRED`
- [[.fit()]] `INFERRED`
- [[evaluate_robustness_degradation_slope()]] `INFERRED`
- [[generate_mock_telemetry_matrix()]] `INFERRED`
- [[run_causal_triangulation()]] `INFERRED`
- [[generate_scalable_synthetic_partition()]] `INFERRED`
- [[.iter_chunks()]] `INFERRED`
- [[inject_gaussian_noise()]] `INFERRED`
- [[get_model()]] `INFERRED`
- [[compute_friedman_test()]] `INFERRED`
- [[compute_nemenyi_critical_difference()]] `INFERRED`
- [[export_benchmark_to_latex()]] `INFERRED`

### contains
- [[test_full_pipeline.py]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
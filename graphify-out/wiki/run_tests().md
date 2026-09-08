# run_tests()

> God node · 16 connections · [D:\Codes\research_banks\is_ai-vuln\scratch\test_full_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_full_pipeline.py#L36)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as run_tests()
    participant P1 as run_closed_loop_fuzzy_dematel()
    participant P2 as normalize_fuzzy_matrices()
    participant P3 as run_monte_carlo_sensitivity_proof()
    participant P4 as compute_total_relation_matrix()
    participant P5 as cfcs_defuzzify()
    participant P6 as generate_mock_telemetry_matrix()
    participant P7 as compute_empirical_nmi_matrix()
    participant P8 as synthesize_triangular_fuzzy_matrix()
    participant P9 as compute_prominence_and_relation()
    participant P10 as construct_axiomatic_prior_matrix()
    participant P11 as StreamingChunkLoader
    participant P12 as .cleanup()
    participant P13 as .fit()
    participant P14 as evaluate_robustness_degradation_slope()
    participant P15 as run_causal_triangulation()
    participant P16 as .iter_chunks()
    participant P17 as inject_gaussian_noise()
    participant P18 as get_model()
    participant P19 as generate_scalable_synthetic_partition()
    participant P20 as compute_friedman_test()
    participant P21 as compute_nemenyi_critical_difference()
    participant P22 as export_benchmark_to_latex()
    P0->>+ P1: calls
    P1-->>- P0: return
    P1->>+ P0: calls
    P0-->>- P1: return
    P1->>+ P2: calls
    P2-->>- P1: return
    P2->>+ P1: calls
    P1-->>- P2: return
    P2->>+ P3: calls
    P3-->>- P2: return
    P1->>+ P4: calls
    P4-->>- P1: return
    P4->>+ P1: calls
    P1-->>- P4: return
    P4->>+ P3: calls
    P3-->>- P4: return
    P1->>+ P5: calls
    P5-->>- P1: return
    P5->>+ P1: calls
    P1-->>- P5: return
    P5->>+ P3: calls
    P3-->>- P5: return
    P1->>+ P6: calls
    P6-->>- P1: return
    P6->>+ P0: calls
    P0-->>- P6: return
    P6->>+ P1: calls
    P1-->>- P6: return
    P1->>+ P7: calls
    P7-->>- P1: return
    P1->>+ P8: calls
    P8-->>- P1: return
    P1->>+ P9: calls
    P9-->>- P1: return
    P1->>+ P10: calls
    P10-->>- P1: return
    P0->>+ P11: calls
    P11-->>- P0: return
    P0->>+ P3: calls
    P3-->>- P0: return
    P0->>+ P12: calls
    P12-->>- P0: return
    P0->>+ P13: calls
    P13-->>- P0: return
    P0->>+ P14: calls
    P14-->>- P0: return
    P0->>+ P15: calls
    P15-->>- P0: return
    P0->>+ P16: calls
    P16-->>- P0: return
    P0->>+ P17: calls
    P17-->>- P0: return
    P0->>+ P18: calls
    P18-->>- P0: return
    P0->>+ P6: calls
    P6-->>- P0: return
    P0->>+ P19: calls
    P19-->>- P0: return
    P0->>+ P20: calls
    P20-->>- P0: return
    P0->>+ P21: calls
    P21-->>- P0: return
    P0->>+ P22: calls
    P22-->>- P0: return
```

## Connections by Relation

### calls
- [[run_closed_loop_fuzzy_dematel()]] `INFERRED`
- [[StreamingChunkLoader]] `INFERRED`
- [[run_monte_carlo_sensitivity_proof()]] `INFERRED`
- [[.cleanup()]] `INFERRED`
- [[.fit()]] `INFERRED`
- [[evaluate_robustness_degradation_slope()]] `INFERRED`
- [[run_causal_triangulation()]] `INFERRED`
- [[.iter_chunks()]] `INFERRED`
- [[inject_gaussian_noise()]] `INFERRED`
- [[get_model()]] `INFERRED`
- [[generate_mock_telemetry_matrix()]] `INFERRED`
- [[generate_scalable_synthetic_partition()]] `INFERRED`
- [[compute_friedman_test()]] `INFERRED`
- [[compute_nemenyi_critical_difference()]] `INFERRED`
- [[export_benchmark_to_latex()]] `INFERRED`

### contains
- [[test_full_pipeline.py]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
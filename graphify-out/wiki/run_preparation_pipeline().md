# run_preparation_pipeline()

> God node · 11 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\prep_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/prep_pipeline.py#L39)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as run_preparation_pipeline()
    participant P1 as .split()
    participant P2 as run_track_a_benchmark()
    participant P3 as CheckpointManager
    participant P4 as AntiLeakageGroupKFold
    participant P5 as .fit()
    participant P6 as .predict()
    participant P7 as get_model()
    participant P8 as .profile_inference()
    participant P9 as evaluate_fold_run()
    participant P10 as flush_memory()
    participant P11 as extract_subnet_mask()
    participant P12 as .should_skip_model()
    participant P13 as .should_skip_fold()
    participant P14 as .transform()
    participant P15 as .predict_proba()
    participant P16 as calculate_ttf_utility()
    participant P17 as safe_slice()
    participant P18 as prepare_dataset()
    participant P19 as code_cell()
    participant P20 as md_cell()
    participant P21 as set_cell_source()
    participant P22 as upgrade_nb04()
    participant P23 as indent_block()
    participant P24 as .split()
    participant P25 as update_cell_2()
    participant P26 as update_nb01()
    participant P27 as update_nb02()
    participant P28 as update_nb03()
    participant P29 as update_nb04()
    participant P30 as update_nb05()
    participant P31 as update_nb06()
    participant P32 as upgrade_nb01()
    participant P33 as upgrade_nb02()
    participant P34 as upgrade_nb04()
    participant P35 as upgrade_nb05()
    participant P36 as upgrade_nb06()
    participant P37 as code_cell()
    participant P38 as md_cell()
    participant P39 as code_cell()
    participant P40 as md_cell()
    participant P41 as upgrade_nb02()
    participant P42 as upgrade_nb03()
    participant P43 as upgrade_nb04()
    participant P44 as validate_notebooks()
    participant P45 as prepare_benchmark_dataset()
    participant P46 as is_synthetic_path()
    participant P47 as initialize_dataset_directories()
    participant P48 as clean_dataset()
    participant P49 as build_networkx_flow_graph()
    participant P50 as export_to_pyg_tensors()
    P0->>+ P1: calls
    P1-->>- P0: return
    P1->>+ P2: calls
    P2-->>- P1: return
    P2->>+ P1: calls
    P1-->>- P2: return
    P2->>+ P3: calls
    P3-->>- P2: return
    P2->>+ P4: calls
    P4-->>- P2: return
    P2->>+ P5: calls
    P5-->>- P2: return
    P2->>+ P6: calls
    P6-->>- P2: return
    P2->>+ P7: calls
    P7-->>- P2: return
    P2->>+ P8: calls
    P8-->>- P2: return
    P2->>+ P9: calls
    P9-->>- P2: return
    P2->>+ P10: calls
    P10-->>- P2: return
    P2->>+ P11: calls
    P11-->>- P2: return
    P2->>+ P12: calls
    P12-->>- P2: return
    P2->>+ P13: calls
    P13-->>- P2: return
    P2->>+ P14: calls
    P14-->>- P2: return
    P2->>+ P15: calls
    P15-->>- P2: return
    P2->>+ P16: calls
    P16-->>- P2: return
    P2->>+ P17: calls
    P17-->>- P2: return
    P1->>+ P0: calls
    P0-->>- P1: return
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
    P1->>+ P24: calls
    P24-->>- P1: return
    P1->>+ P25: calls
    P25-->>- P1: return
    P1->>+ P26: calls
    P26-->>- P1: return
    P1->>+ P27: calls
    P27-->>- P1: return
    P1->>+ P28: calls
    P28-->>- P1: return
    P1->>+ P29: calls
    P29-->>- P1: return
    P1->>+ P30: calls
    P30-->>- P1: return
    P1->>+ P31: calls
    P31-->>- P1: return
    P1->>+ P32: calls
    P32-->>- P1: return
    P1->>+ P33: calls
    P33-->>- P1: return
    P1->>+ P34: calls
    P34-->>- P1: return
    P1->>+ P35: calls
    P35-->>- P1: return
    P1->>+ P36: calls
    P36-->>- P1: return
    P1->>+ P37: calls
    P37-->>- P1: return
    P1->>+ P38: calls
    P38-->>- P1: return
    P1->>+ P39: calls
    P39-->>- P1: return
    P1->>+ P40: calls
    P40-->>- P1: return
    P1->>+ P41: calls
    P41-->>- P1: return
    P1->>+ P42: calls
    P42-->>- P1: return
    P1->>+ P43: calls
    P43-->>- P1: return
    P1->>+ P44: calls
    P44-->>- P1: return
    P0->>+ P45: calls
    P45-->>- P0: return
    P0->>+ P4: calls
    P4-->>- P0: return
    P0->>+ P46: calls
    P46-->>- P0: return
    P0->>+ P47: calls
    P47-->>- P0: return
    P0->>+ P48: calls
    P48-->>- P0: return
    P0->>+ P11: calls
    P11-->>- P0: return
    P0->>+ P49: calls
    P49-->>- P0: return
    P0->>+ P50: calls
    P50-->>- P0: return
```

## Connections by Relation

### calls
- [[.split()]] `INFERRED`
- [[prepare_benchmark_dataset()]] `INFERRED`
- [[AntiLeakageGroupKFold]] `INFERRED`
- [[is_synthetic_path()]] `INFERRED`
- [[initialize_dataset_directories()]] `INFERRED`
- [[clean_dataset()]] `INFERRED`
- [[extract_subnet_mask()]] `INFERRED`
- [[build_networkx_flow_graph()]] `INFERRED`
- [[export_to_pyg_tensors()]] `INFERRED`

### contains
- [[prep_pipeline.py]] `EXTRACTED`

### rationale_for
- [[Execute complete ingestion, cleaning, anti-leakage splitting, and artifact gener]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
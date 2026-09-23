# run_preparation_pipeline()

> God node · 11 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\prep_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/prep_pipeline.py#L39)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as run_preparation_pipeline()
    participant P1 as .split()
    participant P2 as code_cell()
    participant P3 as build_nb03()
    participant P4 as build_nb04()
    participant P5 as build_nb05()
    participant P6 as build_nb06()
    participant P7 as md_cell()
    participant P8 as set_cell_source()
    participant P9 as upgrade_nb04()
    participant P10 as indent_block()
    participant P11 as .split()
    participant P12 as update_cell_2()
    participant P13 as update_nb01()
    participant P14 as update_nb02()
    participant P15 as update_nb03()
    participant P16 as update_nb04()
    participant P17 as update_nb05()
    participant P18 as update_nb06()
    participant P19 as upgrade_nb01()
    participant P20 as upgrade_nb02()
    participant P21 as upgrade_nb04()
    participant P22 as upgrade_nb05()
    participant P23 as upgrade_nb06()
    participant P24 as code_cell()
    participant P25 as md_cell()
    participant P26 as code_cell()
    participant P27 as md_cell()
    participant P28 as upgrade_nb02()
    participant P29 as upgrade_nb03()
    participant P30 as upgrade_nb04()
    participant P31 as validate_notebooks()
    participant P32 as prepare_benchmark_dataset()
    participant P33 as AntiLeakageGroupKFold
    participant P34 as is_synthetic_path()
    participant P35 as initialize_dataset_directories()
    participant P36 as clean_dataset()
    participant P37 as extract_subnet_mask()
    participant P38 as build_networkx_flow_graph()
    participant P39 as export_to_pyg_tensors()
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
    P2->>+ P4: calls
    P4-->>- P2: return
    P2->>+ P5: calls
    P5-->>- P2: return
    P2->>+ P6: calls
    P6-->>- P2: return
    P1->>+ P7: calls
    P7-->>- P1: return
    P7->>+ P1: calls
    P1-->>- P7: return
    P7->>+ P3: calls
    P3-->>- P7: return
    P7->>+ P4: calls
    P4-->>- P7: return
    P7->>+ P5: calls
    P5-->>- P7: return
    P7->>+ P6: calls
    P6-->>- P7: return
    P1->>+ P8: calls
    P8-->>- P1: return
    P1->>+ P9: calls
    P9-->>- P1: return
    P1->>+ P10: calls
    P10-->>- P1: return
    P1->>+ P11: calls
    P11-->>- P1: return
    P1->>+ P12: calls
    P12-->>- P1: return
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
    P0->>+ P32: calls
    P32-->>- P0: return
    P0->>+ P33: calls
    P33-->>- P0: return
    P0->>+ P34: calls
    P34-->>- P0: return
    P0->>+ P35: calls
    P35-->>- P0: return
    P0->>+ P36: calls
    P36-->>- P0: return
    P0->>+ P37: calls
    P37-->>- P0: return
    P0->>+ P38: calls
    P38-->>- P0: return
    P0->>+ P39: calls
    P39-->>- P0: return
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
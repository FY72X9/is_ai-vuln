# run_preparation_pipeline()

> God node · 10 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\prep_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/prep_pipeline.py#L38)

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
    participant P8 as .split()
    participant P9 as create_code_cell()
    participant P10 as create_markdown_cell()
    participant P11 as prepare_benchmark_dataset()
    participant P12 as AntiLeakageGroupKFold
    participant P13 as initialize_dataset_directories()
    participant P14 as clean_dataset()
    participant P15 as extract_subnet_mask()
    participant P16 as build_networkx_flow_graph()
    participant P17 as export_to_pyg_tensors()
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
    P0->>+ P11: calls
    P11-->>- P0: return
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
```

## Connections by Relation

### calls
- [[.split()]] `INFERRED`
- [[prepare_benchmark_dataset()]] `INFERRED`
- [[AntiLeakageGroupKFold]] `INFERRED`
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
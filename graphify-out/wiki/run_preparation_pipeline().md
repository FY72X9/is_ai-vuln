# run_preparation_pipeline()

> God node · 11 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\prep_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/prep_pipeline.py#L39)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as run_preparation_pipeline()
    participant P1 as prepare_benchmark_dataset()
    participant P2 as resolve_track_b_dataset()
    participant P3 as is_synthetic_path()
    participant P4 as initialize_dataset_directories()
    participant P5 as generate_scalable_synthetic_partition()
    participant P6 as test_drive_folder_simulation()
    participant P7 as test_streaming_loader_resolution()
    participant P8 as scan_available_datasets()
    participant P9 as test_drive_downloader_real_vs_synthetic()
    participant P10 as generate_synthetic_benchmark_sample()
    participant P11 as .split()
    participant P12 as AntiLeakageGroupKFold
    participant P13 as clean_dataset()
    participant P14 as extract_subnet_mask()
    participant P15 as build_networkx_flow_graph()
    participant P16 as export_to_pyg_tensors()
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
    P2->>+ P7: calls
    P7-->>- P2: return
    P1->>+ P3: calls
    P3-->>- P1: return
    P3->>+ P0: calls
    P0-->>- P3: return
    P3->>+ P1: calls
    P1-->>- P3: return
    P3->>+ P2: calls
    P2-->>- P3: return
    P3->>+ P8: calls
    P8-->>- P3: return
    P3->>+ P9: calls
    P9-->>- P3: return
    P1->>+ P4: calls
    P4-->>- P1: return
    P1->>+ P8: calls
    P8-->>- P1: return
    P1->>+ P6: calls
    P6-->>- P1: return
    P1->>+ P10: calls
    P10-->>- P1: return
    P1->>+ P9: calls
    P9-->>- P1: return
    P0->>+ P11: calls
    P11-->>- P0: return
    P0->>+ P12: calls
    P12-->>- P0: return
    P0->>+ P3: calls
    P3-->>- P0: return
    P0->>+ P4: calls
    P4-->>- P0: return
    P0->>+ P13: calls
    P13-->>- P0: return
    P0->>+ P14: calls
    P14-->>- P0: return
    P0->>+ P15: calls
    P15-->>- P0: return
    P0->>+ P16: calls
    P16-->>- P0: return
```

## Connections by Relation

### calls
- [[prepare_benchmark_dataset()]] `INFERRED`
- [[.split()]] `INFERRED`
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
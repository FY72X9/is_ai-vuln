# prepare_benchmark_dataset()

> God node · 10 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\drive_downloader.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/drive_downloader.py#L299)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as prepare_benchmark_dataset()
    participant P1 as run_preparation_pipeline()
    participant P2 as .split()
    participant P3 as code_cell()
    participant P4 as md_cell()
    participant P5 as .split()
    participant P6 as code_cell()
    participant P7 as md_cell()
    participant P8 as code_cell()
    participant P9 as md_cell()
    participant P10 as AntiLeakageGroupKFold
    participant P11 as Execute complete ingestion, cleaning, anti-leakage splitting, and artifact gener
    participant P12 as Execute complete ingestion, cleaning, anti-leakage splitting, and artifact gener
    participant P13 as is_synthetic_path()
    participant P14 as initialize_dataset_directories()
    participant P15 as clean_dataset()
    participant P16 as extract_subnet_mask()
    participant P17 as build_networkx_flow_graph()
    participant P18 as export_to_pyg_tensors()
    participant P19 as resolve_track_b_dataset()
    participant P20 as scan_available_datasets()
    participant P21 as test_drive_folder_simulation()
    participant P22 as generate_synthetic_benchmark_sample()
    participant P23 as test_drive_downloader_real_vs_synthetic()
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
    P2->>+ P8: calls
    P8-->>- P2: return
    P2->>+ P9: calls
    P9-->>- P2: return
    P1->>+ P10: calls
    P10-->>- P1: return
    P10->>+ P1: calls
    P1-->>- P10: return
    P10->>+ P11: uses
    P11-->>- P10: return
    P10->>+ P12: uses
    P12-->>- P10: return
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
    P0->>+ P19: calls
    P19-->>- P0: return
    P0->>+ P13: calls
    P13-->>- P0: return
    P0->>+ P14: calls
    P14-->>- P0: return
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
- [[run_preparation_pipeline()]] `INFERRED`
- [[resolve_track_b_dataset()]] `INFERRED`
- [[is_synthetic_path()]] `EXTRACTED`
- [[initialize_dataset_directories()]] `EXTRACTED`
- [[scan_available_datasets()]] `EXTRACTED`
- [[test_drive_folder_simulation()]] `INFERRED`
- [[generate_synthetic_benchmark_sample()]] `EXTRACTED`
- [[test_drive_downloader_real_vs_synthetic()]] `INFERRED`

### contains
- [[drive_downloader.py]] `EXTRACTED`

### rationale_for
- [[Retrieve benchmark dataset: checks for authentic files in user-provided structur]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
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
    participant P5 as set_cell_source()
    participant P6 as upgrade_nb04()
    participant P7 as indent_block()
    participant P8 as .split()
    participant P9 as update_cell_2()
    participant P10 as update_nb01()
    participant P11 as update_nb02()
    participant P12 as update_nb03()
    participant P13 as update_nb04()
    participant P14 as update_nb05()
    participant P15 as update_nb06()
    participant P16 as upgrade_nb01()
    participant P17 as upgrade_nb02()
    participant P18 as upgrade_nb04()
    participant P19 as upgrade_nb05()
    participant P20 as upgrade_nb06()
    participant P21 as code_cell()
    participant P22 as md_cell()
    participant P23 as code_cell()
    participant P24 as md_cell()
    participant P25 as upgrade_nb02()
    participant P26 as upgrade_nb03()
    participant P27 as upgrade_nb04()
    participant P28 as validate_notebooks()
    participant P29 as AntiLeakageGroupKFold
    participant P30 as is_synthetic_path()
    participant P31 as initialize_dataset_directories()
    participant P32 as clean_dataset()
    participant P33 as extract_subnet_mask()
    participant P34 as build_networkx_flow_graph()
    participant P35 as export_to_pyg_tensors()
    participant P36 as resolve_track_b_dataset()
    participant P37 as scan_available_datasets()
    participant P38 as test_drive_folder_simulation()
    participant P39 as generate_synthetic_benchmark_sample()
    participant P40 as test_drive_downloader_real_vs_synthetic()
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
    P2->>+ P18: calls
    P18-->>- P2: return
    P2->>+ P19: calls
    P19-->>- P2: return
    P2->>+ P20: calls
    P20-->>- P2: return
    P2->>+ P21: calls
    P21-->>- P2: return
    P2->>+ P22: calls
    P22-->>- P2: return
    P2->>+ P23: calls
    P23-->>- P2: return
    P2->>+ P24: calls
    P24-->>- P2: return
    P2->>+ P25: calls
    P25-->>- P2: return
    P2->>+ P26: calls
    P26-->>- P2: return
    P2->>+ P27: calls
    P27-->>- P2: return
    P2->>+ P28: calls
    P28-->>- P2: return
    P1->>+ P0: calls
    P0-->>- P1: return
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
    P0->>+ P36: calls
    P36-->>- P0: return
    P0->>+ P30: calls
    P30-->>- P0: return
    P0->>+ P31: calls
    P31-->>- P0: return
    P0->>+ P37: calls
    P37-->>- P0: return
    P0->>+ P38: calls
    P38-->>- P0: return
    P0->>+ P39: calls
    P39-->>- P0: return
    P0->>+ P40: calls
    P40-->>- P0: return
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
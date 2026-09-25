# CheckpointManager

> God node · 11 connections · [D:\Codes\research_banks\is_ai-vuln\src\utils\checkpoint_manager.py](file:///D:/Codes/research_banks/is_ai-vuln/src/utils/checkpoint_manager.py#L7)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as CheckpointManager
    participant P1 as run_track_a_benchmark()
    participant P2 as .split()
    participant P3 as run_preparation_pipeline()
    participant P4 as prepare_dataset()
    participant P5 as code_cell()
    participant P6 as md_cell()
    participant P7 as set_cell_source()
    participant P8 as upgrade_nb04()
    participant P9 as indent_block()
    participant P10 as .split()
    participant P11 as update_cell_2()
    participant P12 as update_nb01()
    participant P13 as update_nb02()
    participant P14 as update_nb03()
    participant P15 as update_nb04()
    participant P16 as update_nb05()
    participant P17 as update_nb06()
    participant P18 as upgrade_nb01()
    participant P19 as upgrade_nb02()
    participant P20 as upgrade_nb04()
    participant P21 as upgrade_nb05()
    participant P22 as upgrade_nb06()
    participant P23 as code_cell()
    participant P24 as md_cell()
    participant P25 as code_cell()
    participant P26 as md_cell()
    participant P27 as upgrade_nb02()
    participant P28 as upgrade_nb03()
    participant P29 as upgrade_nb04()
    participant P30 as validate_notebooks()
    participant P31 as AntiLeakageGroupKFold
    participant P32 as .fit()
    participant P33 as .predict()
    participant P34 as get_model()
    participant P35 as .profile_inference()
    participant P36 as evaluate_fold_run()
    participant P37 as flush_memory()
    participant P38 as extract_subnet_mask()
    participant P39 as .should_skip_model()
    participant P40 as .should_skip_fold()
    participant P41 as .transform()
    participant P42 as .predict_proba()
    participant P43 as calculate_ttf_utility()
    participant P44 as safe_slice()
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
    P2->>+ P29: calls
    P29-->>- P2: return
    P2->>+ P30: calls
    P30-->>- P2: return
    P1->>+ P0: calls
    P0-->>- P1: return
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
```

## Connections by Relation

### calls
- [[run_track_a_benchmark()]] `INFERRED`

### contains
- [[checkpoint_manager.py]] `EXTRACTED`

### method
- [[._load_or_init()]] `EXTRACTED`
- [[.should_skip_model()]] `EXTRACTED`
- [[.should_skip_fold()]] `EXTRACTED`
- [[._persist_state()]] `EXTRACTED`
- [[.record_fold_completion()]] `EXTRACTED`
- [[.mark_completed()]] `EXTRACTED`
- [[.reset_state()]] `EXTRACTED`
- [[.__init__()]] `EXTRACTED`

### rationale_for
- [[Manages experiment state checkpointing, allowing seamless resumption across fold]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
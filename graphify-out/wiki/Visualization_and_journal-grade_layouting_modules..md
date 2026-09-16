# Visualization and journal-grade layouting modules.

> God node · 16 connections · [D:\Codes\research_banks\is_ai-vuln\src\visualization\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/visualization/__init__.py#L1)

**Community:** [[Community 0]]

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as Visualization and journal-grade layouting modules.
    participant P1 as BaseIDSModel
    participant P2 as XGBoostIDS
    participant P3 as Instantiate a benchmark IDS model by name.
    participant P4 as LightGBMIDS
    participant P5 as MambularSSMIDS
    participant P6 as FTTransformerIDS
    participant P7 as SAINTIDS
    participant P8 as TabPFNIDS
    participant P9 as TabICLIDS
    participant P10 as GraphIDSModel
    participant P11 as Classical Gradient Boosted Decision Tree (GBDT) Baselines. Implements XGBoost an
    participant P12 as XGBoost Classifier Baseline with Optuna Tuning and Hist/GPU acceleration.
    participant P13 as LightGBM Classifier Baseline with Histogram Gradient Optimization.
    participant P14 as Deep Tabular Learning Models: Mambular SSM, FT-Transformer, and SAINT. Implement
    participant P15 as Mambular State Space Model (SSM) for Tabular Intrusion Detection.          Exhib
    participant P16 as Feature Tokenizer Transformer (FT-Transformer) for Tabular IDS.          Impleme
    participant P17 as Self-Attention and Intersample Attention Transformer (SAINT).          Computes
    participant P18 as Tabular Foundation Models for Intrusion Detection (Track A). Implements TabPFN v
    participant P19 as Tabular Prior-Data Fitted Network (TabPFN v3) Foundation Model.          Evaluat
    participant P20 as Tabular In-Context Learning (TabICL v2) with KV-Caching.          Evaluates sequ
    participant P21 as GraphIDS: Inductive Graph Neural Network Architecture for Multi-Host Lateral Mov
    participant P22 as Inductive Graph Neural Network for Correlated Multi-Host Flow Intrusion Detectio
    P0->>+ P1: uses
    P1-->>- P0: return
    P1->>+ P0: uses
    P0-->>- P1: return
    P1->>+ P2: uses
    P2-->>- P1: return
    P2->>+ P1: uses
    P1-->>- P2: return
    P2->>+ P0: uses
    P0-->>- P2: return
    P2->>+ P3: uses
    P3-->>- P2: return
    P1->>+ P4: uses
    P4-->>- P1: return
    P4->>+ P1: uses
    P1-->>- P4: return
    P4->>+ P0: uses
    P0-->>- P4: return
    P4->>+ P3: uses
    P3-->>- P4: return
    P1->>+ P5: uses
    P5-->>- P1: return
    P5->>+ P1: uses
    P1-->>- P5: return
    P5->>+ P0: uses
    P0-->>- P5: return
    P5->>+ P3: uses
    P3-->>- P5: return
    P1->>+ P6: uses
    P6-->>- P1: return
    P1->>+ P7: uses
    P7-->>- P1: return
    P1->>+ P8: uses
    P8-->>- P1: return
    P1->>+ P9: uses
    P9-->>- P1: return
    P1->>+ P10: uses
    P10-->>- P1: return
    P1->>+ P3: uses
    P3-->>- P1: return
    P1->>+ P11: uses
    P11-->>- P1: return
    P1->>+ P12: uses
    P12-->>- P1: return
    P1->>+ P13: uses
    P13-->>- P1: return
    P1->>+ P14: uses
    P14-->>- P1: return
    P1->>+ P15: uses
    P15-->>- P1: return
    P1->>+ P16: uses
    P16-->>- P1: return
    P1->>+ P17: uses
    P17-->>- P1: return
    P1->>+ P18: uses
    P18-->>- P1: return
    P1->>+ P19: uses
    P19-->>- P1: return
    P1->>+ P20: uses
    P20-->>- P1: return
    P1->>+ P21: uses
    P21-->>- P1: return
    P1->>+ P22: uses
    P22-->>- P1: return
    P0->>+ P2: uses
    P2-->>- P0: return
    P0->>+ P4: uses
    P4-->>- P0: return
    P0->>+ P8: uses
    P8-->>- P0: return
    P0->>+ P9: uses
    P9-->>- P0: return
    P0->>+ P5: uses
    P5-->>- P0: return
    P0->>+ P6: uses
    P6-->>- P0: return
    P0->>+ P7: uses
    P7-->>- P0: return
    P0->>+ P10: uses
    P10-->>- P0: return
```

## Connections by Relation

### rationale_for
- [[__init__.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`

### uses
- [[BaseIDSModel]] `INFERRED`
- [[XGBoostIDS]] `INFERRED`
- [[LightGBMIDS]] `INFERRED`
- [[TabPFNIDS]] `INFERRED`
- [[TabICLIDS]] `INFERRED`
- [[MambularSSMIDS]] `INFERRED`
- [[FTTransformerIDS]] `INFERRED`
- [[SAINTIDS]] `INFERRED`
- [[GraphIDSModel]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
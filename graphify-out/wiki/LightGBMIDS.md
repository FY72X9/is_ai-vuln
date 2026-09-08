# LightGBMIDS

> God node · 11 connections · [D:\Codes\research_banks\is_ai-vuln\src\models\classical.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py#L114)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as LightGBMIDS
    participant P1 as BaseIDSModel
    participant P2 as Visualization and journal-grade layouting modules.
    participant P3 as XGBoostIDS
    participant P4 as TabPFNIDS
    participant P5 as TabICLIDS
    participant P6 as MambularSSMIDS
    participant P7 as FTTransformerIDS
    participant P8 as SAINTIDS
    participant P9 as GraphIDSModel
    participant P10 as Instantiate a benchmark IDS model by name.
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
    P1->>+ P2: uses
    P2-->>- P1: return
    P2->>+ P1: uses
    P1-->>- P2: return
    P2->>+ P3: uses
    P3-->>- P2: return
    P2->>+ P0: uses
    P0-->>- P2: return
    P2->>+ P4: uses
    P4-->>- P2: return
    P2->>+ P5: uses
    P5-->>- P2: return
    P2->>+ P6: uses
    P6-->>- P2: return
    P2->>+ P7: uses
    P7-->>- P2: return
    P2->>+ P8: uses
    P8-->>- P2: return
    P2->>+ P9: uses
    P9-->>- P2: return
    P1->>+ P3: uses
    P3-->>- P1: return
    P3->>+ P1: uses
    P1-->>- P3: return
    P3->>+ P2: uses
    P2-->>- P3: return
    P3->>+ P10: uses
    P10-->>- P3: return
    P1->>+ P0: uses
    P0-->>- P1: return
    P1->>+ P6: uses
    P6-->>- P1: return
    P1->>+ P7: uses
    P7-->>- P1: return
    P1->>+ P8: uses
    P8-->>- P1: return
    P1->>+ P4: uses
    P4-->>- P1: return
    P1->>+ P5: uses
    P5-->>- P1: return
    P1->>+ P9: uses
    P9-->>- P1: return
    P1->>+ P10: uses
    P10-->>- P1: return
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
    P0->>+ P10: uses
    P10-->>- P0: return
```

## Connections by Relation

### contains
- [[classical.py]] `EXTRACTED`

### inherits
- [[BaseIDSModel]] `EXTRACTED`

### method
- [[._tune_with_optuna()]] `EXTRACTED`
- [[.fit()]] `EXTRACTED`
- [[.__init__()]] `EXTRACTED`
- [[.predict()]] `EXTRACTED`
- [[.predict_proba()]] `EXTRACTED`

### rationale_for
- [[LightGBM Classifier Baseline with Histogram Gradient Optimization.]] `EXTRACTED`

### uses
- [[BaseIDSModel]] `INFERRED`
- [[Visualization and journal-grade layouting modules.]] `INFERRED`
- [[Instantiate a benchmark IDS model by name.]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
# BaseIDSModel

> God node · 30 connections · [D:\Codes\research_banks\is_ai-vuln\src\models\base.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py#L19)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as BaseIDSModel
    participant P1 as Visualization and journal-grade layouting modules.
    participant P2 as XGBoostIDS
    participant P3 as Instantiate a benchmark IDS model by name.
    participant P4 as LightGBMIDS
    participant P5 as TabPFNIDS
    participant P6 as TabICLIDS
    participant P7 as MambularSSMIDS
    participant P8 as FTTransformerIDS
    participant P9 as SAINTIDS
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
    P2->>+ P0: uses
    P0-->>- P2: return
    P2->>+ P1: uses
    P1-->>- P2: return
    P2->>+ P3: uses
    P3-->>- P2: return
    P1->>+ P4: uses
    P4-->>- P1: return
    P4->>+ P0: uses
    P0-->>- P4: return
    P4->>+ P1: uses
    P1-->>- P4: return
    P4->>+ P3: uses
    P3-->>- P4: return
    P1->>+ P5: uses
    P5-->>- P1: return
    P5->>+ P0: uses
    P0-->>- P5: return
    P5->>+ P1: uses
    P1-->>- P5: return
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
    P0->>+ P2: uses
    P2-->>- P0: return
    P0->>+ P4: uses
    P4-->>- P0: return
    P0->>+ P7: uses
    P7-->>- P0: return
    P0->>+ P8: uses
    P8-->>- P0: return
    P0->>+ P9: uses
    P9-->>- P0: return
    P0->>+ P5: uses
    P5-->>- P0: return
    P0->>+ P6: uses
    P6-->>- P0: return
    P0->>+ P10: uses
    P10-->>- P0: return
    P0->>+ P3: uses
    P3-->>- P0: return
    P0->>+ P11: uses
    P11-->>- P0: return
    P0->>+ P12: uses
    P12-->>- P0: return
    P0->>+ P13: uses
    P13-->>- P0: return
    P0->>+ P14: uses
    P14-->>- P0: return
    P0->>+ P15: uses
    P15-->>- P0: return
    P0->>+ P16: uses
    P16-->>- P0: return
    P0->>+ P17: uses
    P17-->>- P0: return
    P0->>+ P18: uses
    P18-->>- P0: return
    P0->>+ P19: uses
    P19-->>- P0: return
    P0->>+ P20: uses
    P20-->>- P0: return
    P0->>+ P21: uses
    P21-->>- P0: return
    P0->>+ P22: uses
    P22-->>- P0: return
```

## Connections by Relation

### contains
- [[base.py]] `EXTRACTED`

### inherits
- [[ABC]] `EXTRACTED`

### method
- [[.cleanup()]] `EXTRACTED`
- [[.profile_inference()]] `EXTRACTED`
- [[.predict_proba()]] `EXTRACTED`
- [[.__init__()]] `EXTRACTED`
- [[.__repr__()]] `EXTRACTED`

### rationale_for
- [[Abstract Base Class for all benchmarked IDS models.]] `EXTRACTED`

### uses
- [[Visualization and journal-grade layouting modules.]] `INFERRED`
- [[XGBoostIDS]] `INFERRED`
- [[LightGBMIDS]] `INFERRED`
- [[MambularSSMIDS]] `INFERRED`
- [[FTTransformerIDS]] `INFERRED`
- [[SAINTIDS]] `INFERRED`
- [[TabPFNIDS]] `INFERRED`
- [[TabICLIDS]] `INFERRED`
- [[GraphIDSModel]] `INFERRED`
- [[Instantiate a benchmark IDS model by name.]] `INFERRED`
- [[Classical Gradient Boosted Decision Tree (GBDT) Baselines. Implements XGBoost an]] `INFERRED`
- [[XGBoost Classifier Baseline with Optuna Tuning and Hist/GPU acceleration.]] `INFERRED`
- [[LightGBM Classifier Baseline with Histogram Gradient Optimization.]] `INFERRED`
- [[Deep Tabular Learning Models: Mambular SSM, FT-Transformer, and SAINT. Implement]] `INFERRED`
- [[Mambular State Space Model (SSM) for Tabular Intrusion Detection.          Exhib]] `INFERRED`
- [[Feature Tokenizer Transformer (FT-Transformer) for Tabular IDS.          Impleme]] `INFERRED`
- [[Self-Attention and Intersample Attention Transformer (SAINT).          Computes]] `INFERRED`
- [[Tabular Foundation Models for Intrusion Detection (Track A). Implements TabPFN v]] `INFERRED`
- [[Tabular Prior-Data Fitted Network (TabPFN v3) Foundation Model.          Evaluat]] `INFERRED`
- [[Tabular In-Context Learning (TabICL v2) with KV-Caching.          Evaluates sequ]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
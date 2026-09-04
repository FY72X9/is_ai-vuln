# fit_fold_isolated_pipeline()

> God node · 5 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\splitters.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/splitters.py#L137)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as fit_fold_isolated_pipeline()
    participant P1 as PureNumPyStandardScaler
    participant P2 as .fit_transform()
    participant P3 as .transform()
    participant P4 as .fit()
    P0->>+ P1: calls
    P1-->>- P0: return
    P1->>+ P0: calls
    P0-->>- P1: return
    P0->>+ P2: calls
    P2-->>- P0: return
    P2->>+ P0: calls
    P0-->>- P2: return
    P2->>+ P3: calls
    P3-->>- P2: return
    P3->>+ P0: calls
    P0-->>- P3: return
    P3->>+ P2: calls
    P2-->>- P3: return
    P2->>+ P4: calls
    P4-->>- P2: return
    P4->>+ P2: calls
    P2-->>- P4: return
    P0->>+ P3: calls
    P3-->>- P0: return
```

## Connections by Relation

### calls
- [[PureNumPyStandardScaler]] `EXTRACTED`
- [[.fit_transform()]] `EXTRACTED`
- [[.transform()]] `EXTRACTED`

### contains
- [[splitters.py]] `EXTRACTED`

### rationale_for
- [[Fit scaler and sampler STRICTLY within the train split, preventing leakage to va]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
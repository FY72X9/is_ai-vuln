# PureNumPyStandardScaler

> God node · 7 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\splitters.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/splitters.py#L47)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as PureNumPyStandardScaler
    participant P1 as fit_fold_isolated_pipeline()
    participant P2 as .fit_transform()
    participant P3 as .transform()
    participant P4 as .fit()
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
    P1->>+ P3: calls
    P3-->>- P1: return
    P3->>+ P1: calls
    P1-->>- P3: return
    P3->>+ P2: calls
    P2-->>- P3: return
```

## Connections by Relation

### calls
- [[fit_fold_isolated_pipeline()]] `EXTRACTED`

### contains
- [[splitters.py]] `EXTRACTED`

### method
- [[.fit_transform()]] `EXTRACTED`
- [[.transform()]] `EXTRACTED`
- [[.fit()]] `EXTRACTED`
- [[.__init__()]] `EXTRACTED`

### rationale_for
- [[Pure NumPy implementation of standard scaler for isolated or minimal environment]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
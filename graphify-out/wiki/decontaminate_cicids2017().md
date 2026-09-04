# decontaminate_cicids2017()

> God node · 4 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\cleaner.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/cleaner.py#L23)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as decontaminate_cicids2017()
    participant P1 as clean_column_names()
    participant P2 as clean_dataset()
    P0->>+ P1: calls
    P1-->>- P0: return
    P1->>+ P0: calls
    P0-->>- P1: return
    P1->>+ P2: calls
    P2-->>- P1: return
    P2->>+ P0: calls
    P0-->>- P2: return
    P2->>+ P1: calls
    P1-->>- P2: return
    P0->>+ P2: calls
    P2-->>- P0: return
```

## Connections by Relation

### calls
- [[clean_column_names()]] `EXTRACTED`
- [[clean_dataset()]] `EXTRACTED`

### contains
- [[cleaner.py]] `EXTRACTED`

### rationale_for
- [[Clean and decontaminate CICIDS2017 dataset according to SPW 2021 and TIFS 2022 f]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
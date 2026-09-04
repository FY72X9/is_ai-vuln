# clean_column_names()

> God node · 4 connections · [D:\Codes\research_banks\is_ai-vuln\src\data\cleaner.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/cleaner.py#L17)

## Call Trace Diagram

```mermaid
sequenceDiagram
    participant P0 as clean_column_names()
    participant P1 as decontaminate_cicids2017()
    participant P2 as clean_dataset()
    P0->>+ P1: calls
    P1-->>- P0: return
    P1->>+ P0: calls
    P0-->>- P1: return
    P1->>+ P2: calls
    P2-->>- P1: return
    P2->>+ P1: calls
    P1-->>- P2: return
    P2->>+ P0: calls
    P0-->>- P2: return
    P0->>+ P2: calls
    P2-->>- P0: return
```

## Connections by Relation

### calls
- [[decontaminate_cicids2017()]] `EXTRACTED`
- [[clean_dataset()]] `EXTRACTED`

### contains
- [[cleaner.py]] `EXTRACTED`

### rationale_for
- [[Strip extraneous whitespace and special characters from DataFrame column headers]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
# Community 0

> 75 nodes · cohesion 0.05

## Key Concepts

- [BaseIDSModel](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py#L19) (30 connections)
- [Visualization and journal-grade layouting modules.](file:///D:/Codes/research_banks/is_ai-vuln/src/visualization/__init__.py#L1) (16 connections)
- [LightGBMIDS](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py#L114) (11 connections)
- [XGBoostIDS](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py#L16) (11 connections)
- [FTTransformerIDS](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py#L131) (10 connections)
- [MambularSSMIDS](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py#L16) (10 connections)
- [SAINTIDS](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py#L221) (10 connections)
- [TabICLIDS](file:///D:/Codes/research_banks/is_ai-vuln/src/models/foundation.py#L99) (10 connections)
- [TabPFNIDS](file:///D:/Codes/research_banks/is_ai-vuln/src/models/foundation.py#L16) (10 connections)
- [GraphIDSModel](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L16) (10 connections)
- [Instantiate a benchmark IDS model by name.](file:///D:/Codes/research_banks/is_ai-vuln/src/models/__init__.py#L26) (10 connections)
- **BaseIDSModel** (8 connections)
- [.predict_proba()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py#L306) (6 connections)
- [base.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py#L1) (5 connections)
- [deep_tabular.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py#L1) (4 connections)
- [.predict_proba()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/foundation.py#L139) (4 connections)
- [.predict_proba()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py#L40) (3 connections)
- [predict()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py#L36) (3 connections)
- [.fit()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py#L165) (3 connections)
- [._tune_with_optuna()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py#L131) (3 connections)
- [.fit()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py#L72) (3 connections)
- [classical.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py#L1) (3 connections)
- [foundation.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/foundation.py#L1) (3 connections)
- [.fit()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py#L232) (3 connections)
- [.__init__()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py#L227) (3 connections)
- *... and 50 more nodes in this community*

## Class Diagram

```mermaid
classDiagram
    class BaseIDSModel {
        +base.py()
        +.__init__()
        +.predict_proba()
        +.profile_inference()
        +.cleanup()
        +.__repr__()
    }
    class LightGBMIDS {
        +classical.py()
        +.__init__()
        +._tune_with_optuna()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class XGBoostIDS {
        +classical.py()
        +.__init__()
        +._tune_with_optuna()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class FTTransformerIDS {
        +deep_tabular.py()
        +.__init__()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class MambularSSMIDS {
        +deep_tabular.py()
        +.__init__()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class SAINTIDS {
        +deep_tabular.py()
        +.__init__()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class TabICLIDS {
        +foundation.py()
        +.__init__()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class TabPFNIDS {
        +foundation.py()
        +.__init__()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class GraphIDSModel {
        +graph_ids.py()
        +.__init__()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    BaseIDSModel --> XGBoostIDS
    BaseIDSModel --> LightGBMIDS
    BaseIDSModel --> MambularSSMIDS
    BaseIDSModel --> FTTransformerIDS
    BaseIDSModel --> SAINTIDS
    BaseIDSModel --> TabPFNIDS
    BaseIDSModel --> TabICLIDS
    BaseIDSModel --> GraphIDSModel
    LightGBMIDS --> BaseIDSModel
    XGBoostIDS --> BaseIDSModel
    FTTransformerIDS --> BaseIDSModel
    MambularSSMIDS --> BaseIDSModel
    SAINTIDS --> BaseIDSModel
    TabICLIDS --> BaseIDSModel
    TabPFNIDS --> BaseIDSModel
    GraphIDSModel --> BaseIDSModel
```

## Relationships

- [[Community 12]] (2 shared connections)

## Source Files

- [D:\Codes\research_banks\is_ai-vuln\src\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/__init__.py)
- [D:\Codes\research_banks\is_ai-vuln\src\data\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/__init__.py)
- [D:\Codes\research_banks\is_ai-vuln\src\dematel\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/dematel/__init__.py)
- [D:\Codes\research_banks\is_ai-vuln\src\evaluation\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/evaluation/__init__.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/__init__.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\base.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\classical.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/classical.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\deep_tabular.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/deep_tabular.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\foundation.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/foundation.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\graph_ids.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py)
- [D:\Codes\research_banks\is_ai-vuln\src\utils\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/utils/__init__.py)
- [D:\Codes\research_banks\is_ai-vuln\src\visualization\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/visualization/__init__.py)

## Audit Trail

- EXTRACTED: 204 (73%)
- INFERRED: 76 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
# Community 1

> 39 nodes · cohesion 0.07

## Key Concepts

- [run_tests()](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_full_pipeline.py#L36) (16 connections)
- [GraphIDSModel](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L16) (10 connections)
- [test_all_models()](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_models.py#L19) (9 connections)
- [StreamingChunkLoader](file:///D:/Codes/research_banks/is_ai-vuln/src/data/streaming_loader.py#L15) (7 connections)
- [.cleanup()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py#L111) (6 connections)
- [run_causal_triangulation()](file:///D:/Codes/research_banks/is_ai-vuln/src/dematel/causal_validation.py#L104) (5 connections)
- [robustness.py](file:///D:/Codes/research_banks/is_ai-vuln/src/evaluation/robustness.py#L1) (5 connections)
- [.fit()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L27) (5 connections)
- [.predict()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L74) (5 connections)
- [evaluate_robustness_degradation_slope()](file:///D:/Codes/research_banks/is_ai-vuln/src/evaluation/robustness.py#L39) (5 connections)
- [run_component_ablation_sweep()](file:///D:/Codes/research_banks/is_ai-vuln/src/evaluation/robustness.py#L73) (5 connections)
- [get_model()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/__init__.py#L25) (4 connections)
- [inject_gaussian_noise()](file:///D:/Codes/research_banks/is_ai-vuln/src/evaluation/robustness.py#L14) (4 connections)
- [.iter_chunks()](file:///D:/Codes/research_banks/is_ai-vuln/src/data/streaming_loader.py#L30) (4 connections)
- [streaming_loader.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/streaming_loader.py#L1) (3 connections)
- [.predict_proba()](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L80) (3 connections)
- [generate_scalable_synthetic_partition()](file:///D:/Codes/research_banks/is_ai-vuln/src/data/streaming_loader.py#L108) (3 connections)
- [test_full_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_full_pipeline.py#L1) (2 connections)
- [graph_ids.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L1) (2 connections)
- [__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/__init__.py#L1) (2 connections)
- [GraphIDS: Inductive Graph Neural Network Architecture for Multi-Host Lateral Mov](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L1) (2 connections)
- [Inductive Graph Neural Network for Correlated Multi-Host Flow Intrusion Detectio](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py#L17) (2 connections)
- [inject_feature_corruption()](file:///D:/Codes/research_banks/is_ai-vuln/src/evaluation/robustness.py#L27) (2 connections)
- [._extract_features_and_target()](file:///D:/Codes/research_banks/is_ai-vuln/src/data/streaming_loader.py#L97) (2 connections)
- [Comprehensive Full-Pipeline Verification Test Suite. Verifies streaming data loa](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_full_pipeline.py#L1) (2 connections)
- *... and 14 more nodes in this community*

## Class Diagram

```mermaid
classDiagram
    class GraphIDSModel {
        +graph_ids.py()
        +.__init__()
        +.fit()
        +.predict()
        +.predict_proba()
    }
    class StreamingChunkLoader {
        +streaming_loader.py()
        +.__init__()
        +.iter_chunks()
        +._extract_features_and_target()
    }
```

## Relationships

- [[Community 4]] (2 shared connections)

## Source Files

- [D:\Codes\research_banks\is_ai-vuln\scratch\test_full_pipeline.py](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_full_pipeline.py)
- [D:\Codes\research_banks\is_ai-vuln\scratch\test_models.py](file:///D:/Codes/research_banks/is_ai-vuln/scratch/test_models.py)
- [D:\Codes\research_banks\is_ai-vuln\src\data\streaming_loader.py](file:///D:/Codes/research_banks/is_ai-vuln/src/data/streaming_loader.py)
- [D:\Codes\research_banks\is_ai-vuln\src\dematel\causal_validation.py](file:///D:/Codes/research_banks/is_ai-vuln/src/dematel/causal_validation.py)
- [D:\Codes\research_banks\is_ai-vuln\src\evaluation\robustness.py](file:///D:/Codes/research_banks/is_ai-vuln/src/evaluation/robustness.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\__init__.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/__init__.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\base.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/base.py)
- [D:\Codes\research_banks\is_ai-vuln\src\models\graph_ids.py](file:///D:/Codes/research_banks/is_ai-vuln/src/models/graph_ids.py)

## Audit Trail

- EXTRACTED: 74 (57%)
- INFERRED: 55 (43%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
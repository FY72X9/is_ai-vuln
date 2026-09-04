# Graph Report - .  (2026-09-04)

## Corpus Check
- Corpus is ~5,682 words - fits in a single context window. You may not need a graph.

## Summary
- 22 nodes · 23 edges · 5 communities (4 shown, 1 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 5,682 input · 1,250 output

## Community Hubs (Navigation)
- Modern AI Models & Benchmarks
- Q1 Strategy & Audit
- Statistical Validation & Rigor
- Fuzzy DEMATEL Causal Modeling
- Reproducibility & Repository Architecture

## God Nodes (most connected - your core abstractions)
1. `is_ai-vuln Project Overview` - 12 edges
2. `Fuzzy DEMATEL` - 4 edges
3. `Q1 Readiness Audit & Gap Analysis` - 4 edges
4. `Repository Directory Structure` - 2 edges
5. `TabPFN v3` - 2 edges
6. `TabICL v2` - 2 edges
7. `Mambular (Mamba SSM)` - 2 edges
8. `FT-Transformer` - 2 edges
9. `Friedman & Nemenyi Statistical Tests` - 2 edges
10. `Target Q1 Journals (IEEE ComSurv, InfoFusion, JSAC)` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Colab Reproducibility Package` --semantically_similar_to--> `Repository Directory Structure`  [INFERRED] [semantically similar]
  docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md → README.md
- `is_ai-vuln Project Overview` --references--> `CICIDS2017 Dataset`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md
- `is_ai-vuln Project Overview` --references--> `FT-Transformer`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md
- `is_ai-vuln Project Overview` --references--> `Fuzzy DEMATEL`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md
- `is_ai-vuln Project Overview` --references--> `GraphIDS`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md

## Hyperedges (group relationships)
- **Modern Tabular & Graph AI Architectures (2025-2026)** — docs_research_blueprint_is_cs_q1_2026_final_v3_tabpfn_v3, docs_research_blueprint_is_cs_q1_2026_final_v3_tabicl_v2, docs_research_blueprint_is_cs_q1_2026_final_v3_graphids, docs_research_blueprint_is_cs_q1_2026_final_v3_saint, docs_research_blueprint_is_cs_q1_2026_final_v3_mambular, docs_research_blueprint_is_cs_q1_2026_final_v3_ft_transformer [EXTRACTED 1.00]
- **Network Intrusion Benchmark Datasets** — docs_research_blueprint_is_cs_q1_2026_final_v3_nsl_kdd, docs_research_blueprint_is_cs_q1_2026_final_v3_cicids2017, docs_research_blueprint_is_cs_q1_2026_final_v3_unsw_nb15 [EXTRACTED 1.00]
- **Q1 Statistical Rigor & Robustness Framework** — docs_research_blueprint_is_cs_q1_2026_final_v3_stratified_5fold_cv, docs_research_blueprint_is_cs_q1_2026_final_v3_friedman_nemenyi_tests, docs_research_blueprint_is_cs_q1_2026_final_v3_ablation_and_robustness, docs_research_blueprint_is_cs_q1_2026_final_v3_q1_readiness_audit [EXTRACTED 1.00]

## Communities (5 total, 1 thin omitted)

### Community 0 - "Modern AI Models & Benchmarks"
Cohesion: 0.24
Nodes (10): CICIDS2017 Dataset, FT-Transformer, GraphIDS, Mambular (Mamba SSM), NSL-KDD Dataset, SAINT, TabICL v2, TabPFN v3 (+2 more)

### Community 1 - "Q1 Strategy & Audit"
Cohesion: 0.50
Nodes (4): Contribution Triangle, OpenAlex & Semantic Scholar Bibliometrics, Target Q1 Journals (IEEE ComSurv, InfoFusion, JSAC), Q1 Readiness Audit & Gap Analysis

### Community 2 - "Statistical Validation & Rigor"
Cohesion: 0.67
Nodes (3): Ablation Study & Robustness Analysis, Friedman & Nemenyi Statistical Tests, 5-Fold Stratified Cross-Validation

### Community 3 - "Fuzzy DEMATEL Causal Modeling"
Cohesion: 0.67
Nodes (3): Causal Network & Prominence-Relation Map, Fuzzy DEMATEL, Triangular Fuzzy Numbers (TFN)

## Knowledge Gaps
- **12 isolated node(s):** `GraphIDS`, `SAINT`, `Triangular Fuzzy Numbers (TFN)`, `Causal Network & Prominence-Relation Map`, `NSL-KDD Dataset` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `is_ai-vuln Project Overview` connect `Modern AI Models & Benchmarks` to `Q1 Strategy & Audit`, `Fuzzy DEMATEL Causal Modeling`, `Reproducibility & Repository Architecture`?**
  _High betweenness centrality (0.614) - this node is a cross-community bridge._
- **Why does `Q1 Readiness Audit & Gap Analysis` connect `Q1 Strategy & Audit` to `Modern AI Models & Benchmarks`, `Fuzzy DEMATEL Causal Modeling`?**
  _High betweenness centrality (0.224) - this node is a cross-community bridge._
- **Why does `Fuzzy DEMATEL` connect `Fuzzy DEMATEL Causal Modeling` to `Modern AI Models & Benchmarks`, `Q1 Strategy & Audit`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **What connects `GraphIDS`, `SAINT`, `Triangular Fuzzy Numbers (TFN)` to the rest of the system?**
  _12 weakly-connected nodes found - possible documentation gaps or missing edges._
# Graph Report - D:\Codes\research_banks\is_ai-vuln  (2026-09-04)

## Corpus Check
- 16 files · ~27,778 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 119 nodes · 127 edges · 13 communities detected
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)
1. `is_ai-vuln Project Overview` - 12 edges
2. `CheckpointManager` - 10 edges
3. `Visualization and journal-grade layouting modules.` - 7 edges
4. `PureNumPyStandardScaler` - 7 edges
5. `fit_fold_isolated_pipeline()` - 5 edges
6. `clean_column_names()` - 4 edges
7. `decontaminate_cicids2017()` - 4 edges
8. `clean_dataset()` - 4 edges
9. `AntiLeakageGroupKFold` - 4 edges
10. `AntiLeakageTimeSeriesSplit` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Colab Reproducibility Package` --semantically_similar_to--> `Repository Directory Structure`  [INFERRED] [semantically similar]
  docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md → README.md
- `is_ai-vuln Project Overview` --references--> `CICIDS2017 Dataset`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md
- `is_ai-vuln Project Overview` --references--> `FT-Transformer`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md
- `is_ai-vuln Project Overview` --references--> `GraphIDS`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md
- `is_ai-vuln Project Overview` --references--> `Mambular (Mamba SSM)`  [EXTRACTED]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md

## Hyperedges (group relationships)
- **Modern Tabular & Graph AI Architectures (2025-2026)** — docs_research_blueprint_is_cs_q1_2026_final_v3_tabpfn_v3, docs_research_blueprint_is_cs_q1_2026_final_v3_tabicl_v2, docs_research_blueprint_is_cs_q1_2026_final_v3_graphids, docs_research_blueprint_is_cs_q1_2026_final_v3_saint, docs_research_blueprint_is_cs_q1_2026_final_v3_mambular, docs_research_blueprint_is_cs_q1_2026_final_v3_ft_transformer [EXTRACTED 1.00]
- **Network Intrusion Benchmark Datasets** — docs_research_blueprint_is_cs_q1_2026_final_v3_nsl_kdd, docs_research_blueprint_is_cs_q1_2026_final_v3_cicids2017, docs_research_blueprint_is_cs_q1_2026_final_v3_unsw_nb15 [EXTRACTED 1.00]
- **Q1 Statistical Rigor & Robustness Framework** — docs_research_blueprint_is_cs_q1_2026_final_v3_stratified_5fold_cv, docs_research_blueprint_is_cs_q1_2026_final_v3_friedman_nemenyi_tests, docs_research_blueprint_is_cs_q1_2026_final_v3_ablation_and_robustness, docs_research_blueprint_is_cs_q1_2026_final_v3_q1_readiness_audit [EXTRACTED 1.00]

## Communities

### Community 0 - "Community 0"

Cohesion: 0.13
Nodes (10): CheckpointManager, State Checkpointing & Fault-Tolerant Autorecovery Pipeline for Google Colab and, Load state from disk if exists, otherwise initialize clean state schema., Check whether all folds for a given model have been completed., Check whether a specific fold for a given model has already completed., Record the completion of a fold, update metrics, and persist to disk., Manages experiment state checkpointing, allowing seamless resumption across fold, Mark the entire track for this dataset as completed. (+2 more)

### Community 1 - "Community 1"

Cohesion: 0.12
Nodes (19): Causal Network & Prominence-Relation Map, CICIDS2017 Dataset, Contribution Triangle, FT-Transformer, Fuzzy DEMATEL, GraphIDS, Mambular (Mamba SSM), NSL-KDD Dataset (+11 more)

### Community 2 - "Community 2"

Cohesion: 0.2
Nodes (9): extract_subnet_mask(), fit_fold_isolated_pipeline(), PureNumPyStandardScaler, Anti-Leakage Data Partitioning Suite. Implements Subnet-Grouped and Time-Aware K, Fit scaler and sampler STRICTLY within the train split, preventing leakage to va, Safely slice pandas DataFrame, Series, or NumPy ndarray by integer indices., Extract subnet group from IPv4 address string (default /24 mask)., Pure NumPy implementation of standard scaler for isolated or minimal environment (+1 more)

### Community 3 - "Community 3"

Cohesion: 0.2
Nodes (6): AntiLeakageGroupKFold, AntiLeakageTimeSeriesSplit, Time-aware chronological cross-validator without future-looking data leakage., Generate sequential train/validation split indices., GroupKFold cross-validator grouped by IP subnets or Host IDs to prevent session, Generate train/validation indices grouped by subnet/host.

### Community 4 - "Community 4"

Cohesion: 0.25
Nodes (1): Visualization and journal-grade layouting modules.

### Community 5 - "Community 5"

Cohesion: 0.36
Nodes (7): clean_column_names(), clean_dataset(), decontaminate_cicids2017(), Data Cleaning & Decontamination Pipeline. Addresses known anomalies in intrusion, Strip extraneous whitespace and special characters from DataFrame column headers, Clean and decontaminate CICIDS2017 dataset according to SPW 2021 and TIFS 2022 f, Universal cleaning dispatcher for benchmark datasets.

### Community 6 - "Community 6"

Cohesion: 0.29
Nodes (7): ensure_gitignore_safeguards(), initialize_dataset_directories(), Drive Dataset Retrieval, Checksum Verification & Automatic .gitignore Safeguards, Ensure data directories exist and safeguards are active., Check and automatically append required exclusion rules to .gitignore., Verify SHA-256 checksum of a downloaded file., verify_file_sha256()

### Community 7 - "Community 7"

Cohesion: 0.29
Nodes (7): flush_memory(), is_colab(), Environment initialization and hardware-runtime abstraction for Google Colab and, Initialize storage directories, Google Drive mounting (if Colab), and memory saf, Trigger Python garbage collection and flush CUDA cache to avoid OOM., Check if the current runtime is Google Colab., setup_environment()

### Community 8 - "Community 8"

Cohesion: 0.33
Nodes (5): build_networkx_flow_graph(), export_to_pyg_tensors(), Graph Construction Engine for GraphIDS. Converts tabular NetFlow records into to, Construct a directed network interaction graph from NetFlow DataFrame.      Args, Convert NetworkX flow graph to edge index and feature arrays (PyG compatible).

### Community 9 - "Community 9"

Cohesion: 0.4
Nodes (5): format_bibtex_entry(), harvest_and_build_library(), Metadata Harvester for Academic References using OpenAlex and CrossRef REST APIs, Format reference dict into a clean BibTeX entry., Harvest metadata from OpenAlex / CrossRef where available and build references/l

### Community 10 - "Community 10"

Cohesion: 0.33
Nodes (5): Journal-grade publication figure styling for IEEE / ACM / Elsevier Q1 venues., Save figure simultaneously in vector PDF format and high-res PNG preview., Apply IEEE/Nature publication styling to matplotlib rcParams.          Args:, save_publication_figure(), set_publication_style()

### Community 11 - "Community 11"

Cohesion: 0.5
Nodes (3): Academic Citation Integrity & Retraction Validator. Verifies DOI resolution via, Validate all references in the provided list for DOI resolution and retraction s, validate_references()

### Community 12 - "Community 12"

Cohesion: 0.67
Nodes (3): Ablation Study & Robustness Analysis, Friedman & Nemenyi Statistical Tests, 5-Fold Stratified Cross-Validation

## Knowledge Gaps
- **53 isolated node(s):** `Data Cleaning & Decontamination Pipeline. Addresses known anomalies in intrusion`, `Strip extraneous whitespace and special characters from DataFrame column headers`, `Clean and decontaminate CICIDS2017 dataset according to SPW 2021 and TIFS 2022 f`, `Universal cleaning dispatcher for benchmark datasets.`, `Drive Dataset Retrieval, Checksum Verification & Automatic .gitignore Safeguards` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components.
# Graph Report - D:\Codes\research_banks\is_ai-vuln  (2026-09-08)

## Corpus Check
- 35 files · ~54,601 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 309 nodes · 442 edges · 26 communities detected
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 94 edges (avg confidence: 0.67)
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
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]

## God Nodes (most connected - your core abstractions)
1. `BaseIDSModel` - 30 edges
2. `run_tests()` - 16 edges
3. `Visualization and journal-grade layouting modules.` - 16 edges
4. `is_ai-vuln Project Overview` - 12 edges
5. `run_closed_loop_fuzzy_dematel()` - 11 edges
6. `XGBoostIDS` - 11 edges
7. `LightGBMIDS` - 11 edges
8. `run_preparation_pipeline()` - 10 edges
9. `MambularSSMIDS` - 10 edges
10. `FTTransformerIDS` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Tabular Foundation Models for Intrusion Detection (Track A). Implements TabPFN v` --uses--> `BaseIDSModel`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\foundation.py → D:\Codes\research_banks\is_ai-vuln\src\models\base.py
- `Tabular Prior-Data Fitted Network (TabPFN v3) Foundation Model.          Evaluat` --uses--> `BaseIDSModel`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\foundation.py → D:\Codes\research_banks\is_ai-vuln\src\models\base.py
- `Tabular In-Context Learning (TabICL v2) with KV-Caching.          Evaluates sequ` --uses--> `BaseIDSModel`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\foundation.py → D:\Codes\research_banks\is_ai-vuln\src\models\base.py
- `GraphIDS: Inductive Graph Neural Network Architecture for Multi-Host Lateral Mov` --uses--> `BaseIDSModel`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\graph_ids.py → D:\Codes\research_banks\is_ai-vuln\src\models\base.py
- `Inductive Graph Neural Network for Correlated Multi-Host Flow Intrusion Detectio` --uses--> `BaseIDSModel`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\graph_ids.py → D:\Codes\research_banks\is_ai-vuln\src\models\base.py

## Hyperedges (group relationships)
- **Modern Tabular & Graph AI Architectures (2025-2026)** — docs_research_blueprint_is_cs_q1_2026_final_v3_tabpfn_v3, docs_research_blueprint_is_cs_q1_2026_final_v3_tabicl_v2, docs_research_blueprint_is_cs_q1_2026_final_v3_graphids, docs_research_blueprint_is_cs_q1_2026_final_v3_saint, docs_research_blueprint_is_cs_q1_2026_final_v3_mambular, docs_research_blueprint_is_cs_q1_2026_final_v3_ft_transformer [EXTRACTED 1.00]
- **Network Intrusion Benchmark Datasets** — docs_research_blueprint_is_cs_q1_2026_final_v3_nsl_kdd, docs_research_blueprint_is_cs_q1_2026_final_v3_cicids2017, docs_research_blueprint_is_cs_q1_2026_final_v3_unsw_nb15 [EXTRACTED 1.00]
- **Q1 Statistical Rigor & Robustness Framework** — docs_research_blueprint_is_cs_q1_2026_final_v3_stratified_5fold_cv, docs_research_blueprint_is_cs_q1_2026_final_v3_friedman_nemenyi_tests, docs_research_blueprint_is_cs_q1_2026_final_v3_ablation_and_robustness, docs_research_blueprint_is_cs_q1_2026_final_v3_q1_readiness_audit [EXTRACTED 1.00]

## Communities

### Community 0 - "Community 0"

Cohesion: 0.07
Nodes (17): BaseIDSModel, Abstract Base Class for all benchmarked IDS models., BaseIDSModel, LightGBMIDS, Classical Gradient Boosted Decision Tree (GBDT) Baselines. Implements XGBoost an, LightGBM Classifier Baseline with Histogram Gradient Optimization., XGBoost Classifier Baseline with Optuna Tuning and Hist/GPU acceleration., XGBoostIDS (+9 more)

### Community 1 - "Community 1"

Cohesion: 0.07
Nodes (25): Release weights and garbage collect GPU/CPU memory., Run DirectLiNGAM causal discovery and calculate SHD against Fuzzy DEMATEL digrap, run_causal_triangulation(), GraphIDSModel, GraphIDS: Inductive Graph Neural Network Architecture for Multi-Host Lateral Mov, Inductive Graph Neural Network for Correlated Multi-Host Flow Intrusion Detectio, get_model(), evaluate_robustness_degradation_slope() (+17 more)

### Community 2 - "Community 2"

Cohesion: 0.07
Nodes (26): create_code_cell(), create_markdown_cell(), generate_notebook(), Generator script for src/notebook/02_phase2_track_a_benchmark_colab.ipynb., build_networkx_flow_graph(), export_to_pyg_tensors(), Graph Construction Engine for GraphIDS. Converts tabular NetFlow records into to, Construct a directed network interaction graph from NetFlow DataFrame.      Args (+18 more)

### Community 3 - "Community 3"

Cohesion: 0.08
Nodes (30): construct_axiomatic_prior_matrix(), Axiomatic Theoretical Prior Matrix (W_theory) for Autonomous Closed-Loop Fuzzy D, Derive the 8x8 theoretical causal prior matrix W_theory.          Self-influence, _calculate_kendalls_w(), compute_structural_hamming_distance(), Monte Carlo Robustness Proof & DirectLiNGAM Algorithmic Causal Triangulation. Va, Execute 10,000 Monte Carlo perturbation iterations to prove stability of promine, Calculate Kendall's W concordance coefficient across m raters for n items. (+22 more)

### Community 4 - "Community 4"

Cohesion: 0.13
Nodes (10): CheckpointManager, State Checkpointing & Fault-Tolerant Autorecovery Pipeline for Google Colab and, Load state from disk if exists, otherwise initialize clean state schema., Check whether all folds for a given model have been completed., Check whether a specific fold for a given model has already completed., Record the completion of a fold, update metrics, and persist to disk., Manages experiment state checkpointing, allowing seamless resumption across fold, Mark the entire track for this dataset as completed. (+2 more)

### Community 5 - "Community 5"

Cohesion: 0.12
Nodes (19): Causal Network & Prominence-Relation Map, CICIDS2017 Dataset, Contribution Triangle, FT-Transformer, Fuzzy DEMATEL, GraphIDS, Mambular (Mamba SSM), NSL-KDD Dataset (+11 more)

### Community 6 - "Community 6"

Cohesion: 0.14
Nodes (14): plot_causal_network_digraph(), Render publication-grade causal network digraph with prominent cause-effect node, Journal-grade publication figure styling for IEEE / ACM / Elsevier Q1 venues., Save figure simultaneously in vector PDF format and high-res PNG preview., Apply IEEE/Nature publication styling to matplotlib rcParams.          Args:, save_publication_figure(), set_publication_style(), compute_friedman_test() (+6 more)

### Community 7 - "Community 7"

Cohesion: 0.2
Nodes (13): download_file(), ensure_gitignore_safeguards(), generate_synthetic_benchmark_sample(), initialize_dataset_directories(), prepare_benchmark_dataset(), Drive Dataset Retrieval, Checksum Verification & Automatic .gitignore Safeguards, Download a file with retry mechanism and SHA256 verification., Generate realistic synthetic NetFlow records for offline pipeline testing and Co (+5 more)

### Community 8 - "Community 8"

Cohesion: 0.21
Nodes (5): Tabular Foundation Models for Intrusion Detection (Track A). Implements TabPFN v, Tabular In-Context Learning (TabICL v2) with KV-Caching.          Evaluates sequ, Tabular Prior-Data Fitted Network (TabPFN v3) Foundation Model.          Evaluat, TabICLIDS, TabPFNIDS

### Community 9 - "Community 9"

Cohesion: 0.56
Nodes (8): build_nb03(), build_nb04(), build_nb05(), build_nb06(), code_cell(), md_cell(), Batch Generator for Google Colab Notebooks: Notebooks 03, 04, 05, 06., write_nb()

### Community 10 - "Community 10"

Cohesion: 0.22
Nodes (5): ABC, predict(), Unified Base Model Interface for Intrusion Detection Models. Standardizes traini, Generate prediction probability distributions. Fallback to binary indicator if u, Profile inference latency (ms/flow), throughput (flows/sec), and peak VRAM/RAM.

### Community 11 - "Community 11"

Cohesion: 0.36
Nodes (7): clean_column_names(), clean_dataset(), decontaminate_cicids2017(), Data Cleaning & Decontamination Pipeline. Addresses known anomalies in intrusion, Strip extraneous whitespace and special characters from DataFrame column headers, Clean and decontaminate CICIDS2017 dataset according to SPW 2021 and TIFS 2022 f, Universal cleaning dispatcher for benchmark datasets.

### Community 12 - "Community 12"

Cohesion: 0.29
Nodes (7): calculate_ttf_utility(), evaluate_classification_metrics(), evaluate_fold_run(), Evaluation Metrics and Task-Technology Fit (TTF) Utility Engine. Computes standa, Calculate comprehensive classification metrics., Combine classification metrics with inference profiling into standard telemetry, Compute formal Task-Technology Fit utility score according to Blueprint v4.0.

### Community 13 - "Community 13"

Cohesion: 0.29
Nodes (7): flush_memory(), is_colab(), Environment initialization and hardware-runtime abstraction for Google Colab and, Initialize storage directories, Google Drive mounting (if Colab), and memory saf, Trigger Python garbage collection and flush CUDA cache to avoid OOM., Check if the current runtime is Google Colab., setup_environment()

### Community 14 - "Community 14"

Cohesion: 0.4
Nodes (5): format_bibtex_entry(), harvest_and_build_library(), Metadata Harvester for Academic References using OpenAlex and CrossRef REST APIs, Format reference dict into a clean BibTeX entry., Harvest metadata from OpenAlex / CrossRef where available and build references/l

### Community 15 - "Community 15"

Cohesion: 0.5
Nodes (3): Academic Citation Integrity & Retraction Validator. Verifies DOI resolution via, Validate all references in the provided list for DOI resolution and retraction s, validate_references()

### Community 16 - "Community 16"

Cohesion: 0.5
Nodes (3): export_benchmark_to_latex(), Automated LaTeX Table Generation for Q1 Journal Publication. Generates professio, Format DataFrame into publication-grade LaTeX table with booktabs.

### Community 17 - "Community 17"

Cohesion: 0.67
Nodes (3): Ablation Study & Robustness Analysis, Friedman & Nemenyi Statistical Tests, 5-Fold Stratified Cross-Validation

### Community 18 - "Community 18"

Cohesion: 1.0
Nodes (1): Train the model on the provided training partition.

### Community 19 - "Community 19"

Cohesion: 1.0
Nodes (1): Generate hard binary / multi-class predictions.

### Community 20 - "Community 20"

Cohesion: 1.0
Nodes (1): Check and automatically append required exclusion rules to .gitignore.

### Community 21 - "Community 21"

Cohesion: 1.0
Nodes (1): Verify SHA-256 checksum of a downloaded file.

### Community 22 - "Community 22"

Cohesion: 1.0
Nodes (1): Ensure data directories exist and safeguards are active.

### Community 23 - "Community 23"

Cohesion: 1.0
Nodes (1): Time-aware chronological cross-validator without future-looking data leakage.

### Community 24 - "Community 24"

Cohesion: 1.0
Nodes (1): Generate sequential train/validation split indices.

### Community 25 - "Community 25"

Cohesion: 1.0
Nodes (1): Fit scaler and sampler STRICTLY within the train split, preventing leakage to va

## Knowledge Gaps
- **109 isolated node(s):** `Generator script for src/notebook/02_phase2_track_a_benchmark_colab.ipynb.`, `Batch Generator for Google Colab Notebooks: Notebooks 03, 04, 05, 06.`, `Data Cleaning & Decontamination Pipeline. Addresses known anomalies in intrusion`, `Strip extraneous whitespace and special characters from DataFrame column headers`, `Clean and decontaminate CICIDS2017 dataset according to SPW 2021 and TIFS 2022 f` (+104 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 18`** (1 nodes): `Train the model on the provided training partition.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `Generate hard binary / multi-class predictions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `Check and automatically append required exclusion rules to .gitignore.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `Verify SHA-256 checksum of a downloaded file.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `Ensure data directories exist and safeguards are active.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `Time-aware chronological cross-validator without future-looking data leakage.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `Generate sequential train/validation split indices.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `Fit scaler and sampler STRICTLY within the train split, preventing leakage to va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
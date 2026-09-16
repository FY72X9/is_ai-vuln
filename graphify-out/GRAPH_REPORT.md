# Graph Report - D:\Codes\research_banks\is_ai-vuln  (2026-09-16)

## Corpus Check
- 40 files · ~467,733 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 352 nodes · 489 edges · 41 communities detected
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 110 edges (avg confidence: 0.69)
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
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]

## God Nodes (most connected - your core abstractions)
1. `BaseIDSModel` - 30 edges
2. `run_tests()` - 16 edges
3. `Visualization and journal-grade layouting modules.` - 16 edges
4. `is_ai-vuln Project Overview` - 12 edges
5. `run_preparation_pipeline()` - 11 edges
6. `run_closed_loop_fuzzy_dematel()` - 11 edges
7. `XGBoostIDS` - 11 edges
8. `LightGBMIDS` - 11 edges
9. `prepare_benchmark_dataset()` - 10 edges
10. `MambularSSMIDS` - 10 edges

## Surprising Connections (you probably didn't know these)
- `BaseIDSModel` --uses--> `Classical Gradient Boosted Decision Tree (GBDT) Baselines. Implements XGBoost an`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\base.py → D:\Codes\research_banks\is_ai-vuln\src\models\classical.py
- `BaseIDSModel` --uses--> `XGBoost Classifier Baseline with Optuna Tuning and Hist/GPU acceleration.`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\base.py → D:\Codes\research_banks\is_ai-vuln\src\models\classical.py
- `BaseIDSModel` --uses--> `LightGBM Classifier Baseline with Histogram Gradient Optimization.`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\src\models\base.py → D:\Codes\research_banks\is_ai-vuln\src\models\classical.py
- `Repository Directory Structure` --semantically_similar_to--> `Colab Reproducibility Package`  [INFERRED] [semantically similar]
  README.md → docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md
- `run_tests()` --calls--> `compute_friedman_test()`  [INFERRED]
  D:\Codes\research_banks\is_ai-vuln\scratch\test_full_pipeline.py → D:\Codes\research_banks\is_ai-vuln\src\evaluation\statistical_tests.py

## Hyperedges (group relationships)
- **Modern Tabular & Graph AI Architectures (2025-2026)** — docs_research_blueprint_is_cs_q1_2026_final_v3_tabpfn_v3, docs_research_blueprint_is_cs_q1_2026_final_v3_tabicl_v2, docs_research_blueprint_is_cs_q1_2026_final_v3_graphids, docs_research_blueprint_is_cs_q1_2026_final_v3_saint, docs_research_blueprint_is_cs_q1_2026_final_v3_mambular, docs_research_blueprint_is_cs_q1_2026_final_v3_ft_transformer [EXTRACTED 1.00]
- **Network Intrusion Benchmark Datasets** — docs_research_blueprint_is_cs_q1_2026_final_v3_nsl_kdd, docs_research_blueprint_is_cs_q1_2026_final_v3_cicids2017, docs_research_blueprint_is_cs_q1_2026_final_v3_unsw_nb15 [EXTRACTED 1.00]
- **Q1 Statistical Rigor & Robustness Framework** — docs_research_blueprint_is_cs_q1_2026_final_v3_stratified_5fold_cv, docs_research_blueprint_is_cs_q1_2026_final_v3_friedman_nemenyi_tests, docs_research_blueprint_is_cs_q1_2026_final_v3_ablation_and_robustness, docs_research_blueprint_is_cs_q1_2026_final_v3_q1_readiness_audit [EXTRACTED 1.00]

## Communities

### Community 0 - "Community 0"

Cohesion: 0.07
Nodes (21): BaseIDSModel, Abstract Base Class for all benchmarked IDS models., BaseIDSModel, FTTransformerIDS, MambularSSMIDS, Deep Tabular Learning Models: Mambular SSM, FT-Transformer, and SAINT. Implement, Feature Tokenizer Transformer (FT-Transformer) for Tabular IDS.          Impleme, Mambular State Space Model (SSM) for Tabular Intrusion Detection.          Exhib (+13 more)

### Community 1 - "Community 1"

Cohesion: 0.07
Nodes (34): download_file(), ensure_gitignore_safeguards(), generate_synthetic_benchmark_sample(), initialize_dataset_directories(), is_synthetic_path(), prepare_benchmark_dataset(), Drive Dataset Retrieval, Checksum Verification & Automatic .gitignore Safeguards, Check and automatically append required exclusion rules to .gitignore. (+26 more)

### Community 2 - "Community 2"

Cohesion: 0.08
Nodes (24): Release weights and garbage collect GPU/CPU memory., Run DirectLiNGAM causal discovery and calculate SHD against Fuzzy DEMATEL digrap, run_causal_triangulation(), export_benchmark_to_latex(), Automated LaTeX Table Generation for Q1 Journal Publication. Generates professio, Format DataFrame into publication-grade LaTeX table with booktabs., evaluate_robustness_degradation_slope(), inject_feature_corruption() (+16 more)

### Community 3 - "Community 3"

Cohesion: 0.1
Nodes (23): construct_axiomatic_prior_matrix(), Axiomatic Theoretical Prior Matrix (W_theory) for Autonomous Closed-Loop Fuzzy D, Derive the 8x8 theoretical causal prior matrix W_theory.          Self-influence, _calculate_kendalls_w(), compute_structural_hamming_distance(), Monte Carlo Robustness Proof & DirectLiNGAM Algorithmic Causal Triangulation. Va, Execute 10,000 Monte Carlo perturbation iterations to prove stability of promine, Calculate Kendall's W concordance coefficient across m raters for n items. (+15 more)

### Community 4 - "Community 4"

Cohesion: 0.16
Nodes (18): code_cell(), generate_nb01(), md_cell(), 100% Self-Contained Generator for src/notebook/01_phase1_pipeline_colab.ipynb. Z, code_cell(), generate_nb02(), md_cell(), Generator script for src/notebook/02_phase2_track_a_benchmark_colab.ipynb. (+10 more)

### Community 5 - "Community 5"

Cohesion: 0.13
Nodes (10): CheckpointManager, State Checkpointing & Fault-Tolerant Autorecovery Pipeline for Google Colab and, Load state from disk if exists, otherwise initialize clean state schema., Check whether all folds for a given model have been completed., Check whether a specific fold for a given model has already completed., Record the completion of a fold, update metrics, and persist to disk., Manages experiment state checkpointing, allowing seamless resumption across fold, Mark the entire track for this dataset as completed. (+2 more)

### Community 6 - "Community 6"

Cohesion: 0.12
Nodes (19): Causal Network & Prominence-Relation Map, CICIDS2017 Dataset, Contribution Triangle, FT-Transformer, Fuzzy DEMATEL, GraphIDS, Mambular (Mamba SSM), NSL-KDD Dataset (+11 more)

### Community 7 - "Community 7"

Cohesion: 0.15
Nodes (11): AntiLeakageTimeSeriesSplit, extract_subnet_mask(), fit_fold_isolated_pipeline(), PureNumPyStandardScaler, Anti-Leakage Data Partitioning Suite. Implements Subnet-Grouped and Time-Aware K, Time-aware chronological cross-validator without future-looking data leakage., Fit scaler and sampler STRICTLY within the train split, preventing leakage to va, Safely slice pandas DataFrame, Series, or NumPy ndarray by integer indices. (+3 more)

### Community 8 - "Community 8"

Cohesion: 0.17
Nodes (5): LightGBMIDS, Classical Gradient Boosted Decision Tree (GBDT) Baselines. Implements XGBoost an, LightGBM Classifier Baseline with Histogram Gradient Optimization., XGBoost Classifier Baseline with Optuna Tuning and Hist/GPU acceleration., XGBoostIDS

### Community 9 - "Community 9"

Cohesion: 0.14
Nodes (14): plot_causal_network_digraph(), Render publication-grade causal network digraph with prominent cause-effect node, Journal-grade publication figure styling for IEEE / ACM / Elsevier Q1 venues., Save figure simultaneously in vector PDF format and high-res PNG preview., Apply IEEE/Nature publication styling to matplotlib rcParams.          Args:, save_publication_figure(), set_publication_style(), compute_friedman_test() (+6 more)

### Community 10 - "Community 10"

Cohesion: 0.22
Nodes (10): compute_empirical_nmi_matrix(), extract_empirical_telemetry_from_experiments(), generate_mock_telemetry_matrix(), pd_qcut_safe(), Empirical Telemetry Mapper (W_empirical) for Autonomous Closed-Loop Fuzzy DEMATE, Generate realistic empirical metric telemetry across the 8 DEMATEL factors for v, Robust quantile binning with fallback for low variance columns., Extract real empirical metrics from Phase 2 benchmark outputs if available, else (+2 more)

### Community 11 - "Community 11"

Cohesion: 0.24
Nodes (10): flush_memory(), is_colab(), Environment initialization and hardware-runtime abstraction for Google Colab and, Initialize storage directories, Google Drive mounting (if Colab), and memory saf, Initialize storage directories, Google Drive mounting (if Colab), and memory saf, Check if the current runtime is Google Colab., Trigger Python garbage collection and flush CUDA cache to avoid OOM., resolve_project_root() (+2 more)

### Community 12 - "Community 12"

Cohesion: 0.22
Nodes (5): ABC, predict(), Unified Base Model Interface for Intrusion Detection Models. Standardizes traini, Generate prediction probability distributions. Fallback to binary indicator if u, Profile inference latency (ms/flow), throughput (flows/sec), and peak VRAM/RAM.

### Community 13 - "Community 13"

Cohesion: 0.36
Nodes (7): clean_column_names(), clean_dataset(), decontaminate_cicids2017(), Data Cleaning & Decontamination Pipeline. Addresses known anomalies in intrusion, Strip extraneous whitespace and special characters from DataFrame column headers, Clean and decontaminate CICIDS2017 dataset according to SPW 2021 and TIFS 2022 f, Universal cleaning dispatcher for benchmark datasets.

### Community 14 - "Community 14"

Cohesion: 0.29
Nodes (7): calculate_ttf_utility(), evaluate_classification_metrics(), evaluate_fold_run(), Evaluation Metrics and Task-Technology Fit (TTF) Utility Engine. Computes standa, Calculate comprehensive classification metrics., Combine classification metrics with inference profiling into standard telemetry, Compute formal Task-Technology Fit utility score according to Blueprint v4.0.

### Community 15 - "Community 15"

Cohesion: 0.4
Nodes (5): format_bibtex_entry(), harvest_and_build_library(), Metadata Harvester for Academic References using OpenAlex and CrossRef REST APIs, Format reference dict into a clean BibTeX entry., Harvest metadata from OpenAlex / CrossRef where available and build references/l

### Community 16 - "Community 16"

Cohesion: 0.5
Nodes (3): Academic Citation Integrity & Retraction Validator. Verifies DOI resolution via, Validate all references in the provided list for DOI resolution and retraction s, validate_references()

### Community 17 - "Community 17"

Cohesion: 0.67
Nodes (3): Ablation Study & Robustness Analysis, Friedman & Nemenyi Statistical Tests, 5-Fold Stratified Cross-Validation

### Community 18 - "Community 18"

Cohesion: 1.0
Nodes (0): 

### Community 19 - "Community 19"

Cohesion: 1.0
Nodes (0): 

### Community 20 - "Community 20"

Cohesion: 1.0
Nodes (1): Train the model on the provided training partition.

### Community 21 - "Community 21"

Cohesion: 1.0
Nodes (1): Generate hard binary / multi-class predictions.

### Community 22 - "Community 22"

Cohesion: 1.0
Nodes (1): Check and automatically append required exclusion rules to .gitignore.

### Community 23 - "Community 23"

Cohesion: 1.0
Nodes (1): Verify SHA-256 checksum of a downloaded file.

### Community 24 - "Community 24"

Cohesion: 1.0
Nodes (1): Download a file with retry mechanism and SHA256 verification.

### Community 25 - "Community 25"

Cohesion: 1.0
Nodes (1): Generate realistic synthetic NetFlow records for offline pipeline testing and Co

### Community 26 - "Community 26"

Cohesion: 1.0
Nodes (1): Ensure data directories exist and safeguards are active.

### Community 27 - "Community 27"

Cohesion: 1.0
Nodes (1): Retrieve benchmark dataset: attempts remote download or synthesizes representati

### Community 28 - "Community 28"

Cohesion: 1.0
Nodes (1): Memory-efficient streaming chunk iterator for large-scale NetFlow partitions.

### Community 29 - "Community 29"

Cohesion: 1.0
Nodes (1): Yield (X_chunk, y_chunk) in bounded batches.

### Community 30 - "Community 30"

Cohesion: 1.0
Nodes (1): Quickly synthesize large-scale streaming NetFlow benchmark partition for Track B

### Community 31 - "Community 31"

Cohesion: 1.0
Nodes (1): Generate realistic empirical metric telemetry across the 8 DEMATEL factors for v

### Community 32 - "Community 32"

Cohesion: 1.0
Nodes (1): Calculate the 8x8 Normalized Mutual Information (NMI) matrix and fold variance.

### Community 33 - "Community 33"

Cohesion: 1.0
Nodes (1): Robust quantile binning with fallback for low variance columns.

### Community 34 - "Community 34"

Cohesion: 1.0
Nodes (1): Trigger Python garbage collection and flush CUDA cache to avoid OOM.

### Community 35 - "Community 35"

Cohesion: 1.0
Nodes (1): Check and automatically append required exclusion rules to .gitignore.

### Community 36 - "Community 36"

Cohesion: 1.0
Nodes (1): Verify SHA-256 checksum of a downloaded file.

### Community 37 - "Community 37"

Cohesion: 1.0
Nodes (1): Ensure data directories exist and safeguards are active.

### Community 38 - "Community 38"

Cohesion: 1.0
Nodes (1): Time-aware chronological cross-validator without future-looking data leakage.

### Community 39 - "Community 39"

Cohesion: 1.0
Nodes (1): Generate sequential train/validation split indices.

### Community 40 - "Community 40"

Cohesion: 1.0
Nodes (1): Fit scaler and sampler STRICTLY within the train split, preventing leakage to va

## Knowledge Gaps
- **131 isolated node(s):** `100% Self-Contained Generator for src/notebook/01_phase1_pipeline_colab.ipynb. Z`, `Generator script for src/notebook/02_phase2_track_a_benchmark_colab.ipynb.`, `Batch Generator for Google Colab Notebooks: Notebooks 03, 04, 05, 06.`, `Comprehensive verification script for Colab notebooks and dataset path resolutio`, `Automated verification test for real vs. synthetic data detection and Colab Driv` (+126 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 18`** (1 nodes): `graphify_query.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `inspect_notebooks.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `Train the model on the provided training partition.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `Generate hard binary / multi-class predictions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `Check and automatically append required exclusion rules to .gitignore.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `Verify SHA-256 checksum of a downloaded file.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `Download a file with retry mechanism and SHA256 verification.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `Generate realistic synthetic NetFlow records for offline pipeline testing and Co`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (1 nodes): `Ensure data directories exist and safeguards are active.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (1 nodes): `Retrieve benchmark dataset: attempts remote download or synthesizes representati`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (1 nodes): `Memory-efficient streaming chunk iterator for large-scale NetFlow partitions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (1 nodes): `Yield (X_chunk, y_chunk) in bounded batches.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `Quickly synthesize large-scale streaming NetFlow benchmark partition for Track B`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (1 nodes): `Generate realistic empirical metric telemetry across the 8 DEMATEL factors for v`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (1 nodes): `Calculate the 8x8 Normalized Mutual Information (NMI) matrix and fold variance.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (1 nodes): `Robust quantile binning with fallback for low variance columns.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `Trigger Python garbage collection and flush CUDA cache to avoid OOM.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `Check and automatically append required exclusion rules to .gitignore.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `Verify SHA-256 checksum of a downloaded file.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `Ensure data directories exist and safeguards are active.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Time-aware chronological cross-validator without future-looking data leakage.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `Generate sequential train/validation split indices.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `Fit scaler and sampler STRICTLY within the train split, preventing leakage to va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
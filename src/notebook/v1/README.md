# Google Colab Notebooks Directory (`src/notebook/`)

This directory houses the 6 core executable Jupyter Notebooks (`.ipynb`) for the research project.

## 🌟 Execution Architecture: 100% Self-Contained

To guarantee zero friction when running in Google Colab (Free Tier / Pro), all notebooks are designed to be **100% self-contained**:
* **Zero External Repository File Dependencies**: Notebooks do not require cloning the repository or issuing `from src...` imports. All PyTorch neural network architectures (`MambularNet`, `FTTransformerNet`, `SAINTNet`, `GraphIDSNet`), baseline wrappers, data loaders, DEMATEL solvers, and publication stylers are fully inlined inside the notebook cells.
* **Dual-Environment Path Auto-Resolution**: Automatically detects Google Drive mount points (`/content/drive/MyDrive/Colab Notebooks` or `Colab Notebook`) and workstation paths.
* **Checkpoint Autorecovery**: State is periodically saved to `checkpoints/checkpoint_state.json` on Google Drive, enabling automatic resumption if a preemptible runtime disconnects.
* **Target Platforms**: Google Colab Free Tier (Tesla T4 GPU, 16 GB VRAM, ~12.7 GB System RAM), Google Colab Pro (A100/V100), and local Jupyter environments.

---

## 📁 Pipeline Notebook Catalog

| Phase | Notebook File | Objective & Scope | Runtime Target | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | [`01_phase1_pipeline_colab.ipynb`](01_phase1_pipeline_colab.ipynb) | Multi-dataset ingestion and decontamination across all 5 benchmarks (`CICIDS2017`, `UNSW-NB15`, `TON_IOT`, `CIC-DDOS2019`, `NSL-KDD`), time-aware and session-grouped splits, and 35-reference DOI audit. | CPU / T4 GPU | ✅ Verified |
| **Phase 2A** | [`02_phase2_track_a_benchmark_colab.ipynb`](02_phase2_track_a_benchmark_colab.ipynb) | Track A few-shot benchmark ($N \le 10\text{k}$) across 8 models (TabPFN, TabICL, Mambular SSM, FT-Transformer, SAINT, GraphIDS, XGBoost, LightGBM) over all 5 datasets (15 epochs, AdamW, 5-fold CV). | Tesla T4 GPU | ✅ Verified |
| **Phase 2B** | [`03_phase2_track_b_scalability_colab.ipynb`](03_phase2_track_b_scalability_colab.ipynb) | Track B industrial streaming scalability benchmark ($N \in \{50\text{k}, 100\text{k}, 250\text{k}, 500\text{k}, 1,000,000\}$ flows) with 25k chunk loader across all 5 datasets. | Tesla T4 GPU | ✅ Verified |
| **Phase 3** | [`04_phase3_statistical_ablation_colab.ipynb`](04_phase3_statistical_ablation_colab.ipynb) | Omnibus Friedman test, Nemenyi Critical Difference analysis, adversarial Gaussian noise injection, and FT-Transformer architectural grid ablation on a multi-domain composite testbed. | CPU / T4 GPU | ✅ Verified |
| **Phase 4** | [`05_phase4_fuzzy_dematel_lingam_colab.ipynb`](05_phase4_fuzzy_dematel_lingam_colab.ipynb) | Closed-loop Fuzzy DEMATEL causal simulation, 10,000-iteration Monte Carlo stability proof ($W \ge 0.95$), and DirectLiNGAM causal triangulation calibrated from multi-dataset telemetry. | CPU | ✅ Verified |
| **Phase 5** | [`06_phase5_manuscript_figures_tables_colab.ipynb`](06_phase5_manuscript_figures_tables_colab.ipynb) | Compiles manuscript publication LaTeX Tables 1–4, Cross-Dataset Master Pareto Frontier with error bars, and seals the Zenodo replication package manifest. | CPU | ✅ Verified |

---

## 🛠️ Google Colab Execution Guidelines

1. **Dataset Organization on Google Drive**:
   Place raw benchmark files under `MyDrive/Colab Notebooks/data/raw/` in their respective folders (`MachineLearningCVE/`, `unsw-data-full/`, `TON-IoT/`, `CIC-DDoS2019/`, `NSL-KDD/`).
2. **Order of Execution**:
   Run notebooks sequentially from `01_...` through `06_...`. Each notebook outputs structured data (`.parquet`, `.csv`, `.json`) into `data/processed/` and `experiment_output/` that downstream notebooks ingest.
3. **Optional Total Reset**:
   Cell 0 in each notebook contains a commented-out cleanup snippet (`# ...`). Uncomment and run this cell only if you wish to wipe previous checkpoints and processed caches to start a fresh run.
4. **Figure & Table Outputs**:
   Every visualizer generates dual outputs: Vector PDF (for LaTeX typesetting) and 300 DPI PNG (for raster review), saved simultaneously to local Colab storage and your Google Drive `experiment_output/figures/` directory. Tables are formatted in `.tex` inside `experiment_output/publication_tables/`.

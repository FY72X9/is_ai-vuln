# Google Colab Notebooks Directory (`src/notebook/`)

This directory is the dedicated repository location for all executable Jupyter Notebooks (`.ipynb`) used in the research project.

## ⚠️ Execution Policy
- **No Heavy Local Execution**: Heavy model training, tabular foundation models (TabPFN, TabICL), streaming benchmarks, and high-volume dataset processing **must NOT** be run on local developer machines.
- **Target Platform**: Google Colab Free Tier (Tesla T4 GPU, 16GB VRAM, ~12.7GB System RAM) and Google Colab Pro if available.
- **Code Modularity**: Notebooks should import and execute modules from `src/` rather than defining massive monolithic scripts inline.

## 📁 Pipeline Notebook Catalog

| Phase | Notebook File | Primary Objective | Runtime Target | Status |
|---|---|---|---|---|
| **Phase 1** | `01_phase1_pipeline_colab.ipynb` | Google Drive setup, `.gitignore` safeguards, 35-reference DOI audit, data cleaning & anti-leakage splitting verification. | CPU / T4 GPU | ✅ Ready |
| **Phase 2A** | `02_phase2_track_a_benchmark_colab.ipynb` | Track A ($N \le 10\text{k}$) 5-fold CV evaluation across TabPFN v3, TabICL v2, Mambular SSM, FT-Transformer, SAINT, GraphIDS, XGBoost, LightGBM. | Tesla T4 GPU | ✅ Ready |
| **Phase 2B** | `03_phase2_track_b_scalability_colab.ipynb` | Track B ($N \ge 100\text{k}$) streaming throughput, latency, and VRAM memory scaling profiling. | Tesla T4 GPU | ✅ Ready |
| **Phase 3** | `04_phase3_statistical_ablation_colab.ipynb` | Non-parametric Friedman test, Nemenyi CD diagram, adversarial noise injection, and hyperparameter ablations. | CPU / T4 GPU | ✅ Ready |
| **Phase 4** | `05_phase4_fuzzy_dematel_lingam_colab.ipynb` | Closed-loop Fuzzy DEMATEL simulation, 10,000-run Monte Carlo proof ($W \ge 0.95$), and DirectLiNGAM causal triangulation. | CPU | ✅ Ready |
| **Phase 5** | `06_phase5_manuscript_figures_tables_colab.ipynb` | Automated publication LaTeX table generation, 300+ DPI vector PDF figures, and Zenodo package sealing. | CPU | ✅ Ready |

## 🛠️ Google Colab Pre-Flight Checklist
1. **Google Drive Integration**: Each notebook automatically mounts Google Drive (`/content/drive/MyDrive/is_ai-vuln/`) to preserve checkpoints and experiment outputs across disconnections.
2. **Preemption Recovery**: Long-running benchmark loops save their state after each fold using `src.utils.checkpoint_manager.CheckpointManager`. If disconnected, re-running the notebook resumes execution seamlessly from the last recorded state in `checkpoint_state.json`.
3. **Memory Management**: At the end of every fold, `src.utils.environment.flush_memory()` is called to flush GPU CUDA cache and reclaim RAM.

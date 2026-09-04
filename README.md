# is_ai-vuln

> **Task-Technology Fit Analysis of Modern AI-Driven Intrusion Detection: An Axiomatic-Empirical Fuzzy DEMATEL Simulation Framework**  
> *Targeting Top-Decile & Q1 Journal Publication in Information Systems & Computer Science (2026)*  
> Venue Targets: *Information Fusion* (IF: 15.5), *IEEE TDSC* (IF: 7.3), *IEEE TIFS* (IF: 6.8), *Expert Systems with Applications* (IF: 7.5)

---

## 📌 Executive Overview

This repository houses the research framework, experimental pipelines, and simulation-based causal modeling for evaluating modern tabular foundation models, state space models, graph neural networks, and self-attention transformers under the **Task-Technology Fit (TTF)** paradigm, synthesized through an **Axiomatic-Empirical Fuzzy DEMATEL** causal discovery engine.

### 🌟 Core Scientific Pillars (Blueprint v4.0)
1. **Primary Theoretical Anchor — Task-Technology Fit (TTF)**: Resolves the Information Systems (IS) identity crisis by formalizing mathematical utility functions across three distinct cyber-defense operational tasks:
   * **$T_1$ (Line-Rate Perimeter Defense)**: Throughput $\ge 10\text{ Gbps}$, latency $< 1\text{ ms}$, bounded memory footprint.
   * **$T_2$ (Zero-Day Payload Isolation)**: High few-shot generalization and adaptation to unseen evasion techniques.
   * **$T_3$ (Correlated Multi-Host Tracking)**: Structural graph topological inference and lateral movement detection.
2. **100% Closed-Loop Theoretical Simulation (Zero External Human Panels)**:
   * Direct influence matrix $\tilde{A}$ synthesized objectively from **Axiomatic Complexity Priors ($W_{\text{theory}}$)** modulated by **5-Fold Normalized Mutual Information ($W_{\text{empirical}}$)**.
   * **Monte Carlo Stochastic Proof (10,000 Iterations)**: Mathematically proves causal stability with Kendall's concordance $W \ge 0.95$.
   * **Algorithmic Causal Triangulation**: Direct cross-validation against **DirectLiNGAM** (Structural Hamming Distance $\le 2$).
3. **2-Track Experimental Benchmark Suite**:
   * **Track A (Few-Shot Generalization, $N \le 10\text{k}$)**: Compares all 6 modern models (TabPFN v3, TabICL v2, GraphIDS, SAINT, Mambular SSM, FT-Transformer) + 2 baselines (XGBoost, LightGBM with Optuna tuning).
   * **Track B (Industrial Streaming Scalability, $N \ge 100\text{k}$)**: Compares scalable linear and tree architectures (Mambular SSM, FT-Transformer, GraphIDS with NeighborLoader, XGBoost, LightGBM).
4. **5 Decontaminated Benchmark Datasets**: CICIDS2017 (algorithmically cleansed), UNSW-NB15, TON_IoT (2021), CIC-DDoS2019, and NSL-KDD (historical baseline anchor).
5. **Anti-Leakage Cross-Validation**: Time-Aware & Session-Grouped `GroupKFold` on subnets and temporal windows to eliminate temporal and spatial data leakage; inductive snapshot evaluation for GraphIDS.
6. **Google Colab Free Tier Fault-Tolerant Autorecovery**: `CheckpointManager` caching fold progress in Google Drive (`checkpoint_state.json`), enabling seamless resumption from preemptible timeouts without restarting from zero.
7. **Specialized Automation Scripts**: Automated reference metadata retrieval, DOI existence/retraction validation, Google Drive dataset downloading with automated `.gitignore` safeguards, and 300+ DPI publication layouting.
8. **Rigorous Literature Base**: 35 peer-reviewed references (29 published $> 2020$ from *Nature*, *NeurIPS*, *ICML*, and *IEEE*, plus 6 foundational theoretical classics).

---

## 📁 Repository Structure

```plaintext
is_ai-vuln/
├── docs/
│   ├── Research_Blueprint_IS_CS_Q1_2026_V4_TTF_SIMULATION.md  # Active Master Blueprint v4.0
│   ├── ACADEMIC_PEER_REVIEW_AND_GAP_ANALYSIS.md              # Doctoral Pre-Execution Audit
│   ├── implementation_plan.md                                # Implementation Roadmap
│   ├── EXECUTION_PLAN.md                                     # [Planned] Step-by-step Technical Guide
│   ├── CHECKLIST.md                                          # [Planned] 14-Week Interactive Tracker
│   └── Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md          # Archived Blueprint v3.0
├── src/
│   ├── data/
│   │   ├── drive_downloader.py    # Automated dataset retrieval to Drive + auto .gitignore
│   │   ├── cleaner.py             # CICIDS2017 & UNSW decontamination pipelines
│   │   ├── splitters.py           # Time-Aware & Session-Grouped K-Fold splitters
│   │   └── graph_builder.py       # Flow-to-Graph converter for GraphIDS (PyG)
│   ├── models/
│   │   ├── unified_interface.py   # Abstract Base Class (fit, predict, predict_proba)
│   │   ├── foundation_models.py   # TabPFN v3 & TabICL v2 wrappers
│   │   ├── state_space.py         # Mambular SSM (DeepTab) wrapper
│   │   ├── graph_models.py        # GraphIDS PyG execution wrapper
│   │   ├── attention_models.py    # SAINT & FT-Transformer wrappers
│   │   └── baselines.py           # Optuna-tuned XGBoost & LightGBM wrappers
│   ├── evaluation/
│   │   ├── metrics.py             # F1, PR-AUC, Latency, Throughput, Energy profiling
│   │   ├── statistical_tests.py   # Friedman test & Nemenyi post-hoc CD diagrams
│   │   ├── ablation.py            # Component & hyperparameter grid ablation
│   │   └── robustness.py          # Gaussian noise & feature corruption injectors
│   ├── dematel/
│   │   ├── axiomatic_priors.py    # Big-O theoretical prior matrix generator
│   │   ├── empirical_mapper.py    # 5-fold NMI to TFN translation engine
│   │   ├── fuzzy_solver.py        # Matrix normalization, inversion, and CFCS
│   │   ├── monte_carlo.py         # 10,000 perturbation stability verifier
│   │   └── causal_triangulation.py # DirectLiNGAM / PC Algorithm cross-validator
│   ├── visualization/
│   │   └── publication_styler.py  # 300+ DPI IEEE/Nature publication layouting
│   └── utils/
│       ├── checkpoint_manager.py  # Granular autorecovery & state checkpointing
│       ├── experiment_logger.py   # Timestamped run directories & manifest tracking
│       ├── references_harvester.py # OpenAlex & CrossRef metadata harvester
│       ├── references_validator.py # DOI resolution, indexing & retraction verifier
│       └── energy_meter.py        # PyJoules / CodeCarbon hardware energy tracker
├── experiment_output/             # Isolated timestamped run folders (run_YYYYMMDD_HHMMSS_v4.0/)
├── references/                    # Bibliographic metadata (.bib) & verification logs
├── .gitignore                     # Automated large dataset and cache exclusions
└── README.md                      # Project overview & quick start
```

---

## 📄 Documentation Index

| Document | Purpose & Description | Status |
|---|---|---|
| **[docs/Research_Blueprint_IS_CS_Q1_2026_V4_TTF_SIMULATION.md](docs/Research_Blueprint_IS_CS_Q1_2026_V4_TTF_SIMULATION.md)** | **Master Research Blueprint v4.0**: Complete specification covering TTF theoretical anchoring, 2-track benchmark, 100% closed-loop simulation DEMATEL, Colab free-tier execution rules, autorecovery, and 35 verified references ($>2020$). | 🟢 Active |
| **[docs/ACADEMIC_PEER_REVIEW_AND_GAP_ANALYSIS.md](docs/ACADEMIC_PEER_REVIEW_AND_GAP_ANALYSIS.md)** | **Doctoral Academic Peer Review**: Pre-execution protocol audit detailing the 7 fatal reviewer vulnerabilities and their mathematical simulation mitigations. | 🟢 Active |
| **[docs/implementation_plan.md](docs/implementation_plan.md)** | **Implementation Roadmap**: Synthesis of deliverables, verification plan, and operational steps. | 🟢 Active |
| **`docs/EXECUTION_PLAN.md`** | **Operational Execution Guide**: Step-by-step execution protocol for modules, Colab setup, and benchmark runs. | 🟡 In Queue |
| **`docs/CHECKLIST.md`** | **14-Week Interactive Checklist**: Interactive tracker (`- [ ]`) covering 10 Q1 audit criteria, Colab recovery, and submission defense. | 🟡 In Queue |
| **[docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md](docs/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md)** | **Blueprint v3.0 Archive**: Previous edition covering 6 models and 10 gap audit. | ⚪ Archive |

---

## 🚀 Execution Environment & Setup (Google Colab Free Tier)

1. **Google Drive Mounting & Autorecovery**:
   The execution engine automatically mounts Google Drive and checks `/content/drive/MyDrive/is_ai-vuln/checkpoint_state.json`. If a session times out, re-running the notebook resumes execution from the exact interrupted fold without re-training completed models.
2. **Dataset Isolation**:
   Large datasets are retrieved directly to Google Drive via `src/data/drive_downloader.py`. The root `.gitignore` automatically guarantees that raw `.csv`, `.pcap`, and `.parquet` files are never tracked in Git.
3. **Artifact Logging**:
   Every run produces a timestamped directory in `experiment_output/run_YYYYMMDD_HHMMSS_v4.0/` containing a hardware `manifest.json`, execution logs, serialized model weights, LaTeX performance tables, and 300+ DPI vector PDF charts.

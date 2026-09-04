# 📋 Research Execution & Q1 Quality Assurance Checklist
## Project: *Task-Technology Fit Analysis of Modern AI-Driven Intrusion Detection: An Axiomatic-Empirical Fuzzy DEMATEL Simulation Framework*
### Document Version: **v4.0 (Aligned with Master Blueprint v4.0)**
### Purpose: Interactive Progress Tracking, Colab Fault-Tolerance, and Q1 Reviewer Defense Audit

---

## 📌 Checklist Navigation & Usage Guide
* `[ ]` **Pending**: Task has not yet commenced.
* `[-]` **In Progress**: Task currently active.
* `[x]` **Completed / Verified**: Task executed, audited, and verified against Q1 criteria.

---

## 1. 🗓️ Phase-by-Phase Operational Checklist (14-Week Timeline)

### Phase 1: Foundation, Infrastructure & Literature Validation (Weeks 1–3)
- [x] **W1.1 Environment Setup**: Initialize repository structure according to Blueprint v4.0 (`src/data/`, `src/utils/`, `src/visualization/`, `src/models/`, `src/dematel/`, `src/evaluation/`).
- [x] **W1.2 Google Drive Integration**: Verify `google.colab.drive.mount('/content/drive')` and establish persistent path via `src/utils/environment.py`.
- [x] **W1.3 Git Safeguards**: Execute `src/data/drive_downloader.py` to automatically update `.gitignore` with all heavy dataset patterns (`*.csv`, `*.pcap`, `*.parquet`, `/data/`, `drive_cache/`).
- [x] **W1.4 Dependency Verification**: Validate installation of core packages (`scikit-learn`, `scipy`, `pandas`, `numpy`, `networkx`, `matplotlib`, `seaborn`) in `requirements.txt`.
- [x] **W2.1 References Harvesting**: Run `src/utils/references_harvester.py` to retrieve verified metadata via OpenAlex and CrossRef APIs for all 35 citations.
- [x] **W2.2 References Validation**: Execute `src/utils/references_validator.py` to confirm 100% active DOI resolution, Scopus indexing status, and absence from CrossRef Retraction Watch database.
- [x] **W2.3 BibTeX Archiving**: Confirm `references/library.bib` and `references/validation_report.json` are generated and sealed (`audit_passed: true`).
- [x] **W3.1 Dataset Ingestion**: Initialize storage layout and ingestion pipeline in `src/data/drive_downloader.py` for benchmark datasets.
- [x] **W3.2 Decontamination Execution**: Run `src/data/cleaner.py` on CICIDS2017 to strip duplicate zero-length flows, eliminate infinite/NaN values, and resolve mislabeled attack windows.
- [x] **W3.3 Anti-Leakage Partitioning**: Implement `GroupKFold` on subnets and temporal windows in `src/data/splitters.py`.
- [x] **W3.4 Graph Construction**: Run `src/data/graph_builder.py` to generate PyG bipartite flow graphs for GraphIDS.

---

### Phase 2: Core 2-Track Benchmark Execution (Weeks 4–7)
- [ ] **W4.1 CheckpointManager Bootstrap**: Verify `CheckpointManager` initializes `checkpoint_state.json` on Google Drive.
- [ ] **W4.2 Track A — Foundation Models ($N \le 10\text{k}$)**:
  - [ ] Evaluate **TabPFN v3** across 5 folds ($N \in \{1\text{k}, 5\text{k}, 10\text{k}\}$).
  - [ ] Evaluate **TabICL v2** across 5 folds with KV-caching.
- [ ] **W5.1 Track A — Deep Learning & Baselines ($N \le 10\text{k}$)**:
  - [ ] Train & evaluate **Mambular SSM** (linear complexity $O(L)$).
  - [ ] Train & evaluate **FT-Transformer** (quadratic attention $O(L^2)$).
  - [ ] Train & evaluate **SAINT** (row + column self-attention).
  - [ ] Train & evaluate **GraphIDS** (self-supervised inductive GNN).
  - [ ] Optimize & evaluate **XGBoost** baseline with Optuna (50 trials).
  - [ ] Optimize & evaluate **LightGBM** baseline with Optuna (50 trials).
- [ ] **W5.2 Track A Verification**: Confirm all 8 models have completed 5 folds and metrics are committed to `checkpoint_state.json`.
- [ ] **W6.1 Track B — Scalable Deep Learning ($N \ge 100\text{k}$)**:
  - [ ] Execute **Mambular SSM** on $N \in \{100\text{k}, 500\text{k}, 1\text{M}\}$ samples; log VRAM and throughput.
  - [ ] Execute **FT-Transformer** on scalable mini-batches; record attention memory wall.
- [ ] **W7.1 Track B — Graph & Tree Scalability ($N \ge 100\text{k}$)**:
  - [ ] Execute **GraphIDS** with streaming `NeighborLoader` mini-batching.
  - [ ] Execute **XGBoost** (Hist-gradient mode) on full-scale partitions.
  - [ ] Execute **LightGBM** (GPU-accelerated histogram mode) on full-scale partitions.
- [ ] **W7.2 Track B Verification**: Generate Track B scalability curves comparing throughput ($\text{flows/sec}$) vs sample size.

---

### Phase 3: Q1 Rigorous Testing — Statistical, Ablation & Robustness (Weeks 8–9)
- [ ] **W8.1 Non-Parametric Friedman Test**:
  - [ ] Compute Friedman test across $k=8$ models and $N=5$ datasets ($\chi_F^2$ statistic).
  - [ ] Verify null hypothesis rejection ($p < 0.01$).
- [ ] **W8.2 Nemenyi Post-Hoc Analysis**:
  - [ ] Compute Critical Difference ($CD$) threshold.
  - [ ] Generate publication-ready Critical Difference (CD) rank diagram via `publication_styler.py`.
- [ ] **W9.1 Component Ablation Study**:
  - [ ] Execute hyperparameter grid sweep on Mambular SSM: depth $L \in \{2, 4, 6, 8\}$, dimension $d \in \{64, 128, 256\}$.
  - [ ] Execute hyperparameter grid sweep on FT-Transformer: depth vs attention heads.
  - [ ] Generate ablation heatmaps showing performance degradation vs parameter efficiency.
- [ ] **W9.2 Adversarial Robustness Injection**:
  - [ ] Test Gaussian noise injection: $\sigma \in \{0.0, 0.02, 0.05, 0.10, 0.20\}$; plot degradation slope.
  - [ ] Test feature corruption: random feature dropout $p \in \{0\%, 10\%, 20\%, 30\%, 50\%\}$.
- [ ] **W9.3 Green Computing Profiling**:
  - [ ] Measure throughput ($\text{flows/second}$) on both GPU (T4) and CPU runtime.
  - [ ] Profile active inference energy expenditure ($\mu\text{J/flow}$) via `CodeCarbon`.

---

### Phase 4: Autonomous Closed-Loop Fuzzy DEMATEL & Causal Triangulation (Weeks 10–11)
- [ ] **W10.1 Axiomatic Prior Derivation**: Construct $8 \times 8$ theoretical prior matrix $W_{\text{theory}}$ derived from Big-O complexity and statistical learning bounds.
- [ ] **W10.2 Empirical Telemetry Extraction**: Run `src/dematel/empirical_mapper.py` to extract Normalized Mutual Information (NMI) and cross-fold variance from 5-fold metric matrices.
- [ ] **W10.3 Triangular Fuzzy Synthesis**: Formulate $\tilde{A} = (L, M, U)$ combining $W_{\text{theory}}$ and $W_{\text{empirical}}$.
- [ ] **W10.4 Matrix Normalization & Total Relation**: Compute normalized matrix $\tilde{X}$ and total relation matrix $\tilde{T} = \tilde{X}(I - \tilde{X})^{-1}$.
- [ ] **W10.5 CFCS Defuzzification**: Defuzzify $\tilde{T}$ into crisp matrix $T$ using Converting Fuzzy data into Crisp Scores.
- [ ] **W10.6 Prominence & Relation Mapping**:
  - [ ] Calculate $D_i$ (row sum) and $R_i$ (column sum).
  - [ ] Calculate Prominence $(D_i + R_i)$ and Relation $(D_i - R_i)$.
  - [ ] Establish threshold $\alpha$ and generate Causal Network Digraph via `publication_styler.py`.
- [ ] **W11.1 Monte Carlo Sensitivity Proof**:
  - [ ] Run 10,000 stochastic perturbation iterations on fuzzy bounds $(l, m, u)$ with $\mathcal{N}(0, 0.05^2)$.
  - [ ] Confirm Kendall's coefficient of concordance $W \ge 0.95$ ($p < 0.001$).
- [ ] **W11.2 Algorithmic Causal Triangulation**:
  - [ ] Execute DirectLiNGAM / PC Algorithm on empirical telemetry.
  - [ ] Confirm Structural Hamming Distance (SHD) $\le 2$ between DEMATEL digraph and LiNGAM graph.

---

### Phase 5: Manuscript Preparation, LaTeX Formatting & Packaging (Weeks 12–14)
- [ ] **W12.1 IMRAD Drafting**: Draft Introduction, TTF Theoretical Framework, Methodology, Results, and Causal Discussion.
- [ ] **W12.2 Task-Technology Fit Synthesis**: Calculate empirical TTF utility scores across $T_1, T_2, T_3$ and formally validate Design Propositions (DP1–DP4).
- [ ] **W12.3 High-Resolution Figures**: Compile all figures in vector PDF and 300+ DPI format into LaTeX document.
- [ ] **W12.4 Tables Generation**: Compile automated `.tex` tables from `experiment_output/run_*/tables/`.
- [ ] **W13.1 Q1 Readiness Audit Review**: Complete Section 4 checklist below to ensure all 10 gaps and 7 fatal vulnerabilities are mitigated.
- [ ] **W13.2 Limitations & Future Trajectories**: Review explicit statements on edge constraints, sample limits, and streaming deployment.
- [ ] **W14.1 Zenodo Packaging**: Archive preprocessed datasets and simulation logs on Zenodo; secure permanent DOI.
- [ ] **W14.2 GitHub Public Sealing**: Ensure GitHub repository contains clean README, `requirements.txt`, reproducible Colab badge, and sealed `.gitignore`.
- [ ] **W14.3 Formal Submission**: Submit manuscript to target Q1 journal (*Information Fusion* / *IEEE TDSC* / *IEEE TIFS* / *ESWA*).

---

## 2. ☁️ Google Colab Free-Tier & Autorecovery Verification Checklist

- [ ] **Drive Persistent Mounting**: Confirm Google Drive mounts cleanly to `/content/drive` without permission errors.
- [ ] **Symlink Performance**: Verify local data directory `/content/data` symlinks to Drive cache for NVMe read speeds.
- [ ] **RAM Ceiling Compliance**: Confirm host memory never exceeds 11.5 GB of the 12.7 GB Colab free tier ceiling.
- [ ] **CUDA Cache Flushing**: Verify `torch.cuda.empty_cache()` executes at every fold boundary (GPU VRAM drops to baseline $< 1\text{GB}$).
- [ ] **State Save Verification**: Confirm `checkpoint_state.json` updates in Drive immediately upon fold completion.
- [ ] **Crash Recovery Simulation**:
  - [ ] Simulate Colab session crash (terminate runtime midway through Model 3 Fold 2).
  - [ ] Restart runtime and re-run execution notebook.
  - [ ] Verify runner automatically detects state, skips completed Model 1, Model 2, and Model 3 Fold 1, and resumes precisely on Fold 2 without restarting from zero.
- [ ] **Force-Restart Flag**: Verify `--force-restart=True` creates a timestamped archive of previous state and re-initializes cleanly.
- [ ] **Versioned Output Folder**: Verify every execution creates an isolated directory `experiment_output/run_YYYYMMDD_HHMMSS_v4.0/` containing `manifest.json`.

---

## 3. 🛠️ Specialized Automation Scripts Checklist

### Reference Harvester (`src/utils/references_harvester.py`)
- [ ] Queries OpenAlex API and CrossRef REST API without rate-limit errors.
- [ ] Extracts complete citation metadata (Title, Authors, Year, Venue, DOI, OA status, FWCI).
- [ ] Appends clean BibTeX entries into `references/library.bib`.

### Reference Validator (`src/utils/references_validator.py`)
- [ ] Performs HTTP HEAD requests to verify 100% active DOI resolution (HTTP 200/301/302).
- [ ] Cross-references DOIs with OpenAlex indexing status (Scopus/WoS eligibility).
- [ ] Queries CrossRef Retraction Watch database; confirms 0 cited papers have been retracted.
- [ ] Generates `references/validation_report.json` with timestamped audit results.

### Drive Downloader & `.gitignore` Automation (`src/data/drive_downloader.py`)
- [ ] Downloads dataset archives directly into Drive cache directory `/content/drive/MyDrive/is_ai-vuln-data/`.
- [ ] Validates SHA-256 archive checksums against published dataset hashes.
- [ ] Automatically appends required exclusion rules to `.gitignore` (`*.csv`, `*.pcap`, `*.parquet`, `data/`, `checkpoints/*.pt`).
- [ ] Confirms `git status` displays 0 gigabyte-scale data files staged for commit.

### Journal Publication Styler (`src/visualization/publication_styler.py`)
- [ ] Sets Matplotlib parameters for IEEE single-column (3.5 in) and double-column (7.0 in).
- [ ] Enforces minimum 300 DPI for line charts and 600 DPI for dense scatter/ROC curves.
- [ ] Uses accessible, colorblind-safe palettes (`colorblind` or `viridis`).
- [ ] Configures professional serif typography matching LaTeX template (`Times New Roman`).
- [ ] Exports simultaneous vector `.pdf` and high-res preview `.png`.

---

## 4. 🎯 Q1 Readiness Audit: 10 Critical Gaps + 7 Fatal Reviewer Vulnerabilities

### Part A: 10 Critical Blueprint Gaps Mitigated
- [ ] **Gap 1: Statistical Significance Testing**: Non-parametric Friedman test + Nemenyi post-hoc CD diagram implemented.
- [ ] **Gap 2: Cross-Validation Rigor**: Time-Aware / Session-Grouped 5-Fold CV implemented; random row shuffle prohibited.
- [ ] **Gap 3: Ablation Study**: Systematic grid sweep across depth, hidden dimensions, and dropout for Mambular and FT-Transformer.
- [ ] **Gap 4: Strong Baselines**: XGBoost and LightGBM tuned with Optuna (50 trials) included in benchmark.
- [ ] **Gap 5: Robustness Analysis**: Gaussian noise perturbation ($\sigma \le 0.2$) and random feature corruption ($p \le 0.5$) evaluated.
- [ ] **Gap 6: Scalability Testing**: 2-Track benchmark isolates small few-shot track ($N \le 10\text{k}$) from streaming scale ($N \ge 100\text{k}$).
- [ ] **Gap 7: Reproducibility Package**: Fixed random seeds (`SEED=42`), `requirements.txt`, and `manifest.json` hardware capture.
- [ ] **Gap 8: Theoretical Framework**: Rooted in Task-Technology Fit (Goodhue & Thompson 1995) and Design Science Research (Hevner et al. 2004).
- [ ] **Gap 9: Honest Limitations Section**: Documents TabPFN sample limits, PyG GNN memory overhead, and Mamba CUDA dependency.
- [ ] **Gap 10: Clear Future Work Section**: Outlines edge hardware TPU/FPGA deployment and online streaming adaptation.

### Part B: 7 Fatal Peer-Review Vulnerabilities Mitigated
- [ ] **Vulnerability 1: Subjective DEMATEL Solved**: Replaced "3-expert simulation" with Axiomatic Complexity Priors ($W_{\text{theory}}$) + Empirical NMI ($W_{\text{empirical}}$).
- [ ] **Vulnerability 2: IS Identity Crisis Solved**: Framed as Task-Technology Fit utility optimization across 3 operational threat profiles ($T_1, T_2, T_3$).
- [ ] **Vulnerability 3: Dataset Obsolescence Solved**: NSL-KDD demoted to historical baseline; CICIDS2017 decontaminated; TON_IoT (2021) and CIC-DDoS2019 added.
- [ ] **Vulnerability 4: Data Leakage Solved**: Session-grouped splitting by subnet IP prevents host session leakage; inductive graph splitting for GraphIDS.
- [ ] **Vulnerability 5: Incommensurability Solved**: 2-Track benchmark prevents unfair direct comparisons between 10k-sample TabPFN and 2.8M-sample models.
- [ ] **Vulnerability 6: Under-Powered Statistics Solved**: Benchmark expanded to $N=5$ datasets, satisfying Demšar asymptotic normality criteria.
- [ ] **Vulnerability 7: Degenerate DEMATEL Solved**: Formulated reciprocal feedback dynamics (Hardware memory F8 and latency F6 restrict architecture F1 and attention depth F3).

---

## 5. 🏛️ Pre-Submission Reviewer Defense Checklist (Target Venues)

### General Manuscript Criteria
- [ ] **Title Appeal**: Contains clear theoretical positioning, model families, and methodological terms without buzzword soup.
- [ ] **Abstract Strict Word Limit**: Exactly 200–250 words following: Context $\to$ TTF Problem $\to$ 2-Track Benchmark $\to$ Closed-Loop DEMATEL $\to$ Key Results $\to$ Systemic Impact.
- [ ] **The Contribution Triangle**:
  - [ ] *Novelty*: First multi-paradigm comparison (Foundation, SSM, GNN, Transformer) + Autonomous Closed-Loop DEMATEL.
  - [ ] *Scientific Value*: Task-Technology Fit utility proof + Asymptotic complexity validation + Monte Carlo sensitivity proof ($W > 0.95$).
  - [ ] *Practical Impact*: Line-rate Pareto frontier identification for real-time edge network defense.
- [ ] **Citation Quality**:
  - [ ] Minimum 35 total references included.
  - [ ] All related works published $> 2020$ (except 6 classic foundational theories).
  - [ ] 0 retracted papers cited; 100% verified in Scopus/WoS indexing.

### Journal-Specific Compliance Matrix
- [ ] **Target 1: *Information Fusion* (IF: 15.5)**:
  - [ ] Highlighted fusion of NetFlow tabular attributes with graph topological connectivity in GraphIDS.
  - [ ] Emphasized fusion of algorithmic complexity priors with empirical metric telemetry in Fuzzy DEMATEL.
- [ ] **Target 2: *IEEE Trans. on Dependable and Secure Computing* (IF: 7.3)**:
  - [ ] Complete line-rate throughput and latency benchmarks provided in Track B.
  - [ ] Memory footprint under extreme volumetric DDoS traffic demonstrated on CIC-DDoS2019.
- [ ] **Target 3: *IEEE Trans. on Information Forensics and Security* (IF: 6.8)**:
  - [ ] Adversarial robustness degradation slopes under noise perturbations reported.
  - [ ] Decontamination protocol on CICIDS2017 thoroughly documented to prove data validity.
- [ ] **Target 4: *Expert Systems with Applications* (IF: 7.5)**:
  - [ ] Step-by-step mathematical demonstration of Fuzzy DEMATEL (TFN synthesis, CFCS defuzzification, $(D+R, D-R)$ ranking).
  - [ ] Sensitivity analysis on defuzzification thresholds and Monte Carlo perturbation results detailed.

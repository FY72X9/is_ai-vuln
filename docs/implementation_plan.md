# Research Execution Plan & Checklist: Q1 Publication Pipeline (2026)

## Overview
Berdasarkan evolusi penelitian hingga Master Blueprint v4.0:
1. `[.idea/Research_Blueprint_IS_CS_Q1_2026_V2-REVISED.md](file:///d:/Codes/research_banks/is_ai-vuln/.idea/Research_Blueprint_IS_CS_Q1_2026_V2-REVISED.md)` (Arsip V2: 4 model modern)
2. `[.idea/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md](file:///d:/Codes/research_banks/is_ai-vuln/.idea/Research_Blueprint_IS_CS_Q1_2026_FINAL_v3.md)` (Arsip V3: 6 model + Q1 audit 10 gap)
3. `[docs/ACADEMIC_PEER_REVIEW_AND_GAP_ANALYSIS.md](file:///d:/Codes/research_banks/is_ai-vuln/docs/ACADEMIC_PEER_REVIEW_AND_GAP_ANALYSIS.md)` (Audit kritis doktoral: 7 celah fatal penolakan Q1 & transisi ke simulasi tertutup 100%)
4. `[docs/Research_Blueprint_IS_CS_Q1_2026_V4_TTF_SIMULATION.md](file:///d:/Codes/research_banks/is_ai-vuln/docs/Research_Blueprint_IS_CS_Q1_2026_V4_TTF_SIMULATION.md)` (**Master Blueprint Aktif v4.0**: Landasan TTF, 2-Track Benchmark, Simulasi Mandiri Tanpa Pakar Eksternal, 35 Referensi >2020, Aturan Google Colab Free Tier dengan Autorecovery, dan 4 Skrip Otomasi Khusus)

Kami menyusun rencana implementasi untuk menghasilkan dua dokumen operasional utama di `docs/`:
- **`docs/EXECUTION_PLAN.md`**: Panduan teknis eksekusi komprehensif langkah-demi-langkah (setup environment, modul `src/`, protokol data anti-leakage, benchmarking 2-track, engine simulasi Fuzzy DEMATEL, autorecovery Colab, dan layouting grafik 300 DPI).
- **`docs/CHECKLIST.md`**: Instrumen kontrol kualitas dan checklist pelacakan interaktif (`- [ ]`) yang memetakan seluruh aktivitas dari Fase 1 hingga Fase 5, audit 10 gap kritis Q1, verifikasi autorecovery Colab, dan integritas sitasi.

---

## User Review Required

> [!IMPORTANT]
> **Pilar Eksekusi Berdasarkan Blueprint v4.0**:
> 1. **Landasan Teori Utama — Task-Technology Fit (TTF)**: Memetakan 6 model modern ke dalam 3 profil tugas operasional ($T_1$: Line-Rate Edge, $T_2$: Zero-Day Few-Shot, $T_3$: Correlated Multi-Host) dengan Design Propositions (DP1–DP4) formal.
> 2. **Simulasi Teoretis Tertutup 100% (Zero External Human Panels)**: Mengeliminasi kuesioner pakar. Matriks langsung $\tilde{A}$ disintesis dari batas teoretis Big-O ($W_{\text{theory}}$) dimodulasi Normalized Mutual Information ($W_{\text{empirical}}$), divalidasi via uji Monte Carlo 10.000 putaran ($W > 0.95$) dan triangulasi DirectLiNGAM ($SHD \le 2$).
> 3. **Protokol Eksperimen 2-Track Benchmark**:
>    - *Track A (Few-Shot Generalization $N \le 10\text{k}$)*: Seluruh 6 model modern (TabPFN v3, TabICL v2, GraphIDS, SAINT, Mambular, FT-Transformer) + 2 Baseline (XGBoost, LightGBM).
>    - *Track B (Industrial High-Throughput Scalability $N \ge 100\text{k}$)*: Khusus model scalable (Mambular SSM, FT-Transformer, GraphIDS, XGBoost, LightGBM).
> 4. **Aturan Lingkungan Google Colab Free Tier**:
>    - Budget memori T4 GPU (15GB VRAM) & 12.7GB RAM dengan `gc.collect()` dan `torch.cuda.empty_cache()` rutin.
>    - Autorecovery caching berbasis `checkpoint_state.json` di Drive: otomatis me-resume fold yang terputus tanpa mengulang dari 0.
>    - Logging output berversi dan bertimestamp (`experiment_output/run_YYYYMMDD_HHMMSS_v4.0/`) dengan `manifest.json`.
> 5. **Otomasi 4 Skrip Khusus**:
>    - Metadata retrieval sitasi via OpenAlex/CrossRef API (`src/utils/references_harvester.py`).
>    - Validasi eksistensi DOI, indeks Scopus, dan Retraction Watch (`src/utils/references_validator.py`).
>    - Pengunduhan dataset ke Drive dengan proteksi otomatis `.gitignore` (`src/data/drive_downloader.py`).
>    - Layouting grafik standar publikasi 300+ DPI double-column (`src/visualization/publication_styler.py`).
> 6. **Basis 35 Referensi Terverifikasi**: 6 teori klasik + 29 riset kontemporer (>2020).

---

## Proposed Changes

### Documentation Layer (`docs/`)

#### [NEW] [`docs/EXECUTION_PLAN.md`](file:///d:/Codes/research_banks/is_ai-vuln/docs/EXECUTION_PLAN.md)
Dokumen panduan eksekusi teknis operasional yang memuat:
1. **Theoretical Foundations (TTF & DSR Integration)**:
   - Formalisasi fungsi utilitas TTF, 3 profil operasional ($T_1, T_2, T_3$), dan Design Propositions (DP1–DP4).
2. **Modular Architecture & Scripts Specification (`src/`)**:
   - Struktur modul lengkap: `src/data/`, `src/models/`, `src/evaluation/`, `src/dematel/`, `src/visualization/`, `src/utils/`.
   - Kode implementasi skrip harvester metadata, validator DOI/retraksi, downloader Drive dengan auto `.gitignore`, dan styler publikasi 300 DPI.
3. **Data Integrity & Leakage Prevention Protocol**:
   - Time-Aware & Session-Grouped 5-Fold Cross-Validation (`GroupKFold` pada subnet IP / jendela waktu).
   - Prosedur pembersihan otomatis CICIDS2017 & kurasi dataset komparasi kontemporer (TON_IoT, CIC-DDoS2019, UNSW-NB15, NSL-KDD).
   - Inductive graph snapshot splitting untuk GraphIDS.
4. **2-Track Benchmark Execution Suite**:
   - Track A ($N \in \{1\text{k}, 5\text{k}, 10\text{k}\}$) & Track B ($N \in \{100\text{k}, 500\text{k}, 1\text{M}\}$).
   - Unified Model Interface untuk 6 arsitektur modern + 2 baseline teroptimasi Optuna.
5. **Closed-Loop Simulation Fuzzy DEMATEL Engine**:
   - Formulasi matematis $W_{\text{theory}} + W_{\text{empirical}} \to \text{TFN}$.
   - Algoritma CFCS defuzzification, ranking Prominence $(D+R)$ dan Relation $(D-R)$.
   - Protokol uji Monte Carlo 10.000 iterasi ($W > 0.95$) dan triangulasi DirectLiNGAM ($SHD \le 2$).
6. **Google Colab Free Tier & Autorecovery Pipeline**:
   - Setup Google Drive mounting, isolasi library (`pip install deeptab tabpfn tabicl pyDEMATEL`).
   - Logika `CheckpointManager`: pembacaan `checkpoint_state.json`, resume otomatis per fold, dan pencegahan restart dari 0.
   - Struktur folder output per eksekusi berversi dan bertimestamp (`experiment_output/run_YYYYMMDD_HHMMSS_v4.0/`).
7. **14-Week Execution Milestones**: Timeline mingguan dari Phase 1 hingga Phase 5.

---

#### [NEW] [`docs/CHECKLIST.md`](file:///d:/Codes/research_banks/is_ai-vuln/docs/CHECKLIST.md)
Dokumen checklist operasional interaktif memuat:
1. **Interactive Phase-by-Phase Checklist** (Phase 1 Setup s.d. Phase 5 Submission).
2. **Q1 Readiness Audit Checklist** (10 Critical Gaps + 7 Fatal Reviewer Pitfalls).
3. **Colab Free-Tier & Autorecovery Verification Checklist** (Drive mount check, checkpoint cache hit/miss, crash recovery test).
4. **References & Data Cleanliness Checklist** (Verifikasi eksistensi 35 DOI, cek retraksi, konfirmasi `.gitignore` data besar).
5. **Publication Quality Checklist** (300+ DPI figures, IMRAD LaTeX format, Pareto frontier plots).

---

#### [MODIFY] [`README.md`](file:///d:/Codes/research_banks/is_ai-vuln/README.md)
- Memperbarui overview proyek dengan landasan TTF, simulasi tertutup 100%, arsitektur 2-track, aturan Colab free-tier, dan tautan lengkap ke blueprint v4.0, dokumen review, execution plan, dan checklist.

---

## Verification Plan

### Automated / Syntax Verification
- Validasi markdown syntax, clickable links, dan diagram Mermaid rendering.
- Verifikasi skrip eksekusi Colab dan sintaks Python pada seluruh modul.

### Academic Rigor & Simulation Verification
- Memastikan formulasi utilitas TTF, matriks DEMATEL tanpa pakar, dan 35 referensi terverifikasi secara konsisten.

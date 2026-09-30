# Chapter 1: Title, Author Metadata, and Abstract

## Title Written with Times New Roman 18
**Task-Technology Fit in Multi-Paradigm Network Intrusion Detection: An Empirical Evaluation of Tree Ensembles, Deep Learning, and Tabular Foundation Models**

### Author Information
**Farrell Yodihartomo**  
Department of Information Systems, Faculty of Computer Science, Universitas Indonesia, Depok 16424, Indonesia  
E-mail: farrell.yodihartomo@ui.ac.id  

---

### ABSTRACTS

*Manuscript received September 2026; revised October 2026; accepted November 2026. Date of publication December 2026. International Journal, JITSI : Jurnal Ilmiah Teknologi Sistem Informasi licensed under a Creative Commons Attribution-Share Alike 4.0 International License.*

*Network intrusion detection systems face conflicting operational demands: sustaining line-rate packet throughput, generalizing to unobserved zero-day exploits, and fitting within strict hardware resource budgets. Most benchmark studies evaluate models as isolated algorithms, ignoring how architectural properties align with real-world security workflows. We evaluate this problem through the theoretical lens of Task-Technology Fit (TTF) and Design Science Research, examining eight architectures spanning gradient-boosted decision trees, tabular transformers, selective state space models, and tabular foundation models. Using five decontaminated network benchmarks (CICIDS2017, UNSW-NB15, TON_IoT, CIC-DDoS2019, and NSL-KDD), our dual-track evaluation applies subnet-isolated cross-validation alongside active zero-day holdouts. The results show that tree ensembles (LightGBM and XGBoost) excel on observed attacks (Seen F1 >= 0.9469) with sub-microsecond processing. In contrast, the prior-data fitted foundation model TabPFN v3 achieves the strongest zero-day transfer (Unseen F1 = 0.6173 +- 0.4275), leading Task T2 utility (U(T2) = 0.7100) and surpassing deep neural baselines by 6 to 10 percentage points, though requiring 3.11 ms per flow. Selective state space models (Mambular SSM) match tree throughput (>929,000 flows/s) while keeping memory consumption flat as batch volumes grow. Non-parametric Demšar tests confirm significant architectural divergence (Friedman chi-square = 29.6667, p = 1.093e-4). Triangular Fuzzy DEMATEL across 10,000 Monte Carlo perturbation runs (Kendall W = 0.9716) identifies model layer formulation as the primary systemic cause of operational performance. These findings support four formal Design Propositions and an operational Three-Tier Security Operations Center blueprint.*

**Keywords / Kata Kunci**: Network Intrusion Detection; Task-Technology Fit; Tabular Foundation Models; Selective State Space Models; Fuzzy DEMATEL.

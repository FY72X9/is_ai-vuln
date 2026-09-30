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

*Network intrusion detection systems operate under severe friction between line-rate packet throughput, out-of-distribution zero-day generalization, and runtime computational footprint. Classical benchmark studies assess machine learning models as isolated mathematical algorithms without grounding their capabilities in operational security workflows. This investigation addresses this theoretical gap by evaluating eight architectures spanning gradient-boosted decision trees, tabular transformers, selective state space models, and tabular foundation models through the theoretical lens of Task-Technology Fit (TTF) and Design Science Research. Across five decontaminated network benchmarks (CICIDS2017, UNSW-NB15, TON_IoT, CIC-DDoS2019, and NSL-KDD), we execute a dual-track experimental evaluation enforcing subnet-isolated cross-validation and active zero-day holdout induction. The empirical evidence demonstrates that tree ensembles (LightGBM and XGBoost) dominate observed attack classification (Seen F1 >= 0.9469) while sustaining sub-microsecond processing. Conversely, the prior-data fitted foundation model (TabPFN v3) achieves the highest zero-day transfer (Unseen F1 = 0.6173 +- 0.4275), leading Task T2 utility (U(T2) = 0.7100) and exceeding deep neural baselines by 6 to 10 percentage points at an inference cost of 3.11 ms per flow. Selective state space models (Mambular SSM) match tree processing speeds (>929,000 flows/sec) while sustaining flat VRAM allocation across expanding data regimes. Non-parametric Demšar tests confirm significant architectural divergence (Friedman chi-square = 29.6667, p = 1.093e-4), while Triangular Fuzzy DEMATEL causal discovery across 10,000 Monte Carlo perturbation runs (Kendall W = 0.9716) isolates model layer formulation as the primary systemic cause of operational performance. From these empirical validations, we confirm four formal Design Propositions and provide an operational Three-Tier Security Operations Center blueprint.*

**Keywords / Kata Kunci**: Network Intrusion Detection; Task-Technology Fit; Tabular Foundation Models; Selective State Space Models; Fuzzy DEMATEL.

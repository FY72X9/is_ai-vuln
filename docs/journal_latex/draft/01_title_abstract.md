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

*Network intrusion detection systems face severe operational divergence between high-throughput packet filtering, zero-day generalization, and computational footprint. Traditional benchmark evaluations examine machine learning models as isolated mathematical constructs, detached from operational security workflows. This study resolves this theoretical disconnect by investigating eight architectures spanning gradient-boosted trees, tabular deep learning, selective state space models, and tabular foundation models through the theoretical lens of Task-Technology Fit (TTF) and Design Science Research. Using a dual-track experimental design across five decontaminated intrusion datasets (CICIDS2017, UNSW-NB15, TON_IoT, CIC-DDoS2019, and NSL-KDD), we evaluate detection efficacy under strict subnet-isolated cross-validation with active zero-day holdout induction. The empirical findings reveal that gradient-boosted trees (LightGBM and XGBoost) achieve superior seen attack detection (Seen F1 >= 0.9469) and sub-millisecond line-rate filtering. Conversely, the prior-data fitted foundation model (TabPFN v3) leads zero-day generalization (Unseen F1 = 0.6173 +- 0.4275), outperforming neural baselines by 6 to 10 percentage points at the cost of a 3.11 ms per-flow latency. Selective state space models (Mambular SSM) match tree throughput (>929,000 flows/sec) while sustaining flat VRAM allocation across expanding data regimes. Non-parametric Demšar tests confirm significant architectural differentiation (Friedman chi-square = 29.6667, p = 1.093e-4), while Triangular Fuzzy DEMATEL causal discovery with 10,000 Monte Carlo runs (Kendall W = 0.9716) isolates model architecture as the primary causal driver of operational performance. Based on these empirical validations, we formulate four formal Design Propositions and present a Three-Tier Security Operations Center blueprint.*

**Keywords / Kata Kunci**: Network Intrusion Detection; Task-Technology Fit; Tabular Foundation Models; Selective State Space Models; Fuzzy DEMATEL.

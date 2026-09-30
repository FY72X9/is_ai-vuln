# Chapter 3: Research Methodology

## 2. Research Methodology

This study establishes a rigorous empirical evaluation architecture combining experimental machine learning benchmarks with formal statistical validation and causal structural equation modeling. Fig. 1 illustrates the end-to-end research methodology, organized into five sequential phases.

```
+-----------------------------------------------------------------------------------+
| Phase 1: Ingestion, Decontamination & Subnet-Isolated Anti-Leakage Partitioning    |
| (5 Multi-Domain Datasets: CICIDS2017, UNSW-NB15, TON_IoT, CIC-DDoS2019, NSL-KDD)   |
+-----------------------------------------+-----------------------------------------+
                                          |
        +---------------------------------+---------------------------------+
        |                                                                   |
        v                                                                   v
+-----------------------------------------+   +-----------------------------------------+
| Phase 2 (Track A): Few-Shot Zero-Day    |   | Phase 2 (Track B): Industrial Streaming |
| Generalization Benchmark                |   | Scalability Profiling                   |
| (8 Architectures, 5 Folds, N <= 10,000, |   | (5 Architectures, N in {50k, 100k,      |
| Active Zero-Day Holdout Induction)      |   |  190.5k, 250k}, Dynamic CUDA Telemetry) |
+-----------------------------------------+   +-----------------------------------------+
        |                                                                   |
        +---------------------------------+---------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 3: Non-Parametric Statistical Testing & Ablation Analysis                   |
| (Demšar Friedman, Iman-Davenport, Nemenyi CD, Wilcoxon, Gaussian Noise Battery)   |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 4: Closed-Loop Causal Structural Discovery & Algorithmic Triangulation      |
| (Triangular Fuzzy DEMATEL, 10,000 Monte Carlo Runs, DirectLiNGAM Convergence)     |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 5: Task-Technology Fit Synthesis & Three-Tier SOC Architectural Blueprint   |
| (Validation of DP1 - DP4, Master TTF Utility Evaluation, Green AI Carbon Modeling)|
+-----------------------------------------------------------------------------------+
```
*Fig. 1. End-to-end empirical research methodology and experimental phases.*

### 2.1 Problem Formulation and Task-Technology Fit Utilities
Let an individual network communication flow be represented by a continuous-discrete feature vector $\mathbf{x}_i \in \mathbb{R}^D$ and an associated class label $y_i \in \mathcal{C}$. The target attack taxonomy comprises three disjoint subsets: $\mathcal{C} = \{\text{Benign}\} \cup \mathcal{C}_{\text{seen}} \cup \mathcal{C}_{\text{unseen}}$, where $\mathcal{C}_{\text{unseen}}$ denotes zero-day exploits excluded from model training. The classification objective is to estimate the posterior distribution $P(y_i = c \mid \mathbf{x}_i; \theta)$.

Because network traffic displays severe class imbalance (often exceeding 100:1 between benign flows and rare attack vectors), overall accuracy provides a misleading measure of operational competence. We evaluate detection efficacy through Macro-averaged F1, Seen Attack F1, and Unseen Zero-Day F1:
$$\text{Precision}_c = \frac{\text{TP}_c}{\text{TP}_c + \text{FP}_c}, \quad \text{Recall}_c = \frac{\text{TP}_c}{\text{TP}_c + \text{FN}_c}, \quad F_{1, c} = \frac{2 \cdot \text{Precision}_c \cdot \text{Recall}_c}{\text{Precision}_c + \text{Recall}_c} \quad (1)$$
$$F_{1, \text{macro}} = \frac{1}{|\mathcal{C}|} \sum_{c \in \mathcal{C}} F_{1, c}, \quad F_{1, \text{seen}} = \frac{1}{|\mathcal{C}_{\text{seen}}|} \sum_{c \in \mathcal{C}_{\text{seen}}} F_{1, c}, \quad F_{1, \text{unseen}} = \frac{1}{|\mathcal{C}_{\text{unseen}}|} \sum_{c \in \mathcal{C}_{\text{unseen}}} F_{1, c} \quad (2)$$

In accordance with Goodhue and Thompson [17], technological utility is evaluated against three operational SOC tasks:
1. **Task $T_1$ (Line-Rate Perimeter Filtering)**: Prioritizes sub-millisecond per-flow latency $L$ (in ms) and high throughput while retaining high seen attack detection:
$$U(T_1) = 0.40 \cdot F_{1, \text{seen}} + 0.35 \cdot \min\left(1.0, \frac{0.005}{L + 10^{-6}}\right) + 0.25 \cdot \text{ROC-AUC} \quad (3)$$
2. **Task $T_2$ (Zero-Day Forensic Isolation)**: Prioritizes generalization on completely unobserved attack manifolds without parameter re-estimation:
$$U(T_2) = 0.70 \cdot F_{1, \text{unseen}} + 0.20 \cdot F_{1, \text{seen}} + 0.10 \cdot \text{ROC-AUC} \quad (4)$$
3. **Task $T_3$ (Enterprise Composite SOC Triage)**: Balances overall classification fidelity, zero-day resilience, and sustained streaming throughput:
$$U(T_3) = 0.35 \cdot F_{1, \text{macro}} + 0.30 \cdot F_{1, \text{unseen}} + 0.20 \cdot \text{ROC-AUC} + 0.15 \cdot \min\left(1.0, \frac{\text{Throughput}}{100,000}\right) \quad (5)$$

### 2.2 Theoretical Grounding and Formal Design Propositions
Following the Design Science Research guidelines of Hevner et al. [18] and the Task-Technology Fit framework of Goodhue and Thompson [17], technological artifacts generate organizational value only when their structural capabilities align with task requirements. In autonomous cyber-defense, task requirements translate into physical processing constraints, while technology dimensions correspond to the mathematical inductive biases of competing model families. Based on these theoretical foundations, we formalize four Design Propositions:

* **Design Proposition 1 ($DP_1$ - Linear Complexity Fit in Line-Rate Streaming)**: *In operational tasks governed by line-rate streaming constraints ($T_1$), selective State Space Models (Mambular SSM) and decision tree ensembles exhibit superior Task-Technology Fit over self-attention transformers due to linear-time $\mathcal{O}(D)$ associative scan efficiency in hardware SRAM.*
* **Design Proposition 2 ($DP_2$ - In-Context Prior Fit in Zero-Day Forensic Isolation)**: *In zero-day forensic tasks characterized by extreme sample scarcity ($T_2$), tabular foundation models (TabPFN v3) maximize Task-Technology Fit through Bayesian in-context inference over synthetic priors without parameter re-estimation.*
* **Design Proposition 3 ($DP_3$ - Topological Correlation Fit in Multi-Host Tracking)**: *In coordinated multi-host intrusion campaigns ($T_3$), relational graph neural networks (GraphIDS) achieve high operational throughput by encoding structural topological priors, but require hybrid tabular feature integration to prevent accuracy degradation on sparse subnet neighborhoods.*
* **Design Proposition 4 ($DP_4$ - Hardware-Constrained Causal Feedback)**: *Hardware memory footprint and inference latency ceilings act as asymptotic bounding constraints governed causally by mathematical layer formulation, rendering post-hoc software pruning ineffective against quadratic attention bottlenecks.*

### 2.3 Dataset Characteristics and Anti-Leakage Protocol
Recent methodological audits demonstrated that standard public NIDS benchmarks contain severe data leakage, synthetic artifact pollution, and duplicate records across train and test splits [19], [24]. To guarantee audit-proof empirical validity, we curate and decontaminate five multi-domain network intrusion datasets, summarized in Table 1.

Table 1. Benchmark Dataset Characteristics and Decontamination Telemetry
| Dataset Identifier | Raw Captured Records | Benchmark Partition ($N$) | Feature Count ($D$) | Subnet Isolation Strategy | Attack Categories Evaluated |
|---|---|---|---|---|---|
| **CICIDS2017** [19] | 2,522,000 | 10,000 | 78 | GroupKFold on `/24` subnet masks | DoS, DDoS, PortScan, Botnet, Infiltration |
| **UNSW-NB15** [20] | 2,540,044 | 10,000 | 49 | GroupKFold on IP subnet pairs | Exploits, Reconnaissance, DoS, Generic, Fuzzers |
| **TON_IoT** [21] | 4,610,455 | 10,000 | 43 | Temporal session and edge node grouping | Backdoor, Injection, DDoS, Scanning, Ransomware |
| **CIC-DDoS2019** [22] | 426,076 | 10,000 | 65 | GroupKFold on client-server IP pairs | TFTP, DrDoS_NTP, Syn, UDP, MSSQL, LDAP |
| **NSL-KDD** [23] | 148,517 | 10,000 | 41 | Service-protocol interaction grouping | DoS, Probe, R2L, U2R |

To prevent distributional leakage and evaluate realistic zero-day generalization, we enforce Algorithm 1 across all dataset folds.

```
Algorithm 1: Subnet-Isolated Anti-Leakage Partitioning with Active Zero-Day Induction
--------------------------------------------------------------------------------------
Input  : Dataset D = {(x_i, y_i, ip_src_i, ip_dst_i, attack_cat_i)}_{i=1}^N,
         Number of folds K = 5, Candidate zero-day attacks C_zd
Output : Evaluated model metrics across all validation partitions M_eval

1:  Extract Subnet Group Identifiers:
    for i = 1 to N do
        group_id[i] <- IPv4Network(ip_src_i).network_address(mask="/24")
    end for
2:  Initialize GroupKFold(n_splits = K) using group_id
3:  Identify top distinct rare attacks for zero-day holdout:
    C_holdout <- SelectTopDistinctAttacks(C_zd, count = 2)
4:  for fold k = 1 to K do
        D_train_k, D_val_k <- SplitFold(D, fold = k, groups = group_id)
        if k in {1, 2} then
            c_target <- C_holdout[k]
            // Purge target attack class entirely from training partition
            D_train_k <- {(x, y) in D_train_k | attack_cat != c_target}
            // Retain c_target in validation partition to evaluate zero-day transfer
        end if
5:      Fit Scaler S strictly on D_train_k (prevent distribution leakage)
        X_train <- S.fit_transform(D_train_k.X)
        X_val   <- S.transform(D_val_k.X)
6:      Train candidate architecture: model.fit(X_train, D_train_k.y)
7:      Evaluate Seen F1 on {attack_cat != c_target}
8:      Evaluate Unseen Zero-Day F1 on {attack_cat == c_target}
9:  end for
10: return Aggregated means and standard deviations across all K folds
```

### 2.4 Evaluated Model Families and Algorithmic Mechanics
We evaluate eight representative architectures covering four core paradigms:
1. **Gradient-Boosted Decision Trees (GBDTs)**: LightGBM [4] and XGBoost [5]. These models construct ensembles of shallow decision trees via gradient-based split finding and histogram binning.
2. **Tabular Deep Learning**: FT-Transformer [8], which tokenizes numerical features into continuous embeddings processed by multi-head self-attention, and SAINT [9], which alternates between self-attention across columns and inter-sample attention across rows.
3. **Selective State Space Models (SSMs)**: Mambular SSM [12], which adapts continuous selective state-space scans [11] to tabular sequences. As specified in Algorithm 2, Mambular projects discretized features into a hidden continuous state $\mathbf{h}_t \in \mathbb{R}^{N_{\text{state}}}$, executing linear-time scans directly in hardware SRAM.
4. **Relational Graph Neural Networks**: GraphIDS [30], which constructs communication graphs where IP endpoints form nodes and packet flows form directed edges, executing message passing over topological neighborhoods [31].
5. **Tabular Foundation Models**: TabPFN v3 [13] and TabICL v2 [14]. As specified in Algorithm 3, TabPFN formulates classification as Prior-Data Fitted in-context Bayesian inference [32], feeding query flows alongside reference exemplars without gradient updates.

```
Algorithm 2: Mambular SSM Hardware-Aware Discretized State Space Scan
--------------------------------------------------------------------------------------
Input  : Tokenized tabular feature sequence X = [x_1, x_2, ..., x_D] in R^{D x d_model},
         Continuous state transition matrices (A, B, C), Discretization step Delta
Output : Sequence representation y_out in R^{d_model}

1:  Compute input-dependent selective discretization parameters:
    Delta_t <- softplus(Parameter_Delta + Linear_Delta(x_t))
    B_t     <- Linear_B(x_t)
    C_t     <- Linear_C(x_t)
2:  Discretize continuous parameters via Zero-Order Hold (ZOH):
    A_bar_t <- exp(Delta_t * A)
    B_bar_t <- (A_bar_t - I) * (A)^{-1} * B_t
3:  Execute parallel associative prefix scan across sequence coordinates:
    h_t <- A_bar_t * h_{t-1} + B_bar_t * x_t   (computed in GPU SRAM)
4:  Generate projected representation:
    y_t <- C_t * h_t + D * x_t
5:  return Pooled sequence representation y_out <- MeanPool(y_1, ..., y_D)
```

```
Algorithm 3: TabPFN Prior-Data Fitted In-Context Bayesian Inference
--------------------------------------------------------------------------------------
Input  : Context exemplars D_ctx = {(x_j, y_j)}_{j=1}^{N_ctx}, Query flow x_q,
         Pre-trained Prior-Data Fitted Network weights Theta_PIR
Output : Posterior intrusion probability P(y_q = 1 | x_q, D_ctx)

1:  Embed input feature dimensions via learned linear projection:
    E_ctx <- [Linear(x_j) || Embedding(y_j)] for j = 1 to N_ctx
    E_q   <- [Linear(x_q) || ZeroEmbedding()]
2:  Concatenate context and query sequence:
    Z_0 <- Concat(E_ctx, E_q) in R^{(N_ctx + 1) x d_model}
3:  for layer l = 1 to L_blocks do
        Z_l <- TransformerBlock_l(Z_{l-1}; Theta_PIR)
    end for
4:  Extract query token representation and compute softmax:
    P(y_q = 1 | x_q, D_ctx) <- Softmax(Linear_out(Z_L[query_index]))
5:  return Posterior probability vector
```

### 2.5 Dual-Track Experimental Architecture
To resolve computational incommensurability across diverse model families, we decouple evaluation into two operational tracks:
* **Track A (Few-Shot Zero-Day Generalization Track)**: Standardizes training on $N \le 10,000$ records per fold across all five datasets. Evaluates all eight models across 5 folds with active zero-day holdout induction to measure Macro F1, Seen F1, Unseen F1, per-flow latency, and throughput.
* **Track B (Industrial Streaming Scalability Track)**: Evaluates high-throughput architectures (LightGBM, XGBoost, Mambular SSM, FT-Transformer, and GraphIDS) across expanding sample sizes ($N \in \{50\text{k}, 100\text{k}, 190,474, 250\text{k}\}$). The threshold $N = 190,474$ corresponds to the full decontaminated partition of the enterprise CICIDS2017 benchmark, while $N = 250\text{k}$ represents the high-volume streaming batch boundary. Telemetry scripts query active CUDA device memory allocation directly from the GPU runtime via `torch.cuda.max_memory_allocated()` alongside per-flow processing latency.

### 2.6 Non-Parametric Significance and Causal Discovery Framework
To evaluate whether observed performance differences represent genuine architectural advantages, we execute Demšar's non-parametric testing suite [25]:
1. **Friedman Test**: Computes the chi-square statistic $\chi_F^2$ based on average model ranks across the five datasets.
2. **Iman-Davenport Correction**: Alleviates the conservative bias of the standard Friedman statistic via an $F$-distribution formulation:
$$F_F = \frac{(M - 1)\chi_F^2}{M(K - 1) - \chi_F^2} \sim F(K - 1, (K - 1)(M - 1)) \quad (6)$$
where $K = 8$ architectures and $M = 5$ datasets.
3. **Nemenyi Post-Hoc Test**: Calculates the Critical Difference (CD) threshold at significance level $\alpha = 0.05$:
$$\text{CD} = q_\alpha \sqrt{\frac{K(K + 1)}{6M}} \quad (7)$$
Two models perform with statistical significance only if their average ranks differ by at least $\text{CD}$.

To uncover structural causal dependencies among model parameters, computational constraints, and performance outcomes, we apply Triangular Fuzzy DEMATEL [26], [27], [28], [33], [34]. We define seven operational factors: Model Architecture ($F_1$), Training Sample Size ($F_2$), Inference Latency ($F_3$), Memory Footprint ($F_4$), Seen Attack F1 ($F_5$), Unseen Zero-Day F1 ($F_6$), and Robustness to Noise ($F_7$). 

Most DEMATEL studies rely on subjective questionnaires filled out by small panels of 3 to 10 experts. In network security, human scoring struggles to quantify microsecond latencies, memory bus contention, or cache behavior, while remaining prone to vendor preferences. To avoid subjective bias, our causal engine calculates initial direct relations ($W_{\text{theory}}$) directly from computational complexity bounds ($\mathcal{O}(D)$ versus $\mathcal{O}(D^2)$) and statistical learning theory, updating them with cross-validation outcomes ($W_{\text{empirical}}$). We build fuzzy direct-relation matrices $\tilde{Z}$, normalize them into $\tilde{X}$, and derive the total-relation matrix $\tilde{T} = \tilde{X}(I - \tilde{X})^{-1}$. Prominence ($D + R$) and net relation ($D - R$) are evaluated across 10,000 Monte Carlo perturbation runs to confirm stability via Kendall's concordance ($W \ge 0.95$). Finally, we validate the resulting causal topology using DirectLiNGAM non-Gaussian causal discovery [29] against a Structural Hamming Distance threshold ($\text{SHD} \le 2$).

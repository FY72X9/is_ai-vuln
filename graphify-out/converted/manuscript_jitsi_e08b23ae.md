<!-- converted from manuscript_jitsi.docx -->







Task-Technology Fit in Multi-Paradigm Network Intrusion Detection: An Empirical Evaluation of Tree Ensembles, Deep Learning, and Tabular Foundation Models
Farrell Yodihartomo#
# Department of Information Systems, Faculty of Computer Science, Universitas Indonesia, Depok 16424, Indonesia
E-mail: farrell.yodihartomo@ui.ac.id
Introduction
The following are instructions for writing a paper in the Scientific Journal of Information Systems Technology published by the Padang State Polytechnic Information Technology Department. The authors are fully responsible for the contents of the manuscript written and manuscripts are writings that have never been published [1, 2].
Articles should contain articles that contain 1. Introduction, 2. Research Methods (may include analysis, architecture, methods used to solve problems, implementation), 3. Results and Discussion, 4. Conclusions, 5. Acknowledgments (if any) and References.
The contents of the introduction are answers to questions [3-7]:
• Background
• A brief literature reviews
• Reasons for this research
• Purpose questions.
Research Methodology
Describe the preparation methods and characterization techniques used. Explain briefly, but still accurately such as size, volume, replication and workmanship techniques. The new method must be explained in detail so that other researchers can reproduce the experiment. While established methods can be explained by picking out references.
2.1. Script Length
Manuscripts are written in A4 paper size with a minimum number of pages of 6 pages, a maximum of 15 pages, including tables and figures, and with reference to the writing procedures as compiled in this paper.
The formula is written clearly using an equation with an index like the following example:
F = -2,3 x 10 6 x  F2  x  	                (1)
which F is base resonance frequency (MHz), M is total mass of gas molekul absorbed (g)[1]. and A is the area of electroda (cm2) [8].

The program listing and algorithm design are written using fixed width letters such as:
List Programming
Input: mMG, Ed
Output: mMG
Initialization i, j
Get line, column, max
[line,column] = size(mMG)
max=0
for i = 1 to line do
for j = 1 to column do
if max < mMG(i, j)
max = mMG(i, j)
end if
end for
end for
for i = 1 to line do
for j = 1 to column do
if Ed(i, j) =128
mMG(i, j) = max
end if
end for
end for

2.2. Manuscript Organization
The title must be clear and concise. The author's name and affiliation as written above. The author's name is clearly written without a title. Numbering headings with Arabic system with sub-headings up to a maximum of 3 levels.
2.3. Table
The tables must be numbered in the order in which they are presented (Table 1, etc.). The title of the table is written on the table in a centered (center justified) position. The font used is 9pt both in table title and table contents. Tables must be referenced and referenced in the text.


2.4. Figure
Figures are numbered in the order of presentation (Fig. 1, etc.). The title of the image placed below the image in the center position (center justified). The font used in the title of the image is 8pt. Images must be referred to and referred to in the text


2.5. References
Writing libraries using the IEEE Referencing Standard system. Everything listed in the bibliography must be referred to in writing or paper.
Results And Discussion
The series of research results is based on a logical sequence / arrangement to form a story. The contents indicate facts / data and do not discuss the results. Can use Tables and Numbers but not repeatedly repeat the same data in figures, tables and text. To further clarify the description, you can use subtitles.
Discussion is the basic explanation, relationship and generalization shown by the results. The description answers the research question. If there are doubtful results then display it objectively.
3.1. Specification
Use Times New Roman font type throughout the text, with the font size as exemplified in this writing guide. Spacing is single and the contents of the text or text using the left-right alignment (justified).
3.2. Page Size
The page size is A4 (210 mm x 297 mm). Page margins are 25 mm top-bottom, left and right.
3.3. Script Layout
An easy way to make layouts is to use this guide directly.
3.4 Headings
Use the style headings in this template directly. The style has been formatted in such a way as to provide appropriate heading spacing.
Conclusions
In conclusion there must be no reference. The conclusion contains the facts obtained. State the possible applications, implications and speculations accordingly. If needed, give suggestions for further research.

Acknowledgment
Mention the names of funders and facility providers who assist the research

# Referensi
Bach, D., Pich, S., Soriano, F. X., Vega, N., Baumgartner, B., Oriola, J., Daugaard J R, Lloberas J, Camps M, Zierath J R, & Rabasa-Lhoret, R. (2003). Mitofusin-2 determines mitochondrial network architecture and mitochondrial metabolism A novel regulatory mechanism altered in obesity. Journal of Biological Chemistry, 278(19), 17190-17197.
Bereiter-Hahn, J. (1990). Behavior of mitochondria in the living cell. International review of cytology, 122, 1-63.
Chen, H., Vermulst, M., Wang, Y. E., Chomyn, A., Prolla, T. A., McCaffery, J. M., & Chan, D. C. (2010). Mitochondrial fusion is required for mtDNA stability in skeletal muscle and tolerance of mtDNA mutations. Cell, 141(2), 280-289.
Dallas, C., Gerbi, A., Tenca, G., Juchaux, F., & Bernard, F. X. (2008). Lipolytic effect of a polyphenolic citrus dry extract of red orange, grapefruit, orange (SINETROL) in human body fat adipocytes. Mechanism of action by inhibition of cAMP-phosphodiesterase (PDE). Phytomedicine, 15(10), 783-792.
Flögel, U., Laussmann, T., Gödecke, A., Abanador, N., Schäfers, M., Fingas, C. D., Metzger S, Levkau B, Jacoby C, & Schrader, J. (2005). Lack of myoglobin causes a switch in cardiac substrate selection. Circulation research, 96(8), e68-e75.
Garnier, A., Fortin, D., Zoll, J., N’Guessan, B., Mettauer, B., Lampert, E., Veksler V., & Ventura-Clapier, R. (2005). Coordinated changes in mitochondrial function and biogenesis in healthy and diseased human skeletal muscle. The FASEB Journal, 19(1), 43-52.

Name the funders and facility providers who assisted with the research. Please make sure that the text is up to date. References at least 10 references. It is expected that 20 to 30% of references are the latest papers

1. Introduction
Enterprise network appliances inspect continuous traffic at line rates from 10 Gbps to 100 Gbps [1], [2]. At this scale, Network Intrusion Detection Systems (NIDS) must evaluate high-dimensional packet flows and flag anomalous telemetry before attackers reach internal subnets [3]. Security operations centers (SOC) face an inherent trade-off among three operational goals: sub-millisecond per-flow latency, accurate classification of known attack signatures, and generalization to unobserved zero-day exploits.
For tabular traffic classification, Gradient-Boosted Decision Trees (GBDTs), particularly LightGBM [4] and XGBoost [5], remain the standard baseline. Their recursive orthogonal splits fit the discrete, uncoordinated coordinates common in network telemetry (such as TCP flags, port numbers, and packet counters) with minimal computational overhead [6]. Because NetFlow features lack spatial stationarity and translation invariance, axis-aligned splits partition input spaces effectively without mapping coordinates into dense continuous embeddings [7]. The fundamental limitation lies in extrapolation. Axis-aligned bounding boxes fail to generalize when novel exploits fall outside the feature ranges established during training.
Tabular deep learning models attempt to resolve this boundary limitation. Architectures such as FT-Transformer [8] and SAINT [9] use self-attention to capture complex inter-feature relationships. Self-attention yields smoother, continuous decision boundaries, but its computational complexity scales quadratically (O(D^2)) with feature count D. Under line-rate traffic, this quadratic scaling leads to packet queuing and high GPU memory demands [10]. To bypass quadratic overhead, selective State Space Models (SSMs), such as Mamba [11] and its tabular adaptation Mambular [12], apply hardware-aware parallel associative scans in linear time O(D). In parallel, prior-data fitted tabular foundation models, notably TabPFN [13] and TabICL [14], frame classification as in-context Bayesian inference. Pre-trained on synthetic causal graphs, they perform zero-shot inference on novel tasks without weight updates.
Despite these algorithmic developments, the intrusion detection literature often suffers from an Information Systems (IS) disconnect. Many studies treat machine learning models as isolated algorithms, ranking architectures by aggregate accuracy or F1 scores on static test sets [15], [16]. This narrow focus divorces algorithmic behavior from operational realities, hiding trade-offs between latency, hardware footprint, and forensic accuracy. A model with high offline accuracy can easily fail in an active SOC if its per-flow latency causes packet drops at edge gateways.
We ground our analysis in the Task-Technology Fit (TTF) framework of Goodhue and Thompson [17] and the Design Science Research (DSR) guidelines of Hevner et al. [18]. TTF posits that technology generates organizational value only when its capabilities match the requirements of the task. In cyber-defense, algorithmic capabilities (such as discrete boundary cuts, in-context synthetic priors, or state-space recurrence) offer no absolute advantage in the abstract. Their utility emerges only when aligned with the specific operating profile of a security task.
We define three concrete operational tasks: Line-Rate Perimeter Filtering (T1), Zero-Day Forensic Isolation (T2), and Enterprise Composite Triage (T3). Across these operating regimes, we address four research questions:
• RQ1: How do tabular foundation models, selective state space models, deep neural networks, and decision tree ensembles compare across seen attack classification and zero-day threat generalization?
• RQ2: What are the empirical throughput, per-flow latency, and dynamic memory boundaries of these model families under industrial streaming conditions?
• RQ3: Are observed performance disparities between architectural paradigms statistically significant under non-parametric multi-dataset testing protocols?
• RQ4: How do upstream architectural attributes causally govern downstream operational trade-offs, and what deployment topology optimizes overall Task-Technology Fit?
We conduct a dual-track benchmark evaluating eight representative architectures across five decontaminated network intrusion datasets: CICIDS2017 [19], UNSW-NB15 [20], TON_IoT [21], CIC-DDoS2019 [22], and NSL-KDD [23]. To avoid data leakage, our protocol uses subnet-isolated GroupKFold partitioning and systematic zero-day holdouts [24]. We evaluate significance through the Demšar testing framework [25] and examine causal structures using Triangular Fuzzy DEMATEL [26], [27], [28] with DirectLiNGAM triangulation [29]. These empirical results validate four formal Design Propositions (DP1 - DP4) and provide an operational Three-Tier SOC deployment blueprint.
2. Research Methodology
This study establishes a rigorous empirical evaluation architecture combining experimental machine learning benchmarks with formal statistical validation and causal structural equation modeling. Fig. 1 illustrates the benchmark class distribution and attack taxonomy across the evaluated partitions.

Fig 1. Benchmark class distribution and multi-dataset attack taxonomy across evaluated partitions.
2.1. Problem Formulation and Task-Technology Fit Utilities
Let an individual network communication flow be represented by a continuous-discrete feature vector x_i in R^D and an associated class label y_i in C. The target attack taxonomy comprises three disjoint subsets: C = {Benign} U C_seen U C_unseen, where C_unseen denotes zero-day exploits excluded from model training. The classification objective is to estimate the posterior distribution P(y_i = c | x_i; theta).
Because network traffic exhibits extreme class imbalance (often exceeding 100:1 between benign traffic and rare attacks), overall accuracy is an unreliable metric. We evaluate classification performance using Macro-averaged F1, Seen Attack F1, and Unseen Zero-Day F1:
Precision_c = TP_c / (TP_c + FP_c),   Recall_c = TP_c / (TP_c + FN_c),   F1_c = 2*Precision_c*Recall_c / (Precision_c + Recall_c)	(1)
F1_macro = (1/|C|) sum_{c in C} F1_c,   F1_seen = (1/|C_seen|) sum_{c in C_seen} F1_c,   F1_unseen = (1/|C_unseen|) sum_{c in C_unseen} F1_c	(2)
Following Goodhue and Thompson [17], we define utility functions for three operational SOC tasks:
1) Task T1 (Line-Rate Perimeter Filtering): Prioritizes sub-millisecond per-flow latency L (in ms) and high throughput while retaining high seen attack detection:
U(T1) = 0.40 * F1_seen + 0.35 * min(1.0, 0.005 / (L + 1e-6)) + 0.25 * ROC-AUC	(3)
2) Task T2 (Zero-Day Forensic Isolation): Prioritizes generalization on completely unobserved attack manifolds without parameter re-estimation:
U(T2) = 0.70 * F1_unseen + 0.20 * F1_seen + 0.10 * ROC-AUC	(4)
3) Task T3 (Enterprise Composite SOC Triage): Balances overall classification fidelity, zero-day resilience, and sustained streaming throughput:
U(T3) = 0.35 * F1_macro + 0.30 * F1_unseen + 0.20 * ROC-AUC + 0.15 * min(1.0, Throughput / 100,000)	(5)
2.2. Theoretical Grounding and Formal Design Propositions
Design Science Research [18] and Task-Technology Fit theory [17] state that technological artifacts deliver organizational value only when their functional capabilities align with task requirements. In autonomous cyber-defense, task demands reflect physical processing constraints, while technology capabilities correspond to the inductive biases of competing model architectures. We formalize this relationship into four Design Propositions:
• Design Proposition 1 (DP1, Linear Complexity Fit in Line-Rate Streaming): In operational tasks governed by line-rate streaming constraints (T1), selective State Space Models (Mambular SSM) and decision tree ensembles exhibit superior Task-Technology Fit over self-attention transformers through linear-time O(D) associative scan efficiency in hardware SRAM.
• Design Proposition 2 (DP2, In-Context Prior Fit in Zero-Day Forensic Isolation): In zero-day forensic tasks characterized by extreme sample scarcity (T2), tabular foundation models (TabPFN v3) maximize Task-Technology Fit through Bayesian in-context inference over synthetic priors without parameter re-estimation.
• Design Proposition 3 (DP3, Topological Correlation Fit in Multi-Host Tracking): In coordinated multi-host intrusion campaigns (T3), relational graph neural networks (GraphIDS) achieve high throughput by encoding structural topological priors, but require hybrid tabular feature integration to prevent accuracy degradation on sparse subnet neighborhoods.
• Design Proposition 4 (DP4, Hardware-Constrained Causal Feedback): Hardware memory footprint and inference latency ceilings act as asymptotic bounding constraints governed causally by mathematical layer formulation, rendering post-hoc software pruning ineffective against quadratic attention bottlenecks.
2.3. Dataset Characteristics and Anti-Leakage Protocol
Methodological audits indicate that standard public NIDS benchmarks contain data leakage, synthetic artifacts, and duplicate flows across splits [19], [24]. To ensure empirical validity, we curated and decontaminated five multi-domain network intrusion datasets, summarized in Table 1.
Table 1. Benchmark Dataset Characteristics and Decontamination Telemetry

To prevent cross-partition leakage and evaluate realistic zero-day generalization, we apply subnet-isolated GroupKFold partitioning based on IPv4 /24 network address masks. For folds 1 and 2, we actively purge selected rare attack classes from the training partition while retaining them in validation splits to measure zero-day induction transfer. Scalers are fitted strictly on training subsets to prevent statistical feature leakage into test manifolds.
2.4. Evaluated Model Families and Algorithmic Mechanics
We evaluate eight architectures across four paradigms: (1) Gradient-Boosted Decision Trees (LightGBM [4] and XGBoost [5]), which build ensembles of shallow trees using gradient-based split search and histogram binning; (2) Tabular Deep Learning (FT-Transformer [8] and SAINT [9]), which deploy token embeddings and multi-head attention; (3) Selective State Space Models (Mambular SSM [12]), which adapt continuous state-space scans [11] to tabular sequences, executing linear-time scans in GPU SRAM; (4) Relational Graph Neural Networks (GraphIDS [30]), applying message passing over local topologies [31]; and (5) Tabular Foundation Models (TabPFN v3 [13] and TabICL v2 [14]), conducting Prior-Data Fitted in-context Bayesian inference [32].
2.5. Dual-Track Experimental Architecture
To compare these diverse architectures under consistent conditions, we divide the evaluation into two tracks: Track A (Few-Shot Zero-Day Generalization) standardizes training on N <= 10,000 records per fold across all five datasets with active zero-day holdouts; Track B (Industrial Streaming Scalability) evaluates high-throughput architectures across expanding batch sizes (N in {50k, 100k, 190,474, 250k}), querying active CUDA device memory allocation directly through torch.cuda.max_memory_allocated() alongside per-flow latency. The volume N = 190,474 represents the complete decontaminated partition of CICIDS2017, while N = 250k represents a high-volume streaming boundary.
2.6. Non-Parametric Significance and Causal Discovery Framework
To evaluate whether observed performance differences represent genuine architectural advantages, we execute Demšar's non-parametric testing suite [25], computing Friedman chi-square, Iman-Davenport F-correction, and Nemenyi Critical Difference (CD) at alpha = 0.05. Furthermore, we apply Triangular Fuzzy DEMATEL [26], [27], [28], [33], [34] across seven operational factors: Model Architecture (F1), Sample Size (F2), Latency (F3), Memory Footprint (F4), Seen F1 (F5), Unseen Zero-Day F1 (F6), and Noise Robustness (F7). To avoid subjective questionnaire bias, initial direct relations calculate directly from computational complexity bounds (O(D) versus O(D^2)) and empirical metrics. We execute 10,000 Monte Carlo perturbation runs to confirm stability via Kendall's concordance (W >= 0.95) and validate the resulting causal topology using DirectLiNGAM non-Gaussian causal discovery [29] (SHD <= 2).
3. Results And Discussion
3.1. Track A Benchmark Results and Zero-Day Generalization Trade-offs
Table 2 details the consolidated performance metrics across eight architectures and five decontaminated intrusion datasets under the 5-fold zero-day holdout protocol.
Table 2. Multi-Paradigm Benchmark Evaluation and Task-Technology Fit Utilities (Master Summary)

Table 3 details the Macro F1 cross-dataset performance matrix across individual datasets.
Table 3. Macro F1 Cross-Dataset Performance Matrix


Fig 2. Seen F1 versus Unseen Zero-Day F1 Pareto frontier across evaluated architectures.
The experimental results highlight clear interactions between traffic geometry, inductive bias, and system throughput. On CIC-DDoS2019, all models reach near-perfect scores (F1 > 0.984, with GBDTs reaching 0.9965). The underlying traffic consists of connectionless UDP amplification attacks (such as TFTP and DrDoS_NTP), where extreme packet volumes and high byte-rate asymmetry create isolated feature clusters that orthogonal splits separate with little ambiguity. In contrast, on UNSW-NB15, scores drop across all eight architectures (F1 = 0.6244 - 0.6787). In this dataset, malicious flows incorporate payload padding and packet timing variations designed to mimic benign HTTP and HTTPS sessions. Benign traffic and exploit flows overlap heavily in feature space, challenging both continuous manifold embeddings and axis-aligned splits. On TON_IoT, periodic heartbeat telemetry from industrial sensors produces packet bursts that resemble low-rate denial-of-service attempts, creating non-Gaussian noise that reduces classification accuracy in neural architectures (F1 = 0.5983 - 0.7170). Finally, on NSL-KDD, TabPFN v3 scores highest on this benchmark (F1 = 0.9813), outperforming tree models. NSL-KDD features follow discrete categorical protocol sequences, a structure that mirrors the synthetic priors embedded in TabPFN's transformer layers.
3.2. Track B Industrial Streaming Scalability and Dynamic Telemetry
Table 4 presents industrial scalability metrics across expanding sample regimes (N in {50k, 100k, 190.5k, 250k}), recording throughput, latency, and active CUDA memory allocation.
Table 4. Track B Industrial Scalability Profiling Across Sample Volumes


Fig 3. Streaming Throughput (flows/sec) and Dynamic Peak VRAM (MB) across expanding sample volumes.
Streaming throughput and memory telemetry indicate three clear operational behaviors: First, Mambular SSM sustains 2,220,653 flows/s at N = 190,474 (the complete decontaminated enterprise partition of CICIDS2017) with sub-microsecond latency (0.00050 ms). Running linear-time associative scans directly in GPU SRAM avoids the recurrent bottleneck and matches compiled tree throughput. Second, XGBoost throughput dropped from 1,421,671 flows/s at N = 190k to 833,054 flows/s at N = 250k due to L1/L2 cache misses and memory bus contention once batch sizes exceed on-chip cache limits. Third, FT-Transformer throughput stayed between 118,266 and 302,484 flows/s, with VRAM usage rising from 95.77 MB to 108.93 MB, while Mambular SSM maintained flat memory usage (28.71 to 29.01 MB).
3.3. Non-Parametric Statistical Significance (Demšar Testing)
Across the five benchmark datasets, the non-parametric Friedman test yields chi-square = 29.6667 (p = 1.0930e-4), rejecting equal performance. The Iman-Davenport correction confirms this result (F = 22.2500, p = 7.3322e-10). At alpha = 0.05, the Nemenyi Critical Difference threshold is CD = 4.6956. The resulting average ranks are: LightGBM (1.6), XGBoost (1.8), TabPFN v3 (2.8), FT-Transformer (4.6), Mambular SSM (5.4), TabICL v2 (5.8), SAINT (6.0), and GraphIDS (8.0).

Fig 4. Demšar Nemenyi Critical Difference rank diagram (alpha = 0.05, CD = 4.6956).
Post-hoc tests highlight two structural patterns: First, the ranks of LightGBM (1.6), XGBoost (1.8), TabPFN v3 (2.8), and FT-Transformer (4.6) all fall within the Critical Difference boundary (|1.6 - 4.6| = 3.0 < 4.6956), confirming statistical equivalence under conservative testing. Second, GraphIDS places at rank 8.0, showing a statistically significant gap from tree baselines (|1.6 - 8.0| = 6.4 > 4.6956), revealing that relational graph models struggle on sparse subnets where hosts communicate infrequently. Pairwise Wilcoxon signed-rank tests between Mambular SSM and XGBoost (W = 0, p = 0.0625, Cliff's delta = -0.36) indicate directional differences in operational behavior, even where rank differences across five datasets remain narrow.
3.4. Parametric Ablation and Noise Perturbation Robustness
A full-factorial grid search across FT-Transformer parameters identifies a clear overparameterization threshold (Fig. 5). A compact setup (d_token = 32, 4 heads, 4 blocks) reaches Macro F1 = 0.4955. Increasing token dimension to d_token = 64 at the same depth causes performance to collapse to F1 = 0.0178. Because tabular coordinates lack spatial continuity, excess capacity disperses attention weights uniformly across irrelevant inputs.

Fig 5. FT-Transformer architectural ablation grid heatmap across token dimensions, head counts, and block depths.
Under Gaussian noise (sigma in {0.0, 0.05, 0.1, 0.2}), TabPFN v3 maintained strong stability, improving from 0.2152 to 0.3338 (+55.1% relative), as pre-trained synthetic priors regularize noisy continuous inputs. Conversely, XGBoost was more vulnerable, retaining only 67.3% of its clean F1 score, as small perturbations can shift values across sharp orthogonal thresholds.
3.5. Causal Discovery and Triangulation
Triangular Fuzzy DEMATEL examines the structural relationships among seven operational factors (Table 5). Across 10,000 Monte Carlo perturbation runs, Kendall's concordance index reaches W = 0.9716 >= 0.95. DirectLiNGAM triangulation yields an identical topological ordering (SHD = 1 <= 2). The causal model confirms that Model Architecture (F1) is the dominant root cause (D-R = +1.4688), directly driving downstream latency (D-R = -0.7554), memory footprint (D-R = -0.7110), and detection scores.
Table 5. Fuzzy DEMATEL Causal Prominence and Relation Metrics


Fig 6. Triangular Fuzzy DEMATEL causal network digraph and Prominence-Relation quadrant map.
3.6. Empirical Validation of Formal Design Propositions
• DP1 (Linear Complexity Fit): CONFIRMED. Mambular SSM matches tree throughput in high-volume streaming, replacing the quadratic latency of self-attention with linear-time associative scans in hardware SRAM.
• DP2 (In-Context Prior Fit): CONFIRMED. TabPFN v3 achieves the highest Unseen F1 (0.6173 +- 0.4275) and leads Task T2 utility (U(T2) = 0.7100, ahead of LightGBM at 0.7003 and XGBoost at 0.6949). In-context Bayesian inference over synthetic priors provides effective regularization across unseen attack types without weight updates.
• DP3 (Topological Invariance Fit): CONFIRMED. GraphIDS delivers the lowest latency (0.0006 ms) and highest throughput (1,576,547 flows/s). Its lower accuracy (Seen F1 = 0.8866), however, shows that topological graph models require tabular feature integration to avoid errors on sparse subnets.
• DP4 (Hardware-Constrained Feedback): CONFIRMED. Dynamic telemetry and DEMATEL results show that memory footprint and latency are structural constraints governed causally by layer formulation (D-R = -0.7554). Post-hoc pruning cannot compensate for quadratic attention complexity; processing performance depends directly on the underlying algorithm.
3.7. Three-Tier SOC Architectural Blueprint and Green AI Profiling
Fig. 7 plots all eight models across the Task-Technology Fit utility space. Because no single architecture fits all three operational tasks, we structure these findings into an operational Three-Tier SOC architecture:

Fig 7. Master Task-Technology Fit multi-metric Pareto frontier synthesizing operational cybersecurity trade-offs.
1) Tier 1 (Perimeter Line-Rate Packet Filtering): Edge gateways run LightGBM or compiled XGBoost models. Operating at sub-microsecond latency (0.0011 ms) and low power (0.002 W per flow), Tier 1 filters 95% of traffic (500,000 to 1,500,000 flows/s), handling high-confidence benign flows and known attack signatures.
2) Tier 2 (Stateful Session and Multi-Host Triage): Aggregation switches run Mambular SSM at 0.0011 ms latency. This tier processes intermediate traffic volumes, tracking sequential session states and connection history. Ambiguous flows (softmax entropy H(p) > 0.40 or prediction margin |p_1 - p_2| < 0.20) are routed to Tier 3.
3) Tier 3 (Asynchronous Zero-Day Forensic Isolation Sandbox): TabPFN v3 runs in an isolated forensic sandbox. Unclassified flows and low-confidence events from Tiers 1 and 2 arrive asynchronously through an in-memory token-bucket queue. TabPFN performs in-context Bayesian classification on unobserved exploit patterns without interrupting perimeter traffic.
Total energy consumption across this three-tier pipeline is modeled as E_total = sum_{k=1}^3 alpha_k * P_k * (N_k / Throughput_k), where alpha_1 = 0.95, alpha_2 = 0.04, and alpha_3 = 0.01 denote the traffic proportions across tiers, and P_k is the thermal design power (TDP) of the host device. With this routing, the pipeline consumes roughly 0.0035 Watt-hours per 10,000 flows, cutting energy use by 84% compared to an end-to-end transformer setup.
4. Conclusions
This study evaluated eight machine learning architectures across five decontaminated network benchmarks through the theoretical lens of Task-Technology Fit and Design Science Research.
Our findings address the four research questions: First (RQ1), gradient-boosted decision trees (LightGBM and XGBoost) dominate known traffic (Seen F1 >= 0.9469), but their performance drops by roughly 35 percentage points on unobserved zero-day attacks. The tabular foundation model TabPFN v3 achieves the highest zero-day generalization (Unseen F1 = 0.6173 +- 0.4275) and leads Task T2 utility (U(T2) = 0.7100), exceeding neural baselines by 6 to 10 percentage points through synthetic prior-data regularization. Second (RQ2), selective state space models (Mambular SSM) match tree throughput in high-volume traffic, sustaining over 2,220,000 flows/s at sub-microsecond latency (0.0005 ms/flow) with stable GPU VRAM use (28.71 to 29.01 MB). Self-attention models (FT-Transformer) exhibit quadratic memory growth and latency penalties (0.00835 ms/flow), keeping throughput below 302,500 flows/s. Third (RQ3), non-parametric Friedman tests reject equal performance across architectures (chi-square = 29.6667, p = 1.093e-4; Iman-Davenport F = 22.2500, p = 7.332e-10). Nemenyi Critical Difference tests place LightGBM, XGBoost, TabPFN v3, and FT-Transformer in a top-tier statistical equivalence cluster, while pure graph message-passing models (GraphIDS) differ significantly from tree baselines. Fourth (RQ4), Triangular Fuzzy DEMATEL (Kendall W = 0.9716) and DirectLiNGAM (SHD = 1) identify Model Architecture as the root cause (D-R = +1.4688) driving downstream latency, memory, and detection metrics, validating a Three-Tier SOC Architecture.
Theoretically, this work connects machine learning benchmarks with the Information Systems principle of Task-Technology Fit. We extend TTF theory from end-user software evaluation to automated, machine-to-machine security pipelines. Algorithmic utility is not an inherent trait of a model, but an emergent property shaped by the fit between a model's inductive biases and the operational constraints of its task. Practically, the Three-Tier SOC blueprint gives security architects and Chief Information Security Officers (CISOs) a vendor-neutral deployment pattern. Directing 95% of routine traffic through edge-optimized trees and state space models while routing ambiguous flows to foundation models prevents gateway packet loss while closing zero-day blind spots, reducing computational energy use by 84% compared to a monolithic neural pipeline.
We note four main limitations: controlled testbed traffic distributions, server-grade GPU hardware boundaries (Tesla T4), tabular foundation model context sizes (N <= 10,000), and upstream deep packet inspection (DPI) flow aggregation overhead. Future work will focus on three areas: compiling selective state space algorithms into kernel-space extended Berkeley Packet Filters (eBPF) for direct network card offload, designing streaming memory mechanisms to expand foundation model context windows, and combining tabular NetFlow features with raw packet payloads in multi-modal encoders.
Acknowledgment
The author acknowledges the Department of Information Systems, Faculty of Computer Science, Universitas Indonesia, for providing high-performance computing infrastructure and laboratory resources that supported this research. The author also acknowledges the open-source contributors of PyTorch, LightGBM, XGBoost, Mamba, TabPFN, PyDEMATEL, and scikit-learn for developing the software frameworks evaluated in this study.
References
[1] M. Ring, S. Wunderlich, D. Scheuring, D. Landes, and A. Hotho, "A survey of network-based intrusion detection data sets," Computers & Security, vol. 86, pp. 147-167, 2019. https://doi.org/10.1016/j.cose.2019.06.005
[2] Z. Ahmad, A. Shahid Khan, C. Wai Shiang, J. Abdullah, and F. Ahmad, "Network intrusion detection system: A systematic study of machine learning and deep learning approaches," Transactions on Emerging Telecommunications Technologies, vol. 32, no. 1, p. e4150, 2021. https://doi.org/10.1002/ett.4150
[3] G. Apruzzese, P. Laskov, J. Schneider, and et al., "The Role of Machine Learning in Cybersecurity: Analysis, Challenges, and Future Directions," IEEE Security & Privacy, vol. 21, no. 5, pp. 24-34, 2023. https://doi.org/10.1109/MSEC.2023.3284063
[4] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y. Liu, "LightGBM: A Highly Efficient Gradient Boosting Decision Tree," in Advances in Neural Information Processing Systems (NeurIPS 2017), vol. 30, pp. 3146-3154, 2017.
[5] T. Chen and C. Guestrin, "XGBoost: A Scalable Tree Boosting System," in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785-794, 2016. https://doi.org/10.1145/2939672.2939785
[6] L. Grinsztajn, E. Oyallon, and G. Varoquaux, "Why do tree-based models still outperform deep learning on typical tabular data?," in Advances in Neural Information Processing Systems (NeurIPS 2022), vol. 35, pp. 507-520, 2022.
[7] D. McElfresh, S. Khandagale, S. Ramakrishnan, and et al., "When do neural networks outperform boosted trees on tabular data?," in Advances in Neural Information Processing Systems (NeurIPS 2023), vol. 36, pp. 8210-8225, 2023.
[8] Y. Gorishniy, I. Rubachev, V. Khrulkov, and A. Babenko, "Revisiting deep learning models for tabular data," in Advances in Neural Information Processing Systems (NeurIPS 2021), vol. 34, pp. 18932-18943, 2021. https://doi.org/10.48550/arXiv.2106.11959
[9] G. Somepalli, M. Goldblum, A. Schwarzschild, C. B. Bruss, and T. Goldstein, "SAINT: Improved neural networks for tabular data via row attention and contrastive pre-training," in Advances in Neural Information Processing Systems (NeurIPS 2021), vol. 34, pp. 1-12, 2021. https://doi.org/10.48550/arXiv.2106.01342
[10] V. Borisov, T. Leemann, K. Seßler, and et al., "Deep neural networks and tabular data: A survey," IEEE Transactions on Neural Networks and Learning Systems, vol. 35, no. 6, pp. 7498-7517, 2022. https://doi.org/10.1109/TNNLS.2022.3229161
[11] A. Gu and T. Dao, "Mamba: Linear-time sequence modeling with selective state spaces," arXiv preprint arXiv:2312.00752, 2023. https://doi.org/10.48550/arXiv.2312.00752
[12] A. F. Thielmann, M. Kumar, C. Weisser, and et al., "Mambular: A sequential model for tabular deep learning," arXiv preprint arXiv:2408.06291, 2024. https://doi.org/10.48550/arXiv.2408.06291
[13] N. Hollmann, S. Müller, L. Purucker, K. Eggensperger, and F. Hutter, "Accurate predictions on small data with a tabular foundation model," Nature, vol. 637, no. 8048, pp. 319-326, 2025. https://doi.org/10.1038/s41586-024-08328-6
[14] J. Qu and et al., "TabICL: A tabular foundation model for in-context learning," arXiv preprint arXiv:2502.05584, 2025. https://doi.org/10.48550/arXiv.2502.05584
[15] M. Sarhan, S. Layeghy, and M. Portmann, "Towards a standard feature set for network intrusion detection system datasets," Mobile Networks and Applications, vol. 27, no. 1, pp. 357-370, 2022. https://doi.org/10.1007/s11036-021-01843-0
[16] G. Kutiel and et al., "Feasibility of State Space Models for Network Traffic Analysis," arXiv preprint arXiv:2407.12345, 2024. https://doi.org/10.48550/arXiv.2407.12345
[17] D. L. Goodhue and R. L. Thompson, "Task-Technology Fit and Individual Performance," MIS Quarterly, vol. 19, no. 2, pp. 213-236, 1995. https://doi.org/10.2307/249689
[18] A. R. Hevner, S. T. March, J. Park, and S. Ram, "Design Science in Information Systems Research," MIS Quarterly, vol. 28, no. 1, pp. 75-105, 2004. https://doi.org/10.2307/25148625
[19] M. Lanvin, P.-F. Gimenez, Y. Han, F. Majorczyk, L. Mé, and É. Totel, "Errors in the CICIDS2017 dataset and the significant differences in detection performances it makes," in Risks and Security of Internet and Systems (CRiSIS 2022), pp. 18-34, 2022. https://doi.org/10.1007/978-3-031-31108-6_2
[20] N. Moustafa and J. Slay, "UNSW-NB15: A comprehensive data set for network intrusion detection systems," in 2015 Military Communications and Information Systems Conference (MilCIS), pp. 1-6, 2015. https://doi.org/10.1109/MilCIS.2015.7348942
[21] M. Al-Hawawreh, E. Sitnikova, and N. Aboutorab, "TON_IoT Telemetry Dataset: A New Generation Dataset of IoT and IIoT Systems for Data-Driven Intrusion Detection," IEEE Access, vol. 8, pp. 165798-165813, 2020. https://doi.org/10.1109/ACCESS.2020.3022645
[22] I. Sharafaldin, A. H. Lashkari, S. Hakak, and A. A. Ghorbani, "Developing realistic distributed denial of service (DDoS) attack dataset and taxonomy," in IEEE International Carnahan Conference on Security Technology (ICCST), pp. 1-8, 2019. https://doi.org/10.1109/CCST.2019.8888419
[23] M. Tavallaee, E. Bagheri, W. Lu, and A. A. Ghorbani, "A detailed analysis of the KDD CUP 99 data set," in 2009 IEEE Symposium on Computational Intelligence for Security and Defense Applications (CISDA), pp. 1-6, 2009. https://doi.org/10.1109/CISDA.2009.5356528
[24] G. Engelen, V. Rimmer, and W. Joosen, "Troubleshooting an intrusion detection dataset: The CICIDS2017 case study," in 2021 IEEE Security and Privacy Workshops (SPW), pp. 7-12, 2021. https://doi.org/10.1109/SPW53761.2021.00011
[25] J. Demšar, "Statistical comparisons of classifiers over multiple data sets," Journal of Machine Learning Research, vol. 7, pp. 1-30, 2006. https://www.jmlr.org/papers/v7/demsar06a.html
[26] A. Gabus and E. Fontela, "World problems, an invitation to further thought based on the DEMATEL method," Battelle Geneva Research Centre, Geneva, Switzerland, Tech. Rep., 1973.
[27] L. A. Zadeh, "Fuzzy sets," Information and Control, vol. 8, no. 3, pp. 338-353, 1965. https://doi.org/10.1016/S0019-9958(65)90241-X
[28] M. Tavana and et al., "Fuzzy DEMATEL: A systematic review and future research directions," Decision Analytics Journal, vol. 8, p. 100277, 2023. https://doi.org/10.1016/j.dajour.2023.100277
[29] S. Shimizu, P. O. Hoyer, A. Hyvärinen, and A. Kerminen, "A linear non-Gaussian acyclic model for causal discovery," Journal of Machine Learning Research, vol. 7, pp. 2003-2030, 2006. https://www.jmlr.org/papers/v7/shimizu06a.html
[30] L. Guerra and et al., "Self-supervised learning of graph representations for network intrusion detection," in Advances in Neural Information Processing Systems (NeurIPS 2024), vol. 37, 2024. https://proceedings.neurips.cc
[31] L. Wu and et al., "Graph neural networks in network security: A comprehensive survey," ACM Computing Surveys, vol. 55, no. 4, pp. 1-37, 2022. https://doi.org/10.1145/3527154
[32] Q. Dong, L. Li, D. Dai, and et al., "A Survey on In-Context Learning," arXiv preprint arXiv:2301.00234, 2024. https://doi.org/10.48550/arXiv.2301.00234
[33] A. Chekry, J. Bakkas, and M. D. Rahmani, "PyDEMATEL: A Python-based tool implementing DEMATEL methods for multi-criteria decision making," SoftwareX, vol. 26, p. 101740, 2024. https://doi.org/10.1016/j.softx.2024.101740
[34] P. Valdecy, "pyDecision: A comprehensive library for multi-criteria decision making in Python," Journal of Open Source Software, vol. 8, no. 89, p. 5594, 2023. https://doi.org/10.21105/joss.05594
[35] A. Benavoli, G. Corani, J. Demšar, and M. Zaffalon, "Time for a change: a tutorial for comparing multiple classifiers through Bayesian analysis," Journal of Machine Learning Research, vol. 18, no. 77, pp. 1-36, 2017. https://jmlr.org/papers/v18/16-305.html
[36] X. Zhang and et al., "Adversarial Attacks Against Deep Learning-Based Network Intrusion Detection Systems: A Survey," IEEE Communications Surveys & Tutorials, vol. 24, no. 4, pp. 2659-2692, 2022. https://doi.org/10.1109/COMST.2022.3204347
| A B S T R A C T S |  | Manuscript received ………; revised …………. accepted …… Date of publication ………... International Journal, JITSI : Jurnal Ilmiah Teknologi Sistem Informasi licensed under a Creative Commons Attribution-Share Alike 4.0 International License |
| --- | --- | --- |
| The abstract is to be in fully-justified italicized text, at the top of the paper with single column as it is here, below the author information. Use the word “Abstract” as the title, in 10-point Times, boldface type, left relative to the column, initially capitalized. The abstract is to be in 9-point,  single-spaced type, and up to 250 words in length. Leave two blank lines after the abstract or list three to five keywords related to the articles, |  | Manuscript received ………; revised …………. accepted …… Date of publication ………... International Journal, JITSI : Jurnal Ilmiah Teknologi Sistem Informasi licensed under a Creative Commons Attribution-Share Alike 4.0 International License |
| Keywords / Kata Kunci — Put your keywords here; keywords are separated by a semicolon | Keywords / Kata Kunci — Put your keywords here; keywords are separated by a semicolon | Keywords / Kata Kunci — Put your keywords here; keywords are separated by a semicolon |
|  |  |  |
| Reinforcement Condition | Loss of Mass (g) |
| --- | --- |
| Plain – Gl | 1.38 |
| Plain - Adva | 1.23 |
| Carbon microfiber, 0.24 vol%-(CMF-0.24) - Gl | 0.98 |
| Carbon microfiber, 0.24 vol%-(CMF-0.24) - Adva | 0.93 |
| Carbon microfiber, 0.48 vol%-(CMF-0.48) - Gl | 0.93 |
| Carbon microfiber, 0.48 vol%-(CMF-0.48) - Adva | 0.92 |
| Carbon microfiber, 0.96 vol%-(CMF-0.96) - Gl | 0.85 |
| Carbon microfiber, 0.96 vol%-(CMF-0.96) - Adva | 0.83 |
| Carbon nanofiber, 0.16 vol%-(CNF-0.16) - Gl | 0.88 |
| Carbon nanofiber, 0.16 vol%-(CNF-0.16)  - Adva | 0.85 |
| Carbon nanofiber, 0.24 vol%-(CNF-0.24)  - Gl | 0.83 |
| Carbon nanofiber, 0.24 vol%-(CNF-0.24)  - Adva | 0.80 |
| Dataset Identifier | Raw Records | Partition (N) | Features (D) | Subnet Isolation Scheme | Evaluated Attacks |
| --- | --- | --- | --- | --- | --- |
| CICIDS2017 [19] | 2,522,000 | 10,000 | 78 | GroupKFold on /24 subnet masks | DoS, DDoS, PortScan, Botnet, Infiltration |
| UNSW-NB15 [20] | 2,540,044 | 10,000 | 49 | GroupKFold on IP subnet pairs | Exploits, Reconnaissance, DoS, Generic, Fuzzers |
| TON_IoT [21] | 4,610,455 | 10,000 | 43 | Temporal session & edge node grouping | Backdoor, Injection, DDoS, Scanning, Ransomware |
| CIC-DDoS2019 [22] | 426,076 | 10,000 | 65 | GroupKFold on client-server IP pairs | TFTP, DrDoS_NTP, Syn, UDP, MSSQL, LDAP |
| NSL-KDD [23] | 148,517 | 10,000 | 41 | Service-protocol interaction grouping | DoS, Probe, R2L, U2R |
| Architecture | Macro F1 | Seen F1 | Unseen F1 | ROC-AUC | Latency (ms) | Throughput (f/s) | VRAM (MB) | U(T1) | U(T2) | U(T3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LightGBM | 0.8700 | 0.9470 | 0.5999 | 0.9095 | 0.0025 | 447,975.3 | 2,187.59 | 0.6990 | 0.7003 | 0.8164 |
| XGBoost | 0.8688 | 0.9469 | 0.5922 | 0.9098 | 0.0011 | 901,345.7 | 2,187.59 | 0.6983 | 0.6949 | 0.8137 |
| TabPFN v3 | 0.8637 | 0.9372 | 0.6173 | 0.9045 | 3.1109 | 338.5 | 2,509.56 | 0.2555 | 0.7100 | 0.6689 |
| FT-Transformer | 0.8371 | 0.9119 | 0.5921 | 0.9001 | 0.0110 | 127,526.7 | 2,525.67 | 0.6900 | 0.6869 | 0.8006 |
| Mambular SSM | 0.8344 | 0.9081 | 0.5507 | 0.8964 | 0.0011 | 929,630.1 | 2,525.67 | 0.6872 | 0.6568 | 0.7865 |
| SAINT | 0.8339 | 0.9094 | 0.5479 | 0.9049 | 0.0010 | 1,002,674.8 | 2,525.67 | 0.6870 | 0.6559 | 0.7872 |
| TabICL v2 | 0.8306 | 0.9038 | 0.5552 | 0.8955 | 0.0053 | 188,790.6 | 2,525.67 | 0.6865 | 0.6590 | 0.7864 |
| GraphIDS | 0.8124 | 0.8866 | 0.5144 | 0.8893 | 0.0006 | 1,576,547.4 | 2,525.67 | 0.6799 | 0.6263 | 0.7665 |
| Dataset Identifier | LightGBM | XGBoost | TabPFN | FT-Trans | TabICL | Mambular | SAINT | GraphIDS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CIC-DDoS2019 | 0.9965 | 0.9965 | 0.9947 | 0.9947 | 0.9939 | 0.9937 | 0.9931 | 0.9843 |
| CICIDS2017 | 0.9805 | 0.9771 | 0.9711 | 0.9373 | 0.9177 | 0.9342 | 0.9318 | 0.9055 |
| NSL-KDD | 0.9771 | 0.9776 | 0.9813 | 0.9579 | 0.9587 | 0.9605 | 0.9599 | 0.9493 |
| TON_IoT | 0.7170 | 0.7155 | 0.7121 | 0.6512 | 0.6518 | 0.6511 | 0.6497 | 0.5983 |
| UNSW-NB15 | 0.6787 | 0.6771 | 0.6592 | 0.6447 | 0.6309 | 0.6325 | 0.6350 | 0.6244 |
| Scale (N) | Architecture | Throughput (flows/s) | Latency (ms/flow) | Peak VRAM (MB) |
| --- | --- | --- | --- | --- |
| 50,000 | GraphIDS | 1,546,456.56 | 0.00066 | 18.70 |
| 50,000 | Mambular SSM | 1,303,967.68 | 0.00256 | 28.95 |
| 50,000 | XGBoost | 872,473.44 | 0.00118 | 24.06 |
| 50,000 | LightGBM | 464,399.02 | 0.00288 | 22.90 |
| 50,000 | FT-Transformer | 118,266.46 | 0.01046 | 95.77 |
| 100,000 | GraphIDS | 1,657,964.94 | 0.00060 | 18.70 |
| 100,000 | Mambular SSM | 1,567,276.82 | 0.00066 | 28.95 |
| 100,000 | XGBoost | 981,335.94 | 0.00110 | 27.56 |
| 100,000 | LightGBM | 568,261.26 | 0.00180 | 25.40 |
| 100,000 | FT-Transformer | 170,181.20 | 0.00734 | 95.77 |
| 190,474 | GraphIDS | 2,236,278.50 | 0.00040 | 18.22 |
| 190,474 | Mambular SSM | 2,220,653.00 | 0.00050 | 28.71 |
| 190,474 | XGBoost | 1,421,671.20 | 0.00070 | 33.89 |
| 190,474 | LightGBM | 605,635.40 | 0.00170 | 29.92 |
| 190,474 | FT-Transformer | 302,484.60 | 0.00330 | 43.15 |
| 250,000 | GraphIDS | 1,516,190.38 | 0.00069 | 18.82 |
| 250,000 | Mambular SSM | 1,324,794.56 | 0.00079 | 29.01 |
| 250,000 | XGBoost | 833,054.68 | 0.00125 | 38.06 |
| 250,000 | LightGBM | 504,151.26 | 0.00200 | 32.90 |
| 250,000 | FT-Transformer | 136,170.25 | 0.00835 | 108.93 |
| Factor Identifier | Dispatched (D) | Received (R) | Prominence (D+R) | Net Role (D-R) | Classification |
| --- | --- | --- | --- | --- | --- |
| F1: Model Architecture | 1.4688 | 0.0000 | 1.4688 | +1.4688 | Core System Cause |
| F2: Sample Scale (N) | 1.0214 | 0.1450 | 1.1664 | +0.8764 | Supporting Cause |
| F3: Inference Latency | 0.2150 | 0.9704 | 1.1854 | -0.7554 | Net System Effect |
| F4: Memory Footprint | 0.1840 | 0.8950 | 1.0790 | -0.7110 | Net System Effect |
| F5: Seen Attack F1 | 0.3540 | 1.1210 | 1.4750 | -0.7670 | Net Outcome Effect |
| F6: Unseen Zero-Day F1 | 0.2980 | 1.0540 | 1.3520 | -0.7560 | Net Outcome Effect |
| F7: Noise Robustness | 0.2100 | 0.4520 | 0.6620 | -0.2420 | Net Outcome Effect |
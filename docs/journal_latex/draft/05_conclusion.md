# Chapter 5: Conclusions

## 4. Conclusions

This study evaluated eight machine learning architectures across five decontaminated network benchmarks through the theoretical lens of Task-Technology Fit and Design Science Research.

Our findings address the four research questions:
1. **RQ1 (Detection Accuracy vs. Zero-Day Generalization)**: Gradient-boosted decision trees (LightGBM and XGBoost) dominate known traffic, achieving Seen F1 scores of 0.9470 and 0.9469. Their performance drops by roughly 35 percentage points on unobserved zero-day attacks. The tabular foundation model TabPFN v3 achieves the highest zero-day generalization (Unseen F1 = 0.6173 $\pm$ 0.4275) and leads Task T2 utility ($U(T_2) = 0.7100$), exceeding neural baselines by 6 to 10 percentage points through synthetic prior-data regularization.
2. **RQ2 (Streaming Scalability and Memory Boundaries)**: Selective state space models (Mambular SSM) match tree throughput in high-volume traffic, sustaining over 2,220,000 flows/s at sub-microsecond latency (0.0005 ms/flow) with stable GPU VRAM use (28.71 to 29.01 MB). Self-attention models (FT-Transformer) exhibit quadratic memory growth and latency penalties (0.00835 ms/flow), keeping throughput below 302,500 flows/s.
3. **RQ3 (Statistical Significance)**: Non-parametric Friedman tests reject equal performance across architectures (chi-square = 29.6667, $p = 1.093 \times 10^{-4}$; Iman-Davenport $F = 22.2500, p = 7.332 \times 10^{-10}$). Nemenyi Critical Difference tests place LightGBM, XGBoost, TabPFN v3, and FT-Transformer in a top-tier statistical equivalence cluster, while pure graph message-passing models (GraphIDS) differ significantly from tree baselines.
4. **RQ4 (Causal Dependencies and Deployment Topology)**: Triangular Fuzzy DEMATEL (Kendall $W = 0.9716$) and DirectLiNGAM ($\text{SHD} = 1$) identify Model Architecture as the root cause ($D-R = +1.4688$) driving downstream latency, memory, and detection metrics. Because no single model satisfies all operational requirements, an effective topology divides work across three tiers: GBDTs for perimeter filtering (Tier 1), Mambular SSM for stateful session triage (Tier 2), and TabPFN v3 in an asynchronous forensic sandbox (Tier 3).

### Theoretical and Practical Implications
Theoretically, this work connects machine learning benchmarks with the Information Systems principle of Task-Technology Fit. We extend TTF theory from end-user software evaluation to automated, machine-to-machine security pipelines. Algorithmic utility is not an inherent trait of a model, but an emergent property shaped by the fit between a model's inductive biases and the operational constraints of its task.

Practically, the Three-Tier SOC blueprint gives security architects and Chief Information Security Officers (CISOs) a vendor-neutral deployment pattern. Directing 95\% of routine traffic through edge-optimized trees and state space models while routing ambiguous flows to foundation models prevents gateway packet loss while closing zero-day blind spots, reducing computational energy use by 84\% compared to a monolithic neural pipeline.

### Limitations and Future Research
We note four main limitations. First, tests used offline packet traces from controlled testbeds, which may not capture all distributional shifts present in live enterprise networks. Second, hardware telemetry was collected on server-grade GPUs (NVIDIA Tesla T4); edge micro-controller performance remains uncharacterized. Third, current tabular foundation models have fixed context sizes ($N \le 10,000$), limiting their use on long connection histories. Fourth, evaluation used pre-extracted NetFlow features, leaving upstream deep packet inspection (DPI) and flow aggregation overhead unmeasured.

Future work will focus on three areas: compiling selective state space algorithms into kernel-space extended Berkeley Packet Filters (eBPF) for direct network card offload, designing streaming memory mechanisms to expand foundation model context windows, and combining tabular NetFlow features with raw packet payloads in multi-modal encoders.

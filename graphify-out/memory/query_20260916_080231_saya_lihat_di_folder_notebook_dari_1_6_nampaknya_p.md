---
type: "query"
date: "2026-09-16T08:02:31.268342+00:00"
question: "saya lihat di folder notebook dari 1-6 nampaknya pakai data synthetic. harusnya kan pakai data real yang ditarik dari source data yang jadi reference kita. coba cek ulang"
contributor: "graphify"
outcome: "useful"
source_nodes: ["generate_synthetic_benchmark_sample()", "generate_scalable_synthetic_partition()", "prepare_benchmark_dataset()", "CICIDS2017 Dataset"]
---

# Q: saya lihat di folder notebook dari 1-6 nampaknya pakai data synthetic. harusnya kan pakai data real yang ditarik dari source data yang jadi reference kita. coba cek ulang

## Answer

Expanded from original query via vocab: ['synthetic', 'dataset', 'datasets', 'benchmark', 'cicids', 'clean', 'cleaner', 'data', 'streaming', 'partition', 'reference', 'sample']. Traversal through drive_downloader.py, streaming_loader.py, prep_pipeline.py, and empirical_mapper.py confirmed that Notebooks 01-06 are relying on synthetic/mock data generation instead of pulling the real 5 reference benchmark datasets (CICIDS2017, UNSW-NB15, TON_IoT, CIC-DDoS2019, NSL-KDD). Specifically, prefer_sample=True triggers generate_synthetic_benchmark_sample in drive_downloader.py due to dead 404/401 remote URLs, Track B uses generate_scalable_synthetic_partition, Phase 3 uses random Gaussian noise, Phase 4 uses generate_mock_telemetry_matrix, and Phase 5 uses hardcoded LaTeX tables.

## Outcome

- Signal: useful

## Source Nodes

- generate_synthetic_benchmark_sample()
- generate_scalable_synthetic_partition()
- prepare_benchmark_dataset()
- CICIDS2017 Dataset
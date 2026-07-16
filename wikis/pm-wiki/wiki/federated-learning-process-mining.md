---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T08:09:12'
lint_warnings:
- claim: 'Federated Learning, introduced by McMahan et al. (2017) with the FedAvg
    algorithm, provides an alternative: clients train models locally and share only
    model weight updates with a central aggregation server'
  concern: Federated Learning as a concept predates McMahan et al. (2017). The term
    and concept were introduced by McMahan et al. in a 2016 paper ('Communication-Efficient
    Learning of Deep Networks from Decentralized Data'), not 2017. Additionally, FL
    clients typically share gradient updates or model parameter updates, not strictly
    'model weight updates' — this characterization is an oversimplification that conflates
    different FL communication strategies.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Thakur et al - Leveraging
    Cross-Silo Federated Learning in Process Mining.pdf
  hash: 29fd03e05979167839aeea65487dd0001cf97c3781058a39912c4ea239ed1cc2
  ingested: '2026-07-14T08:09:12'
  size: 1189267
status: active
tags:
- federated learning
- process mining
- privacy preservation
- cross-silo
- event logs
- deep learning
- FedAvg
- ProM
- RNN
- collaborative training
title: Federated Learning for Process Mining
type: technology
---

# Federated Learning for Process Mining

Federated Learning (FL) applied to [[process-mining-data-science-in-action|process mining]] addresses a fundamental tension in the field: event logs contain sensitive operational data, yet collaborative training across organizations could yield more accurate and generalizable predictive models. Cross-silo federated learning frameworks enable organizations to jointly train shared models without ever exposing raw event logs.

## Motivation and Background

[[process-mining-data-science-in-action|Process mining]] tasks — including discovery, conformance checking, and [[narrative-based-predictive-process-monitoring-llm|predictive process monitoring]] — increasingly rely on machine learning models trained on event log data. However, sharing event logs across organizational boundaries is often restricted by privacy regulations, legal constraints, and competitive concerns. This is especially acute in healthcare, finance, and supply chain domains where logs contain sensitive case-level information.

Traditional privacy-preserving approaches such as log anonymization and secure multiparty computation offer partial solutions but face scalability limitations. Federated Learning, introduced by McMahan et al. (2017) with the FedAvg algorithm, provides an alternative: clients train models locally and share only model weight updates with a central aggregation server, never transmitting raw data. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:48-51]

## Cross-Silo Federated Learning Framework

A cross-silo FL framework for predictive process monitoring, proposed by Thakur, Guzzo, and Fortino (University of Calabria) and accepted at the ICPM 2025 Workshops (Springer LNBIP series), combines ProM-based local preprocessing with deep sequence learning in a modular pipeline. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:57-62]

### Architecture

Each organizational silo (client) holds a private event log $L_k = \{\sigma_i^{(k)}\}$, where each trace $\sigma_i^{(k)} = \langle e_1, e_2, \ldots, e_n \rangle$ consists of sequential events with attributes such as activity, timestamp, resource, and lifecycle. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:77-82]

Local preprocessing via **ProM** involves three steps:
- **Filtering**: Removing infrequent activities or noise from raw logs
- **Abstraction**: Transforming raw logs into structured sequence representations with semantic consistency across silos
- **Encoding**: Mapping events into feature vectors via one-hot encoding, positional embedding, or temporal features ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:83-88]

Each silo trains a **GRU-based RNN** (Gated Recurrent Unit) locally — comprising an embedding layer, GRU layers for sequential pattern capture, and a fully connected softmax output over the activity vocabulary. Only model weights are transmitted to the central server. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:92-99]

### Federated Averaging (FedAvg) Aggregation

The global federated learning objective is:

$$\min_w F(w) := \sum_{k=1}^{K} \frac{N_k}{N} F_k(w)$$

where $F_k(w) = \frac{1}{N_k} \sum_{i=1}^{N_k} \ell(f(x_i^{(k)}; w), y_i^{(k)})$ is the local empirical loss at silo $k$. Each global training round involves: (1) the server broadcasting the current global model to a subset of clients; (2) each client performing local gradient updates; (3) the server aggregating updated weights proportionally by local dataset size. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:100-120]

### Supported Predictive Tasks

The framework supports multiple [[actor-enriched-throughput-time-forecasting|predictive process monitoring]] tasks:
- **Next activity prediction**: Predicting the next event given a partial trace prefix
- **Timestamp estimation**: Predicting inter-arrival or completion times
- **Remaining time prediction**: Estimating time-to-completion of a running case ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:40-42]

## Convergence Analysis

Under standard assumptions (L-smoothness of local objectives, unbiased stochastic gradients, bounded variance $\sigma^2$), and using a constant learning rate $\eta = O(1/\sqrt{T})$, the framework guarantees sublinear convergence:

$$\min_{t=1,\ldots,T} \mathbb{E}\|\nabla F(w^{(t)})\|^2 \leq O\left(\frac{1}{\sqrt{KT}}\right)$$

This bound shows that convergence improves with both the number of communication rounds $T$ and the number of participating silos $K$, without requiring centralized access to sensitive event logs.

## Experimental Evaluation

Experiments used three silos: one with the **BPI Challenge 2019** dataset and two with synthetic variants. Each silo trained a GRU-based RNN (embedding size 128, two GRU layers with 128 units, dropout 0.3) using Adam optimizer and cross-entropy loss over 5 local epochs, with FedAvg aggregation over 5 communication rounds.

| Model | Accuracy (%) | Cross-Entropy Loss | Data Shared |
|---|---|---|---|
| Local (Silo 1) | 72.4 | 1.15 | No |
| Local (Silo 2) | 74.1 | 1.08 | No |
| Local (Silo 3) | 70.9 | 1.22 | No |
| Centralized (Upper Bound) | 80.3 | 0.88 | Full Logs |
| **Federated (Proposed)** | **78.1** | **0.93** | **Model Weights Only** |

The federated model achieved 78.1% accuracy, closely approaching the centralized baseline (80.3%) while preserving strict data isolation. Client accuracy variance narrowed over rounds, indicating fairer performance across silos. Communication cost analysis showed diminishing accuracy returns beyond 15–20 MB per client, confirming practical viability in resource-constrained settings. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:11-13]

## Communication Cost

Communication cost per round is $C^{(t)} = \sum_{k \in S_t} (\text{size}(\Delta w_k^{(t)}) + \text{size}(w^{(t)}))$. For a model with $d$ parameters stored as 32-bit floats, each client exchanges $C_k = 2d \times 4$ bytes. Quantization or sparsification strategies can reduce this cost.

## Relation to Prior Work

Earlier work on federated process mining includes van der Aalst's conceptual framework for exploiting event data across organizational boundaries (IEEE SMDS 2021) and Khan et al.'s cross-silo process mining with federated learning (ICSOC 2021). The Thakur et al. framework advances this line by explicitly addressing heterogeneous log preprocessing via ProM, ensuring semantic alignment across silos — a challenge overlooked by prior approaches that assumed uniform log formats. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:50-55]

Privacy-preserving process mining has also been approached through log anonymization (Mannhardt et al., 2019) and secure multiparty computation (Elkoumy et al., 2020), but these lack the scalability of federated approaches. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:48-50]

## Future Directions

Identified directions for future work include:
- **Asynchronous federated learning** to handle silos with varying computational resources
- **Personalization** strategies to better accommodate heterogeneous local data distributions
- **Differential privacy** mechanisms to provide formal privacy guarantees beyond data isolation
- Integration with [[domain-adaptation-llms-process-mining-peft|LLM-based process mining]] approaches for richer sequence representations

## Applications

The framework is particularly relevant for privacy-sensitive, multi-organizational settings including healthcare (patient pathway analysis), financial services (compliance monitoring), and supply chain management — domains where [[predictive-process-monitoring-pathway-left-shifts|predictive monitoring]] value is high but data sharing is legally or competitively restricted. ^[Thakur et al - Leveraging Cross-Silo Federated Learning in Process Mining.pdf:47-48]

## Key Data

- i = ⟨e1, e2, . . . , en⟩ con-
- k=1 Nk is the total number of
- PNk
i=1 ℓ(f (x(k)
- k = w(t) − η · ∇Fk(w(t)) and finally (3) the server aggregates the updated
- i = aj+1 given partial trace prefix,
- PK
k=1 Fk(w), where
- rate η = O(1/
- mint=1,...,T E∥∇F (w(t))∥2 ≤ O
- PT
t=1 E∥∇F (w(t))∥2 ≤ O
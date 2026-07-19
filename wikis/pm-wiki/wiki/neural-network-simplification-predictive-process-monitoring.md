---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T08:04:48'
lint_warnings:
- claim: a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series)
  concern: ICPM 2025 has not yet occurred at the time of established knowledge, making
    it impossible to verify this acceptance claim. This may be speculative or premature.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Ansari et al - On the Simplification
    of Neural Network Architectures for Predictive Process Monitoring.pdf
  hash: a957dcea86e11a8b3cead362baaef2bc27e9aac5adba649f335c4b312433ad17
  ingested: '2026-07-14T08:04:48'
  size: 1386650
  truncated: true
status: active
tags:
- predictive process monitoring
- deep learning
- process mining
- neural network simplification
- LSTM
- Transformer
- model compression
- event logs
- business process management
- scalability
title: Neural Network Architecture Simplification for Predictive Process Monitoring
type: technology
---

# Neural Network Architecture Simplification for Predictive Process Monitoring

Simplification of neural network architectures for [[narrative-based-predictive-process-monitoring-llm|Predictive Process Monitoring (PPM)]] investigates whether pruning and compressing deep learning models — reducing parameter counts and architectural depth — can preserve predictive accuracy while dramatically lowering computational cost. This line of research is motivated by the practical deployment challenges faced by process mining vendors (e.g., SAP Signavio, Celonis, Apromore) that must train and maintain separate models for each customer process at scale. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:41-48]

The approach was studied by Amaan Ansari, Lukas Kirchdorfer, and Raheleh Hadian (SAP Signavio / University of Mannheim) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series). ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:3-5]

## Motivation

Recent PPM advances rely heavily on deep learning models such as LSTMs and Transformers. While effective, these models are computationally intensive, with large parameter counts and high training costs. Prior efficiency work in PPM has focused on:
- **Data reduction**: sampling informative subsets of event logs for training.
- **Incremental learning**: updating models with new data to avoid full retraining.
- **Alternative architectures**: e.g., Convolutional Neural Networks (CNNs) as faster alternatives to LSTMs.
- **Sequence encoding**: trace encoding as an alternative to prefix sequence encoding. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:108-120]

However, none of these approaches explicitly investigated whether simplifying the model architecture itself — reducing parameter count and depth — can yield efficient PPM solutions without compromising predictive performance. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:11-14]

## PPM Tasks Studied

The paper evaluates five standard PPM tasks on event prefixes:
1. **Next activity prediction (NAP)**: predicting the activity label of the next event.
2. **Next role prediction (NRP)**: predicting the resource/role responsible for the next event.
3. **Next event duration prediction (NDP)**: predicting the duration of the next event.
4. **Next waiting time prediction (NWTP)**: predicting the idle time between the current and next event.
5. **Remaining time prediction (RTP)**: predicting the time until case completion.

These tasks are evaluated using F1-score (categorical) and Mean Absolute Error in days (continuous). See also [[class-balanced-focal-loss-next-activity-prediction]] for related work on next activity prediction and [[actor-enriched-throughput-time-forecasting]] for throughput time forecasting approaches.

## Architectures Evaluated

### Transformer-Based Models

- **MTLFormer** (Wang et al., 2023): The baseline multi-task Transformer with five parallel encoder streams (two for activity, two for role, one for temporal context), each feeding into deep MLP prediction heads. Average parameter count: ~136,412.
- **MTLFormerlight**: Preserves the five-stream backbone but replaces each deep MLP prediction head with a single linear layer, and shrinks backbone hyperparameters (embedding size, number of attention heads, feed-forward dimensions). Average parameter count: ~19,823 — an **85% reduction**.
- **Transformersimple**: Simplifies further by collapsing the five parallel streams into a **single Transformer encoder**, with activity and role tokens concatenated channel-wise. Three single-layer linear prediction heads are used. Average parameter count: ~20,264 — also ~85% reduction from MTLFormer. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:49-61]

### LSTM-Based Models

- **LSTM** (Camargo et al., 2019): Embeds activity, role, and temporal features, feeds them through a shared LSTM backbone with batch normalisation and dropout, then routes the last hidden state into three task-specific heads, each containing a dedicated LSTM layer and a small MLP. Average parameter count: ~75,876.
- **LSTMlight**: Retains the shared LSTM backbone but replaces each task-specific head (LSTM layer + MLP) with a single linear projection. Average parameter count: ~17,193 — a **77% reduction**. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:49-65]

## Key Findings

### Transformer Models Are Highly Compressible

- **MTLFormerlight** achieves an 85% parameter reduction while retaining 98–99% of NAP F1 performance (0.70 → 0.69) and 97% of NRP F1 (0.71 → 0.69). Time-related MAE increases are minimal: NWTP +6.3%, NDP unchanged, RTP +0.7%.
- **Transformersimple** matches MTLFormerlight on time tasks (NWTP +7.0%, NDP unchanged, RTP +1.7%) but shows a ~3 percentage point drop in NAP F1 (0.70 → 0.66), driven largely by the largest dataset (BPI12W).
- Simplified Transformer variants often **converge faster** during training than their full-sized counterparts, suggesting compactness may facilitate optimization. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:56-61]

### LSTM Models Are More Sensitive to Simplification

- **LSTMlight** achieves a 77% parameter reduction with only a 2.9% drop in NAP and NRP F1 (0.70 → 0.68 for both).
- However, time-related tasks are more affected: NWTP MAE increases by **13%**, RTP MAE by 3%, while NDP remains unchanged.
- Compared to Transformersimple, LSTMlight uses 15% fewer parameters and slightly improves NAP (0.68 vs 0.66 F1), but shows **26.8% higher RTP error** (20.80 vs 16.40 MAE days). ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:62-65]

### Summary Comparison

| Model | Avg. Parameters | NAP F1 | NRP F1 | NWTP MAE | RTP MAE |
|---|---|---|---|---|---|
| MTLFormer | 136,412 | 0.70 | 0.71 | 1.43 | 16.12 |
| MTLFormerlight | 19,823 | 0.69 | 0.69 | 1.52 | 16.23 |
| Transformersimple | 20,264 | 0.66 | 0.68 | 1.53 | 16.40 |
| LSTM | 75,876 | 0.70 | 0.70 | 1.38 | 20.19 |
| LSTMlight | 17,193 | 0.68 | 0.68 | 1.56 | 20.80 |

## Experimental Setup

Five event logs were used, spanning financial services, procurement, and manufacturing domains:
- **Production** (real, 225 traces, 24 activities)
- **BPIC2012W** (real, 8,616 traces, 6 activities)
- **P2P** (synthetic, 608 traces, 21 activities)
- **Confidential 1000** (synthetic, 1,000 traces, 42 activities)
- **Confidential 2000** (synthetic, 2,000 traces, 42 activities)

All logs contain both start and end timestamps per event, enabling distinction between event duration and waiting time prediction. A chronological 70/10/20 train/validation/test split was used. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:13-21]

Model selection used a composite score balancing parameter count and validation loss, with uncertainty weighting to combine multi-task losses during training.

## Implications for Practical PPM Deployment

The findings suggest that **lightweight Transformer architectures** are particularly well-suited for scalable PPM deployment in industrial settings. An 85% reduction in parameters with only 1–3% performance loss makes it feasible for vendors to train and maintain per-process, per-customer models at scale. The LSTM architecture, while also compressible, is more sensitive — particularly for temporal prediction tasks such as [[actor-enriched-throughput-time-forecasting|waiting time and remaining time forecasting]]. ^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:16-21]

## Future Directions

- Architecture-aware pruning and neural architecture search for PPM.
- Evaluation on longer-horizon targets (suffix prediction, outcome prediction) beyond next-event tasks.
- Generalizability of lightweight models across unseen process domains.
- Integration into real-time PPM systems.

## Reference

Ansari, A., Kirchdorfer, L., & Hadian, R. (2025). *On the Simplification of Neural Network Architectures for Predictive Process Monitoring*. ICPM 2025 Workshops, Springer LNBIP series.

## Key Data

- pM = #params(M )
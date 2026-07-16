---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T08:07:38'
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Penther et al - Remaining
    Time Prediction in Outbound Warehouse Processes A Case Study.pdf
  hash: 691c2913426e0abb6e3df4e3dda4e0ea813d8d256737071ab7678d060f580682
  ingested: '2026-07-14T08:07:38'
  size: 130434
status: active
tags:
- predictive process monitoring
- remaining time prediction
- process mining
- outbound warehouse
- event log
- deep learning
- boosting
- logistics
- aviation
- case study
title: 'Remaining Time Prediction in Outbound Warehouse Processes: A Case Study'
type: concept
---

# Remaining Time Prediction in Outbound Warehouse Processes: A Case Study

This case study, by Erik Penther, Michael Grohs, and Jana-Rebecca Rehse (University of Mannheim), was accepted at the ICPM 2025 Workshops (Springer LNBIP series). It applies [[actor-enriched-throughput-time-forecasting|Predictive Process Monitoring (PPM)]] remaining time prediction techniques to a real-life outbound warehouse process from a logistics company in the aviation industry, comparing four approaches and releasing a novel public event log.

## Context and Motivation

Remaining time prediction is one of the most common targets in [[narrative-based-predictive-process-monitoring-llm|Predictive Process Monitoring]], aiming to forecast the time until an ongoing process execution completes. Accurate predictions help avoid deadline violations, improve operational efficiency, and provide delivery estimates to customers. In the aviation logistics domain, customers require reliable forecasts to plan maintenance and repair of aircraft supplies. ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:25-60]

A key practical challenge is that many approaches exist — ranging from deep learning to traditional machine learning — and selecting the most suitable one for a given process is non-trivial. Process characteristics such as complexity, available attributes, and computational constraints all influence the choice. ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:28-38]

## The Outbound Warehouse Process

The process originates from a company providing logistics services for the aviation industry, focused on the efficient supply of smaller aircraft components (e.g., spare parts). The control-flow is relatively linear (seven sequential activities, one optional), but cycle times vary due to factors such as item type and weight. ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:54-60]

The company provided an event log with **169,523 traces**, made publicly available in anonymized form (figshare). Each trace corresponds to one order item. 24 attributes are recorded per trace (20 categorical, 4 numerical). Resource information was excluded for privacy reasons. ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:61-80]

## Pre-Processing

- **Outlier removal**: Traces with logically impossible durations or those exceeding half a year were removed; shipment weight outliers above the 95th percentile were excluded.
- **Concept drift handling**: A concept drift occurred in May 2024 (some process variants discontinued, others increased). Only data from June 2024 onward was retained, yielding **41,927 traces** with 330,709 events (7.9 events average). Average cycle time: 24 hours; maximum: 192 hours.
- **Feature selection**: Uninformative features (high-cardinality categoricals, zero-variance features) were removed. Mutual Information (MI) scoring retained 11 features with MI > 1. Additional engineered features included time since trace started, time since last event, day of week, and number of concurrent open traces (inter-case feature for capacity utilization). ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:95-120]

## Approaches Compared

Four remaining time prediction approaches were evaluated:

1. **Data-aware LSTM** — a direct data-aware LSTM architecture processing sequential event data.
2. **SuTraN** — an encoder-decoder transformer for full-context-aware suffix prediction.
3. **PGTNet** — a process graph transformer network using graph-based event log representations.
4. **XGBoost** — a gradient boosting baseline using aggregation/index encoding for temporal features.

Hyperparameters were optimized via grid search on a validation set (last 10% of training traces). The dataset was split 70/30 (train/test). Evaluation metric: **Mean Absolute Error (MAE)** in minutes.

## Results

| Approach | MAE (min) | Training Time | Inference Time |
|----------|-----------|---------------|----------------|
| SuTraN | 554 | 4.65 h | 3.17 ms |
| LSTM | 568 | 1.26 h | 0.63 ms |
| XGBoost | 613 | 2 min | 0.10 ms |
| PGTNet | 1390 | 0.8 h | 95.39 ms |

- **SuTraN** achieved the best accuracy, leveraging attention mechanisms for long-range dependencies, but at the highest computational cost.
- **LSTM** performed closely behind SuTraN but tended to underestimate remaining time — a more problematic error direction in this domain (customers may already need parts when promised).
- **XGBoost** was highly competitive despite its simplicity, training in only 2 minutes with the fastest inference. It does not inherently model temporal dependencies, requiring encoding strategies that may cause information loss.
- **PGTNet** underperformed significantly, likely due to overfitting on this relatively simple, linear process — its graph-based architecture may be over-complex for this event log. ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:41-52]

## Key Findings and Implications

**For practitioners**: Model selection must be adapted to the process at hand. For processes requiring periodic retraining or real-time inference, shallow approaches like XGBoost may be preferable despite slightly lower accuracy. Deep learning models are not always worth the computational overhead.

**For researchers**: Even state-of-the-art approaches could not reduce MAE below ~9 hours on a process with an average cycle time of ~27 hours — indicating substantial room for improvement. Simple architectures appear better suited to shorter, less complex processes, while more complex architectures excel on larger, more intricate logs. This suggests potential benefits of hybrid strategies.

**Limitations**: Executing resources were not recorded (privacy), limiting model inputs. Hyperparameter tuning could be further refined. Only four of many possible approaches were tested. ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:41-80]

## Public Dataset

The anonymized event log (169,523 traces) is publicly available on figshare, and the evaluation pipeline is available on GitHub. The authors encourage researchers to use this dataset, including to study the concept drift present in the pre-June 2024 data. ^[Penther et al - Remaining Time Prediction in Outbound Warehouse Processes A Case Study.pdf:61-106]

## Relation to Other PPM Work

This case study complements benchmark-oriented PPM research such as [[neural-network-simplification-predictive-process-monitoring|neural network simplification studies]] and [[class-balanced-focal-loss-next-activity-prediction|class-imbalance work]] by grounding model comparison in a specific real-world industrial deployment context, emphasizing the practical trade-off between accuracy and computational efficiency.
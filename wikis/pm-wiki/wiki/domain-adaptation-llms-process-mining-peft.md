---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:55:16'
lint_warnings:
- claim: PEFT-based domain adaptation of modern LLMs to raw process data is largely
    unexplored in the PPM literature.
  concern: While this may be relatively underexplored, presenting it as 'largely unexplored'
    is potentially overstated. There is existing literature on fine-tuning language
    models for process mining tasks, and the claim as stated is a strong assertion
    that could misrepresent the state of the field without comprehensive citation
    support.
orphan: false
resource: https://github.com/raseidi/llm-peft-ppm
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Oyamada et al - Domain Adaptation
    of LLMs for Process Data.pdf
  hash: 23e674d587115c618d99bbfb300a99051ce7ef5267c604ef3383dc252310b0e9
  ingested: '2026-07-14T07:55:16'
  size: 475896
  truncated: true
- file: https://github.com/raseidi/llm-peft-ppm
  hash: d3eb5d6ea3cce1ec8d5c1f7c026f07228c4cbbafd9bb6cd84cf77a2c55c5c824
  ingested: '2026-07-16'
  size: 39
status: active
tags:
- LLM fine-tuning
- process mining
- predictive process monitoring
- domain adaptation
- multi-task learning
- parameter-efficient fine-tuning
- event logs
- sequence modeling
- neural networks
- ICPM 2025
title: Domain Adaptation of LLMs for Process Mining via PEFT
type: technology
updated: '2026-07-16'
---

# Domain Adaptation of LLMs for Process Mining via PEFT

Domain adaptation of Large Language Models (LLMs) for process data is an approach within [[narrative-based-predictive-process-monitoring-llm|Predictive Process Monitoring (PPM)]] that fine-tunes pretrained LLMs directly on structured event log sequences — without converting them to natural language — using **parameter-efficient fine-tuning (PEFT)** techniques. The approach was introduced by Rafael Seidi Oyamada, Jari Peeperkorn, Jochen De Weerdt, and Johannes De Smedt (KU Leuven) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series). ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:1-5]

## Motivation

Existing LLM-based approaches to PPM fall into two categories: (1) **prompt engineering**, which crafts structured natural language inputs without modifying model parameters, and (2) **narrative-style fine-tuning**, which reformulates event logs as free-text stories (as in [[narrative-based-predictive-process-monitoring-llm|narrative-based PPM]]). Both strategies rely on the LLM's general language understanding and treat event logs as linguistic artifacts. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:33-43]

The authors argue this creates a fundamental misalignment: event logs are not natural language — they use a small, structured alphabet of activity labels governed by domain-specific behavioral relations, not linguistic grammar. Relying on semantic reasoning alone may introduce noise from irrelevant prior knowledge, and prompt engineering adds fragility (sensitivity to phrasing, expert knowledge requirements, potential for human error). Furthermore, narrative-style approaches may inadvertently leak future information (e.g., listing only activities possible for the ongoing variant, which is unknown in online settings). ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:44-53]

The paper also identifies a gap: **PEFT-based domain adaptation of modern LLMs to raw process data** is largely unexplored in the PPM literature. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:44-47]

## Methodology

The framework consists of four components:

### Input Layers
Raw event features of shape *(B, L, F)* (batch, sequence length, features) are projected into a shared embedding space. Categorical features (e.g., activity labels) are mapped via an embedding layer; numerical features (e.g., time deltas) are projected linearly. Outputs are fused by summation into a latent representation of dimension *E*. Critically, the **language-based tokenizer is replaced** with a task-specific embedding layer trained from scratch on the process vocabulary, enabling the LLM to consume structured process data natively. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:48-53]

### Backbone
The backbone transforms the embedded input into a contextual output tensor *(B, L, D)*. The paper evaluates decoder-only transformer architectures: **GPT-2** (~0.1B parameters, called PM-GPT2), **Qwen2.5** (0.5B), and **Llama3.2** (1B). ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:44-58]

### Output Layers
Task-specific linear heads map backbone outputs to predictions. In the **multi-task** setup, two parallel heads predict:
- **Next Activity (NA)**: classification over the activity set *A*
- **Remaining Time (RT)**: regression to a positive real number

In single-task setups, one head is used per model. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:91-100]

### PEFT Strategies
Three PEFT configurations are evaluated:
- **Full freezing**: all backbone weights frozen; only I/O layers trained
- **Partial freezing**: a selected subset of backbone layers unfrozen (e.g., first layer, last layer, last two layers)
- **LoRA (Low-Rank Adaptation)**: low-rank matrices *B ∈ ℝ^(m×r)* and *A ∈ ℝ^(r×n)* are inserted alongside frozen weight matrices *W*, replacing *W* with *W' = W + BA*; only *A* and *B* are learned. Rank *r = 256*, alpha *= 512* are used. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:116-119]

All I/O layers are trained from scratch regardless of PEFT strategy, since the process-specific vocabulary differs entirely from the LLM's original natural language vocabulary. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:48-53]

## Experimental Setup

Five real-world event logs are used: **BPI12**, **BPI17**, **BPI20 Request for Payment (RfP)**, **BPI20 Prepaid Travel Costs (PTC)**, and **BPI20 Permit Data (PD)**. Preprocessing discards cases with fewer than two events; numerical features are z-score normalized; only activity labels and time features are used (no case/event attributes) for systematic comparability. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:80-83]

Data is split using the **unbiased split** method, and sequences are encoded using **trace encoding** (many-to-many with teacher forcing) rather than prefix encoding. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:101-108]

Baselines include:
- **ST-RNN / MT-RNN**: single-task and multi-task LSTM models
- **PM-GPT2**: GPT-2 fine-tuned via transfer learning (inspired by prior transformer transfer learning work)
- **S-NAP**: narrative-style Llama fine-tuning with LoRA (adapted from [[narrative-based-predictive-process-monitoring-llm|narrative-based PPM]]), with a corrected prompt that uses all training activities rather than variant-specific ones ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:54-58]

Loss functions: cross-entropy (NA), MSE (RT). LLMs are trained for 10 epochs; RNNs for 25. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:54-58]

## Results

### RQ1: Do fine-tuned LLMs outperform existing methods?
- **S-NAP is significantly outperformed** across all datasets and both tasks, suggesting that semantic capabilities alone are insufficient for learning real-world process behavior from activity labels. The corrected (non-leaking) prompt further reduces S-NAP accuracy substantially.
- **MT-RNN never achieves the highest scores** on any dataset, struggling with multi-task complexity.
- **ST-RNN is a strong NA baseline** (especially on BPI12 and BPI17) but inconsistent on RT prediction.
- **Fine-tuned LLMs (Llama3.2, Qwen2.5) are the most consistent** across datasets on both tasks, outperforming RNNs and S-NAP in the multi-task setting.
- Trade-off: LLMs require orders of magnitude more parameters and runtime than RNNs, but demand far less hyperparameter optimization. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:19-23]

### RQ2: Can LLMs handle multi-task PPM?
- LLMs converge within **fewer than 5 epochs** for NA prediction, much faster than RNNs.
- For RT prediction, LLMs consistently outperform both ST-RNN and MT-RNN.
- MT-RNNs struggle with multi-task learning (e.g., converging on NA but underfitting RT on BPI17).
- **Llama3.2** is the most consistent LLM for RT prediction; model size matters for regression stability.
- LLMs exhibit spiky RT loss curves, reflecting their origin as next-token classifiers rather than regressors. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:59-67]

### RQ3: Which PEFT method works best?
- For **NA prediction**: LoRA and partial freezing both perform well; a few unfrozen layers are needed — full freezing is inconsistent.
- For **RT prediction**: **LoRA clearly outperforms freezing**, as adapter layers help bridge the gap between classification-oriented pretraining and regression.
- Full freezing of the backbone (training only I/O layers) can achieve competitive RT performance, suggesting the regression capability is largely driven by the new output head. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:116-119]

## Key Findings and Limitations

- Direct domain adaptation (without natural language conversion) is more effective than narrative-style fine-tuning for structured process data.
- PEFT-adapted LLMs require minimal hyperparameter search compared to RNNs.
- **Narrative-style approaches are sensitive to activity label language** (e.g., BPI12 mixes English and Dutch labels, causing near-zero accuracy until labels are standardized).
- Suffix prediction is not evaluated due to input/output misalignment in decoder-only architectures.
- Only activity labels and time features are used; richer event attributes are left for future work.
- Regression adaptation of classification-pretrained LLMs remains an open challenge. ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:59-67]

## Relation to Other Work

This paper directly contrasts with [[narrative-based-predictive-process-monitoring-llm|narrative-based predictive process monitoring]], arguing that bypassing natural language reformulation and adapting LLMs to process semantics via PEFT yields better and more robust PPM performance. It also relates to [[class-balanced-focal-loss-next-activity-prediction|next activity prediction]] and [[actor-enriched-throughput-time-forecasting|throughput time forecasting]] as complementary PPM techniques. The [[k-traceoids-trace-clustering|k-traceoids]] framework shares authorship (Oyamada) and the broader ICPM 2025 Workshops venue.

## Citation

Oyamada, R.S., Peeperkorn, J., De Weerdt, J., & De Smedt, J. (2025). *Domain Adaptation of LLMs for Process Data*. ICPM 2025 International Workshops, Springer LNBIP. Supported by FWO Project 1294325N, grant G039923N, and KU Leuven Internal Funds C14/23/031. Code: https://github.com/raseidi/llm-peft-ppm ^[Oyamada et al - Domain Adaptation of LLMs for Process Data.pdf:36-39]

## Открытая реализация: репозиторий llm-peft-ppm

Код экспериментов опубликован в открытом репозитории [raseidi/llm-peft-ppm](https://github.com/raseidi/llm-peft-ppm) на GitHub. Репозиторий содержит скрипты для дообучения LLM в режиме многозадачного [[narrative-based-predictive-process-monitoring-llm|предиктивного мониторинга процессов]] (PPM): одновременного предсказания следующего события и оставшегося времени выполнения.^[llm-peft-ppm:88-91]

### Структура репозитория

Проект организован следующим образом:

- `ppm/` — основной исходный код библиотеки;
- `next_event_prediction.py` — главный скрипт обучения;
- `luijken_transfer_learning.py` — скрипт обучения конкурентного метода на основе transfer learning (Luijken et al.);
- `rebmann_et_al.py` — скрипт обучения нарративного конкурентного метода (Rebmann et al.), аналогичного подходу [[narrative-based-predictive-process-monitoring-llm]];
- `notebooks/` — ноутбуки с анализом результатов и визуализациями;
- `scripts/` — конфигурации для запуска на HPC-кластерах через Slurm.^[llm-peft-ppm:103-115]

### Используемые журналы событий

Эксперименты проводились на пяти публичных журналах событий, автоматически загружаемых через библиотеку **SkPM**:^[llm-peft-ppm:117-120]

| Идентификатор | Описание |
|---|---|
| BPI20PTC | Prepaid Travel Costs |
| BPI20RfP | Request for Payment |
| BPI20TPD | Permit Data |
| BPI12 | Кредитные заявки (BPIC 2012) |
| BPI17 | Кредитные заявки (BPIC 2017) |

### Базовые модели и параметры LoRA

В качестве лёгкой отправной точки для отладки рекомендуется модель **Qwen2.5-0.5B** (`qwen25-05b`). Метод [[domain-adaptation-llms-process-mining-peft|PEFT]] реализован через **LoRA** с ключевыми гиперпараметрами `--r` (ранг матриц адаптации) и `--lora_alpha`. При `batch_size=4` модель умещается менее чем в 2 ГБ видеопамяти, что делает эксперименты доступными на потребительском оборудовании.

Для сравнения также поддерживается базовая линия на основе **RNN** с настраиваемыми размерами эмбеддингов и скрытого слоя. Поиск гиперпараметров выполнялся на HPC-кластерах с использованием Slurm; логирование метрик осуществляется через **Weights & Biases** (флаг `--wandb`).

### Многозадачная постановка

В отличие от большинства работ по [[neural-network-simplification-predictive-process-monitoring|предиктивному мониторингу]], репозиторий явно поддерживает многозадачное обучение: модель одновременно предсказывает категориальную цель (следующая активность) и непрерывную цель (оставшееся время), что задаётся аргументами `--categorical_targets` и `--continuous_targets` соответственно.

## Key Data

- HF_TOKEN=<YOUR_TOKEN>
- export HF_TOKEN="<YOUR_TOKEN>"
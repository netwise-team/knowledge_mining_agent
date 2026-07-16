---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:53:36'
lint_warnings:
- claim: k-traceoids is inspired by the k-means clustering algorithm but adapted to
    the structural nature of process traces.
  concern: The name 'k-traceoids' strongly suggests inspiration from k-medoids (not
    k-means), as medoid-based methods use actual data instances as cluster representatives
    — analogous to how k-traceoids uses discovered process models rather than computed
    means. The table itself highlights differences from k-means, making the k-means
    inspiration claim misleading.
orphan: false
resource: https://github.com/NeroCorleone/k-traceoids
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Kanilmaz et al - Introducing
    k-traceoids A Structure-Preserving Trace Clustering Framework.pdf
  hash: 5725c9b1df4615f4b0d3f7d20ab5668dd5906f431e5e5b0757732bcd7f67ede0
  ingested: '2026-07-14T07:53:36'
  size: 3577261
- file: https://github.com/NeroCorleone/k-traceoids
  hash: 6f932e759bef6c4cf23d1d2319e5734db94b70e5ffaa3740ca7478808d2aa952
  ingested: '2026-07-16'
  size: 43
status: active
tags:
- trace clustering
- process mining
- unsupervised learning
- event logs
- sequential data
- process models
- centroids
- vector space
- anomaly detection
- process discovery
title: 'k-traceoids: A Structure-Preserving Trace Clustering Framework'
type: technology
updated: '2026-07-16'
---

# k-traceoids: A Structure-Preserving Trace Clustering Framework

**k-traceoids** is a trace clustering algorithm for [[process-mining-data-science-in-action|process mining]] introduced by Umut Nefta Kanilmaz, Gabriel Marques Tavares, Daniel Schuster, Rafael Seidi Oyamada, and Thomas Seidl (LMU Munich / KU Leuven) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series). The framework addresses a fundamental limitation of existing trace clustering approaches: the loss of sequential and structural information caused by vector-space encodings.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:1-13]

## Motivation

Event logs from real-world processes are often complex and exhibit high variability, with many distinct process execution variants. Trace clustering helps manage this complexity by partitioning event data into smaller, more homogeneous subsets, facilitating tasks such as process discovery and anomaly detection.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:25-31]

Most existing trace clustering methods transform traces into numerical feature vectors (e.g., one-hot encoding, n-grams, learned embeddings) before applying algorithms like k-means or DBSCAN. This transformation inherently discards the **order of activities**, which is a critical dimension of process behavior. k-traceoids avoids this information loss by operating directly on traces and using process models — rather than numerical centroids — to represent clusters.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:32-43]

## Algorithm Design

k-traceoids is inspired by the k-means clustering algorithm but adapted to the structural nature of process traces. The key conceptual analogies and differences are:

| Category | k-traceoids | k-means |
|---|---|---|
| Data Type | Traces | Numerical vectors |
| Initial Assignment | Balanced by variant size | Random centroid choice |
| Cluster Representation | Process model | Cluster centroid (mean) |
| Distance Measure | Conformance (trace-to-model fitness) | Euclidean distance to centroid |
| Convergence Criteria | Stable trace assignments | Stable point and centroid assignments |

^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:91-105]

### Workflow

The algorithm proceeds in three main steps:

1. **Initialization**: The event log's traces are grouped by variant. Variants are distributed across *k* clusters in a balanced manner. The number of clusters *k* and a maximum iteration count are set as hyperparameters.

2. **Model Calculation**: A process model is discovered from the traces in each cluster, serving as the cluster's centroid. Any process discovery algorithm can be used (e.g., Inductive Miner - infrequent (IMF) or Heuristic Miner (HM)).

3. **Reassignment**: Each trace's conformance (fitness) to each of the *k* models is computed. Traces are reassigned to the cluster whose model they fit best. Traces belonging to the same variant are always kept together.

Steps 2 and 3 repeat until assignments stabilize (convergence) or the maximum iteration count is reached.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:83-90]

### Flexibility

k-traceoids is a **generic framework**: the choice of process discovery algorithm (model centroid) and conformance checking method (distance measure) are both configurable hyperparameters. This makes the approach adaptable to diverse datasets without method-specific optimization.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:74-79]

## Relation to Existing Approaches

- **Distance-based clustering** (e.g., DBSCAN, k-means on vectors): These methods risk losing sequential information through vectorial encoding. k-traceoids avoids this by working directly on traces.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:54-59]
- **ActiTrac**: A process-model-based clustering method that uses active learning to iteratively build clusters one at a time. k-traceoids differs by generating all clusters simultaneously and updating all models collectively, improving cluster stability.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:60-69]
- **Entropic clustering**: Groups process variants by minimizing entropic relevance scores on DFGs. This method is tightly coupled to DFGs, whereas k-traceoids is more flexible in its choice of model representation.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:70-73]

Trace clustering is also used as a preprocessing step for [[actor-enriched-throughput-time-forecasting|predictive process monitoring]] and process analytics.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:74-76]

## Experimental Evaluation

Experiments were conducted on the **Road Traffic Fine Management (RTFM)** event log, a widely used benchmark in process mining research. The algorithm was evaluated across all combinations of:

- **k** (number of clusters): 2–10
- **Model discovery algorithm (m)**: IMF, HM
- **Conformance checking method (c)**: Token-Based Replay (TBR), Alignment-Based Fitness (ALB)

Maximum iterations were set to 100; a 10-minute timeout was applied to ALB computations for complex traces.

### Qualitative Results

For the configuration *k=4, IMF, ALB*, k-traceoids identified four distinct clusters with meaningfully different behavioral profiles:
- **Cluster A**: Traces with repeated Payment and Add Penalty activities, varying in length.
- **Cluster B**: Traces with long-term dependencies and activity variations (Add Penalty, Appeal to Judge).
- **Cluster C**: Simple repetition of a single activity (Payment).
- **Cluster D**: Short, linear process executions.

Notably, traces that appear highly dissimilar in vector space (large Euclidean distance) were correctly grouped together based on behavioral similarity captured by the process model.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]

### Quantitative Results

- **Cluster balance (Shannon entropy)**: Most configurations achieved normalized entropy above 0.8, indicating balanced clusters. IMF+TBR tended toward lower entropy at higher *k* values.
- **Fitness**: Mean fitness values were very high across configurations, often reaching 1.0, indicating that traces are well-represented by their cluster models.
- **Precision**: HM consistently achieved precision of 1 (potentially overfitting), while IMF+TBR showed more balanced precision, suggesting better generalization.
- **Convergence speed**: IMF+ALB converged fastest, especially at low *k* values. IMF+TBR and HM+TBR frequently reached the maximum iteration limit.
- **Execution time**: Execution time grows roughly linearly with *k*, as each iteration requires additional model discovery and conformance checks.

The combination HM+ALB produced errors in several runs due to incompatibilities between the two algorithms, requiring further investigation.

## Conclusion

k-traceoids provides a structure-preserving alternative to vector-based trace clustering by using process models as cluster centroids and conformance checking as the distance measure. The framework is highly general, supports pluggable discovery and conformance algorithms, and has been shown to uncover meaningful behavioral clusters in real-world event logs.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:36-50]

## See Also

- [[process-mining-data-science-in-action]]
- [[actor-enriched-throughput-time-forecasting]]
- [[streaming-process-mining-event-streams]]
- [[class-balanced-focal-loss-next-activity-prediction]]

## Algorithm Workflow

The k-traceoids framework operates in three main steps, analogous to [[process-mining-data-science-in-action|k-means]] but applied directly to traces:

1. **Initialization**: The event log's traces are grouped by variant. Variants are distributed across *k* clusters such that the number of traces per cluster is roughly balanced.
2. **Model Calculation**: A process model (the "centroid") is discovered from the traces currently assigned to each cluster. Any process discovery algorithm can be used here — the framework is not tied to a specific technique.
3. **Reassignment**: Each trace's conformance fitness to every cluster model is computed. Each trace is reassigned to the cluster whose model it fits best, with the constraint that all traces of the same variant stay together.

Steps 2 and 3 repeat until either no trace changes cluster (stable assignment) or a maximum iteration count is reached.^[83-120]

### Conceptual Comparison with k-means

| Category | k-traceoids | k-means |
|---|---|---|
| Data type | Traces | Numerical vectors |
| Initial assignment | Balanced by variant size | Random centroids + distance |
| Cluster representation | Process model | Arithmetic centroid |
| Distance measure | Conformance fitness | Euclidean distance |
| Convergence | Stable trace assignments | Stable point/centroid assignments |

## Experimental Setup

Experiments used the **Road Traffic Fine Management (RTFM)** event log, a widely used benchmark in [[process-mining-data-science-in-action|process mining]] research. The hyperparameter grid covered:

- **k** (number of clusters): 2–10
- **m** (process discovery algorithm): Inductive Miner – Infrequent (IMF) and Heuristic Miner (HM)
- **c** (conformance checking): Token-Based Replay (TBR) and Alignment-Based Fitness (ALB)

All combinations were evaluated. A maximum of 100 iterations was enforced, and a 10-minute timeout was applied to ALB computations to handle expensive alignment calculations on complex traces.^[83-120]

## Quantitative Evaluation Results

- **Cluster balance (Shannon entropy)**: Most configurations achieved normalized entropy above 0.8, indicating balanced clusters. IMF+TBR tended toward lower entropy at higher *k*, reflecting the variant-grouping constraint.
- **Mean fitness**: Fitness values were consistently high across configurations, often reaching 1.0, confirming that traces are well-represented by their cluster models.
- **Precision**: HM consistently achieved precision = 1 across all *k*, suggesting tight, specific models. IMF+TBR showed more balanced precision, indicating better generalization.
- **Convergence speed**: IMF+ALB converged fastest, especially at low *k* (2–3). IMF+TBR and HM+TBR frequently hit the 100-iteration maximum.
- **Cluster stability at k=10**: Configurations other than IMF+TBR reached ~98% trace stability within 20 iterations, suggesting the convergence criterion could be relaxed to a stability threshold rather than requiring full convergence.
- **Execution time**: Scales roughly linearly with *k*, as each iteration requires discovering more models and running additional conformance checks. Definitive scaling claims await evaluation on larger, more heterogeneous logs.^[44-50]

## Qualitative Cluster Analysis

For the configuration *k*=4, IMF, ALB on RTFM, the four discovered cluster models differed in size, complexity, and linearity:

- **Cluster A**: Captures traces with repeated *Payment* and *Add Penalty* activities, even across widely varying trace lengths.
- **Cluster B**: Groups traces with long-term dependencies (e.g., *Create Fine → Send Fine → Insert Fine Notification*) and allows variation in *Add Penalty* and *Appeal to Judge*.
- **Cluster C**: Isolates simple repetitions of a single activity (*Payment*), including extreme cases (up to 15 repetitions).
- **Cluster D**: Captures short, linear process executions.

This demonstrates that k-traceoids groups traces that share behavioral structure even when their lengths differ substantially — a grouping that vector-space approaches would miss due to large Euclidean distances between differently-lengthed encodings. The full results and code are available at [https://github.com/NeroCorleone/k-traceoids/](https://github.com/NeroCorleone/k-traceoids/).^[44-50]

## Реализация и репозиторий

Официальный исходный код k-traceoids опубликован в открытом доступе на GitHub в репозитории [NeroCorleone/k-traceoids](https://github.com/NeroCorleone/k-traceoids). Репозиторий содержит код и анализ, использованные при подаче статьи на воркшоп ML4PM @ [[k-traceoids-trace-clustering|ICPM 2025]]. Реализация выполнена преимущественно на Python (26,2%) и Jupyter Notebook (73,7%), что позволяет воспроизводить эксперименты в интерактивном режиме. ^[k-traceoids:1-50]

### Алгоритмический процесс

Алгоритм k-traceoids вдохновлён k-means и работает непосредственно с трассами [[process-mining-data-science-in-action|журнала событий]], не преобразуя их в векторные представления. Процесс состоит из трёх основных этапов: ^[k-traceoids:89-96]

1. **Инициализация.** На вход подаётся журнал событий, содержащий *n* трасс с уникальными идентификаторами случаев. Задаётся число кластеров *k* и максимальное число итераций. Каждая трасса случайным образом назначается одному из *k* кластеров. ^[k-traceoids:99-107]

2. **Вычисление модели.** Для каждого кластера на основе текущих назначений трасс вычисляется представительная модель (центроид). В качестве центроида может выступать процессная модель, наиболее частый вариант или супервариант. ^[k-traceoids:109-110]

3. **Переназначение трасс.** Каждая трасса оценивается на соответствие моделям кластеров с помощью [[federated-learning-process-mining|конформанс-чекинга]]; трасса переназначается в кластер с наилучшей подходящей моделью. Шаги 2 и 3 повторяются до сходимости: либо назначения трасс не изменяются между итерациями, либо достигнуто максимальное число итераций. ^[k-traceoids:112-116]

### Установка и использование

Проект использует [Poetry](https://python-poetry.org/) для управления зависимостями. Установка выполняется следующим образом:

```bash
git clone git@github.com:NeroCorleone/k-traceoids.git
cd k-traceoids
poetry install
```

Команда `poetry install` создаёт виртуальное окружение, устанавливает все зависимости из `pyproject.toml` и устанавливает пакет в редактируемом режиме. Гиперпараметры (*k*, `max_iterations` и др.) задаются в файле `script.py`. Для воспроизводимости результатов опубликован отдельный релиз кода («Code Release for Reproducibility ML4PM 2025»). ^[k-traceoids:119-120]
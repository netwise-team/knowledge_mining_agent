---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:03:45'
lint_warnings:
- claim: TT is widely recognized as one of the most critical KPIs in process mining
    dashboards and operational decision-making
  concern: This is an overstatement. While throughput time is an important metric,
    claiming it is 'widely recognized as one of the most critical KPIs' is not a well-established
    consensus fact — process mining literature treats multiple KPIs (conformance,
    resource utilization, bottleneck identification) as equally or more prominent
    depending on context. This appears to reflect the authors' framing rather than
    an established fact.
orphan: false
resource: https://github.com/aurelieleribaux-1/actor-behavior-TT-forecasting
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Leribaux et al - Actor-Enriched
    Time Series Forecasting of Process Performance.pdf
  hash: fc038bb9dc65843e387597c327d33dd112911cbf765fd1d3b6d4058165d2d1fe
  ingested: '2026-07-14T07:03:45'
  size: 835957
  truncated: true
- file: https://github.com/aurelieleribaux-1/actor-behavior-TT-forecasting
  hash: 9a6fad66adc3b0b4f496e388ebbd8220c343715c1b4f9ff8784085696e9c3383
  ingested: '2026-07-16'
  size: 66
status: active
tags:
- predictive process monitoring
- time series forecasting
- process mining
- actor behavior
- throughput time
- machine learning
- resource behavior
- KPI forecasting
- event logs
- multivariate analysis
title: Actor-Enriched Throughput Time Forecasting in Predictive Process Monitoring
type: concept
updated: '2026-07-16'
---

# Actor-Enriched Throughput Time Forecasting in Predictive Process Monitoring

Actor-enriched throughput time (TT) forecasting is a [[coordinated-projections-multi-faceted-process-exploration|process mining]] technique within Predictive Process Monitoring (PPM) that incorporates dynamic actor behavior — modeled as multivariate time series — to improve the prediction of process-level performance indicators. The approach was introduced by Leribaux, Oyamada, De Smedt, Dasht Bozorgi, Polyvyanyy, and De Weerdt (KU Leuven / University of Melbourne) in a paper accepted at the ICPM 2025 Workshops.

## Motivation

PPM enables organizations to anticipate future behavior and performance of ongoing business processes using historical execution data. While most PPM research focuses on predicting the outcome or remaining time of individual cases, considerably less attention has been given to forecasting process-level performance indicators such as average daily throughput time (TT). TT is widely recognized as one of the most critical KPIs in process mining dashboards and operational decision-making, serving as a proxy for overall process efficiency and supporting resource allocation and capacity management.^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:27-34]

Existing approaches to incorporating resource information in PPM typically encode resources in a static or categorical way (e.g., one-hot encoded identifiers, activity frequency counts, or clustering-based groupings), neglecting the dynamic nature of actor behavior. This paper addresses that gap by modeling actor behavior as time-varying signals aligned with TT.^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:35-43]

## Background: Event Logs and Actor Behavior

Event logs are the primary data source in process mining, capturing the execution history of business processes. Each event is represented as a tuple *e = (c, a, t, r)*, where *c* is the case identifier, *a* is the activity, *t* is the timestamp, and *r* is the resource (actor) that executed the event.^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:68-75]

Actor behavior is extracted by analyzing pairs of consecutive events (transitions) within the same case. Each transition is classified into one of four behavior types:

- **Continuation (C):** A resource continues their own work on the same case.
- **Interruption (I):** A resource is interrupted by other cases.
- **Handover to Idle (HI):** Work is passed to another actor who is currently idle.
- **Handover to Busy (HB):** Work is passed to another actor who is already busy.^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:78-83]

These behavior types are then aggregated into daily time series:
- **Daily behavior count** *F_b(d)*: Number of transitions of type *b* whose first event occurred on day *d*.
- **Daily behavior duration** *T_b(d)*: Total time (in seconds) spent in transitions of type *b* on day *d*.

This produces eight actor feature time series (four behavior types × two metrics: count and duration).^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:86-114]

## Methodology

### Multivariate Time Series Construction

The framework constructs two categories of time series features:

1. **Baseline features (BF):** Derived solely from historical TT values. These include daily lagged values (1–20 days), rolling statistics (mean, standard deviation, maximum) over windows of 3, 7, and 14 days, a 7-day z-score, and a peak indicator (set to 1 on days where TT shows a local maximum).

2. **Actor-enriched features (AF):** The time-varying actor behavior series *F_b(d)* and *T_b(d)*, engineered with the same lag and rolling statistics as the baseline features.

Two datasets are generated: a **baseline dataset** (BF only) and an **actor-enriched dataset** (BF + AF).

### Target Variable

The target is the daily average TT of cases starting on the following day:

*TT(d) = (1/|C_d|) × Σ TT(c)* for all completed cases *c* starting on day *d*.

To improve temporal learning stability, models predict the **daily smoothed first difference** of TT (ΔTT), computed via a 3-point rolling average. Final TT predictions are reconstructed by adding predicted ΔTT to the previous day's TT value. This residual learning strategy focuses models on short-term variation rather than the full TT trajectory.

### Models

Three model families are compared on both baseline and actor-enriched feature sets:

- **ARIMA:** Trained solely on historical first differences of TT (benchmark).
- **Gradient Boosted Trees:** XGBoost and LightGBM, trained on structured engineered features.
- **Hybrid Deep Learning:** Conv1D layers for local pattern extraction combined with bidirectional RNNs (GRU or LSTM), with optional attention mechanisms.

All models use five-fold time series cross-validation (chronological split), with hyperparameter tuning via grid search. Final evaluation uses an 80/20 chronological train/test split, reporting RMSE, MAE, and R².

## Experimental Evaluation

The framework is validated on three real-life BPIC event logs:
- **BPIC 2017** and **BPIC 2012:** Financial services domain.
- **BPIC 2011 (Hospital log):** Healthcare domain (see also [[process-mining-healthcare-radiological-workflows]]).^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:54-55]

### Results

Across all datasets and model types, actor-enriched models consistently outperform baseline models in RMSE, MAE, and R²:

- **Tree-based models** (XGBoost, LightGBM) deliver the strongest and most robust improvements. On BPIC 2012, actor-enriched XGBoost reduces RMSE by ~2.93 hours, MAE by ~1.78 hours, and improves R² by 5.8 percentage points.
- **RNN models** (LSTM, GRU, with and without attention) also benefit from actor enrichment, though gains are more variable. On BPIC 2012, attention-enhanced LSTM achieves an RMSE reduction of over 4.4 hours and an R² improvement of 8.5 percentage points.
- **BPIC 2011** shows less consistent improvements for RNNs, attributed to the dataset's larger size, higher variance, and more complex case structure.
- All actor-enriched models significantly outperform the ARIMA benchmark.^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:19-23]

### Feature Importance

**SHAP values** (tree-based models) show that the most influential features are lagged TT values and z-score transformations, but actor-related variables (e.g., *Count_C_lag4*, *Time_HB_seconds_lag4*) also rank highly, confirming their added predictive value.

**Permutation importance** (RNN models) reveals a strong reliance on actor features, with lagged and rolling indicators of handovers (*Count_HB_lag13*, *Count_HB_seconds_lag8*) and continuations (*Count_C_rolling_mean3*) frequently appearing among the top predictors.

## Key Contributions

1. A novel **actor-enriched forecasting framework** that models actor behavior as time series features aligned with daily TT.
2. Empirical validation on three real-life BPIC event logs from distinct domains and scales.
3. Demonstration that actor behavior features consistently improve TT forecasting across multiple model families, especially tree-based learners and recurrent networks.^[Leribaux et al - Actor-Enriched Time Series Forecasting of Process Performance.pdf:51-58]

## Relationship to Broader Process Mining

This work sits at the intersection of PPM and resource-aware process mining. It complements [[sustainability-aware-process-mining|sustainability-aware process mining]] by providing operational performance forecasting grounded in resource dynamics. The use of event logs as the primary data source connects it to foundational process mining methodology, and the healthcare evaluation dataset links it to [[process-mining-healthcare-radiological-workflows|healthcare process mining]] applications. The behavioral taxonomy (continuation, interruption, handover) also relates to [[deviation-desirability-assessment|conformance and deviation analysis]] by characterizing how work transitions deviate from ideal resource coordination patterns.

## References

- Leribaux, A., Oyamada, R., De Smedt, J., Dasht Bozorgi, Z., Polyvyanyy, A., & De Weerdt, J. (2025). *Actor-Enriched Time Series Forecasting of Process Performance.* Pre-print, ICPM 2025 International Workshops, Springer LNBIP.
- Code repository: https://github.com/aurelieleribaux-1/actor-behavior-TT-forecasting

## Key Data

- b = {x(m)

## Открытая реализация: репозиторий на GitHub

Авторы опубликовали полный исходный код метода в открытом репозитории [`aurelieleribaux-1/actor-behavior-TT-forecasting`](https://github.com/aurelieleribaux-1/actor-behavior-TT-forecasting). Репозиторий предоставляет модульный конвейер для прогнозирования производительности процессов на основе поведения акторов, извлечённого из [[process-mining-data-science-in-action|журналов событий]].^[actor-behavior-TT-forecasting:83-83]

### Структура проекта

Репозиторий организован следующим образом:

- **`dataset pipeline/time_series_generation.py`** — скрипт преобразования журнала событий и файла поведения акторов в итоговый многомерный временной ряд (`data/final_multivariatetimeseries.csv`). Входными данными служат: исходный журнал событий в формате `.xes` и CSV-файл поведения акторов, сгенерированный методом «Linking Actor Behavior to Process Performance Over Time».^[actor-behavior-TT-forecasting:91-118]
- **`models/`** — реализации всех поддерживаемых моделей:
  - `xgboost_model.py` — XGBoost (базовая версия и версия, обогащённая акторами);
  - `lightgbm_model.py` — LightGBM (базовая версия и версия, обогащённая акторами);
  - `arima_model.py` — ARIMA с остаточным прогнозированием;
  - `RNN_Attn.py` — GRU/LSTM с механизмом внимания;
  - `RNN_model.py` — GRU/LSTM без механизма внимания;
  - `feature_engineering.py` — инженерия признаков.^[actor-behavior-TT-forecasting:93-99]
- **`utils/data_utils.py`** и **`utils/train_test_split.py`** — утилиты загрузки и разбиения временных рядов на обучающую и тестовую выборки.^[actor-behavior-TT-forecasting:101-103]

### Конвейер обучения и оценки

Каждый скрипт модели следует единой структуре:
1. Загрузка и разбиение многомерного временного ряда через общую утилиту `load_train_test_split`.
2. Применение базовой или обогащённой акторами инженерии признаков — частоты и длительности поведения акторов, участие ресурсов, пропускное время (TT).
3. Обучение и валидация модели с использованием кросс-валидации.
4. Оценка на финальной отложенной тестовой выборке.
5. Визуализация предсказаний и важности признаков.^[actor-behavior-TT-forecasting:108-120]

### Метрики и выходные данные

Результаты включают:
- RMSE, MAE и R² на кросс-валидации (с доверительными интервалами) и на отложенной тестовой выборке;
- SHAP-значения или перестановочную важность признаков;
- графики фактических и предсказанных временных рядов.

Данная реализация позволяет воспроизвести эксперименты статьи, принятой на воркшопах [[class-balanced-focal-loss-next-activity-prediction|ICPM 2025]], и адаптировать конвейер к собственным журналам событий в формате XES.
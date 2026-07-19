---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:36:34'
lint_warnings:
- claim: The only prior PPM work addressing this (Mehdiyev et al.) frames it as a
    binary problem, which is unsuitable for multi-class next activity prediction.
  concern: This claim that Mehdiyev et al. is the *only* prior PPM work addressing
    class imbalance is likely overstated. The PPM literature is broad, and asserting
    a single prior work exists on this topic requires exhaustive verification; other
    works may address imbalance in related PPM tasks even if not framed identically.
orphan: false
resource: https://github.com/Xiaomeng-He/CBFL
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/He et al - Tackling Multi-Class
    Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf
  hash: 846f9f1c7e0b85a764005b225bae4b9420b0e54382c308b3379cc93a427bbac5
  ingested: '2026-07-14T07:36:34'
  size: 732503
  truncated: true
- file: https://github.com/Xiaomeng-He/CBFL
  hash: 4ff85edd1acf9dddf74a5862a79ff420760fe2e66123c418803ce706ec97f96e
  ingested: '2026-07-16'
  size: 35
status: active
tags:
- multi-class imbalance
- focal loss
- process mining
- machine learning
- deep learning
- cross-entropy loss
- event logs
- loss re-weighting
- classification
- predictive modeling
title: Class-Balanced Focal Loss for Next Activity Prediction
type: technology
updated: '2026-07-16'
---

# Class-Balanced Focal Loss for Next Activity Prediction

Class-Balanced Focal Loss (CBFL) is a loss re-weighting technique applied to the **next activity prediction** task within [[narrative-based-predictive-process-monitoring-llm|Predictive Process Monitoring]] (PPM). The approach was introduced by Xiaomeng He, Rafael Oyamada, Johannes De Smedt, Seppe vanden Broucke, and Jochen De Weerdt (KU Leuven / Ghent University) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

In real-life event logs, activity label distributions are typically skewed: a few dominant (majority) classes contribute most instances, while many minority classes are underrepresented. Standard machine learning models trained with cross-entropy loss (CEL) are biased toward majority classes, leading to poor predictive performance on infrequent yet potentially critical activities — such as "Application_Denied" or "Offer_Accepted" in loan application processes.^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:14-18]

Despite the known impact of class imbalance on model quality, the PPM literature has largely ignored this issue. Accuracy metrics that aggregate over all classes can give an inflated view of model quality when rare classes are poorly predicted. The only prior PPM work addressing this (Mehdiyev et al.) frames it as a binary problem, which is unsuitable for multi-class next activity prediction.^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:84-98]

## Task Definition

Next activity prediction is defined formally as: given a prefix $hd_k(\sigma_c) = \langle e_1, \ldots, e_k \rangle$ of a case trace, predict the activity label $\pi_A(e_{k+1})$ of the next event. This is a multi-class classification problem where each class corresponds to a possible activity label in the set $A$.

Event logs record process executions as traces of events $e = (a, t, c, d_1, \ldots, d_m)$, where $a$ is the activity label, $t$ is the timestamp, $c$ is the case ID, and $d_i$ are optional attributes. This formalism is consistent with standard [[process-mining-handbook|process mining]] event log definitions.

## Cross-Entropy Loss and Its Limitations

The conventional loss function for next activity prediction is cross-entropy loss (CEL):

$$L_{\text{CEL}} = -\log(\hat{p}_{i,a_i})$$

where $\hat{p}_{i,a_i}$ is the predicted softmax probability for the true activity label $a_i$. CEL weights all training instances equally, so majority classes — contributing more instances — dominate gradient updates, reducing the model's attention to minority classes.^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:104-112]

## Class-Balanced Focal Loss (CBFL)

CBFL extends CEL with two additional weighting terms:

$$L_{\text{CBFL}} = -\frac{1-\beta}{1-\beta^{n_{a_i}}} (1 - \hat{p}_{i,a_i})^\gamma \log(\hat{p}_{i,a_i})$$

where $n_{a_i}$ is the number of training instances in class $a_i$, $\beta \in [0,1)$ controls class-level smoothing, and $\gamma \in [0, \infty)$ controls instance-level down-weighting.^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:55-64]

### Class-Level Weighting (Class-Balanced Term)

The CB term $\frac{1-\beta}{1-\beta^{n_{a_i}}}$ assigns higher weights to infrequent classes in a smoother manner than naive inverse frequency weighting. It narrows the weight gap between the most and least frequent classes, reducing the risk of overfitting on very rare classes. The degree of smoothing is controlled by $\beta$: as $\beta$ increases, smoothing decreases.

### Instance-Level Weighting (Focal Term)

The focal term $(1 - \hat{p}_{i,a_i})^\gamma$ dynamically down-weights well-classified instances (high predicted probability for the true class) and emphasizes harder instances. This adapts during training as predicted probabilities are updated each epoch. Instance-level weighting complements class-level weighting because classes with similar frequencies can still vary in predictive difficulty.^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:55-64]

## Empirical Evaluation

### Datasets

Experiments were conducted on four real-life event logs:

| Event Log | Cases | Events | Activities | Max/Min Class Freq. | Majority % |
|-----------|-------|--------|------------|---------------------|------------|
| BPIC2017 | 28,977 | 1,067,714 | 25 | 117,543 / 173 | 63.58% |
| BPIC2019 | 169,142 | 907,557 | 36 | 100,530 / 1 | 95.63% |
| BPIC2020 | 5,753 | 29,902 | 17 | 3,570 / 1 | 73.48% |
| BAC | 362,506 | 1,964,221 | 57 | 231,869 / 1 | 89.35% |

Majority classes are defined as those with frequencies above the 75th percentile.^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:24-27]

### Architectures

Four model architectures were evaluated with both CEL and CBFL:
- **XGBoost** — traditional ML baseline (CBFL applied without focal term, as XGBoost inherently emphasizes difficult instances)
- **LSTM** — most commonly used sequence model in PPM
- **Transformer** — strong alternative for sequential modeling
- **xLSTM** — novel architecture, first examined in the PPM context in this work; motivated by superior rare token prediction in language modeling^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:60-64]

### Feature Encoding

Features include one-hot encoded (XGBoost) or embedded (DL) activity labels, plus two temporal features: time since previous event and time since trace start, both log-transformed and min-max normalized. Prefix-based encoding is used for XGBoost; trace-based many-to-many encoding for DL models.

### Results

CBFL substantially improves overall macro-averaged F1-score in most settings:

- **XGBoost, LSTM, xLSTM**: statistically significant F1 improvements on 3 of 4 datasets (BPIC2019 being the exception)
- **Transformer**: significant improvement on BPIC2020; no significant difference on other datasets
- **Minority classes**: consistent recall improvements across all datasets and architectures; F1 gains on 3 of 4 datasets
- **Majority classes**: F1-scores largely unaffected; CBFL also improves majority class precision, suggesting that better sensitivity to minority classes reduces false positives for majority classes^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:24-27]

Hyperparameter tuning shows that model performance is more sensitive to $\beta$ than $\gamma$, and that a well-tuned CB term always outperforms naive inverse frequency weighting.

## Relation to Broader PPM Research

This work addresses a gap in the [[narrative-based-predictive-process-monitoring-llm|PPM]] literature by providing a principled, multi-class-compatible solution to class imbalance. It complements research on [[actor-enriched-throughput-time-forecasting|throughput time forecasting]] and other PPM tasks by improving the reliability of next activity predictions for rare but business-critical process behaviors. The [[data-quality-sensitivity-process-discovery|data quality]] of event logs — including skewed distributions — is a recognized challenge across process mining tasks.^[He et al - Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss.pdf:44-50]

## Code and Reproducibility

The implementation is publicly available at: [https://github.com/Xiaomeng-He/CBFL](https://github.com/Xiaomeng-He/CBFL)

## References

- He, X., Oyamada, R., De Smedt, J., vanden Broucke, S., De Weerdt, J. (2025). *Tackling Multi-Class Imbalance in Next Activity Prediction with Class-Balanced Focal Loss*. ICPM 2025 International Workshops, Springer LNBIP.

## Key Data

- Aneventcanbedefinedasatuple e=(a,t,c,d1,...,dm),where a∈Aistheactivitylabel( A
- LCEL=−log(ˆpi,ai) (1)
- LCBFL=− 1−β
- p = 0.002 p = 0.002 p = 0.002 p = 0.002
- p = 0.002 p = 0.004 p = 0.006 p = 0.004
- p = 0.160 p = 0.105 p = 0.002 p = 0.557
- p = 0.010 p = 0.131 p = 0.002 p = 0.013

## Стратегии кодирования признаков

Репозиторий проекта раскрывает детали выбора стратегий кодирования, которые сравнивались на валидационной выборке по макро-усреднённому F1-показателю. Для модели XGBoost в качестве основной стратегии используется **prefix-based index encoding** (кодирование на основе индекса префикса), а в качестве альтернативы — prefix-based aggregation encoding (агрегационное кодирование префиксов), широко применяемое в предшествующих работах. Для моделей глубокого обучения (LSTM, Transformer, xLSTM) основной стратегией служит **trace-based encoding** (кодирование на основе трасс), а альтернативой — prefix-based index encoding.^[CBFL:97-101]

Результаты сравнения на четырёх наборах данных (BPIC2017, BPIC2019, BPIC2020, BAC) показывают, что выбранные стратегии работают на уровне альтернатив или превосходят их, что обосновывает сделанный выбор. Наиболее заметное преимущество наблюдается для XGBoost на наборах BPIC2017 (+3,6 п.п.) и BPIC2019 (+4,9 п.п.).^[CBFL:102-119]

## Расширенные метрики производительности

Помимо макро-усреднённого F1-показателя, репозиторий публикует полную таблицу результатов, включающую **площадь под кривой точность–полнота (AUC-PR)**, точность (Accuracy), прецизионность (Precision) и полноту (Recall) — все в виде макро-средних по всем классам активностей.^[CBFL:92-93]

Ключевые наблюдения из расширенной таблицы:

- **Базовая линия (Cross-Entropy Loss)** демонстрирует более высокую точность (Accuracy) на большинстве наборов данных, поскольку оптимизируется под доминирующие классы.
- **CBFL** систематически повышает показатель полноты (Recall) для всех архитектур и наборов данных, что подтверждает его способность улучшать предсказание миноритарных классов активностей.
- На наборе BPIC2020 применение CBFL заметно снижает точность (Accuracy) при одновременном росте Precision и Recall, что отражает компромисс между общей точностью и сбалансированностью по классам.
- Показатель AUC-PR варьируется в зависимости от архитектуры и набора данных; ни одна из конфигураций не доминирует по всем метрикам одновременно.

## Реализация и структура репозитория

Репозиторий `Xiaomeng-He/CBFL` на GitHub реализован на **Python 3.12.7** и организован следующим образом:

- **`preprocessing/`** — скрипты предобработки данных: `preprocessing.py` (очистка и подготовка данных), `train_test_split.py` (разбивка на обучающую, валидационную и тестовую выборки), `create_trace_prefix.py` (генерация трасс для trace-based encoding, а также префиксов и следующих активностей для prefix-based encoding).
- **`models/`** — реализации всех архитектур: `create_dl_model.py` определяет модели LSTM, Transformer и [[domain-adaptation-llms-process-mining-peft|xLSTM]]; `xgboost.ipynb` реализует модель XGBoost.
- **`train_evaluate/`** — функции обучения и оценки: `loss_function.py` содержит реализации Cross-Entropy Loss (CEL), Class-Balanced Focal Loss (CBFL) и взвешивания по обратной частоте; `train_evaluate.py` — процедуры обучения, валидации и тестирования.

Для воспроизведения экспериментов достаточно установить зависимости командой `pip install -r requirements.txt`.^[CBFL:57-78]
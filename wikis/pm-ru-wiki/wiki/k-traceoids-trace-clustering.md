---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:56:42'
lint_warnings:
- claim: вместо числовых центроидов в качестве представителей кластеров используются
    процессные модели. Это позволяет работать непосредственно с трассами, не прибегая
    к их векторному кодированию.
  concern: The comparison to k-means is misleading here. The closer analogy would
    be k-medoids (PAM), not k-means, since k-traceoids uses representative objects/models
    per cluster rather than computed mean centroids. The page itself names the algorithm
    'k-traceoids' (echoing 'medoids'), yet frames the novelty as a departure from
    k-means rather than acknowledging the more direct relationship to k-medoids, potentially
    overstating the originality of the core idea.
- claim: большинство из них преобразуют трассы в числовые векторы (one-hot encoding,
    н-граммы, обученные эмбеддинги). Такое преобразование неизбежно ведёт к потере
    информации о порядке активностей
  concern: The claim that vectorization 'inevitably' leads to loss of ordering information
    is overstated. N-gram encodings explicitly capture local sequential order, and
    sequence embeddings (e.g., LSTM-based or transformer-based) are specifically designed
    to preserve ordering information. Characterizing all such approaches as necessarily
    losing order is inaccurate.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Kanilmaz et al - Introducing
    k-traceoids A Structure-Preserving Trace Clustering Framework.pdf
  hash: 5725c9b1df4615f4b0d3f7d20ab5668dd5906f431e5e5b0757732bcd7f67ede0
  ingested: '2026-07-14T20:56:42'
  size: 3577261
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
- activity ordering
- anomaly detection
title: 'k-traceoids: Структурно-сохраняющий фреймворк кластеризации трасс'
type: technology
---

# k-traceoids: Структурно-сохраняющий фреймворк кластеризации трасс

**k-traceoids** — алгоритм кластеризации трасс для [[process-mining-overview]], предложенный Умутом Нефтой Канилмазом, Габриэлем Маркесом Тавареcом, Даниэлем Шустером (LMU Munich / Munich Center for Machine Learning), Рафаэлем Сейди Оямадой (KU Leuven) и Томасом Зайдлем (LMU Munich). Работа принята к представлению на воркшопах ICPM 2025 и выйдет в серии Springer LNBIP.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:1-7]

## Мотивация и проблематика

Событийные данные реальных процессов отличаются высокой сложностью и разнообразием: трассы, порождённые одним и тем же процессом, могут существенно различаться из-за большого числа вариантов исполнения. Кластеризация трасс позволяет разбить журнал событий на более однородные подмножества, упрощая последующий анализ — в частности, обнаружение процессов и выявление аномалий.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:8-31]

Основная проблема существующих подходов состоит в том, что большинство из них преобразуют трассы в числовые векторы (one-hot encoding, n-граммы, обученные эмбеддинги). Такое преобразование неизбежно ведёт к потере информации о порядке активностей — ключевой структурной характеристике трасс. Это ограничивает качество последующих задач, включая [[class-balanced-focal-loss-next-activity-prediction|предсказание следующей активности]] и предиктивный мониторинг процессов.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:32-35]

## Описание фреймворка

k-traceoids вдохновлён алгоритмом k-means, однако принципиально отличается от него: вместо числовых центроидов в качестве представителей кластеров используются **процессные модели**. Это позволяет работать непосредственно с трассами, не прибегая к их векторному кодированию.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:36-43]

### Основные концепции

| Категория | k-traceoids | k-means |
|---|---|---|
| Тип данных | Трассы | Числовые векторы |
| Начальное назначение | Балансировка по размеру варианта | Случайный выбор k центроидов |
| Представление кластера | Процессная модель | Центроид кластера |
| Мера расстояния | Соответствие трассы модели (fitness) | Расстояние до центроида |
| Шаг переназначения | Трасса → кластер с наилучшей моделью | Точка → ближайший центроид |
| Критерий сходимости | Стабильность назначений трасс | Стабильность точек и центроидов |

### Алгоритм

Фреймворк включает три основных шага:^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:83-90]

1. **Инициализация.** Задаётся число кластеров *k* и максимальное число итераций. Трассы группируются по вариантам, варианты распределяются по кластерам с балансировкой числа трасс.
2. **Вычисление модели.** Для каждого кластера по входящим в него трассам строится процессная модель — «центроид» кластера. В качестве модели может выступать любое описание группы трасс: процессная модель, наиболее частый вариант, супервариант и др.
3. **Переназначение трасс.** Для каждой трассы вычисляется её соответствие (fitness) каждой из *k* моделей; трасса переназначается в кластер с наилучшей моделью. Трассы одного варианта всегда остаются в одном кластере.

Шаги 2 и 3 повторяются до достижения сходимости: либо назначения трасс не меняются между итерациями, либо достигается максимальное число итераций.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:106-120]

## Связанные подходы

Методы кластеризации трасс традиционно делятся на **дистанционные** (distance-based) и **основанные на процессных моделях** (process model-based).^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:52-53]

- **ActiTrac** использует активное обучение и процессные модели для определения принадлежности трасс кластерам, однако формирует кластеры последовательно, по одному, что может влиять на стабильность. k-traceoids генерирует все кластеры одновременно.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:60-69]
- **Энтропийная кластеризация** (Peeperkorn et al., 2025) минимизирует оценки энтропийной релевантности на DFG-моделях, будучи жёстко привязана к этому типу моделей. k-traceoids предлагает большую гибкость в выборе типа модели и меры расстояния.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:70-73]
- Дистанционные методы (DBSCAN, k-means на векторах) теряют информацию о порядке активностей при кодировании трасс.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:54-59]

k-traceoids также связан с задачами [[data-quality-sensitivity-process-discovery|обнаружения процессов]] и [[object-centric-distance-metric|метриками расстояния в майнинге процессов]].

## Экспериментальная оценка

### Настройка эксперимента

Эксперименты проводились на широко используемом журнале событий **Road Traffic Fine Management (RTFM)**. Гиперпараметры:^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]

- *k* (число кластеров): от 2 до 10
- *m* (алгоритм обнаружения процессов для центроида): Inductive Miner — infrequent (IMF) и Heuristic Miner (HM)
- *c* (метод проверки соответствия): Token Based Replay (TBR) и Alignment-Based Fitness (ALB)

Максимальное число итераций — 100; для ALB введён таймаут 10 минут с присвоением нулевого fitness при превышении.

### Качественная оценка

Для конфигурации k=4, IMF, ALB алгоритм выделил четыре содержательно различных кластера:^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]

- **Кластер A** — трассы с циклами по активности *Payment* и *Add Penalty*, существенно различающиеся по длине.
- **Кластер B** — трассы с долгосрочными зависимостями и вариациями двух активностей (*Add Penalty*, *Appeal to Judge*).
- **Кластер C** — трассы с простым повторением одной активности (*Payment*).
- **Кластер D** — короткие линейные исполнения процесса.

### Количественная оценка

- **Энтропия Шеннона** назначений кластеров в большинстве конфигураций превышает 0,8, что свидетельствует о сбалансированном распределении трасс. Комбинация IMF+TBR при больших *k* демонстрирует более низкую энтропию.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]
- **Fitness** трасс к моделям высок во всех конфигурациях; во многих случаях равен 1, что указывает на содержательность кластеров.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]
- **Точность (precision)** моделей HM стабильно равна 1 (возможное переобучение), тогда как IMF+TBR показывает более сбалансированные значения.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]
- **Сходимость**: IMF+ALB сходится быстрее при малых *k*; конфигурации с TBR чаще достигают максимального числа итераций. При k=10 большинство конфигураций достигают ~98% стабильности после 20 итераций.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]
- **Время выполнения** растёт приблизительно линейно с увеличением *k*.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:44-50]

## Выводы и перспективы

k-traceoids представляет собой гибкий и эффективный фреймворк кластеризации трасс, сохраняющий структурные характеристики событийных данных и избегающий потерь информации, характерных для векторных представлений. Фреймворк допускает широкую параметризацию: выбор алгоритма обнаружения процессов и метода проверки соответствия позволяет адаптировать его к разнообразным наборам данных. Исходный код и результаты экспериментов доступны в публичном репозитории на GitHub.^[Kanilmaz et al - Introducing k-traceoids A Structure-Preserving Trace Clustering Framework.pdf:19-22]

Перспективные направления включают оценку на более крупных и разнородных журналах событий, исследование критериев ранней остановки (например, при достижении заданного процента стабильных трасс), а также изучение причин быстрой сходимости IMF+ALB при малых значениях *k*.
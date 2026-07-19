---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:04:45'
lint_warnings:
- claim: представлен на воркшопах ICPM 2025
  concern: ICPM 2025 has not yet taken place as of the knowledge cutoff (early 2025),
    making it impossible to confirm this paper was presented there. This appears to
    be a future or unverified event stated as fact.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Bertrand et al - A framework
    for measuring data quality sensitivity in process discovery.pdf
  hash: ce1349c22b55d33e276a09dd11db1ead412401d41fab7ac009a76651040d2529
  ingested: '2026-07-14T20:04:45'
  size: 641997
  truncated: true
status: active
tags:
- process discovery
- data quality
- sensitivity analysis
- event logs
- business processes
- data quality issues
- process models
- missing events
- concept drift
- pipeline
title: Оценка чувствительности майнинга процессов к проблемам качества данных
type: concept
---

# Оценка чувствительности майнинга процессов к проблемам качества данных

Оценка чувствительности алгоритмов обнаружения процессов к проблемам качества данных (Data Quality Issues, DQI) — направление в [[process-mining-overview]], изучающее, как ошибки и несоответствия в журналах событий влияют на качество моделей бизнес-процессов, порождаемых алгоритмами обнаружения процессов. Систематический фреймворк для такой оценки предложен Яннисом Бертраном, Мартином Кабьерски, Яри Пиперкорном и Сеппе Ванден Брукке (Гентский университет, Венский университет, KU Leuven) и представлен на воркшопах ICPM 2025.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:3-11]

## Контекст и мотивация

Алгоритмы обнаружения процессов — такие как α-Miner, Inductive Miner, Declare Miner и Split Miner — строят модели бизнес-процессов на основе журналов событий. Они предполагают, что журналы корректны и полны. Однако реальные журналы событий часто содержат DQI: пропущенные события, некорректные метки активностей, неточные временны́е метки и посторонние события. Несмотря на широкое признание негативного влияния DQI на майнинг процессов, систематическое количественное исследование этого влияния до появления данной работы практически отсутствовало.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:28-49]

Авторы соотносят свою работу с двумя ключевыми вызовами, сформулированными в исследовательской повестке по качеству данных в майнинге процессов:^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:37-49]
- **C14**: какие измерения качества данных наиболее важны для майнинга процессов и для его конкретных подзадач?
- **C15**: как наилучшим образом продемонстрировать, каким образом проблемы качества данных повлияли на аналитические результаты?

## Формальные определения

Фреймворк опирается на стандартные определения [[process-mining-overview|майнинга процессов]]:^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:70-81]

- **Событие** (event): кортеж *e = (a ∈ A, c ∈ C, t ∈ T)*, где *A* — множество активностей, *C* — идентификаторы случаев, *T* — временны́е метки.
- **Трасса** (trace): непустая последовательность событий с одним идентификатором случая, упорядоченная по временны́м меткам.
- **Журнал событий** (event log): конечное множество трасс.

## Архитектура фреймворка

Фреймворк реализован в виде модульного конвейера на Python (открытый исходный код на GitHub). Он принимает четыре входных параметра:^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:50-59]
1. Журнал событий для анализа.
2. Список DQI с параметрами (например, доля затронутых событий).
3. Набор алгоритмов обнаружения процессов и их настройки.
4. Набор метрик проверки соответствия (conformance checking) для оценки качества моделей.

### Шаг 1. Формирование чистого журнала (опционально)

Для контролируемых экспериментов из исходного журнала удаляются трассы, не соответствующие модели, обнаруженной алгоритмом Inductive Miner Infrequent (IMf, порог 0,2). Полученный «чистый журнал» служит отправной точкой перед искусственным внесением DQI.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:50-59]

### Шаг 2. Внедрение проблем качества данных

Концептуально определяется функция-«загрязнитель» *P : L → L*, систематически применяющая изменения к журналу событий. Реализованы следующие атомарные DQI:^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:107-117]

| DQI | Описание | Класс реализации |
|---|---|---|
| Пропущенные события | Случайное удаление заданного процента событий | `DeleteActivityPolluter` |
| Некорректные временны́е метки | Добавление случайной задержки (распределение Гамма) | `DelayedEventLoggingPolluter` |
| Неточные метки активностей | Слияние нескольких детальных меток в одну обобщённую | `ImpreciseActivityPolluter` |
| Неточные временны́е метки | Агрегация меток до грубого уровня (минута, час, день) | `AggregatedEventLoggingPolluter` |
| Посторонние события | Вставка событий с «чужой» меткой активности | `InsertAlienActivityPolluter` |

### Шаг 3. Применение алгоритма обнаружения

Алгоритм обнаружения применяется как к чистому, так и к загрязнённому журналу, порождая «чистую модель» и «загрязнённую модель» соответственно. Фреймворк не зависит от конкретного алгоритма.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:50-59]

### Шаг 4. Оценка моделей

Качество моделей измеряется метриками проверки соответствия по четырём измерениям: **полнота** (fitness), **точность** (precision), **обобщаемость** (generalisation) и **простота** (simplicity). Фреймворк поддерживает воспроизведение на основе токенов и выравнивание (alignment-based conformance checking). Четыре комбинации журнал–модель позволяют изолировать влияние DQI на алгоритм обнаружения от влияния на алгоритм проверки соответствия.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:95-105]

## Экспериментальная валидация

Фреймворк применён к четырём публично доступным журналам событий: Road Traffic Fines Management, Sepsis Cases, Helpdesk и Hospital Billing. Тестировались алгоритмы α-Miner, Inductive Miner (IM, пороги 0,0 и 0,2) и ILP Miner (пороги 1,0 и 0,8). Уровень загрязнения варьировался от 10% до 90% с шагом 10%.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:57-59]

### Основные результаты

- **Полнота** (fitness) остаётся относительно стабильной при большинстве DQI: ILP (порог 0,8) и IM без фильтрации демонстрируют наибольшую устойчивость; α-Miner наиболее чувствителен к шуму.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:57-59]
- **Точность** (precision) страдает значительно сильнее: все алгоритмы показывают снижение точности при большинстве DQI. ILP (0,8) и IM (0,2) в целом превосходят остальные алгоритмы.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:57-59]
- **Временны́е DQI** (неточные метки) оказывают минимальное влияние на полноту и точность.
- **Структурные DQI** (удаление и вставка событий) существенно снижают качество модели.
- **Неточные метки активностей** дают неоднозначный эффект: иногда снижают полноту, но повышают точность за счёт упрощения модели.
- Даже небольшой уровень загрязнения (~10%) может резко снизить качество модели, после чего наступает плато — это указывает на высокую чувствительность алгоритмов к самому факту наличия DQI.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:57-59]

## Ограничения и направления будущих исследований

- Метрики качества модели оцениваются относительно журнала событий, а не истинной модели процесса, что затрудняет однозначную интерпретацию результатов.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:60-65]
- В экспериментах рассматривались только изолированные DQI; совместное влияние нескольких DQI остаётся предметом будущих исследований.
- Планируется расширение фреймворка: поддержка дополнительных паттернов загрязнения, крупномасштабный бенчмарк со статистическими тестами, оценка чувствительности других задач майнинга процессов (проверка соответствия, предиктивный мониторинг), а также интеграция с языком FLAWD для описания паттернов загрязнения.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:60-65]

## Связь с другими направлениями

Фреймворк дополняет исследования по [[process-mining-overview|майнингу процессов]] в части оценки зрелости алгоритмов обнаружения и оценки на основе знания истинной модели. Стохастическая проверка соответствия рассматривается как перспективный инструмент для анализа влияния DQI на распределения меток активностей. Качество журнала событий тесно связано с полнотой журнала как опосредующим фактором между качеством данных и результатами обнаружения процессов.^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:60-65]
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:47:03'
lint_warnings:
- claim: опубликованный в рамках ICPM 2025 Workshops
  concern: ICPM 2025 has not yet taken place as of the knowledge cutoff (early 2025),
    making it impossible to confirm this publication venue. The paper may be a preprint
    or submitted work, and claiming it is 'published' at a future workshop is premature
    and potentially inaccurate.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Kourani et al - Revealing
    Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf
  hash: 4905eff9b9ae11c0b94fb06cbb29cf0a0587d4dac944a3d1c4a691d03773dba2
  ingested: '2026-07-14T20:47:03'
  size: 767307
  truncated: true
status: active
tags:
- process mining
- process discovery
- partial orders
- concurrency
- event logs
- scalability
- hierarchical algorithm
- timestamp abstraction
- workflow modeling
- LNBIP
title: Обнаружение процессов на основе частичных порядков с использованием POWL
type: technology
---

# Обнаружение процессов на основе частичных порядков с использованием POWL

Обнаружение процессов на основе частичных порядков — направление в [[process-mining-overview]], нацеленное на преодоление ключевого ограничения традиционных алгоритмов: принудительной линеаризации событий, скрывающей истинный параллелизм реальных процессов. Работа Хумама Курани, Гюнама Парка и Вила ван дер Aalst (Fraunhofer FIT и RWTH Aachen University) представляет масштабируемый алгоритм, напрямую использующий частичные порядки при обнаружении процессов и опубликованный в рамках ICPM 2025 Workshops.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:1-20]

## Проблема линеаризации событий

Традиционные методы [[process-mining-overview|майнинга процессов]] предполагают, что каждый экземпляр процесса представляет собой строгую последовательность активностей (например, ⟨a, b, c⟩). Это противоречит реальности сложных процессов, в которых активности часто выполняются параллельно или перекрываются во времени. Информационные системы нередко фиксируют интервальные данные (временны́е метки начала и завершения), однако традиционные методы отбрасывают эту информацию, выбирая единственную метку и теряя сведения об истинной семантике выполнения.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:26-32]

Дополнительные источники проблемы:
- события могут иметь одинаковые временны́е метки, что само по себе указывает на отсутствие строгой последовательной зависимости;
- зафиксированные метки могут быть ненадёжными или иметь разную гранулярность;
- в таких областях, как здравоохранение, задержки ручного ввода данных приводят к расхождению между реальным временем события и временем его записи.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:32-38]

В подобных случаях необходима абстракция временны́х меток до более грубого уровня (час, день или бизнес-период), что естественным образом раскрывает лежащие в основе частичные порядки.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:38-39]

## Язык POWL (Partially Ordered Workflow Language)

Алгоритм опирается на **POWL** — иерархический язык моделирования процессов, в котором подмодели объединяются в более крупные либо как частичные порядки, либо с помощью операторов управления потоком:
- **×** — исключающий выбор (XOR);
- **⟲** — повторяющееся поведение (цикл).

Ключевое свойство POWL: модели **корректны по построению** (sound by construction) — они транслируются в сети Петри, свободные от тупиков и других структурных проблем. Частичные порядки являются фундаментальным конструктом языка, что делает POWL идеальным инструментом для обнаружения процессов из частично упорядоченных данных.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:56-64]

## Преобразование журнала событий в частичные порядки

### Интервальный журнал событий

Исходный журнал событий преобразуется в **интервальный журнал событий** (interval event log, *L*_int), где каждое событие представлено кортежем *(a, c, st, et)*: метка активности *a*, идентификатор случая *c*, время начала *st* и время завершения *et* (при *st ≤ et*). Если информация о жизненном цикле отсутствует, создаются атомарные интервальные события с одинаковыми метками начала и конца.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:113-118]

### Частично упорядоченный след (POT)

Для каждого случая *c* строится **частично упорядоченный след** (Partially Ordered Trace, POT) — пара *(V_c, ≺_c)*, где:
- *V_c* — множество переходов, по одному на каждое интервальное событие;
- *t_i ≺_c t_j* тогда и только тогда, когда событие *e_i* завершается строго до начала *e_j*.

Это определение естественным образом обрабатывает параллелизм: активности с перекрывающимися интервалами выполнения не имеют отношения предшествования между собой. Отношение ≺_c является строгим частичным порядком (иррефлексивным и транзитивным).^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:109-112]

### Частично упорядоченный журнал событий

Мультимножество всех POT, полученных из *L*_int, образует **частично упорядоченный журнал событий** *L*_PO, который служит непосредственным входом для алгоритма обнаружения POWL.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:65-70]

## Алгоритм обнаружения POWL из частичных порядков

Алгоритм является рекурсивным и включает пять шагов.

### Шаг 1: Обнаружение XOR-ветвей

Алгоритм выявляет **максимальные группы конфликтов** — разбиения множества активностей, в которых каждая пара активностей из разных частей никогда не встречается совместно в одном экземпляре процесса. Для каждой ветви рекурсивно строится подмодель, все ветви объединяются оператором ×.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:65-70]

### Шаг 2: Группировка по совместному появлению

Алгоритм строит **разбиение по совместному появлению** (co-occurrence partitioning): два узла совместно появляются, если они присутствуют или отсутствуют одновременно во всех частичных порядках. Для каждой группы рекурсивно строится подмодель POWL.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:65-70]

### Шаг 3: Обнаружение циклов

Множество узлов разбивается на **классы эквивалентности POWL**: если класс содержит более одного экземпляра семантически идентичной подмодели, все экземпляры заменяются конструкцией цикла ⟲(ψ, τ).^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:65-70]

### Шаг 4: Обнаружение пропусков (Skip Mining)

Для каждого узла ψ, отсутствующего хотя бы в одном частичном порядке, он заменяется конструкцией ×(ψ, τ), допускающей его пропуск.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:65-70]

### Шаг 5: Агрегация частичных порядков

Оставшиеся узлы объединяются в единый агрегированный частичный порядок функцией **CombineOrders**:
1. **Базовое отношение предшествования**: фиксирует зависимости, присутствующие хотя бы в одном частичном порядке и не противоречащие ни одному другому.
2. **Расширенное отношение предшествования**: осторожно расширяет базовое по транзитивности, не вводя противоречий.
3. **Транзитивное агрегированное отношение**: применяет функцию Prune для устранения нарушений транзитивности.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:65-70]

## Гарантии корректности и полноты

- **Корректность по построению (Soundness)**: все модели POWL по определению свободны от тупиков и структурных дефектов.
- **Идеальная полнота (Perfect Fitness)**: любая последовательность активностей, являющаяся допустимой линеаризацией любого POT из входного мультимножества, воспроизводима обнаруженной моделью POWL. Это обеспечивается консервативной агрегацией порядков (шаг 5) и обработкой опциональности (шаг 4).^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:14-20]

## Реализация и оценка

Алгоритм реализован в Python-библиотеке `powl` (устанавливается командой `pip install powl`) и доступен через веб-приложение для демонстрации.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:17-18]

Эксперимент проводился на двух широко известных реальных журналах событий: **BPI Challenge 2012** и **BPI Challenge 2017**. Для каждого журнала создавались варианты с фильтрацией по 4, 6, 8 и 12 наиболее частым активностям, а также использовались полные журналы.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:17-20]

Для сравнения выбраны два современных метода: **Zebra Miner** и **eST2 Miner**. Установлен таймаут в один час на каждый запуск обнаружения. Качество моделей измерялось стандартными метриками **fitness** и **precision** на основе выравнивания (alignment-based), вычисленными с помощью PM4Py.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:97-100]

### Результаты

| Журнал событий | POWL Miner (время, сек) | eST2 Miner (время, сек) |
|---|---|---|
| BPIC 2012, 4 активности | 8 | 145 |
| BPIC 2012, 6 активностей | 12 | 799 |
| BPIC 2012, 8 активностей | 13 | 2683 |
| BPIC 2012, 12 активностей | 19 | Таймаут |
| BPIC 2012, полный (24) | 25 | Таймаут |
| BPIC 2017, полный (26) | 41 | Таймаут |

- **Zebra Miner** достиг таймаута на всех вариантах журналов.
- Оба метода (POWL Miner и eST2 Miner) достигли идеальной полноты на всех журналах.
- По **точности (precision)** POWL Miner стабильно превосходил eST2 Miner, что свидетельствует о менее чрезмерно обобщённом представлении процесса.
- POWL Miner успешно обработал все варианты журналов; самая длительная задача заняла 42 секунды для полного журнала BPIC 2017.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:97-100]

## Связанные подходы

Среди существующих методов, работающих с частично упорядоченными данными:
- **Inductive Miner** с данными жизненного цикла — различает параллелизм и последовательное чередование;
- **Split Miner** — обнаруживает перекрывающиеся интервалы выполнения;
- **Prime Miner** — использует простые структуры событий и синтез сетей Петри методом регионов;
- **Multi-Phase Miner** — агрегирует графы экземпляров в модели высокого уровня;
- **eST2 Miner** — комбинирует воспроизведение трасс с синтезом сетей Петри из частичных порядков;
- **ILP2 Miner** — применяет целочисленное линейное программирование;
- **Zebra Miner** — использует инкрементальную технику на основе регионов.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:76-96]

Основное преимущество предложенного подхода перед методами синтеза (на основе регионов или ILP) — значительно лучшая масштабируемость на больших и сложных журналах событий.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:97-100]

## Направления дальнейших исследований

Авторы указывают на необходимость разработки механизмов фильтрации шума для абстрагирования от редких или исключительных поведений, что позволит повысить практическую применимость алгоритма в условиях зашумлённых реальных данных.^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:17-20]

## Key Data

- P = {X1, . . . , Xn} such that X = X1 ∪ · · · ∪Xn, Xi ̸= ∅
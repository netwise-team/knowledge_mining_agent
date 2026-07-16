---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:44:39'
orphan: false
resource: https://github.com/loeseke/object-centric-streaming-discovery
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Liss et al - Object-Centric
    Streaming-Based Process Discovery.pdf
  hash: 1dab96c17fc7e9fabab63d1efe2032e4f2678dd9ae1f5839dd88783ee0bbb63d
  ingested: '2026-07-14T07:44:39'
  size: 533258
  truncated: true
- file: https://github.com/loeseke/object-centric-streaming-discovery
  hash: 971e5e340220373ce7214dd8f8da143b05fcee7d461c12df6287910bfdf8a7d5
  ingested: '2026-07-16'
  size: 61
status: active
tags:
- process mining
- object-centric
- streaming
- process discovery
- scalability
- event logs
- Petri nets
- online analysis
- directly-follows graph
- cache management
title: Object-Centric Streaming-Based Process Discovery (Liss et al.)
type: technology
updated: '2026-07-16'
---

# Object-Centric Streaming-Based Process Discovery (Liss et al.)

This work, authored by **Lukas Liss**, **Nina Löseke**, and **Wil M. P. van der Aalst** (RWTH Aachen University), proposes the first streaming framework for [[streaming-object-centric-process-mining|object-centric process discovery]] from continuous, unbounded event streams. It was accepted at the ICPM 2025 Workshops (Springer LNBIP series) and is available as a pre-print with a publicly accessible Python implementation on GitHub. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:1-40]

## Motivation

Traditional [[process-mining-data-science-in-action|process mining]] focuses on case-centric event logs where each case evolves in isolation. [[object-centric-distance-metric|Object-centric process mining]] addresses real-world processes where multiple interrelated objects participate in shared events. However, object-centric event data — including events, object-to-object (O2O) relations, and object attributes — produces significantly larger data volumes than case-centric logs, making offline, single-file analysis infeasible at scale. Existing streaming process mining approaches (e.g., S-BAR, StrProM) are restricted to traditional, case-centric settings. This work bridges the gap by enabling online discovery of object-centric process models under memory constraints. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:6-116]

## Contributions

The paper makes five main contributions:

1. **Object-centric event stream definition** — A formal definition of potentially infinite streams of timestamped stream items, each containing events, O2O updates, and object-attribute changes, conforming to the OCEL 2.0 and OCED standards.
2. **Intermediate model buffers** — Six fixed-size buffers that capture relevant process behavior without storing the full log: object buffer, arc buffer, event-activity buffer, temporal-relation buffer, log-cardinality buffer, and event-cardinality buffer.
3. **Cache replacement strategies** — Support for FIFO, Random Replacement (RR), LFU, LFU-DA, and LRU policies to manage buffer eviction under memory constraints.
4. **Object-centric priority policies** — Optional policies that weight replacement decisions by object or object-type characteristics (stride, lifespan, objects per event, objects per type, events per type, or custom rankings), compensating for unbalanced object-type distributions in buffers.
5. **Adapted discovery algorithms** — Streaming variants of three prominent object-centric process models: Object-Centric Directly-Follows Graphs (OC-DFG), Object-Centric Petri Nets (OCPN), and Temporal Object Type Models (TOTeM). ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:69-77]

## Object-Centric Event Streams

An object-centric event stream is a possibly infinite, partially time-ordered sequence of stream items. Each item is a tuple `(timestamp, events, O2O_updates, object_attribute_updates)`. Multiple events or updates can occur concurrently within one stream item. Unlike case-centric streaming frameworks, this formalization incorporates concrete timestamps, which serve as input for model annotation and cache-replacement policies. The framework supports transformation of OCEL 2.0 event logs into object-centric event streams. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:55-63]

## Streaming Framework Architecture

The framework uses six model buffers as intermediate representations:

- **Object buffer**: Tracks each object's type, last-seen activity, and last-seen timestamp. Used for OC-DFG and OCPN discovery.
- **Arc buffer**: Records directly-follows relations per object (and object type), with target-activity frequency and arc duration. Frequencies are computed as `1 / number of objects in event` to avoid the convergence issue common in case-centric approaches.
- **Event-activity buffer**: Records, for each activity and object type, whether multiple objects of that type were involved — used to assign variable arcs in OCPNs.
- **Temporal-relation buffer**: Stores first-seen and last-seen timestamps per object, enabling computation of temporal relations (during, during-inverse, precedes, precedes-inverse, parallel) for TOTeM.
- **Log-cardinality buffer**: Records connected object pairs (from events and O2O updates) to compute log cardinalities for TOTeM arcs.
- **Event-cardinality buffer**: Stores allowed event cardinalities per directed object-type pair per event, used to derive TOTeM event cardinalities via minimum support thresholds.

Buffers can be configured as mixed (all object types together) or type-specific (separate buffer per object type). Optional **buffer synchronization** removes entries for objects or object types absent from any buffer, ensuring consistency and optimal memory use. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:55-116]

## Supported Process Models

### Object-Centric Directly-Follows Graph (OC-DFG)
Nodes represent activities; arcs are typed by object type and annotated with frequencies and durations. Computed by grouping arc-buffer entries by object type, summing frequencies, and averaging durations. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:73-94]

### Object-Centric Petri Net (OCPN)
Discovered by deriving per-type case-centric DFGs from the OC-DFG, applying an Inductive Miner variant on DFGs (as in PM4Py), and merging the resulting Petri nets. Variable arcs are assigned based on the event-activity buffer. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:73-94]

### Temporal Object Type Model (TOTeM)
A graph of object types with arcs annotated by log cardinality, event cardinality, and temporal relation. Computed from the temporal-relation, log-cardinality, and event-cardinality buffers. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:73-89]

## Evaluation

The framework was evaluated on two publicly accessible object-centric event logs:
- **Container Logistics (CL)**: 14,013 objects, 7 object types, 35,413 events, 14 activities, 15,926 O2O updates.
- **Age of Empires (AoE)**: 361,935 objects, 25 object types, 34,860 events, 829 activities.

Key findings:
- **Structural similarity** improves with larger buffer sizes until a plateau is reached; precision was constantly 1.0 across experiments.
- **Cache and priority policy selection** has a severe impact on model quality (accuracy and recall vary widely for a fixed buffer size of 125).
- **Runtime**: Stream item processing time grows linearly with buffer size but remains feasible for high data velocity (~2.5 ms per item even with priority policies and buffer synchronization enabled).
- LRU and FIFO with no priority policy or max-events-per-type priority achieved the highest accuracy and recall on the CL dataset for TOTeM discovery. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:15-21]

## Relation to Other Streaming Frameworks

This framework is conceptually related to the S-BAR architecture (Van Zelst et al.) for case-centric streaming process mining, adopting the same principle of condensing information into fixed-size intermediate buffers rather than buffering raw event windows. It extends this concept to the object-centric setting. A parallel effort, [[streaming-object-centric-process-mining|SOCPM]] (Mikkelsen, Rivkin, Burattin; DTU), also addresses streaming object-centric process mining but uses a different architectural approach and targets different model types. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:95-116]

## Limitations and Future Work

- The Inductive Miner variant on DFGs does not provide the same soundness guarantees as the original Inductive Miner.
- Evaluation is currently limited to structural comparison with offline models; semantic/language-based comparison is identified as future work.
- Strategy selection guidance (matching cache/priority policies to process characteristics) requires further investigation.
- Object-centric event logs with concept drift are needed to evaluate drift-handling capabilities.
- Theoretical guarantees for the streaming discovery algorithms remain an open problem.

## Implementation

A publicly accessible Python implementation is available at [https://github.com/loeseke/object-centric-streaming-discovery](https://github.com/loeseke/object-centric-streaming-discovery), including `CacheMonitor` and `RuntimeMonitor` classes for performance and buffer utilization tracking. ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:76-84]

## References and Context

This work is situated within the broader [[process-mining-handbook|process mining]] research community and builds on the [[object-centric-distance-metric|object-centric process mining]] paradigm. It was funded by the German Federal Ministry of Research, Technology and Space (grant 01IS25011).

## Реализация: репозиторий на GitHub

Открытая реализация фреймворка доступна в репозитории [loeseke/object-centric-streaming-discovery](https://github.com/loeseke/object-centric-streaming-discovery). Основной автор кода — **Nina Löseke**; **Lukas Liss** внёс исходный код майнера [[object-centric-distance-metric|Temporal Object Type Model (TOTeM)]]. Реализация написана на **Python 3.12**.

### Поддерживаемые модели

Фреймворк поддерживает онлайн-обнаружение трёх типов объектно-ориентированных моделей процессов из потоков событий:

- **OC-DFG** (Object-Centric Directly-Follows Graph) — объектно-ориентированный граф непосредственного следования ^[Liss et al - Object-Centric Streaming-Based Process Discovery.pdf:1-40]
- **OCPN** (Object-Centric Petri Net) — объектно-ориентированная сеть Петри
- **TOTeM** (Temporal Object Type Model) — темпоральная модель типов объектов

Входные данные — журналы событий в формате **OCEL 2.0** (JSON или XML), которые симулируются как потоки событий.

### Настройка окружения

Из-за конфликта зависимостей между библиотеками требуется создание **двух отдельных виртуальных окружений**:

- Для обнаружения OC-DFG и OCPN используется **pm4py** версии 2.7.15.
- Для обнаружения TOTeM используется библиотека **ocpa** версии 1.3.3, которая требует pm4py версии 2.2.32.

### Ключевые компоненты API

- `EventStream` — класс для загрузки журнала OCEL 2.0 и преобразования его в поток событий.
- `OcdfgBuffer` / `OcdfgBufferPerObjectType` / `OcpnBuffer` / `TotemBuffer` — буферы потоковых представлений моделей с настраиваемым размером буфера, политикой вытеснения кэша (`CachePolicy`, например LRU или FIFO) и опциональной политикой приоритетов (`PPBLifespanPerObject`, `PPBEventsPerObjectType`).
- `OcdfgModel` / `OcpnModel` / `TotemModel` — классы для майнинга, визуализации и оценки моделей из буферов.

Параметр `prune_node_frac` / `prune_arc_frac` позволяет отсекать наименее частотные узлы и дуги при построении итоговой модели.

### Наборы данных для оценки

Репозиторий включает скрипты для автоматической загрузки двух крупных журналов OCEL 2.0:

- **Container Logistics** — журнал контейнерной логистики (Graves & Knopp, 2023, Zenodo).
- **Age of Empires** — журнал игровых взаимодействий Age of Empires (Liss et al., 2024, Zenodo).

### Три уровня оценки

1. **A-priori evaluation (априорная оценка):** сбор и визуализация объектно-ориентированных характеристик, связанных с политиками приоритетов, по всему журналу/потоку (Jupyter-ноутбук `apriori_evaluation.ipynb`).

2. **Online-vs-offline evaluation (онлайн против офлайн):** сравнение онлайн-модели с офлайн-моделью, построенной на полном журнале. Метрики включают точность (accuracy), прецизионность (precision) и полноту (recall). Для OC-DFG дополнительно вычисляется среднеквадратичная ошибка (MSE) аннотаций узлов и дуг. Для TOTeM применяется специальная метрика расстояния со значениями от 0 до 1, отражающая различие в отношениях между онлайн- и офлайн-моделями. Для OCPN попарное сравнение недоступно из-за неразличимых тихих переходов.

3. **Runtime and cache-behavior evaluation (оценка времени выполнения и поведения кэша):** опциональные атрибуты `RuntimeMonitor` и `CacheMonitor` в каждом буфере позволяют фиксировать время обновления буфера и распределение типов объектов по буферам модели на каждые 10% обработанного потока.

Все результаты оценки и графики воспроизводятся через Jupyter-ноутбуки в директории `examples`; итоговые рисунки хранятся в директории `figures`.

## Key Data

- EventStream
event_stream
=
EventStream
- o2o_has_time
=
False
- event_stream
=
EventStream
- ocdfg_buf
=
OcdfgBuffer
- pp_buf
=
PPBLifespanPerObject
- prio_order
=
PrioPolicyOrder
- coupled_removal
=
False
- ocdfg_model
=
OcdfgModel
- verbose
=
False
- ots
=
sorted
- visualize_dfgs
=
False
- ocdfg_model_offl
=
OcdfgModel
- score_dict
=
get_ocdfg_accuracy
- totem_buf
=
TotemBuffer
- pp_buf
=
PPBEventsPerObjectType
- cache_monitor
=
CacheMonitor
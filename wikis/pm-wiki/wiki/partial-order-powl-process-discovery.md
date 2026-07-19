---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:46:29'
lint_warnings:
- claim: 'POWL models are **sound by construction**: they translate into Workflow
    nets inherently free from structural issues such as deadlocks.'
  concern: Soundness of a Workflow net means it is free from deadlocks AND livelocks
    AND has proper completion, but it is not accurate to say POWL models are universally
    sound by construction without qualification. More importantly, the claim that
    they are 'inherently free from structural issues such as deadlocks' is an oversimplification
    — soundness in Workflow nets is a behavioral property that depends on the semantics
    of the model, and while POWL's hierarchical structure does provide strong guarantees,
    claiming blanket freedom from all structural issues is overstated.
orphan: false
resource: https://github.com/humam-kourani/POWL
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Kourani et al - Revealing
    Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf
  hash: 4905eff9b9ae11c0b94fb06cbb29cf0a0587d4dac944a3d1c4a691d03773dba2
  ingested: '2026-07-14T07:46:29'
  size: 767307
  truncated: true
- file: https://github.com/humam-kourani/POWL
  hash: 7e7b6cd81e8c9d0d62e5d720a2c6673d9b176a9792b97148271cd482053c35f4
  ingested: '2026-07-16'
  size: 37
status: active
tags:
- process mining
- partial orders
- concurrency
- event data
- process discovery
- scalability
- interval event data
- hierarchical algorithm
- process model
- timestamp abstraction
title: Partial-Order-Based POWL Process Discovery
type: technology
updated: '2026-07-16'
---

# Partial-Order-Based POWL Process Discovery

This page covers a novel [[process-mining-handbook|process discovery]] algorithm that leverages the **Partially Ordered Workflow Language (POWL)** to discover process models directly from partially ordered event data. The work was authored by **Humam Kourani**, **Gyunam Park**, and **Wil M.P. van der Aalst** (Fraunhofer FIT and RWTH Aachen University) and accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation: Concurrency in Real-World Processes

Traditional [[process-mining-handbook|process discovery]] algorithms assume totally ordered event data, treating each process instance as a strict activity sequence (e.g., ⟨a, b, c⟩). This assumption clashes with the reality of complex processes where activities frequently execute concurrently or overlap in time. ^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:26-28]

Several factors compound this problem:

- **Interval data discarded**: Information systems often record start and completion timestamps, but conventional methods discard one, losing true execution semantics.
- **Identical timestamps**: Events sharing the same timestamp naturally indicate the absence of strict sequential dependency.
- **Unreliable timestamps**: Timestamps may suffer from varying granularities, recording delays (common in healthcare with manual data entry), or may need abstraction to coarser levels (hour, day, business-defined periods). ^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:29-39]

Imposing a total order on such data introduces fictitious sequential dependencies that misrepresent actual process logic. The paper advocates for discovery techniques that natively handle partially ordered data. ^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:49-54]

## Background: The Partially Ordered Workflow Language (POWL)

POWL is a hierarchical process modeling language where submodels are combined using:
- **Partial orders** — for concurrent or sequentially constrained execution
- **× (exclusive choice)** — only one branch executes
- **⟲ (loop)** — a do-part executes, optionally followed by a redo-part and repetition

POWL models are **sound by construction**: they translate into Workflow nets inherently free from structural issues such as deadlocks. This soundness guarantee makes POWL particularly suitable as a target language for discovery from partially ordered data. ^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:56-64]

## Deriving Partial Orders from Event Data

### Interval Event Logs

The algorithm first transforms a raw event log into an **interval event log** where each event is a tuple (activity label, case identifier, start timestamp, completion timestamp). Start and complete lifecycle transitions are matched on a FIFO basis. If lifecycle information is absent, atomic interval events (identical start and end timestamps) are created.

### Partially Ordered Traces (POTs)

For each case, a **Partially Ordered Trace (POT)** is constructed as a pair (V, ≺) where:
- V is a set of transitions (one per interval event)
- The precedence relation ti ≺ tj holds if and only if event i completes strictly before event j starts (eti < stj)

This definition naturally handles concurrency: activity instances whose execution intervals overlap have no precedence relation between them. The resulting relation is a strict partial order (irreflexive, transitive, asymmetric).

The multiset of all POTs derived from an interval event log forms the **Partially Ordered Event Log** (LPO), which serves as direct input to the discovery algorithm.

## The POWL Discovery Algorithm

The recursive algorithm (DiscoverPOWL) operates on a multiset of partial orders M and proceeds through five steps:

### Step 1: XOR Mining
Activities that never co-occur within the same process instance are identified as **conflicting**. Maximal conflict groups partition activities into mutually exclusive sets. For each group, a submodel is recursively discovered and combined with the × operator.

### Step 2: Co-Occurrence Grouping
Activities that always appear together across all instances are grouped using a **node co-occurrence relation** (ψ ↔M ψ′). Each co-occurrence group is recursively processed and replaced by a single POWL submodel, enabling loop detection at higher abstraction levels.

### Step 3: Loop Mining
The algorithm partitions nodes into **POWL equivalence classes** — groups of semantically identical submodels. If a class contains multiple instances, they are abstracted into a loop construct ⟲(ψ, (τ,1)), where τ is a silent transition.

### Step 4: Skip Mining
For each node absent in at least one partial order in M, the node is replaced with ×(ψ, (τ,1)) to model optional behavior.

### Step 5: Partial Order Aggregation (CombineOrders)
The remaining nodes are aggregated into a single encompassing partial order:
1. **Base Precedence Relation**: Captures sequential dependencies present in at least one POT and never contradicted in any other.
2. **Extended Precedence Relation**: Cautiously extends the base relation by transitivity, unless contradicted.
3. **Transitive Aggregated Relation**: Applies a Prune function to iteratively resolve transitivity violations, yielding a valid partial order.

## Soundness and Fitness Guarantees

The algorithm provides two key formal guarantees:
- **Soundness by construction**: Inherited from POWL's design.
- **Perfect fitness**: Any sequence that is a valid linearization of any input POT can be replayed by the discovered model. This stems from the conservative order aggregation (Step 5) and optional behavior handling (Step 4).

## Implementation and Evaluation

The algorithm is implemented in the Python library **`powl`** (installable via `pip install powl`) with a web demonstrator available at https://po-aware-powl-miner.streamlit.app/.

### Experimental Setup
Evaluation was conducted on two well-known real-life event logs:
- **BPI Challenge 2012** and **BPI Challenge 2017**

Log variants were created by filtering to the top 4, 6, 8, and 12 most frequent activities, plus the full unfiltered logs. Comparison was made against:
- **Zebra Miner** (region-based, incremental)
- **eST2 Miner** (replay-based Petri net synthesis)

A one-hour timeout was applied per run. Fitness and precision were measured using alignment-based conformance checking in PM4Py.

### Results

| Log | POWL Miner Time | eST2 Miner Time |
|---|---|---|
| BPIC 2012 (4 activities) | 8 sec | 145 sec |
| BPIC 2012 (12 activities) | 19 sec | Timeout |
| BPIC 2017 (full, 26 activities) | 41 sec | Timeout |

Key findings:
- **Zebra Miner** timed out on all log variants.
- **eST2 Miner** timed out on BPIC 2012 with 12 activities and BPIC 2017 with 6 activities.
- **POWL Miner** completed all variants, with the longest run at 42 seconds (full BPIC 2017).
- Both POWL Miner and eST2 Miner achieved **perfect fitness** on all completed runs.
- POWL Miner consistently achieved **higher precision** than eST2 Miner, indicating less over-generalization.

## Relation to Existing Work

Prior POWL-based discovery approaches (e.g., Kourani et al., ICPM 2023; Kourani et al., Inf. Syst. 2025) operated on totally ordered traces. This work is the first to extend POWL discovery to natively handle partially ordered input. ^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:72-75]

Other related techniques for partial-order-based discovery include:
- **Inductive Miner with lifecycle data** (Leemans et al., BPM 2015)
- **Split Miner with overlapping intervals** (Augusto et al., ICPM 2020)
- **Prime Miner** using prime event structures (Bergenthum, ICPM 2019)
- **ILP2 Miner** using integer linear programming (Folz-Weinstein et al., PETRI NETS 2023)
- **Multi-Phase Miner** aggregating instance graphs
- **eST2 Miner** combining replay with Petri net synthesis ^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:76-96]

A comprehensive survey of partial-order-based process mining is provided by Leemans, van Zelst, and Lu (KAIS, 2023). ^[Kourani et al - Revealing Inherent Concurrency in Event Data A Partial Order Approach to Process Discovery.pdf:75-76]

## Future Directions

The authors identify **noise filtering** as a key avenue for future work — incorporating mechanisms to abstract from infrequent or exceptional behaviors while preserving the scalability and formal guarantees of the current approach.

## See Also
- [[process-mining-handbook]]
- [[streaming-process-mining-event-streams]]
- [[object-centric-streaming-process-discovery-liss]]

## Key Data

- P = {X1, . . . , Xn} such that X = X1 ∪ · · · ∪Xn, Xi ̸= ∅ for all 1 ≤ i ≤ n, and
- G = {A1, . . . , An} be a partitioning ofA into n ≥ 2 parts. We say thatG is a

## Программная реализация: POWL Miner

Исследовательская группа Fraunhofer FIT опубликовала открытый инструмент **POWL Miner** — реализацию [[partial-order-powl-process-discovery|алгоритма обнаружения процессов на основе POWL]] — в виде публичного репозитория на GitHub (`fit-process-mining/POWL`, лицензия AGPL-3.0). Инструмент поддерживает **POWL 2.0** и позволяет выполнять [[process-mining-handbook|обнаружение процессов]] из журналов событий с последующим экспортом полученных моделей в форматы BPMN и Petri net (PNML). Теоретическая основа POWL 2.0 изложена в статье *«Unlocking Non-Block-Structured Decisions: Inductive Mining with Choice Graphs»*.^[POWL:104-112]

### Способы запуска

- **Облачное веб-приложение (Streamlit):** размещённая версия доступна по адресу [https://powl-miner.streamlit.app/](https://powl-miner.streamlit.app/) без необходимости локальной установки.
- **Локальный запуск:** после клонирования репозитория и установки зависимостей (`requirements.txt`, `packages.txt`) приложение запускается командой `streamlit run app.py`.
- **Docker:** готовый образ доступен через GitHub Container Registry (`ghcr.io/humam-kourani/powl:latest`); запуск осуществляется командой `docker run -p 8501:8501 powl`.
- **Python-библиотека:** инструмент устанавливается как пакет через pip (`pip install powl`) и может быть интегрирован в пользовательские скрипты; примеры использования находятся в директории `examples/` репозитория.^[POWL:113-120]

### Технические характеристики

Репозиторий написан преимущественно на Python (78 %) с использованием JavaScript (22 %) для визуализации BPMN (компонент `bpmn-auto-layout`, лицензия MIT). По состоянию на июнь 2025 года выпущена версия v1.0.0. Инструмент поддерживает два режима работы: стандартное обнаружение процессов (`app.py`) и обнаружение на основе частичных порядков (`app_po_based_discovery.py`), что соответствует двум направлениям исследований группы — классическому POWL и [[partial-order-powl-process-discovery|алгоритму на основе частично упорядоченных данных]].^[POWL:92-95]
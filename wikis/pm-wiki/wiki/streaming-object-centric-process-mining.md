---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:35:08'
lint_warnings:
- claim: 'An **OC-stream** is an infinite, temporally ordered sequence `S : N₀ → O`
    of OC-events, where events are emitted in real time upon occurrence'
  concern: Defining a stream as strictly infinite is an overstatement. Real-world
    event streams are potentially unbounded but not mathematically infinite; they
    are finite at any point in time and may terminate. This conflates a theoretical
    model with practical reality in a misleading way.
- claim: OC-DFGs highlight cross-object behavioral patterns and interdependencies
    between object lifecycles, though they do not capture AND/XOR splits and joins
  concern: This claim about OC-DFGs not capturing AND/XOR splits is a known characteristic
    of standard DFGs generally, but stating it as a definitive limitation of OC-DFGs
    specifically may be overstated depending on the variant. However, the more concrete
    concern is that the page presents this as a settled, universal fact about OC-DFGs
    when the referenced framework may define its own variant with different properties.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Mikkelsen et al - Push your
    objects into streams! - Streaming OCPM.pdf
  hash: effc586f858d9b88f028b4c4bac665a69e8d1c48787c27e3a0bf95543ef94b65
  ingested: '2026-07-14T07:35:08'
  size: 896788
  truncated: true
status: active
tags:
- process mining
- streaming data
- object-centric
- real-time analysis
- event logs
- concept drift
- ERP
- CRM
- online discovery
- pyBeamline
title: Streaming Object-Centric Process Mining (SOCPM)
type: technology
updated: '2026-07-16'
---

# Streaming Object-Centric Process Mining (SOCPM)

Streaming Object-Centric Process Mining (SOCPM) is a framework that combines [[streaming-process-mining-event-streams|Streaming Process Mining]] with [[object-centric-distance-metric|Object-Centric Process Mining (OCPM)]], enabling real-time, online discovery of object-centric process models from continuous, unbounded event streams. The framework was introduced by Jeppe M. Mikkelsen, Andrey Rivkin, and Andrea Burattin (DTU Compute, Technical University of Denmark) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series). ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:1-41]

## Motivation

Traditional OCPM techniques operate exclusively on static, finite event logs, creating a gap between the theoretical richness of object-centric analysis and the real-time demands of modern enterprise environments. ERP and CRM systems continuously generate streams of multi-object events, and waiting for post-mortem log collection introduces latency that is incompatible with operational decision-making. SOCPM bridges this gap by enabling continuous, low-latency discovery of [[object-centric-distance-metric|object-centric]] process models from live data streams, supporting concept drift detection and adaptability to evolving behaviors. ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:24-40]

## Formal Foundations

### Object-Centric Events and Streams

The framework builds on a simplified event model aligned with the OCEL 1.0 standard. An **OC-event** is a tuple `(e, act, t, omap)` where:
- `e` is the event identifier
- `act` is the activity name
- `t` is the timestamp
- `omap : OT ↛ (P(I) \ {∅})` is a partial function mapping object types to sets of involved object identifiers ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:84-95]

An **OC-stream** is an infinite, temporally ordered sequence `S : N₀ → O` of OC-events, where events are emitted in real time upon occurrence — analogous to the event stream model used in [[streaming-process-mining-event-streams|streaming process mining]]. ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:102-115]

### Object-Centric Directly-Follows Graph (OC-DFG)

The primary output model is the **Object-Centric Directly-Follows Graph (OC-DFG)**, a tuple `(A, OT, N, F, πfreqn, πfreqe)` where typed arcs in `F ⊆ N × OT × N` link activities through the lens of object type co-occurrence. OC-DFGs highlight cross-object behavioral patterns and interdependencies between object lifecycles, though they do not capture AND/XOR splits and joins.

### Object Occurrence Model (OOM)

To address a known limitation of OC-DFGs — their inability to distinguish whether associated object types actually co-occurred within the same event — the framework introduces the **Object Occurrence Model (OOM)**, a tuple `(A, E, R)` where:
- `A` is a set of activities
- `E : A → P(OT)` maps activities to associated object types
- `R ⊆ A × OT × OT × C` captures observed cardinality qualifiers (`1:1`, `1:N`, `N:M`) between object type pairs per activity

The OOM provides a complementary relational perspective to the OC-DFG, enabling analysts to detect whether object types are jointly involved in the same event instance or merely share activity labels independently.

## The SOCPM Pipeline Architecture

The framework implements a seven-step pipeline:

1. **Source**: Continuously emits OC-events as an OC-stream.
2. **Flatten**: Transforms multi-object events into sets of single-object events (one per object identifier), preserving object-centric semantics. The flattening is lossless and reversible via a composition operator.
3. **Routing**: Partitions flattened events into object-type-specific sub-streams. Supports two modes:
   - *Static routing*: A predefined set of object types `R ⊆ OT` is monitored.
   - *Dynamic routing*: All encountered object types are discovered automatically; new sub-streams are instantiated on first encounter.
4. **Control-flow discovery**: Applies [[streaming-process-mining-event-streams|streaming]] discovery techniques (e.g., Heuristics Miner with Lossy Counting) independently to each object-type sub-stream, using object identifiers as case identifiers.
5. **Inclusion strategy**: Determines which object types are ACTIVE (included in the global model) or INACTIVE, enabling graceful handling of concept drift. Three strategies are supported:
   - *Relative Frequency*: Retain types based on update frequency.
   - *Sliding Window*: Retain types that have emitted models within a fixed temporal window.
   - *Lossy Counting*: Approximate frequency tracking with bounded memory; infrequent types are gradually pruned.
6. **Relationship mining**: A dedicated **Lossy Counting Miner** operates on the raw, unflattened OC-stream to infer inter-object cardinalities (1:1, 1:N, N:M) from co-occurrence observations per activity, producing an OOM.
7. **Merging**: Integrates per-type DFGs (from Step 4), active object type set (from Step 5), and OOM (from Step 6) into a unified OC-DFG. Due to streaming constraints (bounded memory, approximate frequency tracking, convergence/divergence issues), activity frequencies `πfreqn` are omitted from the merged model, yielding *restricted OC-DFGs*.

## Implementation

The framework is implemented using the open-source **[[pybeamline|pyBeamline]]** library — a Python streaming process mining framework built on ReactiveX/RxPY, available at [https://github.com/beamline/pybeamline](https://github.com/beamline/pybeamline) (`pip install pybeamline`). It is compatible with OCEL 1.0-formatted streams, ensuring interoperability with existing offline OCPM tools such as PM4Py. ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:19-21]

## Experimental Evaluation

The framework was validated on three public multi-object process logs:
- **Logistics log**: Synthetic logistics simulation; 7 object types, 14 event classes, 35,761 events.
- **Order Management log**: Customer order lifecycle; 6 object types, 11 event types, 21,008 events.
- **Procure-to-Pay (P2P) log**: Organizational procurement process; 7 object types, 10 event types, 14,671 events. ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:19-21]

Performance was measured using **Jaccard Similarity** between the edge sets of the streaming-discovered OC-DFG and the offline PM4Py OC-DFG, computed as a function of events processed.

Key findings:
- The framework achieves strong alignment with offline methods, with near-perfect Jaccard similarity on P2P within 2,000 events under Relative Frequency strategy.
- Tuning inclusion parameters (e.g., frequency threshold, window size, approximation error) directly impacts structural completeness.
- Sliding Window and Relative Frequency strategies yield comparable peak similarities; smaller windows introduce fluctuations as object types intermittently enter and exit the active set.
- Lossy Counting inclusion strategy provides robust performance in high-volume environments.
- The framework successfully detects and adapts to concept drift in evolving process behaviors. ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:19-21]

## Relationship to Related Work

SOCPM extends the standard offline OCPM discovery pipeline — which involves flattening, projection, per-type mining, and merging of static logs — to the streaming setting. It is closely related to [[streaming-process-mining-event-streams|Streaming Process Mining]] techniques such as Heuristics Miner with Lossy Counting and sliding window methods, and to [[object-centric-distance-metric|Object-Centric Process Mining]] frameworks. The [[ocpm-from-time-series-sensor-data|transformation of sensor data into OCED]] represents a complementary upstream step that could feed into SOCPM pipelines. The [[ocpm-personal-health-management|application of OCPM to personal health management]] illustrates the broader domain applicability of object-centric approaches that SOCPM could extend to real-time settings. A parallel effort on [[object-centric-streaming-process-discovery-liss|object-centric streaming discovery]] (Liss et al.) uses a different architectural approach with fixed-size buffers and cache replacement strategies. ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:43-75]

## Key Data

- o = (e1, Place Order , {Order : {o1}, Item : {i1, i2}}) ^[Mikkelsen et al - Push your objects into streams! - Streaming OCPM.pdf:116-120]

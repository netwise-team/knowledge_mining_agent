---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:10:55'
lint_warnings:
- claim: The page appears to be cut off mid-sentence, but no clearly overstated or
    factually incorrect claims are present in the completed portions.
  concern: Actually, reviewing carefully, no claims in the completed text clearly
    contradict well-established facts or are demonstrably overstated with high confidence.
    The content is narrowly scoped to a specific methodology paper and makes no broad
    empirical claims that can be easily falsified.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Abu Sbeit et al - Enabling
    Object-Centric Process Mining from Time-Series.pdf
  hash: d6787463bcecd7d53b4c3985eff5bd8053dac89c9a579175a4f987635a25781b
  ingested: '2026-07-14T07:10:55'
  size: 587505
  truncated: true
status: active
tags:
- process mining
- time-series
- industrial processes
- sensor data
- discretization
- chemical recycling
- batch processing
- event log
- material flow
- OCPM
title: Enabling Object-Centric Process Mining from Time-Series Sensor Data
type: technology
---

# Enabling Object-Centric Process Mining from Time-Series Sensor Data

This page covers a methodology for transforming raw time-series sensor data into Object-Centric Event Data (OCED) suitable for [[object-centric-distance-metric|Object-Centric Process Mining (OCPM)]]. The approach was introduced by Abd Alrhman Abu Sbeit and Dirk Fahland (Eindhoven University of Technology) and Franco Cavadini (GR3N SA, Lugano) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

OCPM requires discrete events that explicitly reference activities and the objects they affect (object-centric event data, OCED). In industrial processes — such as chemical manufacturing — behavior is recorded solely by low-level sensors as time-series data. These signals reflect the evolving state of actuators and continuous variables (flow, level, temperature) but do not directly represent process-level events or object identities. Without activities and object identifiers being recorded, OCPM is inapplicable.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:8-29]

The paper identifies three input characteristics that make the problem challenging:
- **(I1)** Data originates from high-frequency, noisy time-series (boolean and continuous).
- **(I2)** Multiple sensors monitor parts of the same activity but no single sensor indicates its full extent.
- **(I3)** Object existence, movement, or processing is not explicitly recorded.

And three OCED requirements that must be satisfied:
- **(O1)** Discrete events with timestamps and types.
- **(O2)** Uniquely identified objects.
- **(O3)** Explicit relations between events and objects.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:30-36]

## Problem Decomposition

The methodology decomposes the overall transformation into four sub-problems:

- **P1**: Discretize noisy low-level time-series into event records per sensor.
- **P2**: Aggregate low-level events from related sensors into process-level events.
- **P3**: Infer objects from process-level events.
- **P4**: Link events to inferred objects.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:47-56]

The setting assumes material handling processes where (C1) handled objects are unrecorded (semi-)batches of material, (C2) materials reside at stations or move between them via defined connections (e.g., pipes), (C3) each connection carries at most one batch at a time, (C4) batches can merge or split at stations, and (C5) movements are driven by equipment tracked by low-level sensors.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:38-46]

## Methodology

### Step 1: Time-Series Discretization (P1)

Raw sensor signals are transformed into low-level event records using:

1. **Status Interpretation**: Domain-specific rules map sensor values to discrete statuses. Boolean signals map directly (e.g., `true` → Transfer Active). Real-valued signals map value ranges or trends to statuses (e.g., motor speed in a specific range → Transfer Active).
2. **Segmentation**: The time-series is segmented into maximal continuous intervals where all entries share the same status, producing tuples of the form `⟨sensorId, T_start, T_end, label⟩`.
3. **Noise Filtering and Debouncing**: Adjacent intervals with the same label separated by a time gap shorter than a threshold parameter *k* are merged, suppressing electrical noise and sensor jitter. The parameter *k* is determined from historical sensor data and validated against known scenarios.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:57-59]

### Step 2: Multi-Sensor Event Integration (P2)

Individual sensor events provide only a partial view of material movement. To reconstruct complete transport events, the methodology:

1. Groups sensors by the physical connection (pipeline) they monitor, using system topology knowledge.
2. Constructs an **Event Knowledge Graph (EKG)** with `:STATION` and `:SENSOR` nodes linked to `:CONNECTION` nodes (with `:ORIGIN` and `:DESTINATION` relations).
3. Identifies process-level material movement intervals as the longest time intervals during which a **majority (≥65%) of sensors** assigned to a connection agree on observing activity. This threshold is adjusted dynamically for sensor failures.
4. Each inferred movement interval `[t1, t2]` is materialized as two atomic `:EVENT` nodes (START and END) connected by a `:DF` (directly-follows) relation and linked to the relevant sensor and stations.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:59-65]

### Step 3: Object and Relation Inference (P3 & P4)

Building on the partial EKG from Step 2, five inference rules (IR1–IR5) enrich the graph with object nodes and relations. These rules are expressed as graph queries (e.g., in Cypher) over the EKG:

- **IR1 — Object Inference**: From a pair of START/END events at a connection from station A to station B, infer a `:BATCH` node representing the material batch moved, correlated to both events.
- **IR2 — Related-To Relations**: A batch M2 is related to batch M1 if both are correlated to events at the same station and M2's start time ≥ M1's end time (sequential processing).
- **IR3 — Material Splitting**: A batch M1 is inferred to split into multiple batches (M2, M3, ...) if M1 ends at a station from which multiple downstream batches emerge shortly thereafter toward different destinations.
- **IR4 — Material Merging**: A batch M3 is inferred to result from merging multiple batches (M1, M2, ...) if they originate from different upstream stations and arrive at a common destination before M3's start.
- **IR5 — Directly-Follows Relations**: A `:DIRECTLY_FOLLOWS` relation is inferred between transport events when their corresponding material batches are connected through IR2–IR4 relations, enabling end-to-end flow path reconstruction.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:63-65]

The resulting EKG conforms to OCED requirements (O1–O3) and supports [[object-centric-distance-metric|OCPM]] tasks such as discovery and conformance checking.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:63-65]

## Implementation and Validation

The methodology was validated on a real-world industrial case study at **Gr3n's MADE demonstration plant**, which processes polyethylene terephthalate (PET) via microwave-assisted alkaline hydrolysis. The dataset covered several months of sensor readings from **218 sensors** (binary and real-valued), comprising over **three million timestamped records**.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:66-70]

- Time-series-to-event transformation was implemented in Python.
- EKG construction and inference rules (IR1–IR5) were implemented using the open-source **PromG library** (https://github.com/promg-dev).
- Results: **4,146 low-level transportation events** → **1,566 process-level events** → **1,566 material batches** and **3,001 relations** between them.

**Runtime**: Event discretization took 622.91 seconds (due to high-frequency input); EKG loading took 16.09 seconds; object inference took 31.17 seconds.

Validation with Gr3n's process owner confirmed that extracted event sequences and inferred material flows align with known station connections, timing, and operational behavior, including splitting and merging behavior.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:66-70]

## Relation to Existing Work

This work addresses a gap in the literature where prior approaches to P3 and P4 assumed at least some object references exist in the data. Here, **no case identifiers or object identifiers exist at all** — object existence itself must be inferred. The approach builds on:
- EKG-based frameworks for modeling event context and entity relations.
- Sensor data discretization techniques (segmentation, thresholding, debouncing).
- Physical principles for inferring entity presence in industrial systems (Swevels et al.).^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:102-113]

The methodology complements [[sustainability-aware-process-mining|process mining in industrial settings]] and extends the applicability of [[object-centric-distance-metric|OCPM]] to domains where structured event data is absent. It also relates to [[process-mining-handbook|foundational OCPM concepts]] introduced in the process mining literature.

## Limitations and Future Work

- The methodology currently applies to processes satisfying characteristics C1–C5 (batch-based material handling with sensor-monitored movements).
- Further process analysis may require additional data detecting non-transport activities (e.g., processing events at stations).
- The work lacks generalized evaluation criteria applicable across use cases, due to the novelty of the transformation from low-level sensor data to OCED.
- Future work may incorporate refined event detection techniques and adjustments to EKG construction for broader industrial applicability.^[Abu Sbeit et al - Enabling Object-Centric Process Mining from Time-Series.pdf:38-56]

## References

Abu Sbeit, A. A., Cavadini, F., & Fahland, D. (2025). *Enabling Object-Centric Process Mining from Time-Series*. Pre-print accepted at ICPM 2025 International Workshops, to appear in Springer LNBIP series. Research supported by AutoTwin EU GA n. 101092021.
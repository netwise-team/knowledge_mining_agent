---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T08:06:18'
lint_warnings:
- claim: Only Petri net–based discovery algorithms were used, as Petri nets support
    precise representation of concurrency, branching, looping, and synchronization
  concern: The claim that only Petri net-based algorithms were used is presented as
    a methodological fact, but the Inductive Miner and other common process discovery
    algorithms can output multiple model notations (e.g., process trees, BPMN) — not
    exclusively Petri nets. More importantly, the justification conflates the output
    notation with the algorithm itself, which is misleading.
- claim: The [[k-traceoids-trace-clustering|Inductive Miner]] uses recursive partitioning
    to detect sequential, parallel, concurrent, and loop structures
  concern: Linking 'Inductive Miner' to a 'k-traceoids-trace-clustering' wiki page
    is factually incorrect — the Inductive Miner is a process discovery algorithm
    unrelated to trace clustering or k-traceoids methods. This appears to be a mislabeled
    internal wiki link that misrepresents the algorithm's category.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Kim et al - Bus stop congestion
    monitoring based on process discovery algorithms.pdf
  hash: c0a4e2b3794eaa131137f2e533a3ff1f2954aae513ce0c456ef1acc2d5b1e77c
  ingested: '2026-07-14T08:06:18'
  size: 1307029
status: active
tags:
- bus stop congestion
- process discovery
- process mining
- congestion monitoring
- public transit
- complexity metrics
- traffic flow
- commuting hours
- process model
- transportation systems
title: Process Mining for Bus Stop Congestion Monitoring
type: technology
---

# Process Mining for Bus Stop Congestion Monitoring

This page covers the application of [[process-mining-data-science-in-action|process mining]] — specifically [[process-mining-data-science-in-action|process discovery]] algorithms and process model complexity metrics — to quantitatively evaluate congestion at bus stops. The work was authored by Seon Kim, Jungtak Oh, and Jongchan Kim (Yonsei University, South Korea) and accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

Bus stop congestion directly affects punctuality, passenger experience, traffic flow, and environmental sustainability. Traditional congestion assessment methods rely on aggregate statistics (average travel speed, traffic volume) or GPS-derived data at the road-network or route level. This study proposes a novel, event-log-driven framework that quantifies congestion at the individual bus stop level using process mining techniques — requiring only public transportation card data rather than GPS infrastructure.^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:7-20]

The core insight is to conceptualize each bus passing through a specific stop as a distinct process case. By analyzing the operational history of all buses traversing a stop, the complexity of the resulting process model serves as a proxy for congestion level.^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:34-42]

## Event Log Construction

The study used a publicly available dataset from Jeju Island, South Korea (DACON competition), covering bus card boarding and alighting events from September 1 to October 31, 2019. Raw records include: bus route ID, vehicle ID, boarding date/time, boarding station code/name, and alighting station name.

Preprocessing steps:
- Missing alighting records were excluded.
- Data were transformed into standard event log format with three fields:
  - **Case ID**: date + bus stop name + bus stop code (one case per stop per day, directionally distinguished)
  - **Activity**: bus route ID stopping at that stop
  - **Timestamp**: exact date and time of the boarding/alighting event
- Logs were partitioned into two temporal windows:
  - **Morning commuting hours**: 07:00–09:59
  - **Non-commuting hours**: 10:00–11:59
- Eighteen bus stops with the highest passenger volumes were selected for analysis.^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:110-119]

## Process Discovery Algorithms

Only Petri net–based discovery algorithms were used, as Petri nets support precise representation of concurrency, branching, looping, and synchronization — enabling quantification of complex behavioral patterns.

### Inductive Miner
The [[k-traceoids-trace-clustering|Inductive Miner]] uses recursive partitioning to detect sequential, parallel, concurrent, and loop structures. It guarantees a sound Petri net output and is robust to noise. Key hyperparameters tuned: `noise_threshold` (0.0–0.3), `multi_processing`, and `disable_fallthroughs`.

### Heuristic Miner
The Heuristic Miner generates realistic models by analyzing direct frequency and causal relationships between events, prioritizing frequent paths. It handles incomplete or noisy logs well. Key hyperparameters tuned: `dependency_thresh` (0.3–0.9), `and_threshold` (0.5–0.8), and `loop_two_threshold` (0.3–0.7).

## Process Model Complexity Metrics as Congestion Indicators

Six complexity metrics were computed on the discovered Petri nets to serve as congestion proxies:

1. **Simplicity**: Quantifies structural simplicity; higher = simpler model. Computed via PM4Py.
2. **Size**: Total number of places (P) in the Petri net. Larger = more complex.
   - Size(PN) = |P|
3. **Extended Cyclomatic Metric (ECyM)**: Counts linearly independent paths (loops, branches, cycles).
   - ECyM(PN) = |E| − |V| + p
4. **Extended Cardoso Metric (ECaM)**: Evaluates branching complexity considering AND/OR/XOR decision points.
   - ECaM(PN) = Σ ECFC_p(p) for p ∈ P
5. **Modified Density** (novel contribution): Derived from the standard Density metric but restricted to activities actually observed in the event log (excluding unobserved activities). Captures real-world connectivity more accurately.
   - MD(PN) = E / (N × (N − 1))
6. **Entropy**: Quantifies uncertainty and variability in path/event distribution.
   - Entropy = −Σ P_i × log₂(P_i) for i ∈ {T, P, A}^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:43-52]

## Experimental Results

### Key Finding: Modified Density is the Most Reliable Congestion Indicator

Across both discovery algorithms and all hyperparameter combinations, **Modified Density** consistently and significantly distinguished commuting from non-commuting hours:

- **Heuristic Miner**: Modified Density was significant in 34/36 Wilcoxon tests and 17/36 permutation tests. No other metric achieved any significance in the permutation test (0/36).
- **Inductive Miner**: ECyM (14/16 Wilcoxon, 10/16 permutation) and Modified Density (12/16 Wilcoxon, 6/16 permutation) performed best.^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:14-20]

Statistical validation used two non-parametric tests (given non-normal distributions):
- **Wilcoxon signed-rank test**: Tests whether median differences between paired time-period measurements are significant.
- **Permutation test**: Assesses significance by randomly rearranging observed values between conditions.

### Structural Metrics Fail to Capture Congestion

Simplicity showed no significant differences in either test under either algorithm. Size and ECaM showed inconsistent results. This indicates that traditional structure-oriented metrics do not reliably reflect real congestion dynamics at bus stops.^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:14-18]

### Temporal Pattern

Modified Density values were consistently higher during commuting hours than non-commuting hours across most of the 18 analyzed bus stops, aligning with real-world expectations of peak-hour congestion.^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:53-59]

## Contributions and Significance

- **Novel application domain**: First framework to apply process discovery and process model complexity metrics to bus stop congestion monitoring at the individual stop level.
- **Data accessibility**: Demonstrates that public transportation card data (boarding/alighting records) suffices for congestion analysis — no GPS data required — reducing cost and improving accessibility.
- **Modified Density metric**: Proposed as a more accurate complexity measure for real-world event logs by restricting density calculation to observed activities.
- **Temporal analysis**: Commuting vs. non-commuting hour partitioning captures dynamic congestion variation.^[Kim et al - Bus stop congestion monitoring based on process discovery algorithms.pdf:100-104]

## Limitations and Future Work

- Analysis limited to 18 bus stops in one region (Jeju Island), limiting generalizability.
- Each event treated as representing a single passenger; actual passenger counts per card transaction not incorporated.
- Future work should extend to diverse urban areas, more routes, and longer time periods, and incorporate passenger count attributes for more realistic congestion modeling.

## Relation to Other Process Mining Applications

This work joins a growing body of process mining applications in public services and infrastructure. Related applications include [[process-mining-egovernment-collaborative-choreography|e-Government process choreography]], [[process-mining-public-procurement|public procurement analysis]], and [[predictive-process-monitoring-pathway-left-shifts|hospital pathway monitoring]], all demonstrating the versatility of process mining beyond traditional business process management contexts.

## Key Data

- lower = more complex
- True = some paths may
- Higher = More signifi-
- Higher = stricter recog-
- Higher = stricter detec-
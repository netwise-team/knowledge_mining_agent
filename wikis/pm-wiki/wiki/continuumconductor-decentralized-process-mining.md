---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:39:52'
lint_warnings:
- claim: The work was accepted at the ICPM 2025 Workshops (Springer LNBIP series)
  concern: As of the knowledge cutoff, ICPM 2025 had not yet taken place, making it
    impossible to verify this acceptance claim. While this may be a forthcoming publication,
    stating it as an established fact is premature and potentially overstated if the
    acceptance had not yet been confirmed at the time of writing.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Reiter et al - ContinuumConductor
    Decentralized Process Mining on the Edge-Cloud Continuum.pdf
  hash: 4b9f6d838d5eab1776e21662095f79c6c812288e7ab75f18b1072d23e75d4dcc
  ingested: '2026-07-14T07:39:52'
  size: 587318
  truncated: true
status: active
tags:
- process mining
- edge computing
- IoT
- decentralization
- privacy-preserving
- resource efficiency
- cyber-physical systems
- event data
- distributed computing
- IIoT
title: 'ContinuumConductor: Decentralized Process Mining on the Edge-Cloud Continuum'
type: technology
---

# ContinuumConductor: Decentralized Process Mining on the Edge-Cloud Continuum

ContinuumConductor is a layered decision framework for distributing [[process-mining-data-science-in-action|process mining]] tasks across edge-cloud computing infrastructures in Industrial Internet of Things (IIoT) environments. It was proposed by Hendrik Reiter, Janick Edinger, Martin Kabierski, Agnes Koschmider, Olaf Landsiedel, Arvid Lepsien, Xixi Lu, Andrea Marrella, Estefania Serral, Stefan Schulte, Florian Tschorsch, Matthias Weidlich, and Wilhelm Hasselbring, representing institutions including Kiel University, University of Hamburg, University of Vienna, University of Bayreuth, Hamburg University of Technology, Utrecht University, Sapienza University of Rome, KU Leuven, TU Dresden, and Humboldt University of Berlin. The work was accepted at the ICPM 2025 Workshops (Springer LNBIP series) and originated from Dagstuhl Seminar 25103 on "Process Mining on Distributed Event Sources."^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:1-17]

## Motivation

Traditional process mining assumes centralized event data collection and analysis. However, modern IIoT systems increasingly operate over distributed, resource-constrained edge-cloud infrastructures. Three critical objectives drive the need for decentralization:

- **G1 — Privacy preservation:** Sensitive data (e.g., video streams capturing human behavior) must be anonymized close to the source to comply with privacy regulations.
- **G2 — Real-time responsiveness:** Immediate detection of process deviations (e.g., unauthorized access) requires near-sensor computation.
- **G3 — Resource efficiency:** Raw sensor data from high-resolution video and telemetry streams exceed available network bandwidth if transmitted unprocessed.

These goals align with and extend concerns addressed in [[z-anonymity-edge-filtering-process-mining|z-anonymity edge filtering]] and [[streaming-process-mining-event-streams|streaming process mining]].^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:18-48]

## Use Case: Inland Port Automation (InteGreatDrones)

The framework is demonstrated through the InteGreatDrones project, which modernizes data collection and operational transparency in inland port terminals. The sensor ecosystem includes:

1. **Fixed cameras** — permanently installed, streaming high-resolution data to central edge servers over stable connections.
2. **Vehicle-mounted cameras** — on reach stackers, straddle carriers, and trucks; intermittently connected via wireless links.
3. **Autonomous drone cameras** — aerial video for monitoring operational zones; dynamically focused on areas of interest.
4. **Sensor boxes on vehicles** — recording GPS position, acceleration, vibration, and spreader beam height for precise cargo handling reconstruction.

Event logs generated from this ecosystem describe the lifecycle of each cargo unit (arrival, handling, storage, departure) and vehicle states (loading, unloading, idle, maintenance).^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:81-120]

## IIoT Process Mining Pipeline

ContinuumConductor structures process mining into five pipeline steps, each presenting distinct challenges in a distributed IIoT context:

| Step | Description | Key Challenges |
|---|---|---|
| **Preprocessing** | Transform raw unstructured sensor data (video, JSON, time-series) into low-level events | C1 (large unstructured data), C2 (uncertainty from ML), C4 (compute limits) |
| **Aggregation** | Combine low-level events into high-level events using temporal patterns and context | C3 (ambiguous context), C4 (compute limits), C5 (erroneous/incomplete data) |
| **Correlation** | Assign activities to cases or objects (cf. [[object-centric-distance-metric|object-centric process mining]]); requires global shared case/object IDs | C5 (temporal ordering), C6 (shared notation) |
| **Discovery** | Transform event logs into process models (Petri nets, process trees) | C5 (completeness), C6 (merging local fragments) |
| **Insights** | Conformance checking, performance diagnostics, simulation, root-cause analysis | C4 (complex ML), C5 (partial data robustness) |

The six identified challenges are: C1) large volume of unstructured data; C2) uncertainty; C3) sensitivity to ambiguous context; C4) network and computing limitations; C5) erroneous and incomplete data; C6) necessity of shared case/object notion.

## The Edge-Cloud Continuum

The edge-cloud continuum spans a hierarchical tree of computing resources — edge nodes (sensors, IoT gateways, mini-computers), fog nodes (intermediate GPU-equipped servers), and cloud instances. Each node can store or compute locally, on a higher tier, or peer-to-peer. In the InteGreatDrones project, four computing layers are used:

1. Directly at/within sensors (e.g., smart cameras for license plate detection)
2. Edge devices (mini-computers, gateways)
3. Edge clusters (GPU-equipped servers for video preprocessing and anonymization)
4. Cloud instance (application and visualization services)

This architecture supports [[streaming-process-mining-event-streams|streaming]] real-time analytics at the edge while leveraging the cloud for deeper, long-term insights.^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:49-57]

## Goal-Supporting Techniques

### Privacy Preservation
Privacy threat modeling using frameworks such as LINDDUN identifies trust zones where data processing is safe. Privacy design strategies — *separate*, *minimize*, *aggregate*, *hide* — naturally align with decentralized architectures. Privacy-enhancing technologies (PETs) such as secure multi-party computation and local differential privacy process sensitive data locally and share only obfuscated or aggregated outputs. This complements approaches like [[z-anonymity-edge-filtering-process-mining|z-anonymity edge filtering]] for distributed environments.

### Real-Time and Resource-Efficient Analysis
Edge-side complex event processing (CEP) reduces data volume before cloud transmission. Incremental process discovery and online conformance checking algorithms enable continuous model updates and immediate deviation detection. On-edge AI/ML (including TinyML) performs activity recognition and event abstraction directly at the sensor, generating richer event logs with minimal bandwidth usage.

## ContinuumConductor Decision Framework

The ContinuumConductor comprises **16 questions** across the five pipeline steps. Each question has four possible answers: *centralized (critical)*, *centralized (favorable)*, *decentralized (favorable)*, *decentralized (critical)*. A conflict arises when both a critical-centralized and critical-decentralized answer appear for the same step, requiring specialized algorithms or hardware adaptations.

| Phase | Question | Challenge/Goal |
|---|---|---|
| Preprocessing | Pre1. Are compute resources enough for preprocessing? | C1 |
| | Pre2. Is raw data privacy-critical? | G1 |
| | Pre3. Does raw data transfer need high bandwidth? | C4, G3 |
| | Pre4. Is preprocessing faster on device? | C4, G2 |
| Aggregation | Agg1. Are low-level events still privacy-critical? | G1 |
| | Agg2. Are low-level events still high-volume? | C1 |
| | Agg3. Can events be built from local context? | C3 |
| | Agg4. Can sensor/network outages be tolerated? | C4, C5 |
| Correlation | Cor1. Does a global notion of case/object IDs exist? | C6 |
| | Cor2. Is time synchronized between nodes? | C5 |
| | Cor3. Do out-of-order events violate real-time objectives? | C5, G2 |
| Discovery | Dis1. Is the process model privacy-critical? | C6, G1 |
| | Dis2. Does the discovery algorithm benefit from locality? | G2, G3 |
| | Dis3. Does the algorithm require consistent/complete event logs? | C5 |
| Insights | Ins1. Does insight extraction need advanced hardware? | C4 |
| | Ins2. Can insight extraction tolerate partial results? | C5, G1 |

### Application to InteGreatDrones

- **Preprocessing:** Decentralized is mandatory. Video anonymization at the edge (Pre2), intelligent filtering for bandwidth (Pre3), and edge server preprocessing for vehicle cameras (Pre1, Pre4).
- **Aggregation:** Distributed processing feasible. Complex events require sensor fusion (Agg3); single sensor outages tolerable (Agg4).
- **Correlation:** Distributed possible. Global IDs exist via trailer/container identifiers (Cor1); robust time synchronization needed (Cor2); out-of-order detection critical (Cor3).
- **Discovery:** Centralized recommended. No privacy-critical data remains post-anonymization (Dis1); complete event logs benefit central processing (Dis3).
- **Insights:** Centralized preferred. Comprehensive view of all data sources required (Ins1, Ins2).

## Relationship to Related Work

ContinuumConductor builds on and extends several lines of research:

- **Streaming process mining:** [[streaming-process-mining-event-streams|Streaming process mining]] algorithms handle continuous event streams; ContinuumConductor addresses *where* in the infrastructure these algorithms run.
- **Distributed discovery:** Van der Aalst's decomposition of Petri nets from partial event logs; Map-Reduce parallelization; Single-Entry Single-Exit conformance checking.
- **EdgeMiner:** A distributed, resource-efficient algorithm operating directly on resource-constrained sensor nodes with real-time event data (limited to footprint-matrix-based algorithms like the alpha miner).
- **Privacy in process mining:** Group-based privacy notions, differential privacy, and multiparty computation approaches, including [[z-anonymity-edge-filtering-process-mining|z-anonymity edge filtering]].
- **Object-centric process mining:** Correlation to cases/objects in distributed settings relates to [[ocpm-from-time-series-sensor-data|OCPM from time-series sensor data]] and [[ocpm-personal-health-management|OCPM for health management]].

## Funding and Origin

The work received funding from the Deutsche Forschungsgemeinschaft (DFG), grant 496119880, and from the German Federal Ministry for Digital and Transport (BMDV) under the Innovative Hafentechnologien II (IHATEC II) program. It originated at Dagstuhl Seminar 25103 (Schloss Dagstuhl, Leibniz-Zentrum für Informatik).
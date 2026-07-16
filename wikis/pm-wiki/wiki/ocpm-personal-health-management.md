---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:21:28'
lint_warnings:
- claim: traditional process mining requires a single case notion, flattening the
    multidimensional and interdependent nature of real-life health processes
  concern: While it is true that classical process mining typically assumes a single
    case notion, this is an oversimplification. Many traditional process mining techniques
    and tools have supported multiple perspectives and case notions for years, and
    the framing that all traditional process mining 'requires' a single case notion
    ignores well-established extensions and variants predating OCPM.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Ribeiro et al - Towards Object-Centric
    Process Mining for Personal Health Management.pdf
  hash: 3a9851b5e3d26ee022020813ad613bb3c85f8bfabfe0b180ed4027fd949681fe
  ingested: '2026-07-14T07:21:28'
  size: 466231
status: active
tags:
- process mining
- digital health
- behavior change
- sensor data
- wearables
- personalized interventions
- human-centric process mining
- non-communicable diseases
- temporal patterns
- health monitoring
title: Object-Centric Process Mining for Personal Health Management
type: concept
---

# Object-Centric Process Mining for Personal Health Management

This page covers the application of [[object-centric-distance-metric|Object-Centric Process Mining (OCPM)]] to personal health management, including a proposed sensor-augmented Object-Centric Event Log (OCEL) standard and a proof-of-concept framework. The work was introduced by Maria Inês Ribeiro, Laura Genga, and Pieter Van Gorp (Eindhoven University of Technology) and Monique Simons (Wageningen University & Research), accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

Wearable and mobile technologies enable continuous monitoring of health behaviors such as exercise, sleep, and stress, generating rich multi-modal sensor streams. Current data-driven approaches model users through aggregated features or sequential patterns, overlooking complex temporal patterns and interdependencies among health behaviors in dynamic contexts. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:8-29]

Traditional [[process-mining-healthcare-radiological-workflows|process mining]] has been applied to capture the process nature of human behaviors — including temporal structures, habits, interleaving, and contextual decisions — in what is termed *human-centric process mining*. However, traditional process mining requires a single case notion, flattening the multidimensional and interdependent nature of real-life health processes. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:30-36]

OCPM addresses this limitation by allowing a user to be modeled as a central entity alongside interdependent health processes and dynamic context, without forcing a single case notion. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:37-39]

## Sensor-Augmented Object-Centric Event Log

The authors propose a **sensor-augmented OCEL** — a four-dimensional extension of the standard OCEL format — that integrates sensor data and models relationships between behavior events, objects, and time. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:59-66]

### Four Dimensions

1. **Objects**: Entities forming case notions, each characterized by a single object type. In personal health management, objects can represent:
   - A *user* (with dynamic attributes such as self-efficacy, motivation, social environment, location, weather)
   - *Health behaviors* with lifecycles (e.g., physical activity bouts, sleep episodes)
   - *Structured time periods* (e.g., days, intervention periods)
   - *Devices* (e.g., a wearable)

2. **Behavior Events**: Timestamped semantic activity instances, including:
   - Directly extracted events: user-system interactions (content viewing, notifications) and self-reports (food intake, physical activity logs)
   - Recognized events: derived from sensor data (e.g., sleep episodes, physical activity bouts)
   - Atomic and non-atomic behaviors abstracted via lifecycle attributes (start/end)

3. **Sensor Events**: Timestamped raw measurements from sensing hardware (smartphones, wearables), forming time series. Each event is linked to a single sensor type (e.g., accelerometer with x, y, z attributes).

4. **Time**: The foundational synchronization dimension across all heterogeneous data, providing single timestamps to events and dynamic object attributes. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:67-91]

### Relations

The sensor dimension is modeled separately to capture **Sensor Event to Behavior Event (SE2BE)** relationships — many-to-many, semantically qualified links connecting sensor time series to behavior events recognized via dedicated time-series methods. For example, accelerometer events may 'recognize' a physical activity bout or a sleep episode. Sensor events, behavior events, and objects also relate to any number of objects (SE2O, BE2O, O2O) with semantic qualifiers. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:92-100]

This design preserves raw sensor data in the OCEL, enabling multiple activity recognition strategies tailored to different case notions — a key advantage over traditional process mining pipelines that apply a single pre-processing step. This approach is complementary to work on [[ocpm-from-time-series-sensor-data|enabling OCPM from time-series sensor data]].

## OCPM Framework: Proof-of-Concept

A stepwise OCPM framework was demonstrated through a case study exploring interdependencies between physical activity, perceived stress, and user engagement in self-reporting. Data was collected over 2 weeks from one participant using a wrist-worn device (≥12 hours/day) via the GameBus-Experiencer app. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:102-109]

### Step 1: Data Extraction
Data was extracted from source systems into the sensor-augmented OCEL format, integrating sensor and behavior data typically stored in fragmented health systems. Sensor event types: accelerometer and heart rate. Behavior event types: notification and stress self-report. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:110-116]

### Step 2: Activity Recognition
A validated threshold decision rule method transformed accelerometer and heart rate sensor data into physical activity bout events (with start/end). Physical activity bout objects were related to self-report objects based on temporal proximity (within 3 hours), enabling investigation of how prior activity affected perceived stress.

### Step 3: Data Query
Object-centric queries filtered the sensor-augmented OCEL for a subset of behavior events and objects, forming an **OCEL profile** (sensor dimension omitted but represented by recognized activities). Implemented using the PM4PY library.

### Step 4: Process Discovery
The OCEL profile was transformed into an **Object-Centric Petri Net (OCPN)** using the Inductive Miner algorithm via PM4PY. The discovered model revealed:
- **Decision patterns**: The user may choose to self-report stress upon receiving a notification.
- **Interleaved patterns**: Notifications may arrive before, during, or after physical activity, affecting perceived stress and self-report response rate (e.g., lower likelihood of self-reporting during physical activity).

## Implications for Personalized Digital Health

OCPM in personal health management supports **just-in-time adaptive interventions (JITAIs)** — tailored content delivered at opportune moments based on modeled personal health processes. Prediction and conformance checking techniques could guide users from current behaviors toward healthier behaviors aligned with digital engagement and health goals.

This approach captures complex behavior including temporal patterns, habits, interleaving, and decision points — advantages over data mining with aggregated features — while also capturing the multidimensional and interdependent nature of real-life health behavior, unlike traditional process mining.

## Limitations and Future Directions

- The proof-of-concept focused on a single user and system at one abstraction level.
- Scaling requires addressing data quality, advancing contextual inference, and adapting discovery techniques for unstructured human behavior.
- Use of personal health data raises important questions about privacy, surveillance, and data governance.

## Relation to Broader Process Mining Research

This work contributes to the emerging **human-centric process mining** paradigm and extends OCPM — originally conceptualized for business applications — into the personal health domain. It connects to [[ocpm-from-time-series-sensor-data|sensor-to-OCPM transformation methodologies]] and [[process-mining-healthcare-radiological-workflows|healthcare process mining]] more broadly, while introducing a novel application domain focused on individual behavior change rather than institutional clinical workflows. ^[Ribeiro et al - Towards Object-Centric Process Mining for Personal Health Management.pdf:37-57]

## References

- Ribeiro, M.I., Genga, L., Simons, M., Van Gorp, P. (2025). *Towards Object-Centric Process Mining for Personal Health Management*. ICPM 2025 Workshops, Springer LNBIP.
- Open-source repository: [GameBus-HealthBehaviorMining](https://github.com/MariaInesRibeiro98/GameBus-HealthBehaviorMining)
- Aalst, W.M.P. van der (2023). Object-Centric Process Mining: Unraveling the Fabric of Real Processes. *Mathematics*, 11, 2691.
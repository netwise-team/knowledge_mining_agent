---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:33:32'
lint_warnings:
- claim: Processing one month of data takes approximately 15 minutes.
  concern: Given that the dataset totals approximately 1.7 TB of raw message metadata,
    processing one month of data in ~15 minutes would require exceptionally high throughput.
    While not impossible with modern infrastructure, this figure seems implausibly
    fast for that data volume and is worth scrutinizing for accuracy or missing context
    (e.g., whether it refers to preprocessed/sampled data rather than the full raw
    logs).
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Antunes et al - Process Mining
    for e-Government collaborative processes choreography a case study.pdf
  hash: f4f929f989507ffc222ceaa753f89d4274ab8530ba200b9864efcc29186eee3f
  ingested: '2026-07-14T07:33:32'
  size: 525930
  truncated: true
status: active
tags:
- process mining
- e-government
- choreography
- collaborative processes
- digital government
- interoperability
- BPMN
- event log
- public sector
- inter-organizational
title: Process Mining for e-Government Collaborative Process Choreography
type: technology
---

# Process Mining for e-Government Collaborative Process Choreography

This page covers the application of [[process-mining-data-science-in-action|process mining]] techniques to discover **BPMN 2.0 choreography models** from inter-organizational message logs in e-Government settings. The work was presented by Lucía Antunes, Andrea Delgado, and Laura González (Universidad de la República, Uruguay) at the ICPM 2025 Workshops.

## Background and Motivation

Digital Government processes are inherently distributed: multiple public organizations collaborate to deliver services to citizens, exchanging messages across shared infrastructure. These **collaborative business processes** differ from traditional intra-organizational (orchestration-like) processes in that no single organization controls the full control flow. Instead, the interaction between participants is specified as a **process choreography** — a model focused on message exchanges rather than internal activities. ^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:27-37]

A key challenge is that the logs produced by such platforms typically lack explicit **case identifiers**, making it difficult to reconstruct individual process instances (traces) from raw event data. This is the central problem addressed by this work. ^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:54-58]

## The Uruguayan Interoperability Platform (PDI)

The Uruguayan Digital Government Agency (**AGESIC**) operates a centralized **Interoperability Platform (PDI)** that enables government organizations to expose and consume web services. All inter-organizational service invocations pass through the PDI, which records message metadata (timestamps, requesting organization, requested service, partial identifiers, etc.) but does not assign explicit case identifiers to collaborative process instances. ^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:92-96]

The dataset used in this study covers PDI logs from 2020–2022, totaling approximately **1.7 TB** of raw message metadata. Processing one month of data takes approximately 15 minutes.

## Event Correlation Without Case Identifiers

Because PDI logs lack case identifiers, a **correlation algorithm** must reconstruct coherent event traces from raw, interleaved message records. The authors adapted the algorithm of Motahari-Nezhad et al. (2011), originally designed for web service interaction logs, to the specific characteristics of the PDI data. ^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:60-65]

### Algorithm Design

The adapted algorithm operates in three main stages:

1. **Exploratory Analysis**: Raw records are parsed and structured. Key attributes are identified — timestamps, partial identifiers (TRANSID, GTID), requested services, requesting organizations, and IP addresses. Traditional transaction identifiers proved insufficient for cross-organizational trace reconstruction, motivating attribute-based correlation.

2. **Definition of Correlation Rules**: Three types of rules are applied:
   - **Atomic rules** (`ra`): Filter individual events considered noise based on specific attribute values.
   - **Conjunctive rules** (`rc`): Enforce simultaneous constraints on sequences — temporal windows (e.g., 5-minute threshold), minimum sequence length, and minimum frequency.
   - **Disjunctive rules** (`rd`): Require that at least one event in a sequence satisfies semantic attribute conditions (inclusion filters).

3. **Evaluation and Adjustment**: Candidate sequences are validated against known real-world procedures and through statistical comparison where possible. ^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:60-68]

The algorithm groups consecutive events within a **temporal window** (configurable threshold), applies the rule hierarchy, and retains only recurrent sequences meeting minimum frequency criteria. Output is exported in **XES format** for compatibility with process mining tools such as ProM.

### Trace Export for Choreography Discovery

Generated traces are exported as XES event logs extended for the choreography perspective, including standard attributes (activity name, timestamp, resource) plus custom attributes (source participant, destination participant). These are consumed by a ProM plug-in developed in prior work to discover BPMN 2.0 choreography models. ^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:62-66]

## Case Study: Selected e-Government Processes

Four processes were analyzed using real PDI data:

### 1. Unique State Suppliers Registry (RUPE)
The most significant case. ACCE (State Procurement Regulatory Agency) verifies that a candidate state provider meets all requirements by querying multiple agencies in parallel:
- **AGESIC**: ProviderUpdates / ProviderUpdate
- **DGI** (Tax Directorate): CVA_WS / ExecuteCVA
- **BPS**: GetCertificate / GetCommonCertificate
- **BSE** (State Insurance Bank): ADTCertificate / dayCertificate
- **MIEM** (Ministry of Industry): PYME_Certificate / Get

The discovered choreography model (Figure 3 in the paper) shows these messages executing **in parallel**, reflecting that certificate checks do not follow a strict sequential order.

### 2. Passport Application
Two messages were identified:
- MI → DNIC: Return personal data based on identity identifier.
- DGREC → DNPT: Verify judicial records.

This aligns with the known procedure logic.

### 3. Birth Certificate (CNV)
A multi-participant process involving MSP (Ministry of Public Health), AGESIC, and DGREC (Civil Registry). The key message — "CNV Certificate" between MSP and DGREC — was **statistically validated** by comparing occurrence counts against national birth statistics, confirming correct identification. The complete trace was not fully reconstructed, likely due to the process spanning a longer time window than tested.

### 4. Equity Plan
A monthly monetary benefit administered by MIDES and BPS. Two messages were identified:
- BPS → MIDES: Socioeconomic vulnerability status.
- MIDES → BPS: Equity plan payment service execution.

## Findings and Limitations

**Key findings**:
- Reduced PDI message metadata is sufficient to identify choreographies and discover process models.
- The adapted correlation algorithm is scalable; processing one month of data takes ~15 minutes.
- Discovered choreography models are useful for **conformance checking** — comparing real inter-organizational interactions against expected procedures and detecting deviations.
- Incomplete traces were observed in some cases, pointing to gaps in data registration within the PDI. ^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:15-23]

**Limitations**:
- Single-site case study (Uruguay/AGESIC).
- Event logs cannot be shared publicly due to privacy constraints.
- Only one correlation algorithm was adapted and evaluated; no comparative evaluation against alternatives was performed.

**Future work** includes evaluating alternative correlation algorithms and extending the time window for processes with longer execution spans.

## Relation to Process Mining Concepts

This work sits at the intersection of several process mining challenges:
- **Inter-organizational process mining**: Discovering processes that span organizational boundaries (cf. van der Aalst, 2011).
- **Event correlation / case identification**: Reconstructing traces from logs without explicit case identifiers — a known challenge in [[process-mining-data-science-in-action|process mining]].
- **Collaborative process discovery**: Extending standard discovery to produce BPMN 2.0 choreography diagrams rather than orchestration models.
- **[[sustainability-aware-process-mining|Domain-specific applications]]**: Applying process mining to public sector / e-Government contexts.

The approach complements domain-specific applications such as [[process-mining-healthcare-radiological-workflows|healthcare workflow mining]] and [[process-mining-cybersecurity-attack-flow|cybersecurity attack flow analysis]], demonstrating the breadth of process mining applicability across sectors.

## References

- Antunes, L., Delgado, A., González, L. (2025). *Process Mining for e-Government collaborative processes choreography: a case study*. ICPM 2025 Workshops, Springer LNBIP.
- Motahari-Nezhad, H., Saint-Paul, R., Casati, F. et al. (2011). Event correlation for process discovery from web service interaction logs. *The VLDB Journal*, 20, 417–444.
- Peña, L., Andrade, D., Delgado, A., Calegari, D. (2024). An approach for discovering inter-organizational collaborative business processes in BPMN 2.0. *Process Mining Workshops*, Springer.
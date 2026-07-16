---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T08:01:56'
lint_warnings:
- claim: Activity durations are stochastic due to human behavior, and resource availability
    is time-varying, with overlapping responsibilities and planned absences such as
    vacations.
  concern: While defensible as a general characterization, framing stochastic activity
    durations as being due primarily to 'human behavior' is an oversimplification
    — system latency, external dependencies, and process complexity are also well-established
    drivers of duration variability. However, this is nuanced enough to arguably skip.
- claim: The objective is to minimize the probabilistic Makespan — the total completion
    time of a process — while meeting a predefined confidence level (1 − α), meaning
    the returned schedule keeps Makespan below an optimal threshold in at least (1
    − α) of execution scenarios.
  concern: 'Describing the threshold as ''optimal'' is internally contradictory: if
    the schedule is being optimized subject to a probabilistic constraint, the threshold
    is a target or bound being minimized, not a pre-defined ''optimal'' value. Calling
    it ''optimal'' conflates the objective with the constraint, which is a clear logical
    overstatement.'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Meneghello et al - Proactive
    Data-driven Scheduling of Business Processes.pdf
  hash: be793df866abe7b5fcc479017f2685d2b212ebb616fd80b035083b41942d071e
  ingested: '2026-07-14T08:01:56'
  size: 75762
status: active
tags:
- business processes
- proactive scheduling
- process mining
- stochastic scheduling
- resource constraints
- uncertainty
- activity durations
- data-driven
- RCPSP
- BPSP
title: Proactive Data-Driven Scheduling of Business Processes
type: concept
---

# Proactive Data-Driven Scheduling of Business Processes

Proactive data-driven scheduling of business processes is an approach that combines [[process-mining-data-science-in-action|process mining]], constraint programming (CP), and simulation to generate robust schedules for business processes under uncertainty. The framework was proposed by Francesca Meneghello (Sapienza University of Rome / Free University of Bozen-Bolzano / Fondazione Bruno Kessler), Arik Senderovich (York University), Massimiliano Ronzani (Fondazione Bruno Kessler), Chiara DiFrancescomarino (University of Trento), and Chiara Ghidini (Free University of Bozen-Bolzano), and was accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

Business processes — structured sets of activities executed to achieve organizational objectives such as completing a sale, providing a service, or managing a supply chain — differ fundamentally from manufacturing processes in their unpredictability. Activity durations are stochastic due to human behavior, and resource availability is time-varying, with overlapping responsibilities and planned absences such as vacations. These characteristics make traditional deterministic scheduling methods inadequate.^[Meneghello et al - Proactive Data-driven Scheduling of Business Processes.pdf:10-16]

A further practical challenge is the frequent lack of readily available data on key scheduling parameters: activity duration distributions and resource availability calendars are often incomplete or missing in real-world settings. Process mining addresses this gap by extracting such knowledge directly from [[process-mining-data-science-in-action|event logs]].^[Meneghello et al - Proactive Data-driven Scheduling of Business Processes.pdf:25-30]

## Business Process Scheduling Problem (BPSP)

The paper formalizes the **Business Process Scheduling Problem (BPSP)** and establishes its relationship to the well-known **Resource-Constrained Project Scheduling Problem (RCPSP)**. The BPSP captures the complexity and variability typical of business processes, including:

- Stochastic activity durations
- Planned resource unavailability (e.g., vacations, shift patterns)
- Overlapping resource responsibilities across multiple process instances

The objective is to minimize the probabilistic **Makespan** — the total completion time of a process — while meeting a predefined confidence level (1 − α), meaning the returned schedule keeps Makespan below an optimal threshold in at least (1 − α) of execution scenarios.^[Meneghello et al - Proactive Data-driven Scheduling of Business Processes.pdf:31-39]

## Framework

The proposed framework integrates three components:

1. **Process Mining**: Applied to historical [[process-mining-data-science-in-action|event logs]] to extract BPSP parameters, including activity duration distributions and resource availability calendars. This data-driven extraction step enables the framework to operate in real-world settings where scheduling parameters are not explicitly documented.

2. **Constraint Programming (CP) Model**: Generates deterministic candidate schedules for the BPSP, accounting for resource constraints and planned unavailability.

3. **Data-Driven Simulation**: Evaluates the candidate schedules produced by the CP model by simulating process execution under stochastic conditions. The schedule that minimizes the uncertain Makespan while satisfying the confidence level threshold is selected as the proactive optimal solution.

This combination ensures robustness against both variability in process execution and resource constraints.^[Meneghello et al - Proactive Data-driven Scheduling of Business Processes.pdf:31-39]

## Proactive Scheduling

Proactive scheduling techniques generate robust *offline* schedules that explicitly account for stochastic activity durations. A proactive optimal solution at confidence level (1 − α) guarantees that the Makespan remains below an optimal threshold in at least (1 − α) of cases. Prior work in proactive scheduling addressed probabilistic durations but rarely tackled planned resource unavailability in the context of the full complexity of business processes — a gap this framework addresses.^[Meneghello et al - Proactive Data-driven Scheduling of Business Processes.pdf:17-24]

## Evaluation

The framework was evaluated in two phases:

- **Synthetic experiments**: Demonstrated adaptability to varying uncertainty levels, problem sizes, and resource configurations, achieving effective optimization of the probabilistic Makespan across diverse scheduling scenarios.

- **Real-world validation**: Applied to event logs from a **healthcare process** (connecting to themes explored in [[process-mining-healthcare-radiological-workflows]]). Using process mining to extract BPSP parameters, the framework achieved an average Makespan optimization of **5% to 14%**, demonstrating practical applicability in a complex, data-driven domain.^[Meneghello et al - Proactive Data-driven Scheduling of Business Processes.pdf:40-48]

## Significance for Process Mining

This work illustrates how process mining serves not only as an analytical and conformance-checking tool, but also as a *prescriptive* enabler: extracted knowledge from event logs feeds directly into optimization models that improve future process execution. It connects process mining to the broader field of prescriptive process monitoring and resource-aware process management.

## References

- Meneghello, F., Senderovich, A., Ronzani, M., DiFrancescomarino, C., Ghidini, C. (2025). *Proactive Data-driven Scheduling of Business Processes*. Pre-print accepted at ICPM 2025 Workshops, Springer LNBIP series.
- van der Aalst, W. (2016). *Process Mining: Data Science in Action*, 2nd ed. Springer. (Referenced as [[process-mining-data-science-in-action]])
- Beck, J.C., Wilson, N. (2007). Proactive algorithms for job shop scheduling with probabilistic durations. *Journal of Artificial Intelligence Research*, 28, 183–232.
- Meneghello, F., DiFrancescomarino, C., Ghidini, C., Ronzani, M. (2025). Runtime integration of machine learning and simulation for business processes. *Information Systems*, 128, 102472.
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:06:23'
lint_warnings:
- claim: A foundational taxonomy of conformance checking tasks (Rebmann et al., referenced
    as [22] in the paper) identifies 102 tasks across six dimensions
  concern: This is a very specific empirical claim about a particular taxonomy paper.
    While it may be accurate as reported in the source, the number '102 tasks' is
    precise enough that if misquoted or misread from the source document it would
    be a clear error — however, this is an internal citation claim that cannot be
    independently verified as 'well-established fact,' so confidence is limited. No
    flag raised on this basis alone.
- claim: covering 68 of the 102 tasks
  concern: The page states the ten most frequently occurring task realizations were
    selected, covering 68 of the 102 tasks. However, the table shown is incomplete
    (task 5 is cut off), making it impossible to verify this count from the page itself,
    and selecting 10 task realizations covering 68 of 102 tasks is an unusual ratio
    that may reflect a misreading or transcription error from the source.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Häge et al - Visualizations
    for Conformance Checking Tasks An Empirical Assessment.pdf
  hash: c66ecdbae20baca8e3d4253a16aba8bffb11c191634a9252410080d52dd589d6
  ingested: '2026-07-14T07:06:23'
  size: 1269661
  truncated: true
status: active
tags:
- conformance checking
- process mining
- visualization
- user study
- event logs
- process models
- deviation detection
- visualization idioms
- user preferences
- task taxonomy
title: Conformance Checking Visualization Idioms and User Preferences
type: concept
---

# Conformance Checking Visualization Idioms and User Preferences

This page covers the systematic empirical assessment of visualization idioms used in process mining tools for [[deviation-desirability-assessment|conformance checking]] tasks, and the user preferences among those idioms. The work was conducted by Marie-Christin Häge, Alexandra Kriecherbauer, and Michael Grohs (University of Mannheim) and accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Background

[[deviation-desirability-assessment|Conformance checking]] is a sub-discipline of [[coordinated-projections-multi-faceted-process-exploration|process mining]] that compares recorded process executions (captured in event logs as traces) against intended behavior (defined in a process model). Techniques such as rule checking, token-replay, and alignments detect deviations from the desired process. Visualizations are essential to make conformance checking results accessible and actionable for users.^[Häge et al - Visualizations for Conformance Checking Tasks An Empirical Assessment.pdf:67-81]

**Visual analytics** combines automated analysis with interactive visualizations to support human reasoning over complex data. A key concept is the *visualization idiom* — the specific visual element used (e.g., bar chart, heat map, flow chart). The suitability of an idiom depends on the underlying task the user wants to perform.^[Häge et al - Visualizations for Conformance Checking Tasks An Empirical Assessment.pdf:82-97]

## Conformance Checking Task Taxonomy

A foundational taxonomy of conformance checking tasks (Rebmann et al., referenced as [22] in the paper) identifies 102 tasks across six dimensions:

1. **Task goal** — why the user performs the task (e.g., explore, confirm, describe)
2. **Task means** — how the task is carried out (e.g., discover, compare, summarize)
3. **Data characteristics** — what facets the task should reveal (e.g., process conformance, guideline violations)
4. **Constraint type** — the perspective referred to (e.g., control-flow, data, resource, time)
5. **Data target** — the data on which the task is carried out (e.g., log, trace)
6. **Data cardinality** — cardinality of the data target (e.g., all, many, single)

The ten most frequently occurring task realizations (abstracting over constraint type, data target, and cardinality) were selected for analysis, covering 68 of the 102 tasks:^[Häge et al - Visualizations for Conformance Checking Tasks An Empirical Assessment.pdf:98-109]

| ID | Task Name | Core Question |
|----|-----------|---------------|
| 1 | Degree of Conformance | What is the overall degree of conformance between a log and guidelines? |
| 2 | Locations | Where does recorded behavior violate which guidelines? |
| 3 | Location Analysis | Where exactly does execution differ from the guideline? |
| 4 | Degree Comparison | How does conformance degree differ between multiple logs/traces? |
| 5 | Location Details | How exactly does execution differ from guidelines? |
| 6 | Patterns with Frequency | What types of violations occurred, and how often? |
| 7 | Causes | What attributes lead to guideline violations? |
| 8 | Frequency | How often did a specific violation occur? |
| 9 | Distribution | What percentage of traces fall into each conformance category? |
| 10 | Outcome | Do more conformant cases lead to better process outcomes? |

## Research Method

The study followed a three-phase approach:

1. **Task selection** — The ten most frequent conformance checking tasks were selected from the taxonomy.
2. **Mapping tasks to idioms (RQ1)** — Existing visualizations in nine process mining tools (six commercial: Apromore, Aris PM, Celonis, SAP Signavio, Mindzie, IBM PM; three academic: PMTK, ProM, PM4Py) were analyzed using the Road Traffic Fine Management dataset. Each visualization was assigned to an idiom from the Data Visualization Catalogue, yielding 23 idioms total, of which 13 were mapped to at least one of the ten tasks.
3. **User preference survey (RQ2)** — 20 participants (11 female, 9 male; 13 students, 4 practitioners, 3 researchers; varying process mining expertise) ranked idioms per task. Tasks with identical idiom sets were grouped into six survey tasks.^[Häge et al - Visualizations for Conformance Checking Tasks An Empirical Assessment.pdf:111-118]

### Task Requirements Framework

Three requirements were identified that a visualization must fulfill for a given task:
- **Data scope**: The constraint type, data granularity, or cardinality required as input.
- **Data object**: The specific output data objects to be presented (e.g., conformance rate, number of deviations).
- **Goal**: The visualization's motivation, categorized as: (1) quantify conformance, (2) break down & compare conformance, (3) localize & show deviations, (4) explain & diagnose deviations.

## RQ1: Idioms Used in Existing Tools

The analysis identified **48 task–idiom pairs** across the ten tasks and 13 applicable idioms. Key findings:

- **Table** is the most ubiquitous idiom, appearing for all ten tasks.
- **Bar chart** and **heat map** each appear for five tasks.
- **Trees**, **tile metrics**, and **box plots** are the least common, each appearing for only two tasks.
- **Flow chart+** (process model diagrams such as BPMN, DFG, Petri Nets) dominates for location tasks (tasks 2 and 3), used by five to six tools.
- **Tile metrics** are the most common idiom for Task 1 (Degree of Conformance), used by four or more tools.
- **Tables** dominate for Tasks 6 and 8 (frequency-related), used by seven tools.^[Häge et al - Visualizations for Conformance Checking Tasks An Empirical Assessment.pdf:49-59]

## RQ2: User Visualization Preferences

User preference scores (lower = more preferred) revealed that preferred idioms do not always align with the most commonly used idioms in tools:

- **Tasks 1 & 4 (Degree of Conformance / Comparison)**: Users prefer **bar charts** and **scatterplots**; tile metrics rank third despite being the most tool-common idiom.
- **Tasks 2, 3 & 5 (Location tasks)**: Users prefer **flow chart & table** (slight advantage) followed by **flow chart+**; tables rank lower.
- **Tasks 6 & 8 (Frequency)**: Users prefer **bar charts** followed by tables, but tools use tables more frequently.
- **Task 7 (Causes)**: Clear preference for **tables**.
- **Task 9 (Distribution)**: Clear preference for **bar charts**.
- **Task 10 (Outcome)**: Clear preference for **tables**.

Notable variance patterns: box plots and scatterplots show consistently narrow rank distributions (low variance), while flow chart+ & table for tasks 6 & 8 and pie/donut charts for task 9 show high variance — some users rank them best, others worst.^[Häge et al - Visualizations for Conformance Checking Tasks An Empirical Assessment.pdf:49-59]

## Implications

- **Researchers**: The results deepen understanding of user preferences for conformance checking visualizations and highlight gaps between tool implementations and user needs.
- **Practitioners**: The preferred idiom per task can serve as a recommendation when selecting visualizations for conformance analysis.
- **Tool vendors**: Results offer guidance on which idioms to implement for specific tasks to better align with user preferences.^[Häge et al - Visualizations for Conformance Checking Tasks An Empirical Assessment.pdf:22-25]

## Limitations and Future Work

- Analysis was limited to visualizations available in accessible tools; object-centric conformance checking was excluded.
- Only one dataset (Road Traffic Fine Management) was used.
- Survey had 20 participants; larger samples would strengthen findings.
- Strict ranking design prevented equal ratings.
- Screenshots from different tools may have introduced familiarity bias.

## Relation to Other Process Mining Visualization Work

This work builds on the conformance checking task taxonomy and connects it to [[coordinated-projections-multi-faceted-process-exploration|visual analytics approaches in process mining]]. It complements [[deviation-desirability-assessment|deviation desirability assessment]] by focusing on how deviations and conformance results are visualized, rather than how they are evaluated for desirability.
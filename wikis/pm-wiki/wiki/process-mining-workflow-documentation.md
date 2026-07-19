---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:49:44'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Lu et al - Documenting Process
    Mining Workflows.pdf
  hash: 2117313472c575143a52127de447a952050c063f3f5fc6d0697c471aa1911966
  ingested: '2026-07-14T07:49:44'
  size: 450929
  truncated: true
status: active
tags:
- process mining
- workflow documentation
- reproducibility
- structured logging
- event logs
- process discovery
- conformance checking
- educational settings
- logging template
- thematic coding
title: 'Documenting Process Mining Workflows: Structured Logging in Educational Settings'
type: concept
---

# Documenting Process Mining Workflows: Structured Logging in Educational Settings

This page covers a study by Xixi Lu, Iris Beerepoot, Niels Martin, Elisabetta Benevento, Carlos Fernández-Llatas, Thomas Grisold, Mieke Jans, Owen Johnson, Agnes Koschmider, Suhwan Lee, Hajo A. Reijers, Marcos Sepúlveda, Alessandro Stefanini, and Moe Wynn, accepted at the ICPM 2025 Workshops (Springer LNBIP series). The paper addresses the lack of structured, reproducible documentation in [[process-mining-data-science-in-action|process mining]] workflows and proposes a lightweight logging template piloted in a graduate-level course.^[Lu et al - Documenting Process Mining Workflows.pdf:17-35]

## Motivation

[[process-mining-data-science-in-action|Process mining]] workflows are typically exploratory and iterative, involving preprocessing, discovery, conformance checking, and enhancement steps. Despite methodological advances, reproducibility, traceability, and workflow transparency remain insufficiently supported. Most tools lack support for reusable workflows or context-specific customization. Without analytic provenance — structured records of how data and models are transformed — stakeholders cannot retrace the steps that led to specific insights or evaluate how preprocessing decisions affected outcomes.^[Lu et al - Documenting Process Mining Workflows.pdf:45-54]

This problem is especially acute in educational settings, where transparency is essential for reflection and learning. A review of BPI Challenge 2020 submissions found that only a small fraction of papers reported which techniques were used, making it nearly impossible to trace how process models were generated. Similarly, studies on process mining using unstructured data found that only a minority provided source code, datasets, or research method descriptions.^[Lu et al - Documenting Process Mining Workflows.pdf:55-69]

Real-world event logs compound the problem: they often contain missing or inconsistent data, duplicate events, misaligned timestamps, or heterogeneous case structures, requiring extensive preprocessing. Yet preprocessing is frequently undocumented and executed ad-hoc, with little methodological support for selecting appropriate techniques.^[Lu et al - Documenting Process Mining Workflows.pdf:70-76]

## The Logging Template

To support transparent documentation of [[process-mining-data-science-in-action|process mining]] workflows, the authors designed a lightweight, tool-agnostic structured logging template. The template captures:

- **Business question**: The analytical goal driving the workflow.
- **Order**: Sequential step number indicating the order of operations.
- **Activity**: A brief description of the operation performed (e.g., Data Import, Filtering, Discovery).
- **Tool**: The software, library, or platform used (e.g., PM4Py, ProM, Disco, Python).
- **Parameters / Configuration**: Configuration details or parameter settings applied (e.g., filter thresholds, miner selection, case ID settings).
- **Purpose**: The goal or intention behind the step (e.g., Remove noise, Improve fitness).
- **Outcome / Notes**: Observed results, relevant observations, or comments (e.g., data reduction, model type).

The template is intentionally lightweight, requiring manual input but designed to facilitate easy documentation. Structurally, it mirrors the concept of an event log, making it familiar to process mining practitioners. It is intended to bridge the gap between informal notes and heavyweight integrated provenance systems such as RapidProM or distributed pipeline platforms.^[Lu et al - Documenting Process Mining Workflows.pdf:77-87]

### Example Workflow Log Entry

| Order | Activity | Tool | Parameters/Config | Purpose | Outcome/Notes |
|-------|----------|------|-------------------|---------|---------------|
| 1 | Data Import | PM4Py | – | Load XES log | File successfully loaded |
| 2 | Preprocessing | Python (pandas) | Removed empty cases | Clean noisy data | Reduced from 10k to 9.2k cases |
| 3 | Discovery | ProM (Inductive Miner) | Default settings | Discover process model | Obtained a sound model with loops |

## Pilot Study

The template was piloted in a graduate-level [[teaching-process-mining-challenges|process mining course]]. Ten student groups (four members each) performed process mining projects, each selecting one real-world event log (BPIC14, Sepsis, or BPIC19) and formulating two to three business questions. Completion of the logging template was voluntary; four out of ten groups participated and provided consent for their data to be included.^[Lu et al - Documenting Process Mining Workflows.pdf:90-96]

The four participating groups submitted logbooks covering 16 individual analyses, with a combined total of 151 documented steps. The number of logged steps per analysis ranged from 5 to 22.^[Lu et al - Documenting Process Mining Workflows.pdf:90-96]

## Results

### Business Question Categorization

Thematic coding of the 16 business questions yielded six themes:

1. **Process comparison** (5 questions, 31%): Differences across groups such as priority levels, patient age groups, or closure codes. The most broadly applicable type, present in all four teams.
2. **Compliance (SLA adherence)** (5 questions): Often combined with impact/causal analysis.
3. **Impact/causal analysis** (7 questions, 44%): Frequently conducted as a follow-up to explain non-compliance, rework, or performance issues.
4. **Pattern discovery**: Identification of recurring behaviors or structures.
5. **Process prediction**: Predicting active cases likely to become stuck.
6. **Performance analysis** (4 questions): Bottleneck detection, resolution time, case duration.

Two distinct analytical approaches were observed: (1) starting with a simple question and breaking it into sub-questions (shorter, focused analyses), and (2) formulating a complex question guiding multiple consecutive steps within a single cohesive analysis.^[Lu et al - Documenting Process Mining Workflows.pdf:97-101]

### Workflow Activity Categorization

Across 151 logged steps, students reported approximately 80 distinct activities. After thematic coding and merging duplicates, 12 main activity categories were identified:

- **Analysis** (42 occurrences across 11 of 16 cases): Sub-activities include resource analysis, performance analysis, and comparison.
- **Preprocessing** (38 occurrences across 13 cases): Sub-activities include filtering (15), enriching (6), and bucketing (5). Bucketing — creating sublogs using attributes or conditions — was frequently combined with comparison.
- **Data import**, **Visualization**, **Process discovery**, and **Conformance/compliance checking** were also common.
- **Optimization** and **Prediction** appeared only in specific contexts.

The most frequently reported individual activities were discovery (27 steps), data import (18), preprocessing (15), and data export (5).^[Lu et al - Documenting Process Mining Workflows.pdf:97-101]

### Tool Usage

Tools were categorized into four main families:

- **Python** (75 steps): Primarily data handling (pandas, numpy), custom logic, and visualization.
- **PM4Py** (57 steps): Filtering, Inductive Miner, conformance checking, log statistics, DFG Miner, Declare.
- **Disco** (16 steps): Process map view most frequently cited.
- **Other** (3 steps): Machine learning tools and Cortado.

Many entries did not specify the exact module or functionality used within a tool family, limiting reproducibility.^[Lu et al - Documenting Process Mining Workflows.pdf:97-101]

### Template Field Utilization

The **Activity**, **Tool**, and **Purpose** fields were consistently filled for all 151 steps. However:

- **Parameters / Configuration**: Left blank or marked with a dash in 19 entries (13%). Only about 10 entries included concrete configurations (e.g., filter conditions, miner parameters).
- **Outcome / Notes**: Ranged widely from quantitative results (e.g., "ROC-AUC = 0.826", "Reduced from 1050 to 782 cases") to high-level qualitative observations, often lacking detail required for reproducibility.

^[Lu et al - Documenting Process Mining Workflows.pdf:92-96]

## Lessons Learned and Recommendations

### Strengths of the Template

For standard tasks — data import, log filtering, process map discovery, basic visualizations — the template supported clear and consistent documentation. Students familiar with tools like PM4Py and Disco were able to report these steps effectively.^[Lu et al - Documenting Process Mining Workflows.pdf:92-96]

### Challenges

For exploratory or customized analyses (e.g., creating new variables, integrating external data, scripting custom logic in Python), entries were often less structured, with activity labels sometimes misaligned with described purposes and parameter settings described only at a high level.^[Lu et al - Documenting Process Mining Workflows.pdf:94-96]

### Recommendations

1. **Shared vocabulary / ontology**: Develop a shared ontology or repository categorizing common process mining activities (import, preprocessing, discovery, conformance checking) with finer-grained subcategories (filtering, abstraction, enrichment) and linking tools and techniques to each activity.
2. **Standardization of parameters and results**: Encourage detailed reporting of parameter values, expected outcomes, and rationale. Tool developers could support this by printing standardized configuration messages that can be copied directly into logging reports.
3. **Automated tool support**: An interactive logging tool could guide users step-by-step with built-in consistency checks — for example, selecting "data import" could trigger a list of relevant tools with incompatible options disabled.
4. **Support for concurrent/parallel workflows**: Future template versions should support parallel branches or concurrent sub-workflows (e.g., applying the same steps to multiple filtered sublogs), through grouping mechanisms or step references.

^[Lu et al - Documenting Process Mining Workflows.pdf:97-101]

## Relation to Existing Work

The study builds on prior taxonomies of [[event-log-extraction-clinical-narratives|event log]] preprocessing tasks (e.g., Marin-Castro & Tello-Leal's review of 70 papers; Van Zelst et al.'s taxonomy of event abstraction techniques; Liu et al.'s six high-level and 22 low-level preprocessing tasks). It contrasts with heavyweight provenance systems (RapidProM, distributed pipeline platforms) by proposing a lightweight, tool-agnostic alternative suited for heterogeneous tool ecosystems (Disco, Celonis, PM4Py, Python, ProM) common in educational and exploratory settings.^[Lu et al - Documenting Process Mining Workflows.pdf:103-118]

The work is closely related to [[teaching-process-mining-challenges|challenges in teaching process mining]], as structured documentation supports reflection, learning, and knowledge sharing in educational contexts. It also connects to [[wearable-data-event-log-enrichment|event log enrichment]] research, where preprocessing transparency is equally important.

## Limitations

The pilot was limited to four student groups in a single graduate-level course. The tools and questions were constrained by course content, excluding tools such as BupaR. Future work aims to improve the template and repeat the study in different settings.^[Lu et al - Documenting Process Mining Workflows.pdf:90-96]
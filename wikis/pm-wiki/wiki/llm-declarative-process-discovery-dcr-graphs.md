---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:17:30'
lint_warnings:
- claim: DCR graphs are considered to have lower cognitive load than the Declare language
    due to fewer constraint patterns.
  concern: Declare typically has around 12-18 commonly used constraint templates,
    while DCR graphs also have multiple constraint types. The claim that DCR has fewer
    constraint patterns and therefore lower cognitive load is a contested research
    finding, not a well-established fact, but more critically the direction of the
    comparison is questionable — DCR graphs are generally considered more expressive
    and complex, not simpler, than basic Declare templates.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Lindner et al - Discovering
    Declarative Processes in Textual Descriptions using Large Language Models.pdf
  hash: b48d709a3ee66a8f2c6637d2df7295814b801aeea2fd6c3ee0a515c192205c40
  ingested: '2026-07-14T07:17:30'
  size: 1283584
  truncated: true
status: active
tags:
- declarative process models
- process mining
- text-to-process extraction
- prompt engineering
- constraint mining
- natural language processing
- normative text
- process discovery
- LLM architecture
- compliance
title: LLM-Based Discovery of Declarative Processes as DCR Graphs
type: technology
---

# LLM-Based Discovery of Declarative Processes as DCR Graphs

This page covers the use of Large Language Models (LLMs) and prompt engineering to extract declarative process models — specifically **DCR (Dynamic Condition Response) graphs** — from natural language business process descriptions. The work was presented by Jonas M. Lindner and Hugo A. López (Technical University of Denmark) at the ICPM 2025 Workshops.

## Background and Motivation

Process models are central artifacts in [[process-mining-handbook|process mining]] and Business Process Management (BPM), enabling understanding, analysis, compliance checking, and automation of processes. Two broad families of process models exist:

- **Imperative models** (e.g., BPMN, Petri nets): specify the exact sequence of activities.
- **Declarative models** (e.g., DCR graphs, Declare): specify rules and constraints that executions must satisfy, leaving freedom in how they are fulfilled.

Normative texts — such as service operating procedures (SOPs), clinical guidelines, and legal regulations — describe how processes *should* behave. Mining declarative process models from these texts produces reference models that can be compared against actual process executions, supporting organizational compliance tasks (see [[deviation-desirability-assessment]]). ^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:27-35]

Manual elicitation of declarative models from text is complex: it requires understanding the semantics of the modelling language and resolving linguistic ambiguities. Prior NLP-based approaches (e.g., Named Entity Recognition, Part-of-Speech tagging, pattern matching) have struggled to generalize across writing styles and linguistic variation. ^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:36-83]

## DCR Graphs

A **DCR graph** is a formal process modelling notation designed for knowledge-intensive processes. It consists of:

- **Events** (labelled boxes): activities or actions in the process.
- **Roles**: access control and collaboration constraints assigned to events.
- **Typed constraints** between events:
  - *Condition* (e →• f): f cannot execute until e has executed or is excluded.
  - *Response* (e •→ f): when e executes, f becomes pending and must eventually occur or be excluded.
  - *Dynamic Inclusion* (e →+ f): executing e includes f among possible actions.
  - *Dynamic Exclusion* (e →% f): executing e excludes f from possible actions.
  - *Milestone* (e →◆ f): if e is pending, f cannot be enabled.

DCR graphs are used in large-scale digitalization projects in the public sector and are considered to have lower cognitive load than the Declare language due to fewer constraint patterns. ^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:96-116]

## LLM-Based Discovery Architecture

Lindner and López propose a **bottom-up prompt engineering pipeline** that:

1. Identifies **roles** first (simplest concepts).
2. Identifies **events** assigned to those roles.
3. Identifies **constraints** between discovered events.

Two pipeline variants were evaluated:
- **Pipeline A**: identifies all constraint types simultaneously.
- **Pipeline B**: identifies each constraint type individually (task breakdown).

Five prompts of increasing complexity were defined:
| Prompt | Description |
|--------|-------------|
| 1 | Simple: context, task, output format, instructions, process description |
| 2 | Adds in-context learning with DCR definitions |
| 3 | Adds a correct one-shot example |
| 4 | Adds one correct and one false example (three-shot) |
| 5 | Adds annotation guidelines for legal/business process descriptions |

**Retrieval Augmented Generation (RAG)** was applied in prompts 2–5, providing the LLM with a DCR knowledge document and annotation guidelines as additional context.

Because generating consistent XML output proved difficult, the LLM was instructed to output **JSON**, which was then converted to XML. An output validation loop re-ran the pipeline on invalid outputs (up to a configurable maximum number of retries). ^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:64-70]

## Models Used

The experiments used small, locally runnable open-source LLMs to support reproducibility and integration with local modelling environments:

| Model | Parameters | Size |
|-------|-----------|------|
| Llama 3.1 | 8B | 4.7 GB |
| Llama 3.2 | 3B | 2 GB |

## Evaluation Methodology

### Gold Standard
Ten business process descriptions were manually annotated following adapted annotation guidelines (originally designed for legal texts). The gold standard comprised 215 events, 41 roles, and 188 constraints across 121 sentences. ^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:64-70]

### Similarity Thresholds
Since LLM outputs may be semantically equivalent but syntactically different from gold standard labels, **SBERT** (Sentence-BERT) cosine similarity was used for matching:
- Roles threshold: **0.7**
- Events threshold: **0.4**

### Metrics
Precision, Recall, and F1-score were computed for roles, events, role-event assignments, and constraints. Each pipeline/prompt/model combination was run **10 times per process description** (2,000 total runs) to account for LLM non-determinism.

## Key Results

### Internal Validation
- **Events**: consistently high precision (>0.90) across all prompts and models; F1 scores above 0.6 throughout.
- **Roles**: precision and recall mostly above 0.5; Llama 3.1 generally outperformed Llama 3.2 in F1.
- **Constraints**: near-zero F1 for prompts 1–2; marginal improvement with examples (prompts 3–5), but still very low (F1 ≈ 0.01–0.03).
- Pipeline B (task breakdown) increased LLM response time for constraints by ~2.8× without improving constraint F1.
- Llama 3.1 had more generation errors (66/100 successful on average) vs. Llama 3.2 (95/100).
- Adding more prompt detail did not produce a consistent performance trend, partly due to increased hallucination with longer prompts. ^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:7-23]

### External Validation (vs. DCR Highlighter)
Comparison against the commercial **DCR Highlighter** NLP tool showed:
- LLM pipelines achieved up to **50% higher precision** than the DCR Highlighter on roles.
- The DCR Highlighter had higher recall on roles (0.75) but lower overall F1 (average 0.31 vs. 0.38–0.53 for best LLM configurations).
- The DCR Highlighter cannot automatically discover constraints; LLM pipelines, while weak, provide at least partial automated constraint discovery.

| Entity | DCR Highlighter F1 | Llama3.1-A-3 F1 | Llama3.1-B-3 F1 |
|--------|-------------------|-----------------|------------------|
| Roles | 0.44 | 0.62 | 0.73 |
| Events | 0.49 | 0.77 | 0.74 |
| Role-Event | 0.31 | 0.58 | 0.62 |
| Constraints | 0.00 | 0.02 | 0.02 |

^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:68-70]

## Findings and Limitations

- LLMs are effective at extracting **events and roles** from process descriptions, as these concepts are language-independent and do not require deep DCR semantics.
- **Constraint mining** remains the hardest sub-task; current LLM pipelines are insufficient for fully automated constraint extraction.
- LLMs hallucinate more with longer prompts; precise task descriptions and explicit prohibitions help reduce hallucination rates.
- The pipeline is recommended as a **supportive tool** for human modellers rather than a fully automated system. ^[Lindner et al - Discovering Declarative Processes in Textual Descriptions using Large Language Models.pdf:7-23]

## Future Work

- Extending the gold standard dataset with more annotated process descriptions.
- Evaluating larger LLMs (e.g., GPT-4, Llama 3 70B).
- Exploring additional prompting strategies and evaluation metrics.
- Applying the pipeline to regulatory texts: clinical guidelines, legal contracts.
- Integrating the pipeline as a supportive component in DCR graph modelling tools (e.g., DCR-js).
- Revising and publishing updated annotation guidelines for business process descriptions.

## References

- Lindner, J. M. & López, H. A. (2025). *Discovering Declarative Processes in Textual Descriptions using Large Language Models*. ICPM 2025 Workshops, Springer LNBIP.
- Hildebrandt, T. T. & Mukkamala, R. R. (2011). *Declarative event-based workflow as distributed dynamic condition response graphs*. arXiv:1110.4161.
- Friedrich, F., Mendling, J. & Puhlmann, F. (2011). *Process model generation from natural language text*. CAiSE, Springer.

## Key Data

- P recision= true positive
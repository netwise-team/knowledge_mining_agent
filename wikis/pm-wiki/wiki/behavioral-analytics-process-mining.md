---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:37:50'
lint_warnings:
- claim: The Event Data and Behavioral Analytics (EdbA) workshop at the International
    Conference on Process Mining (ICPM) is the only dedicated venue for exploring
    behavior-centric perspectives in process mining.
  concern: This is an overstated absolute claim. There are other workshops and venues
    in the broader process mining and BPM communities that address behavior-centric
    perspectives, and asserting exclusivity based on a single paper's scope is not
    verifiable as a well-established fact.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Van Suetendael et al - Behavioral
    Analytics What does that even mean.pdf
  hash: d8b965d593cdfcb02980a5be550762f2f48a94250789caa850a9ffe2be168a70
  ingested: '2026-07-14T07:37:50'
  size: 605495
  truncated: true
status: active
tags:
- behavioral analytics
- process mining
- behavior
- event data
- conformance checking
- process discovery
- performance analysis
- conceptualization
- qualitative analysis
- theory-building
title: Behavioral Analytics in Process Mining
type: concept
updated: '2026-07-14'
---

# Behavioral Analytics in Process Mining

**Behavioral Analytics** is an emerging sub-field of [[process-mining-data-science-in-action|process mining]] concerned with the systematic analysis of behavior as captured in event data. Despite behavior being a foundational concept underlying techniques such as process discovery, [[deviation-desirability-assessment|conformance checking]], and performance analysis, the term has historically been used without explicit conceptualization in the process mining literature.^[10-16]

This page synthesizes findings from Van Suetendael et al. (2025), *"Behavioral Analytics: What does that even mean?"*, accepted at the ICPM 2025 Workshops (Springer LNBIP series), which provides the first systematic exploration of how behavior and behavioral analytics are understood within the process mining community.

## Motivation

In a process mining context, behavior typically refers to the observable dynamics of a process as it unfolds over time: sequences of activities, branching choices, repetitions, and timing patterns. Behavioral aspects are central to process discovery, [[deviation-desirability-assessment|conformance checking]], and performance analysis. Yet despite this foundational role, the notion of behavior is often *assumed* rather than explicitly defined.^[39-46]

This lack of conceptual clarity creates several problems:
- It hinders the development of more precise analysis techniques (e.g., distinguishing individual behavior from collective behavior).
- It complicates communication across research efforts, as different studies may implicitly use divergent interpretations.
- It makes it difficult to compare findings or build cumulatively on prior work.^[46-52]

## The EdbA Workshop

The **Event Data and Behavioral Analytics (EdbA)** workshop at the International Conference on Process Mining (ICPM) is the only dedicated venue for exploring behavior-centric perspectives in process mining. It explicitly focuses on understanding, modeling, and analyzing behavior within event data. Van Suetendael et al. analyzed all 39 papers published at EdbA from 2020–2024, of which 27 met inclusion criteria (explicitly addressing behavior or behavioral analytics).^[53-60]

Notably, *none* of the 27 papers explicitly defined what they understood as behavior or behavioral analytics — all mentions were implicit.

## Methodology: Straussian Grounded Theory

The study applied **Straussian Grounded Theory (SGT)**, an inductive qualitative method that integrates existing literature throughout the research process. Three coding stages were used:

1. **Open Coding**: 247 distinct codes were identified from the 27 papers.
2. **Axial Coding**: The 247 codes were grouped into 44 code categories by identifying underlying structures and connections.
3. **Selective Coding**: The 44 categories were refined into **9 major themes**, forming the basis for two conceptual frameworks.^[70-75]

## The Behavior Framework

The Behavior Framework describes the core components of behavior in a process mining context:

- **Action**: The smallest unit of behavior (also called event, move, or state change). Examples include atomic instant actions such as "click a button". Actions appear in 15 of the 27 analyzed papers.
- **Activity**: A high-level act of behavior consisting of one or more actions. Activities represent a higher level of granularity. 14 of 27 papers described behavior at multiple levels of granularity.
- **Time Aspect**: Each action has a timestamp (or multiple timestamps, e.g., start and end) that establishes ordering. Duration is treated as a derived attribute rather than a time aspect.
- **Attributes**: Contextual information about behavior, such as location, priority, or purpose. Attributes can be instance-specific or summarize patterns across behavior types.
- **Entity**: The actor performing the action — human, animal, human-engineered system, or natural system. Each action is performed by exactly one entity.
- **Object**: Something on or with which behavior is performed (e.g., a document). Distinct from entities: objects are acted upon, while entities perform actions.
- **Dependencies**: Control-flow relations between activities, such as direct succession, causality, concurrency, or choice.

## The Behavioral Analytics Framework

The Behavioral Analytics Framework describes any behavioral analytics endeavor along **four dimensions**:

### 1. Entity
The type of actor performing the behavior:
- Human (13 papers)
- Human-engineered system (17 papers)
- Animal (1 paper)
- Natural system (1 paper)

### 2. Behavioral Pattern
The phenomenon of interest that frames the scope of analysis. 18 distinct behavioral patterns were identified across the workshop papers. The most common were:
- Process behavior (7 papers)
- Routine behavior (3 papers)
- Anomalous behavior (2 papers)
- Daily behavior (2 papers)

Other patterns included foraging behavior, switch behavior, collaborative work, and user journeys.

### 3. Goal
The intended outcome of the analysis. Goals identified include:
- **Visualizing behavior** (20 papers) — most common
- **Uncovering behavior** (19 papers)
- **Collecting behavior** (3 papers)
- **Learning patterns** (3 papers)
- **Comparing behavior** (1 paper)
- **Measuring behavior** (1 paper)

Goals often overlap; a common combination is uncovering and then visualizing behavior (e.g., identifying routines and presenting them as process models).

### 4. Perspective
The analytical viewpoint from which behavior is examined:
- **Holistic** (16 papers) — most common; analyzing behavior at the system or population level
- **Individual** (6 papers)
- **Collective** (2 papers)
- **Control-flow** (2 papers)
- **Performance** (1 paper)
- **Local** (1 paper)

## Relation to Broader Behavioral Research

The paper situates process mining behavioral analytics within three broader data-driven behavioral research domains:
- **Behavior Informatics**: Focuses on modeling, pattern detection, and simulation.
- **Behavior Analytics**: Addresses observable behavior through analysis, prediction, and management.
- **Behavior Computing**: An umbrella concept embedding behavior in social, organizational, and environmental context.^[103-111]

Process mining primarily focuses on process behavior but can also take an organizational perspective — analyzing resources, building social networks, evaluating performance, and detecting preferences and skills.^[117-120]

## Implications and Limitations

**Practical implications** include:
- Supporting the design of behavior-aware tools by clarifying which behavioral perspectives analysts prioritize.
- Aiding training of novice analysts through a clearer vocabulary and conceptual structure.
- Encouraging more reflective and interdisciplinary discourse in the community.

**Limitations** of the study:
- Restricted to a single venue (EdbA), offering a focused but incomplete view.
- Qualitative coding involves interpretive subjectivity; alternative categorizations are possible.
- Findings are exploratory rather than definitive.^[72-75]

Future work should broaden the scope to main-track ICPM papers, journals, and industry reports, and may employ interviews, surveys, or Delphi studies to validate and refine the frameworks.

## References

- Van Suetendael, J., Depaire, B., Jans, M., & Martin, N. (2025). *Behavioral Analytics: What does that even mean?* Pre-print accepted at ICPM 2025 Workshops, Springer LNBIP series.
- van der Aalst, W. M. P. (2016). *Process Mining: Data Science in Action*. Springer. (See [[process-mining-data-science-in-action]])

## Coding Process: Quantitative Summary

The study by Van Suetendael et al. applied Straussian Grounded Theory (SGT) across three coding stages to 27 EdbA papers (selected from 39 total, spanning 2020–2024):

- **Open coding**: 247 distinct codes identified across the 27 papers.
- **Axial coding**: 247 codes grouped into 44 code categories.
- **Selective coding**: 44 categories refined into 9 major themes.

None of the 27 analyzed papers explicitly defined "behavior" or "behavioral analytics"; all mentions were implicit.^[10-16]

## Related Fields: Behavior Informatics, Analytics, and Computing

The paper situates process mining behavioral analytics within three broader data-driven behavioral research domains:

- **Behavior Informatics**: Focuses on modeling, pattern detection, and simulation to uncover hidden mechanisms behind behavior.
- **Behavior Analytics**: Addresses observable behavior through analysis, prediction, and management, while informatics explains its underlying structure and meaning.
- **Behavior Computing**: A broader umbrella framework embedding behavior in its social, organizational, and environmental context, integrating insights from both Analytics and Informatics while emphasizing contextual influences.

In process mining, behavior is typically represented as sequences of activities performed by people or systems, and event logs reflect both process behavior and organizational/resource behavior.^[103-120]

## Entity and Object Distinction in the Behavior Framework

The Behavior Framework distinguishes between **entities** and **objects**:

- **Entity**: The actor performing an action (human, animal, human-engineered system, or natural system). An entity can exist in a dataset without interacting with a specific activity, because it may still be recorded as performing the actions that constitute an activity.
- **Object**: Something on which or with which behavior is performed (e.g., a document in a business context). An object must interact with at least one activity to appear in the dataset — a zero-interaction object would not be recorded.

This distinction separates actors that perform behavior from things that are acted upon, clarifying their different analytical roles.^[10-16]

## Behavioral Analytics Framework: Empirical Counts

Across the 27 analyzed EdbA papers, the four dimensions of the [[behavioral-analytics-process-mining|Behavioral Analytics Framework]] showed the following distribution:

**Entity dimension**:
- Human-engineered systems: 17 papers
- Human entities: 13 papers
- Animal entities: 1 paper
- Natural systems: 1 paper

**Behavioral Patterns dimension**: 18 distinct patterns were identified. The most frequent were:
- Process behavior: 7 papers
- Routine behavior: 3 papers
- Anomalous behavior: 2 papers
- Daily behavior: 2 papers

Other patterns included foraging behavior, switch behavior, collaborative work, and user journeys.

**Goal dimension**:
- Visualizing behavior: 20 papers
- Uncovering behavior: 19 papers
- Collecting behavior: 3 papers
- Learning patterns: 3 papers
- Comparing behavior: 1 paper
- Measuring behavior: 1 paper

**Perspective dimension**:
- Holistic perspective: 16 papers
- Individual perspective: 6 papers
- Collective perspective: 2 papers
- Control-flow perspective: 2 papers
- Performance perspective: 1 paper
- Local perspective: 1 paper

The dominance of holistic and individual perspectives indicates a tendency to analyze behavior at the level of systems or populations rather than process fragments.^[10-16]

## Practical Implications

The frameworks proposed by Van Suetendael et al. carry several practical implications for the [[process-mining-data-science-in-action|process mining]] community:

1. **Behavior-aware tool design**: Clarifying which behavioral perspectives analysts prioritize (e.g., identifying unusual paths vs. spotting bottlenecks over time) can inform interface design and automated pattern suggestions.
2. **Training novice analysts**: A clearer vocabulary and conceptual structure supports targeted learning modules and annotated process examples for those new to behavioral analysis in event data.
3. **Community discourse**: The work encourages researchers to make their assumptions about behavior explicit and to consider how definitions influence both research outcomes and practical applications.

Future work is recommended to broaden the corpus beyond EdbA to main-track [[process-mining-handbook|ICPM]] papers, journals, and industry reports, and to complement qualitative coding with interviews, surveys, or Delphi studies with researchers and practitioners.^[10-16]
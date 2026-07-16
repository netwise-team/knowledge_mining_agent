---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:56:48'
lint_warnings:
- claim: A single source place (no incoming transitions)
  concern: A source place in a Petri net/WF-net is defined as having no incoming arcs
    (from transitions), but the parenthetical description conflates places and transitions.
    More precisely, the source place has no incoming transitions feeding into it,
    but the phrasing 'no incoming transitions' is an imprecise/potentially misleading
    description of what defines a source place in standard Petri net terminology,
    where it should be 'no incoming arcs.'
- claim: BPMN diagrams can be converted to this format using the established method
    by Dijkman and Ouyang.
  concern: The well-known BPMN-to-Petri-net translation work is typically attributed
    to Dijkman, Dumas, and Ouyang (three authors), not just Dijkman and Ouyang. Omitting
    Dumas misattributes a well-established foundational reference.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Qureshi et al - Bridging Imperative
    Process Models and Process Data Queries—Translation and Relaxation.pdf
  hash: 757c348c927ef383074f9cac2380c998ed4a009414058932b2701bd7dbffb8f5
  ingested: '2026-07-14T07:56:48'
  size: 698440
  truncated: true
status: active
tags:
- business process management
- conformance checking
- imperative process models
- declarative models
- SQL queries
- process querying
- relational databases
- data-driven BPM
- behavioral footprints
- process mining
title: 'Bridging Imperative Process Models and Process Data Queries: Translation and
  Relaxation'
type: technology
---

# Bridging Imperative Process Models and Process Data Queries: Translation and Relaxation

This page covers a structured approach to translate imperative process models (specifically sound, free-choice workflow nets) into declarative constraints and executable SQL-based process data queries, enabling flexible [[process-mining-handbook|conformance checking]]. The work was authored by Abdur Rehman Anwar Qureshi and Mathias Weske (Hasso Plattner Institute, University of Potsdam), Adrian Rebmann and Timotheus Kampik (SAP Signavio / Umeå University), and Matthias Weidlich (Humboldt Universität zu Berlin), and accepted at the ICPM 2025 Workshops (Springer LNBIP series).^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:1-11]

## Motivation

Imperative process models — typically formalized as BPMN diagrams or Petri nets — are the standard tool for designing and communicating operational processes. However, they are not straightforwardly applicable to the relational databases that store much of the available structured process execution data. This creates a gap between traditional process modeling and data-driven process analysis, leading to under-utilization of existing process models.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:12-19]

Additionally, imperative models tend to be overly rigid for real-world [[deviation-desirability-assessment|conformance checking]]: they flag any deviation from the prescribed path, even when the deviation reflects a legitimate, context-dependent exception (e.g., skipping a quality check for a low-value routine purchase). Declarative approaches, by contrast, specify constraints rather than exact paths, offering more flexibility.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:42-56]

The paper addresses both problems by providing a method to translate imperative models into *relaxed* declarative constraints that map directly to SQL queries executable on event data.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:64-73]

## Formal Foundations

### Sound, Free-Choice Workflow Nets

The approach takes as input a **sound, free-choice workflow net (WF-net)** — a specific type of Petri net with:
- A single source place (no incoming transitions)
- A single sink place (no outgoing transitions)
- Full connectedness (every node lies on a path from source to sink)
- **Soundness**: the process can always complete without deadlocks
- **Free-choice**: routing decisions are self-contained and not dependent on other parts of the net

BPMN diagrams can be converted to this format using the established method by Dijkman and Ouyang.

### Behavioral Relations (Alpha-Relations)

From the WF-net, the approach derives three types of behavioral relations between activities:
- **Directly-follows (a → b)**: activity *a* can be immediately followed by *b*
- **Concurrency (a ∥ b)**: activities *a* and *b* can occur in any order
- **Choice (a − b)**: activities *a* and *b* never directly follow each other

The **transitive closure** of directly-follows relations yields **eventually-follows (a ≺ b)** relations. Directly-follows relations are inferred from the net's structure using the Minimal Structural Successor (MSS) function, avoiding exhaustive trace generation or state-space exploration.

### Declarative Constraints (Branched Declare)

Behavioral relations are translated into **Branched Declare** constraints, an extension of Declare based on Linear Temporal Logic on Finite Traces (LTLf). Key templates used include:
- **Init({p₁,...,pₙ})**: at least one activity from the set must occur at the start
- **ChainResponse({p₁,...,pₙ}, {q₁,...,qₙ})**: whenever one activity from the first set occurs, one from the second must occur immediately after
- **AlternateResponse({p₁,...,pₙ}, {q₁,...,qₙ})**: whenever one activity from the first set occurs, one from the second must eventually occur, with no recurrence of the first set in between

## Three-Step Approach

### Step 1: Determine Behavioral Relations

The approach computes directly-follows relations from the input WF-net using the MSS-based method, then derives the full set of alpha-relations. The result is a **behavioral relation matrix** encoding all pairwise relationships between activities.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:64-73]

### Step 2: Relax Behavioral Relations

A process analyst can apply four types of relaxation operations to the matrix:

1. **Remove Activity**: Makes an activity optional and unconstrained in ordering. All its relations are set to undirected eventually-follows (≺≻). Useful for context-dependent steps (e.g., skipping a quality check for routine purchases).

2. **Remove All Relationships Between Two Activities**: Makes two activities completely independent (both set to ≺≻). Useful when process fragments are less coupled than the model suggests (e.g., allowing invoice receipt before goods receipt).

3. **Turn Exclusive Choice (−) into Direct Relationship (→)**: Replaces a choice between activities with a sequence, allowing formerly exclusive activities to co-exist. Also enables self-loops for modeling rework or iterative tasks.

4. **Turn Direct (→) into Indirect Relationship (≺)**: Allows intermediate unmodeled steps between two activities, accommodating real-world process variability.

The matrix is updated transparently after each relaxation, allowing the analyst to assess downstream effects.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:64-73]

### Step 3: Generate Declarative Constraints

Algorithm 1 automatically generates declarative constraints from the (relaxed) relation matrix:
- An **Init** constraint is created from start activities (those never appearing as successors)
- **ChainResponse** constraints are generated for directly-follows relations
- **AlternateResponse** constraints are generated for parallel relations and for eventually-follows relations not covered by the transitive closure of directly-follows
- Optional activities (detectable via a bypass pattern) are excluded from mandatory AlternateResponse constraints to preserve their optionality

The resulting Declare constraints translate directly into **SQL queries** using the `MATCH_RECOGNIZE` clause, executable on a standard event log table (`case_id`, `end_time`, `event_name`).^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:64-73]

## Proof of Concept

The approach was validated on the **BPI Challenge 2019 (BPIC19)** dataset (251,734 cases), using the *3-way matching, invoice before goods receipt* model from the winning submission by Diba et al. (covering 86.36% of cases). The model was converted to a sound, free-choice WF-net and processed through the three-step pipeline.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:78-79]

Relaxations applied included:
- Allowing recurring invoicing and deliveries (turning direct parallel relations into indirect ones)
- Decoupling early procurement stages (removing relationships between order confirmation and price/quantity change activities)

Results compared against alignment-based conformance checking:

| Approach | Conformance Rate |
|---|---|
| Alignments | 0.691 |
| Relaxed queries | 0.823 |

The relaxed query approach reduced detected deviating traces substantially, enabling analysts to focus on genuine non-conformance rather than legitimate process variations.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:78-79]

## Relationship to Related Work

- **Imperative-to-declarative translation**: Prior work (Barbaro et al. 2025; Bergmann et al. 2023) translated Petri nets and BPMN into declarative specifications but did not address systematic relaxation or direct query generation.^[Qureshi et al - Bridging Imperative Process Models and Process Data Queries—Translation and Relaxation.pdf:57-63]
- **Alignment-based conformance checking**: Traditional alignment methods can implement limited relaxation via cost function manipulation, but cannot handle context-sensitive relaxations (e.g., allowing co-occurrence of formerly exclusive activities).
- **Declarative conformance checking**: Languages like Declare have been used for flexible conformance checking; this work bridges them with imperative modeling.
- **Process querying with SQL**: Builds on prior work using SQL's `MATCH_RECOGNIZE` clause for behavioral querying of process data (Brand et al., ICPM 2024).
- **[[llm-declarative-process-discovery-dcr-graphs|Declarative process discovery]]**: Complements LLM-based approaches to declarative modeling by providing a systematic, model-driven path from imperative specifications.
- **[[deviation-desirability-assessment|Deviation desirability]]**: Both works address the problem of over-flagging in conformance checking, from complementary angles.

## Limitations and Future Work

- It remains unproven whether the generated constraints (without relaxation) are behaviorally equivalent to the original model, particularly in the presence of **silent transitions**.
- The set of relaxation operations is limited and could be extended.
- Validation was conducted on a single dataset; broader evaluation is needed.
- No user study has been conducted to validate practical utility.

Future directions include: expanding relaxation operations, developing a visual interface for domain experts, and extending the translation to process models beyond free-choice workflow nets.

## Implementation

The approach is implemented as a Python-based command-line interface. Source code is publicly available at: https://github.com/rehman-qureshi/bridging-models-and-queries

## Key Data

- I = {a ∈ A | ∀b ∈ A, (b, a) /∈ D}. Then the algorithm continues with gener-
- event_name = 'CPO', RR AS event_name = 'RR'
- event_name = 'SP'
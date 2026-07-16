---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:02:22'
lint_warnings:
- claim: The concept was formalized by Grohs et al. (2025) in a paper accepted at
    the ICPM 2025 Workshops.
  concern: Presenting a 2025 workshop paper as having 'formalized' a concept implies
    it is the definitive or original source for deviation desirability assessment.
    This is an overstatement — workshop papers are preliminary works, and the claim
    of formalization based on a single workshop paper is not well-established in the
    broader literature.
- claim: CATE estimates the causal (not merely correlative) effect of a deviation
    on the outcome dimension.
  concern: CATE (Conditional Average Treatment Effect) is a statistical estimation
    technique that can be used within causal inference frameworks, but its application
    does not automatically guarantee causal conclusions. In process mining contexts,
    where confounding is common and randomized assignment is absent, CATE estimates
    are typically observational and cannot straightforwardly be interpreted as truly
    causal without strong additional assumptions.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Grohs et al - Towards an Automated
    Assessment of Deviation Desirability.pdf
  hash: ce428c7c2c588b111e8a2f19e5114d0b8c9f257d4e672f1f92365e6f92e56389
  ingested: '2026-07-14T07:02:22'
  size: 415490
  truncated: true
status: active
tags:
- process mining
- conformance checking
- deviation desirability
- automation
- event log
- process model
- impact assessment
- business process
- framework
- process analytics
title: Deviation Desirability Assessment in Conformance Checking
type: concept
updated: '2026-07-14'
---

# Deviation Desirability Assessment in Conformance Checking

Deviation desirability assessment is a process mining technique that extends [[coordinated-projections-multi-faceted-process-exploration|conformance checking]] by evaluating not just whether process executions deviate from a process model, but also the *desirability* of those deviations — i.e., the degree to which stakeholders want or do not want their recurrence in the future. The concept was formalized by Grohs et al. (2025) in a paper accepted at the ICPM 2025 Workshops.

## Motivation

Conformance checking techniques detect deviations between event logs and process models, but they do not evaluate whether those deviations are harmful, beneficial, or irrelevant. Without such evaluation, analysts must manually assess each deviation in an ad-hoc, unstructured way — a process that is labor-intensive, requires substantial domain knowledge, and is prone to human error. False conclusions (e.g., misclassifying a logging error as a severe negative deviation) can lead to wasted effort investigating irrelevant root causes or even creating new problems.^[37-47]

Deviations differ along two axes:
- **Impact**: whether the effect on the process is positive, neutral, or negative.
- **Significance**: the perceived importance of that impact to stakeholders (low to high).

Together, these determine a deviation's desirability.^[32-36]

## Three-Step Framework

Grohs, Monashev, and Rebmann (2025) propose a three-step framework that enables analysts to set up an automated pipeline for deviation desirability assessment. Once instantiated, the pipeline runs automatically in subsequent analysis iterations without further manual input.^[48-61]

### Step 1: Check Conformance

A conformance checking technique is selected and applied to compare an event log against a process model. The framework supports:
- **Imperative techniques** (e.g., trace alignments on Petri nets or BPMN models), where log moves indicate inserted activities and model moves indicate skipped activities.
- **Declarative techniques** (e.g., Declare constraint checking), where any trace is allowed unless it violates a defined constraint such as precedence, response, or succession.
- **Multi-perspective declarative techniques** (e.g., MP-Declare), which extend constraints to cover time, resources, and other perspectives beyond control-flow.

The output is a labeled event log where each trace is associated with all deviations detected within it.^[77-98]

### Step 2: Quantify Deviation Impact

For each trace, a numerical feature is generated to represent the chosen impact dimension (e.g., time, cost, outcome). The analyst then defines an **impact function** that links deviation occurrence to this dimension. The framework illustrates the use of **Conditional Average Treatment Effect (CATE)** as the impact function, which estimates the causal (not merely correlative) effect of a deviation on the outcome dimension. Other impact functions — such as regression, decision trees, or direct cost summation — may be used depending on the use case.^[99-107]

CATEs are computed using causal inference tools (e.g., the DoWhy package), accounting for confounding effects from other co-occurring deviations.^[99-107]

### Step 3: Assign Deviation Desirability

A **desirability function** maps the quantified impact value to a desirability category: *positive*, *neutral*, or *negative*. Analysts may define discrete thresholds (e.g., neutral if impact is between −0.1 and +0.1, positive if ≥ 0.1, negative if ≤ −0.1) or more granular levels (low/medium/high positive or negative).^[119-120]

The framework recommends applying this process across multiple impact dimensions to reveal trade-offs. For example, a deviation may be time-positive but cost-negative. Results can be presented as a multi-dimensional desirability heatmap.^[20-25]

## Impact Dimensions

Building on prior work by Grohs et al. [2024], the framework recognizes four primary impact dimensions:
1. **Compliance** — adherence to regulatory or contractual rules.
2. **Process outcome** — whether the process achieves its intended goal.
3. **Performance** — time, cost, and quality (analyzed via the Devil's Quadrangle).
4. **Standardization** — consistency of execution across cases.

Inherent trade-offs exist between these dimensions and must be considered during assessment.^[108-116]

## Proof of Concept

The framework was demonstrated on the real-world **BPI Challenge 2019** purchase order handling event log (3-way match after Goods Receipt variant), across three scenarios:

1. **Alignment-based deviations × time dimension**: Trace alignments yielded 47 log/model moves. CATE on trace duration revealed, e.g., that a log move on *Change Price* increases duration by 82.9 days (negative), while skipping *Record Goods Receipt* reduces duration by 59.0 days (positive on time, likely negative on outcome).

2. **Declare violations × outcome dimension**: 46 declarative constraint violations were mined. CATE on a binary outcome feature (goods received and invoice cleared) showed, e.g., that violating a precedence constraint between *Record Service Entry Sheet* and *Create Purchase Order Item* increased positive outcome likelihood by 26.47% — a high positive desirability finding.

3. **MP-Declare violations × cost dimension**: Three time-bounded constraints were defined. Costs were computed directly as penalty sums (5% of purchase value per 7 days exceeding the time frame). Two of three violations were categorized as high negative (e.g., costs of 8.6M USD for one constraint).^[58-61]

## Relationship to Related Work

**Quantitative approaches** (cost functions, criticality rankings) rank deviations by a single score but do not account for multi-dimensional trade-offs. **Qualitative approaches** (exception vs. anomaly classification, true vs. false alarm labeling) distinguish neutral from negative deviations but largely ignore positive ones. The proposed framework synthesizes both: it classifies deviations as positive/neutral/negative (qualitative) and ranks them by impact within each dimension (quantitative), enabling multi-facet trade-off analysis.^[17-25]

On the causal inference side, the framework distinguishes itself from correlation-based process analysis (decision trees, regression) by using CATE to estimate causal effects, and from existing causal discovery approaches in process mining by applying causality specifically to deviation desirability evaluation.^[99-107]

## Limitations

- The framework requires domain knowledge for initial setup (impact dimension quantification, impact function selection, desirability thresholds) and is not fully automated end-to-end.
- A single impact dimension may be quantifiable in multiple ways, potentially yielding contradictory results; no one-size-fits-all solution is proposed.
- The framework focuses on one dimension at a time; aggregating across dimensions requires additional analyst judgment.^[17-25]

## References

- Grohs, M., Monashev, M., & Rebmann, A. (2025). *Towards an Automated Assessment of Deviation Desirability*. ICPM 2025 International Workshops, Springer LNBIP.
- Grohs et al. (2024). Manual desirability assessment framework (foundational prior work).

## Automated Deviation Desirability Assessment Framework

Grohs, Monashev, and Rebmann (ICPM 2025 Workshops) extended the manual [[deviation-desirability-assessment|deviation desirability assessment]] approach by proposing a three-step framework that enables process analysts to set up an **automated pipeline** for assessing the desirability of conformance deviations. The framework builds on the manual five-step approach and focuses on automating the fourth step — evaluating deviation impact — one dimension at a time. ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:48-61]

### Motivation for Automation

Manual deviation desirability assessments are labor-intensive, require substantial domain knowledge, and are prone to human error (e.g., misclassifying a logging error as a severe negative deviation). False conclusions can lead analysts to investigate root causes and develop corrective actions for irrelevant deviations, wasting time and effort. The automated framework addresses these risks by providing a structured, repeatable pipeline. ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:41-47]

### Three-Step Framework

The framework consists of three steps that an analyst configures once; subsequent analysis iterations then run automatically:

1. **Check Conformance (Step 3.1):** A [[conformance-checking-visualization-idioms|conformance checking]] technique is selected to identify deviating traces. Supported techniques include trace alignments (imperative), declarative constraint checking (Declare, MP-Declare), and high-level deviation pattern detection. The only assumption is that each deviation can be assigned to individual traces, producing a labeled event log where each trace is marked for each deviation it contains.

2. **Quantify Deviation Impact (Step 3.2):** The analyst selects an impact dimension (e.g., time, cost, outcome) and defines an **impact function** that links deviation occurrence to a numerical impact value. The framework illustrates the use of **Conditional Average Treatment Effect (CATE)** — which estimates the causal (not merely correlative) effect of a deviation on the chosen dimension — though other methods such as regression or decision trees are also applicable. In cases where the causal effect is directly known (e.g., contractual penalties), simpler summation functions suffice. ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:99-107]

3. **Assign Deviation Desirability (Step 3.3):** A **desirability function** maps the quantified impact value to one of three categories: *positive*, *neutral*, or *negative*. For example, a discrete function may assign neutral for impacts between −0.1 and +0.1, positive for ≥ 0.1, and negative for ≤ −0.1. Custom category names (e.g., "critical") are also supported. The framework recommends applying this step across multiple impact dimensions to surface trade-offs (e.g., a deviation that is positive for time but negative for cost). ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:19-26]

The multi-dimensional output can be presented as a heatmap or table showing each deviation's desirability across outcome, time, cost, and other dimensions, enabling analysts to prioritize mitigation of the most severe deviations. ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:20-26]

### Proof of Concept on BPIC 2019

The framework was demonstrated on the real-world purchase order handling process from the BPI Challenge 2019 (3-way match after Goods Receipt variant) across three scenarios:

- **Alignment-based deviations / Time dimension:** Trace alignments yielded 47 log and model moves. CATE on total trace duration (via DoWhy) showed, e.g., that a log move on *Change Price* increases duration by 82.9 days (negative), while skipping *Record Goods Receipt* reduces duration by 59.0 days (positive on time, but likely negative on outcome).

- **Declare violations / Outcome dimension:** 46 declarative constraint violations were mined (precedence and response constraints). CATE on a binary outcome feature (goods received and invoice cleared) revealed, e.g., that violating the precedence between *Record Service Entry Sheet* and *Create Purchase Order Item* increased positive outcome likelihood by 26.47% — a high positive desirability finding.

- **MP-Declare violations / Cost dimension:** Three time-enriched constraints were defined. Costs were computed directly as penalty sums (5% of purchase value per 7 days exceeding the time frame), bypassing the need for CATE. Two of three violations were categorized as high negative (costs exceeding 1M$, including one totaling 8.6M$). ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:58-61]

### Relationship to Related Work

Existing approaches either assign a single numerical non-conformance score (cost functions, criticality rankings) or use qualitative classifications (exceptions vs. anomalies, true vs. false alarms). The automated framework synthesizes both: it classifies deviations as positive, negative, or neutral (qualitative) while ranking them by impact within each dimension (quantitative), and uniquely surfaces trade-offs across dimensions. The use of CATE distinguishes it from correlation-based process analysis approaches by providing causal rather than associative impact estimates. ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:99-107]

### Limitations

The framework requires domain knowledge for initial setup (selecting techniques, defining impact and desirability functions), so it is not fully automated end-to-end. Impact dimensions can be quantified in multiple ways, potentially yielding contradictory results across instantiations. The framework does not prescribe a one-size-fits-all solution but provides structured guidance adaptable to specific use cases. Source code is available at [GitHub](https://github.com/michaelgrohs/deviation_desirability_assessment). ^[Grohs et al - Towards an Automated Assessment of Deviation Desirability.pdf:48-61]
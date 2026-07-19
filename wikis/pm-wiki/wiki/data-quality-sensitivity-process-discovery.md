---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:15:45'
lint_warnings:
- claim: 'Precision: whether the model only accepts log-observed traces'
  concern: Precision in process mining measures whether the model avoids allowing
    behavior not seen in the log, but a precise model can still accept traces not
    observed in the log as long as it does not over-generalize. Defining precision
    as accepting 'only log-observed traces' conflates precision with a perfect fit
    to the log and overstates the strictness of the concept.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Bertrand et al - A framework
    for measuring data quality sensitivity in process discovery.pdf
  hash: ce1349c22b55d33e276a09dd11db1ead412401d41fab7ac009a76651040d2529
  ingested: '2026-07-14T07:15:45'
  size: 641997
  truncated: true
status: active
tags:
- process discovery
- data quality
- sensitivity analysis
- event logs
- business processes
- data quality issues
- process models
- missing events
- concept drift
- pipeline
title: Data Quality Sensitivity in Process Discovery
type: concept
---

# Data Quality Sensitivity in Process Discovery

Data quality sensitivity analysis in [[process-mining-handbook|process mining]] is a systematic approach to quantifying how data quality issues (DQIs) in event logs affect the outputs of [[process-mining-handbook|process discovery]] algorithms. The framework introduced by Bertrand, Kabierski, Peeperkorn, and Vanden Broucke (Ghent University, University of Vienna, KU Leuven) — accepted at the ICPM 2025 Workshops — provides a configurable pipeline for this purpose.

## Motivation

Process discovery techniques generate models of business processes from event logs, but they typically assume that logs are correct and complete. In practice, real-world event logs are frequently affected by errors, inconsistencies, and missing information caused by human or system faults. While it is widely acknowledged that DQIs negatively affect process mining results, little prior research had systematically quantified this impact. The framework addresses two key open challenges in PM data quality research: ^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:12-49]

- **C14**: Which dimensions of data quality are particularly important for process mining, and are certain dimensions more important for specific sub-areas?
- **C15**: How can we best show how process-data quality issues may have impacted analytical outcomes?

## Background Concepts

### Event Logs
An event log *L* is a finite set of traces, where each trace is an ordered sequence of events sharing the same case identifier. Each event *e* is a tuple *(activity, case, timestamp)*. ^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:70-81]

### Process Discovery and Model Quality
Process discovery algorithms — such as the α-Miner, Inductive Miner (IM), Declare Miner, and Split Miner — identify recurrent patterns in event logs to construct process models (Petri nets, BPMN, process trees, etc.). Model quality is evaluated along four standard dimensions: ^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:85-105]
- **Fitness**: extent to which the model accepts traces in the log
- **Precision**: whether the model only accepts log-observed traces
- **Generalisation**: whether the model accepts unseen but plausible traces
- **Simplicity**: complexity of the model structure

Conformance checking techniques such as token-based replay and alignment-based methods are used to compute these metrics. ^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:95-105]

### Data Quality Issues (DQIs)
DQIs are discrepancies between the recorded event log and the real executed process. A foundational classification organises DQIs by issue type (incorrect, irrelevant, imprecise, or missing data) and the affected log component (cases, events, attributes, activity names, timestamps, resources). The most common DQIs identified in the literature are: ^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:107-117]
- Missing events
- Incorrect timestamps
- Imprecise activity names
- Imprecise timestamps
- Irrelevant events

## The Framework

The framework takes four inputs:
1. An **event log** to be analysed
2. A **list of DQIs** with associated parameters (e.g., percentage of events to pollute)
3. A set of **process discovery algorithms** and their configurations
4. A set of **conformance checking metrics**

It outputs a sensitivity analysis quantifying the impact of each DQI on the models discovered by the selected algorithms. The pipeline is implemented in Python and is freely available on GitHub. ^[Bertrand et al - A framework for measuring data quality sensitivity in process discovery.pdf:50-59]

### Step 1: Generate a Clean Event Log (Optional)
To ensure a controlled starting point, a clean log is constructed by:
1. Discovering an original model from the raw log using the Inductive Miner Infrequent (IMf, threshold 0.2)
2. Filtering out all traces that do not perfectly fit this model

If a normative model is available, it can substitute the discovered model for filtering.

### Step 2: Inject Data Quality Issues
A **polluter** is defined as a function *P: L → L* that systematically applies changes to an event log. The framework implements the following atomic DQI polluters:

- **Missing Events** (`DeleteActivityPolluter`): randomly drops a specified percentage of events
- **Incorrect Timestamps** (`DelayedEventLoggingPolluter`): adds random delays (sampled from a Gamma distribution) to a percentage of event timestamps, potentially reordering events
- **Imprecise Activity Names** (`ImpreciseActivityPolluter`): merges fine-grained activity labels into coarser ones (e.g., multiple release variants → "release")
- **Imprecise Timestamps** (`AggregatedEventLoggingPolluter`): aggregates timestamps to coarser granularity levels (second, minute, 15 minutes, hour, day)
- **Irrelevant Events** (`InsertAlienActivityPolluter`): injects events with activity labels alien to the process

### Step 3: Apply Process Discovery
Discovery is applied to both the clean log and the polluted log, yielding a **clean model** and a **polluted model** respectively. The framework is algorithm-agnostic.

### Step 4: Evaluate Process Models
Four log–model combinations can be evaluated, providing complementary information:
1. Clean log + clean model (baseline)
2. Clean log + polluted model (isolates DQI impact on discovery)
3. Polluted log + clean model (isolates DQI impact on conformance checking)
4. Polluted log + polluted model (uncontrolled setup)

The primary experimental focus is combination 2, which isolates the effect of DQIs on the discovery step.

## Experimental Evaluation

### Setup
Four publicly available event logs were used: Road Traffic Fines Management, Sepsis Cases, Helpdesk, and Hospital Billing. Discovery algorithms evaluated: α-Miner, Inductive Miner (IM, thresholds 0.0 and 0.2), and ILP Miner (thresholds 1.0 and 0.8). Pollution levels ranged from 10% to 90% in 10% increments. Metrics: token-based fitness and precision.

### Key Findings
- **Fitness** remains relatively stable across most DQIs; ILP (threshold 0.8) and IM without filtering show the highest robustness, while the α-Miner is most sensitive.
- **Precision** degrades more substantially across all algorithms and DQIs, indicating that polluted models allow more incorrect behaviour.
- **Control-flow DQIs** (missing events, irrelevant events) cause the most severe degradation in model quality.
- **Timestamp-related DQIs** have minimal impact on fitness and precision.
- **Imprecise activity names** show a nuanced effect: sometimes decreasing fitness while increasing precision by simplifying the model.
- Even **small amounts of noise (10%)** can cause sharp performance drops, followed by a plateau — suggesting that even low-severity DQIs can materially affect discovery suitability.
- Algorithms with noise-filtering mechanisms (ILP 0.8, IM 0.2) generally outperform their non-filtering counterparts under polluted conditions.

## Limitations and Future Work

- Model quality metrics are holistic and may not fully capture nuanced DQI effects; stochastic conformance checking is suggested as a complementary approach.
- The framework currently evaluates only isolated, atomic DQIs; co-occurring DQIs (which are common in practice) are left for future work.
- No formal statistical tests are computed in the current experiments; large-scale benchmarking with many logs is planned.
- The clean log is derived from a discovered (not normative) model, which may introduce imprecision.
- Future extensions include support for additional pollution patterns, more discovery algorithms, additional conformance metrics, and sensitivity analysis of other PM tasks (e.g., conformance checking, [[actor-enriched-throughput-time-forecasting|predictive process monitoring]]).

## Relation to Broader Process Mining Research

This framework complements research on evaluating process discovery approaches, including work on maturity stages of discovery algorithms and ground-truth-based evaluation methods. It also connects to [[sustainability-aware-process-mining|data-driven process analysis]] and [[process-mining-handbook|process mining]] quality assessment more broadly. The sensitivity analysis methodology is applicable beyond process discovery to other PM analysis tasks.

## References

- Bertrand, Y., Kabierski, M., Peeperkorn, J., Vanden Broucke, S. (2025). *A framework for measuring data quality sensitivity in process discovery*. ICPM 2025 Workshops, Springer LNBIP.
- Bose, R.J.C., Mans, R.S., Van Der Aalst, W.M. (2013). Wanna improve process mining results? IEEE CIDM.
- Buijs, J.C., Van Dongen, B.F., van Der Aalst, W.M.P. (2012). On the role of fitness, precision, generalization and simplicity in process discovery. CoopIS 2012.
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:31:57'
lint_warnings:
- claim: All sequential dependencies in the model are causally inverted; event traces
    and descriptions are adjusted accordingly.
  concern: Completely inverting all sequential dependencies in a business process
    model to create a coherent 'reversed' process that still makes logical sense as
    a process (with adjusted traces and descriptions) is methodologically questionable.
    True causal inversion of all dependencies in a complex process with cycles and
    concurrency would likely produce an incoherent or non-executable model, making
    it unclear how valid event traces could be 'adjusted accordingly.' This claim
    may overstate the rigor or feasibility of the reversal procedure.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Kourani et al - Knowledge-Driven
    Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf
  hash: c082f0fd7351eab62a3b23d5cb87777a0af65b131fd8d95ac9f3772daf272a38
  ingested: '2026-07-14T07:31:57'
  size: 625152
  truncated: true
status: active
tags:
- hallucination
- LLMs
- process modeling
- BPM
- generative AI
- trustworthy AI
- empirical study
- pre-trained knowledge
- evidence fidelity
- ICPM 2025
title: Knowledge-Driven Hallucination in LLMs for Process Modeling
type: concept
---

# Knowledge-Driven Hallucination in LLMs for Process Modeling

Knowledge-driven hallucination is a phenomenon where a Large Language Model (LLM) generates output that contradicts explicit source evidence because its generalized pre-trained internal knowledge overrides the provided input. This concept was formally introduced and empirically studied in the context of [[process-mining-handbook|Business Process Management (BPM)]] and automated process modeling by Humam Kourani, Anton Antonov, Alessandro Berti, and Wil M.P. van der Aalst (Fraunhofer Institute FIT and RWTH Aachen University) in a paper accepted at the ICPM 2025 Workshops. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:1-11]

## Motivation

LLMs are increasingly used to automate complex analytical tasks, including generating formal process models from textual descriptions or event logs. Their utility stems from vast pre-trained knowledge that enables inference over ambiguous inputs. However, this same capability introduces a critical reliability risk: when the provided evidence describes an atypical or unconventional process, the LLM may "correct" the output toward its internalized schema of how a standard process "should" operate, rather than faithfully representing the actual input. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:45-59]

Business processes such as purchase-to-pay, order-to-cash, and incident management follow well-established patterns across organizations, making it highly likely that LLMs possess strong pre-trained schemas for them. This creates a realistic and measurable conflict between evidence fidelity and background knowledge. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:64-72]

## Experimental Methodology

The study uses four diverse business processes selected from an established benchmark:
- **Sales Order** (8 activities, no cycles or concurrency)
- **Booking System** (13 activities, with decisions, cycles, and concurrency)
- **Complaint Handling** (9 activities, with decisions)
- **Internal Audit** (24 activities, with decisions, cycles, and concurrency)

For each process, three artifact variants were created:
- **Standard (M+, D+, L+):** The conventional ground-truth model, natural language description, and simulated event log.
- **Reversed (M−, D−, L−):** All sequential dependencies in the model are causally inverted; event traces and descriptions are adjusted accordingly.
- **Shuffled (M∗, D∗, L∗):** Activity labels are randomly permuted across the model structure, preserving control-flow topology but breaking semantic meaning.

LLMs were tasked with two generation scenarios:
1. **Text-to-Model:** Generate a process model from a textual description (D+, D−, D∗).
2. **Log-to-Model:** Discover a process model from a textual abstraction of an event log (L+, L−, L∗), generated using the [[veco-multimodal-process-mining-library|PM4Py]] library.

All experiments used the **ProMoAI** framework, which generates models in the POWL language and converts them to Petri nets or BPMN. Two prompting conditions were tested:
- **Standard Prompt:** The original optimized ProMoAI prompt.
- **Strict Adherence Prompt:** Augmented with an explicit instruction to disregard background knowledge and rely solely on the provided input.

Generated models were evaluated using **behavioral footprint similarity** (via PM4Py) against all three ground truth variants (M+, M−, M∗) to determine which the LLM's output most closely resembled. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:73-82]

## Models Evaluated

Ten LLMs were benchmarked, spanning a range of sizes, architectures, and reasoning capabilities:

| Model | Open-Source | Reasoning | Parameters (est.) | LB Score |
|---|---|---|---|---|
| command-r | No | No | 35B | 27.15 |
| gemini-2.5-flash | No | No | ~400B, 20B active | 64.42 |
| gemini-2.5-pro | No | No | ~1500B, 40B active | 69.39 |
| gpt-4.1-nano | No | No | ~18B, 2B active | 40.51 |
| grok-3-fast | No | No | ~2700B, 50B active | 56.05 |
| grok-3-mini-fast | No | Yes | ~250B, 35B active | 62.36 |
| kimi-k2 | Yes | No | ~1000B, 32B active | 62.70 |
| o3 | No | Yes | ~200B | 71.98 |
| o4-mini | No | Yes | ~60B, 8B active | 66.87 |
| qwen3-235b-a22b | Yes | Yes | 235B, 22B active | 64.72 |

## Key Findings

### Hallucination is Pervasive
Knowledge-driven hallucination was observed across **all tested LLMs** — no model achieved full adherence to atypical evidence. When given reversed or shuffled artifacts, models frequently generated outputs more similar to the standard ground truth (M+) than to the actual source evidence, indicating reversion to pre-trained schemas. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:73-82]

### Strict Prompting Helps but Does Not Eliminate the Problem
Explicit instructions to ignore background knowledge reduced hallucination instances:
- Text-based: from 27 to 13 clear hallucination cases
- Log-based: from 20 to 10 clear hallucination cases

However, the persistence of hallucination even under strict prompting demonstrates how deeply ingrained pre-trained knowledge is. Model responsiveness varied: **o3** showed marked improvement with strict prompting, while **grok-3-fast** continued to hallucinate frequently regardless. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:24-31]

### Event Logs Provide Stronger Evidence Than Text
Fewer hallucinations occurred when models were generated from event logs (30 total instances) compared to textual descriptions (40 total instances) across both prompt types. The structured, unambiguous format of event logs appears to serve as stronger grounding evidence than natural language, though it does not fully prevent hallucination. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:26-31]

### Performance Degrades Even Without Full Hallucination
Even when LLMs correctly followed atypical process structures, the quality of generated models (measured by similarity scores) was generally lower than for standard processes. This suggests that contradicting the LLM's internal schema degrades generation quality even when hallucination is avoided. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:53-59]

### No Clear Relationship Between Model Size and Hallucination
The study found no direct relationship between parameter count and susceptibility to knowledge-driven hallucination. Smaller reasoning models (e.g., o4-mini) outperformed larger non-reasoning models on evidence adherence. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:26-31]

### Best Performers
**o4-mini** and **o3** achieved the highest average diagonal similarity scores (evidence adherence) across configurations, with o4-mini showing the smallest gap to best performance in text-based tasks and o3 excelling in log-based tasks with strict prompting. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:26-31]

## Implications for Process Mining

This work raises important concerns for the use of LLMs in evidence-based [[llm-declarative-process-discovery-dcr-graphs|process discovery]] and [[narrative-based-predictive-process-monitoring-llm|process monitoring]] tasks:

1. **Validation is essential:** AI-generated process artifacts may appear well-formed and plausible while failing to accurately represent the actual process described in the source data.
2. **Atypical processes are high-risk:** Organizations with non-standard workflows are particularly vulnerable, as LLMs are more likely to override unusual evidence with common patterns.
3. **Prompt engineering is a partial mitigation:** Strict adherence prompts reduce but do not eliminate hallucination, and their effectiveness varies by model.
4. **Structured inputs are preferable:** When possible, providing event logs rather than textual descriptions reduces hallucination risk. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:28-31]

## Methodology for Assessing Knowledge-Driven Hallucination

The paper contributes a reusable evaluation methodology:
1. Select standard process models with known ground truth.
2. Generate conflicting variants (reversed, shuffled) that preserve structure but contradict semantic expectations.
3. Task LLMs with model generation from both standard and conflicting artifacts.
4. Compare generated models against all variants using behavioral similarity metrics.
5. Measure the ratio of evidence adherence vs. knowledge reversion. ^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:73-82]

All artifacts and results are publicly available at https://github.com/antonov1/process-hallucinations.

## References

- Kourani, H., Antonov, A., Berti, A., & van der Aalst, W.M.P. (2025). *Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling.* ICPM 2025 Workshops, Springer LNBIP.
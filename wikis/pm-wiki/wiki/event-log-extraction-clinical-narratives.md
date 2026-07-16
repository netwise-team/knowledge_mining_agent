---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T06:59:39'
lint_warnings:
- claim: KM is fast (~20 ms per sentence)
  concern: Keyword matching is typically an extremely simple string/pattern matching
    operation and would normally execute in microseconds per sentence, not ~20 milliseconds.
    20 ms per sentence would be unusually slow for a basic keyword lookup and may
    reflect a misreported or misattributed benchmark figure.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Susaiyah et al - Extracting
    Events from Nursing Notes a MIMIC-III Case Study.pdf
  hash: 689fc293b8ae136e2115890ad5cd77796b842cf1a7eba99ad1a615f72a6c1abd
  ingested: '2026-07-14T06:59:39'
  size: 483812
  truncated: true
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Gómez-Noé et al - Extraction
    and Identification of Medications from EHR Notes with LLMs - A Tool and a Case
    Study.pdf
  hash: 59c0007b17c936f3416845ead74d79b4ef2d2559bac36b5c33e56148838c19fa
  ingested: '2026-07-14'
  size: 450809
status: active
tags:
- clinical NLP
- event extraction
- hybrid framework
- EHR
- unstructured text
- LLMs
- sentence embeddings
- process mining
- nursing notes
- MIMIC-III
title: Event Log Extraction from Clinical Narratives
type: technology
updated: '2026-07-14'
---

# Event Log Extraction from Clinical Narratives

Event log extraction from clinical narratives is a foundational preprocessing step in [[process-mining-healthcare-radiological-workflows|healthcare process mining]], addressing the challenge of transforming unstructured free-text clinical records — such as nursing notes — into structured event logs suitable for process analysis. Because electronic health records (EHRs) contain rich but unstructured clinical narratives, automated extraction methods are essential for enabling data-driven process discovery and conformance checking in clinical settings.

## Motivation

Clinical narratives such as nursing notes capture observations about patient experience and care that are often absent from structured EHR data: daily life activities, social interactions, causal and temporal relationships (e.g., symptom relief following medication). Prior work has shown that converting free-text clinical narratives into structured records can reveal events and relationships otherwise unknown from structured data alone.^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:19-25]

However, clinical text introduces unique challenges:
- **Non-standardized vocabulary** with frequent abbreviations and clinical shorthand (e.g., *NAPPING T/O AM*)
- **Fragmented or ungrammatical sentences** (e.g., *WELL THROUGH OUT NIGHT*)
- **Temporal ambiguity**: a mix of past events, future references, and hypothetical events
- **Irrelevant actors**: references to family members or staff rather than the patient
- **Implicit event mentions**: e.g., *patient not waking easily* as an implicit Sleep event^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:30-51]

## Hybrid Event Extraction Framework

Susaiyah and Sidorova (ICPM 2025 Workshops, Eindhoven University of Technology) proposed a hybrid framework combining three complementary methods to extract patient events from nursing notes, evaluated on the publicly available **MIMIC-III** dataset.^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:65-81]

### Keyword Matching (KM)
Keyword matching provides a low-cost, interpretable baseline. Each event type (e.g., *Sleep*, *Pain*, *Eating*) is associated with a set of keyword lemmas and their surface forms. A sentence is assigned an event type if it contains all lemmas of a keyword phrase in the correct order. KM is fast (~20 ms per sentence) and highly transparent but cannot capture linguistic variation or implicit mentions.^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:102-113]

### Embedding-Based Similarity (EM)
Embedding-based matching leverages semantic content by encoding sentences and event type names into a shared vector space using a sentence encoder. Cosine similarity between a sentence embedding and an event type embedding is compared against a threshold θ. The domain-specific biomedical sentence transformer **BioLORD** is used to improve results in clinical text. EM can capture paraphrased or implicit mentions but requires careful threshold calibration.^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:114-119]

### Large Language Models (LLMs)
LLMs (evaluated using Llama3 70B) are applied as a prompt-based classifier. The model receives a sentence, candidate event types with descriptions, and optional supporting evidence. LLMs can interpret nuanced phrasing, resolve ambiguity, and infer implicit mentions — but at high computational cost (~4–24 seconds per sentence on an A10 GPU, versus 20 ms for KM).^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:58-64]

### Hybrid Strategy: Selective LLM Application
The key innovation is **selective LLM use**: LLMs are applied only to *ambiguous cases* — sentences where KM and EM disagree. This reserves expensive LLM inference for the most challenging cases while maintaining overall extraction quality. Approximately 10% of sampled sentences fall into the disagreement set (D-SET), making this approach computationally efficient.^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:65-71]

## Prompt Configuration Space

The framework explores 16 prompt variants derived from four binary design choices:
- **Ki**: Include KM-detected keywords in the input prompt
- **Si**: Include embedding similarity scores in the input
- **Ko**: Request keyword evidence in the LLM output
- **Qo**: Request quoted text justification in the LLM output^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:78-81]

## Experimental Results (Sleep Event Type)

Experiments focused on five event types from MIMIC-III nursing notes: *Eating*, *Excretion*, *Sleep*, *Family*, and *Pain*. Detailed evaluation was performed on the *Sleep* event type.

The dataset comprised 338,395 sentences from 15,222 nursing reports. Only 0.78% of sentences were labeled as *Sleep* under KM, illustrating severe class imbalance.

| Model | F1 (M-SET) | Precision | Recall |
|---|---|---|---|
| KM | 0.918 | 0.862 | 0.982 |
| LLM Ki | 0.923 | 0.900 | 0.947 |
| LLM Ko | 0.933 | 0.889 | 0.982 |

On the full dataset (F-SET), KM outperforms LLMs due to class imbalance. On the more representative M-SET (containing ambiguous cases), LLM-based approaches outperform KM, validating the hybrid strategy.^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:72-81]

## Keyword Refinement via LLM

LLM outputs (particularly with Ko prompting) are used to refine keyword lists:
- **Removal**: The keyword *bundle* was identified as an unreliable trigger for *Sleep* (8 of 9 false positives involved this keyword) and removed.
- **Addition**: For *Excretion*, high-precision candidates such as *urinal*, *diuresis*, *pass stool*, and *void pass* were added; *discharge* was removed as it commonly referred to hospital discharge rather than bodily excretion.^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:79-81]

## Data and Reproducibility

The annotated dataset and code are publicly available at [https://github.com/allmin/event_log_from_text](https://github.com/allmin/event_log_from_text). The work was funded by the NWO project TACTICS (628.011.004).

## Relationship to Process Mining

This work addresses the **event log construction** phase of process mining pipelines in healthcare. Structured event logs derived from clinical narratives enable downstream [[coordinated-projections-multi-faceted-process-exploration|process exploration]] and analysis tasks, including process discovery, conformance checking, and performance analysis. The approach complements [[process-mining-healthcare-radiological-workflows|radiological workflow mining]] by extending process mining to care dimensions captured only in free-text nursing documentation.

## Limitations and Future Work

- Clinical notes often lack punctuation and grammar, complicating sentence segmentation
- Class imbalance limits statistical confidence for underrepresented event types
- Some sentences are inherently ambiguous without broader note context or structured patient data
- The current framework assumes a many-to-one keyword-to-event-type mapping; future work will explore many-to-many associations
- Future directions include modeling temporal relationships and cross-sentence reasoning for complex event log extraction^[Susaiyah et al - Extracting Events from Nursing Notes a MIMIC-III Case Study.pdf:82-85]

## Key Data

- P = Given the sentence: {sentence},
- E ={e1,e 2,...,e k}, and a short task description. Optionally, the prompt may
- pos = 6 sentences per bin per
- neg = 6 sen-
- pos = 0.09 and θSleep
- neg = 0.48. M-SET includes 192 sentences, comprising 57

## LLM-Based Medication Extraction from EHR Notes

A complementary approach to general event log extraction focuses specifically on **medication data extraction** from unstructured EHR notes using Large Language Models (LLMs), as demonstrated in a COPD case study by Gómez-Noé et al. (ICPM 2025 Workshops). This work addresses the challenge of transforming free-text clinical notes — particularly in **non-English languages** — into structured medication events suitable for [[process-mining-psychiatric-pharmacotherapy|process mining of treatment trajectories]].

### Motivation and Context

While structured data sources (ICD codes, timestamps, medication administration records) are commonly used in healthcare [[process-mining-handbook|process mining]], unstructured clinical notes contain rich treatment information that is typically inaccessible to automated PM workflows. Data quality in free-text notes is identified as a key challenge (Munoz-Gama et al., challenge C6). Traditional NLP approaches — rule-based systems, fine-tuned neural networks — require extensive annotated datasets and domain expertise, making them impractical for many healthcare IT teams, especially for non-English corpora.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:79-120]

### Prompt-Based LLM Extraction

The study used **Llama 3** (8B parameter model) hosted locally via **Ollama** to extract medication names from 842 Spanish-language emergency care discharge reports for COPD patients. Local self-hosting was essential for compliance with data privacy regulations, as the free-text notes could expose sensitive patient information.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:10-29]

Five prompt configurations were systematically tested, varying:
- **Language** of the prompt (English vs. Spanish)
- **Output format** (plain text vs. JSON)
- **Prompt style** (single paragraph vs. bulleted instructions)
- **Scope** (all medications vs. COPD-specific medications)
- **Spelling correction** instructions

A key finding was that including spelling correction tasks in the prompt caused the LLM to alter medication names (e.g., "Seguril" → "Seguiril"), increasing model uncertainty. The selected prompt (JSON output, English, no spelling correction) with **temperature set to 0** for deterministic outputs achieved the best results.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:64-73]

### Custom Tooling

Two tools were developed (implemented in C#, publicly available):

- **Medication Parser**: Automates LLM API calls and saves extracted medications in CSV format.
- **Medication Manual Validator**: An interactive desktop tool that presents original EHR text alongside a SNOMED-CT search interface. It uses the **Levenshtein distance algorithm** to match LLM-extracted names back to original text (accounting for LLM-introduced alterations) and supports iterative expert corrections with color-coded validation (green = TP, red = FP, yellow = FN).

SNOMED-CT terminology was used to standardize extracted medication names, enabling consistent downstream analysis.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:24-29]

### Performance and Results

Evaluated on a random sample of 100 reports:

| Metric | Value |
|---|---|
| Precision | 0.978 |
| Recall | 0.998 |
| F1-Score | 0.9877 |

Across all 842 reports, **3,739 medication instances** were identified covering **122 unique medications**. The most frequent were ipratropium bromide (681 instances) and salbutamol (649 instances), consistent with standard COPD bronchodilator therapy.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:26-29]

The high performance is partly attributed to the relatively concise and structured nature of the selected EHR field ("Treatment administered in emergency care"), and may not generalize to more complex clinical narrative fields.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:26-29]

### Integration into a Process Mining Model

Extracted medications were grouped by a physician into 7 categories (bronchodilators, inhaled glucocorticoids, systemic glucocorticoids, PDE4 inhibitors, antibiotics, mucolytics, non-COPD) using SNOMED-CT classifications. These categories became **event types** in a PM model, where co-administered medications within a visit were represented as combined events (e.g., "Med A+B"). Analysis revealed that antibiotics and inhaled glucocorticoids were more common in patients with repeat emergency visits, informing potential care protocol improvements.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:26-29]

### Limitations and Future Directions

- LLMs have **limited contextual understanding**: medications mentioned as contraindications or allergies may be incorrectly extracted as administered drugs.
- Performance on more complex, verbose clinical notes remains to be evaluated.
- Future work includes sequential LLM pipelines for combined extraction and normalization, and comparison with advanced NLP workflows on diverse datasets.^[Gómez-Noé et al - Extraction and Identification of Medications from EHR Notes with LLMs - A Tool and a Case Study.pdf:64-76]

This approach complements [[narrative-based-predictive-process-monitoring-llm|narrative-based predictive process monitoring]] by demonstrating LLMs as a preprocessing tool for structured event log construction rather than for direct outcome prediction.
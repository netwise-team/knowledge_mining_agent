---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:25:39'
lint_warnings:
- claim: Each patient's prefix trace (events up to the midpoint of the case) is converted
    into a coherent clinical narrative
  concern: Defining a 'prefix trace' as events up to the midpoint is non-standard
    and potentially misleading. In predictive process monitoring literature, prefix
    traces are typically defined by a fixed prefix length (number of events) or a
    time window, not the midpoint of a case, which would require knowing the full
    case length in advance — undermining the predictive utility of the approach.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Nai et al - From Clinical
    Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf
  hash: 3278a7309daaf521341be3178d21061f35a0ef518c5a835e433f7e81d48af701
  ingested: '2026-07-14T07:25:39'
  size: 1455657
  truncated: true
status: active
tags:
- LLM
- outcome prediction
- clinical event logs
- narrative encoding
- transformer models
- predictive process monitoring
- emergency care
- patient flow
- healthcare AI
- embeddings
title: Narrative-Based Predictive Process Monitoring with LLMs
type: technology
---

# Narrative-Based Predictive Process Monitoring with LLMs

Narrative-based predictive process monitoring is an approach that transforms structured [[event-log-extraction-clinical-narratives|clinical event logs]] into free-text narrative descriptions using Large Language Models (LLMs), then encodes those narratives as sentence embeddings for outcome classification. This contrasts with traditional [[process-mining-healthcare-radiological-workflows|predictive process monitoring]] methods that operate directly on structured event sequences.

The approach was demonstrated in a case study by Roberto Nai, Emilio Sulis (University of Turin), Laura Genga (Eindhoven University of Technology), and Adriana Boccuzzi (A.O.U. San Luigi Hospital) at the ICPM 2025 Workshops (Springer LNBIP series), applied to emergency department (ED) patient outcome prediction.^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:4-11]

## Motivation

Emergency departments face high variability in patient arrivals, limited resources, and unpredictable care pathways. Early prediction of patient outcomes — specifically whether a patient will be discharged or hospitalised — supports resource allocation and timely clinical decision-making. Traditional predictive process monitoring (PPM) methods encode event sequences as structured feature vectors, which can lose contextual and semantic richness. Narrative representations offer improved interpretability and leverage the contextual understanding capabilities of pre-trained language models.^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:33-45]

## Pipeline Overview

The methodology consists of five stages:

1. **Dataset Extraction**: An event log is extracted from the Hospital Information System (HIS), with each record containing a patient identifier (Case ID), clinical treatment (activity), timestamp, ESI triage level, operator identifier, and outcome label.
2. **Event Log Construction**: Following standard event log structure guidelines (van der Aalst 2016), the log is exported in CSV format and validated using process discovery techniques.
3. **Event Log Enrichment**: Contextual features are added to each activity: concurrent ESI patients (crowding indicator), day of the week, and work shift (morning/afternoon/night).
4. **Narrative Generation via LLMs**: Each patient's *prefix trace* (events up to the midpoint of the case) is converted into a coherent clinical narrative using prompt-based generation with GPT-4. Two prompt types were explored — free-form and template-guided — with template-guided prompts adopted for their consistency and alignment with event log semantics.
5. **Classification via Sentence Embeddings**: Generated narratives are encoded using pre-trained Sentence-Transformer models into fixed-length dense vectors, which serve as input features for downstream classifiers (Random Forest, XGBoost, Feed-Forward Neural Network).^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:119-120]

## Prefix Traces and Prediction Point

Because outcome prediction requires observing only a partial process sequence, the study defines a *prefix trace* as the sequence of events available before a prediction point. Prefixes covering up to half of each case were used, reflecting a trade-off between early intervention and predictive accuracy supported by prior PPM literature.^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:71-76]

## Prompt Design

Three prompt formulations were evaluated:
- **Prompt 1 (free-form)**: Open-ended instructions allowing flexible natural language generation.
- **Prompt 2 (semi-structured)**: Guided sentence openings for moderate consistency.
- **Prompt 3 (template-guided)**: Fully constrained template with explicit placeholders, ensuring alignment with event log semantics.

Prompt 3 was selected for the full experiment. Narrative generation was parallelised using a thread-based approach, completing the full dataset in approximately 30 minutes with GPT-4.^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:18-29]

## Sentence Embedding Models

Eight pre-trained transformer models from the Sentence-Transformer (ST) library were evaluated, spanning architectures including BERT, MPNet, RoBERTa, and T5, with both general-purpose and biomedical-domain variants:

- `all-mpnet-base-v2` (MPNet, Microsoft)
- `intfloat/e5-base-v2` (BERT, Hugging Face)
- `BioBERT-mnli-snli-scinli-scitail-mednli-stsb` (BERT, DMIS Korea)
- `nli-roberta-base-v2` (RoBERTa, Facebook AI)
- `multi-qa-mpnet-base-dot-v1` (MPNet, Microsoft)
- `sentence-t5-base` (T5, Google)
- `princeton-nlp/sup-simcse-roberta-base` (RoBERTa, Princeton NLP)

Models were used in a *frozen* manner (no fine-tuning), with embeddings computed once and reused across classifiers.^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:23-25]

## Results

The case study used a real-world ED event log from San Luigi Gonzaga Hospital (Orbassano, Italy), covering 3,478 cases over one month (1,036 variants; median case duration 2.9 hours; 456 hospitalised, 2,807 discharged).^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:102-109]

Top classification results (ranked by F1-score):

| Embedding Model | Classifier | F1-score |
|---|---|---|
| multi-qa-mpnet-base-dot-v1 | FFNN | 0.868 |
| sup-simcse-roberta-base | XGB | 0.849 |
| multi-qa-mpnet-base-dot-v1 | XGB | 0.835 |
| e5-base-v2 | RF | 0.830 |

Averaged across top-10 combinations, FFNN achieved the highest average F1-score (0.834), followed by XGB (0.835) and RF (0.828). MPNet-based models consistently outperformed T5 and BioBERT variants in this setting.^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:54-61]

## Relationship to Existing PPM Approaches

This work builds on and extends two prior lines of research:
- **ProcessTransformer**: Models event sequences directly for next-activity and remaining-time prediction.
- **LUPIN**: Converts event logs into textual narratives for suffix prediction using a fine-tuned Medium BERT model.

The key distinction of this approach is that it uses *prompt-based LLM generation* (rather than rule-based templates) and *frozen sentence embeddings* (rather than supervised fine-tuning), reducing computational cost and enabling rapid experimentation.^[Nai et al - From Clinical Event Logs to Narrative-Based Outcome Prediction with Large Language Models.pdf:86-100]

## Limitations and Future Work

- No direct comparison with established PPM baselines was included in the initial study.
- The event log covers a single hospital and one month of data, limiting generalisability.
- Future directions include: (i) integrating explainability techniques to identify which narrative components drive predictions; (ii) systematic comparison with traditional PPM encoding methods; (iii) multi-task and cross-hospital generalisation studies.

## Connections to Related Topics

This approach bridges [[event-log-extraction-clinical-narratives|event log extraction]], [[process-mining-healthcare-radiological-workflows|healthcare process mining]], and [[process-mining-oncology-care-pathways|oncology care pathway analysis]] by introducing a narrative intermediary layer that improves interpretability for clinical staff and hospital management. The use of LLMs for event log verbalization also connects to broader work on [[veco-multimodal-process-mining-library|multimodal process mining]] and LLM-augmented process analysis.
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:58:24'
lint_warnings:
- claim: ~2% of patients are readmitted to ICU within 48 hours of ward transfer; 3.7%
    within 120 hours (across 156 U.S. ICUs)
  concern: The claim that the 120-hour readmission rate (3.7%) is lower than or only
    slightly higher than the 48-hour rate (2%) is implausible — a cumulative readmission
    rate over a longer window (120 hours) should always be equal to or greater than
    the rate over a shorter window (48 hours), but the figures cited suggest an unusually
    small incremental increase, raising doubts about whether these statistics are
    being accurately represented or compared on the same basis.
- claim: Unplanned ICU readmissions carry a mortality rate of 21–40%, vs. 3–8% for
    non-readmitted patients
  concern: While elevated mortality for ICU readmissions is well-established, the
    upper bound of 40% mortality is at the high end of published literature and the
    comparison baseline of 3–8% for non-readmitted patients conflates very different
    patient populations, making the contrast potentially misleading. However, this
    is more a nuance issue than a clear factual error, so this flag is offered with
    moderate confidence only.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Aljebreen et al - Predicting
    Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf
  hash: 9e49ad1daa1302f6a239e3b1d14985e53167040302d1f95eef9a74d034a426da
  ingested: '2026-07-14T07:58:24'
  size: 531581
  truncated: true
status: active
tags:
- pathway left shift
- care pathway
- ICU readmission
- surgical ward readmission
- patient deterioration
- machine learning
- deep learning
- event log
- healthcare
- patient flow
title: Predictive Process Monitoring for Pathway Left Shifts in Hospital Care
type: technology
---

# Predictive Process Monitoring for Pathway Left Shifts in Hospital Care

Predicting 'pathway left shifts' in hospital care is an application of [[narrative-based-predictive-process-monitoring-llm|Predictive Process Monitoring (PPM)]] that aims to forecast when a patient will deteriorate and return from less acute to more acute care — a clinically significant and costly event. This work, by Aljebreen, Pang, de Kamps, and Johnson (University of Leeds / Royal Centre for Defence Medicine), was accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Concept: Pathway Left Shifts

Hospital care pathways (CPs) are typically modelled as linear processes moving from left to right: admission → surgery → acute care → recovery → discharge. A **left shift** occurs when a patient moves *backwards* — from a less acute ward to a more acute one — indicating deterioration, premature transfer, or inadequate care planning.^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:38-44]

The paper focuses on two types of left shift:
- **ICU left shift**: unplanned readmission to the Intensive Care Unit
- **SW left shift**: unplanned readmission to the Surgical Ward (including unplanned reoperation)

Epidemiological context from the paper:
- ~2% of patients are readmitted to ICU within 48 hours of ward transfer; 3.7% within 120 hours (across 156 U.S. ICUs)
- Unplanned ICU readmissions carry a mortality rate of 21–40%, vs. 3–8% for non-readmitted patients
- ~14% of major head and neck surgery patients require unplanned reoperation during the same stay^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:47-53]

## Motivation for a Process Mining Approach

Prior studies on ICU/SW readmission prediction have largely overlooked process aspects, focusing instead on narrow clinical feature sets or specific patient cohorts. [[process-mining-oncology-care-pathways|Process Mining (PM)]] of clinical event data provides deeper contextual insights — capturing the sequence, timing, and frequency of patient transfers — that can substantially improve prediction accuracy.^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:55-61]

PPM extends PM by leveraging completed case traces to make predictions for *ongoing* cases at different process stages. This aligns with **Challenge 2: Discover Beyond Discovery** identified by the PM4H (Process Mining for Healthcare) research community.^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:76-85]

## Dataset: MIMIC-IV

The study uses the openly available **MIMIC-IV** electronic health record database (Beth Israel Deaconess Medical Centre, Boston, USA), covering >380,000 patients from 2008–2019. Using MIMIC-IV addresses **Challenge 4: Deal with Reality** from the PM4H community, ensuring reproducibility and real-world applicability.^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:95-103]

Two event logs were constructed from the Transfers Table:
- **ICU log**: 54,782 admissions, 234,294 events; 9,239 admissions (16.8%) had at least one ICU left shift
- **SW log**: 61,312 admissions, 193,513 events; 6,966 admissions (11.36%) had at least one SW left shift

Pathway lengths ranged from 2 to 23 events. Transfer events were aggregated into 11 clinical categories (e.g., 'Admission to ICU', 'Admission to Surgery', 'Admission to Medical Ward').

## PPM Framework: OOPPM

The study adopts the **Outcome-Oriented PPM (OOPPM)** framework, comprising:
- **Offline phase**: event log creation, prefix extraction, encoding, and classifier training
- **Online phase**: real-time bucketing, encoding, and classification of ongoing cases

A key methodological contribution is the addition of an explicit **'Create Extended Event Log'** step to the OOPPM framework, recognising that careful feature engineering is critical in healthcare PM.

### Feature Categories

| Category | Examples | Count |
|---|---|---|
| Demographic | Age (grouped), gender, ethnicity, insurance, marital status | 5 |
| Clinical | Abnormal lab %, Charlson Comorbidity Index, ICD disease categories, polypharmacy, BMI, prior unplanned readmissions | 27 |
| Process | Accumulated duration, ICU/SW duration, total events, admission location, number of ICU/SW stays | 7 |

Clinical diagnoses used ICD-9 and ICD-10 codes, consolidated into 18 disease categories to avoid encoding thousands of individual codes.

### Prefix Encoding

- **ML models**: Bag-of-Words (BoW) with N-gram range 1–3 for activity sequences
- **DL/DS models**: Label encoding of activities into integer sequences, zero-padded to maximum pathway length
- Bucketing used K-Means clustering (2 clusters) and process-state decision points (ICU vs. SW logs)

## Models Evaluated

The study compared a broad range of classifiers:
- **Baseline**: Logistic Regression (LR)
- **Machine Learning**: Gradient Boosting (GB), Random Forest (RF), K-Nearest Neighbours (KNN)
- **Deep Learning**: MLP, CNN, CNN-LSTM hybrid
- **Deep Sequence**: RNN, LSTM, BiLSTM, GRU, BiGRU

All models used class weights, hyperparameter tuning, and 10-fold cross-validation. Metrics included accuracy, AUROC, AUPRC, precision, recall, F1, and computation time.

## Key Results

### Without Process Features
- Best ML model (RF): ICU accuracy 0.83, F1 0.30; SW accuracy 0.89, F1 0.44
- DL/DS models: ICU F1 ≤ 0.39, SW F1 < 0.47
- LR showed high recall (0.95 for ICU) but very low precision — over-predicting positives in imbalanced settings

### With Process Features
- RF: ICU accuracy 0.94, F1 0.82; SW accuracy 0.96, F1 0.86
- GB: ICU AUROC 0.98, F1 0.83; SW AUROC 0.99, F1 0.85
- GRU: ICU F1 0.81, SW F1 0.84
- AUROC reached up to **0.99** across multiple models
- Including pathway activities improved F1 by up to 0.05 (ML) and 0.15 (DL)^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:25-28]

Process features drove the largest performance gains. The most important process features were:
- Accumulated duration (total time in hospital)
- ICU and surgery duration
- Total number of transfer events

Key clinical features: abnormal lab test percentage, total medications, number of respiratory diseases.

### Practical Considerations
- Tree-based models (RF, GB) offered fast prediction times (<0.2s) with competitive accuracy — attractive for real-time PPM
- DL/DS models required longer training and prediction times but delivered higher accuracy
- N-gram modelling showed no benefit, likely due to high pathway heterogeneity (activity *presence* mattered more than *order*)
- Activity aggregation had minimal impact (±0.01 F1)
- K-Means clustering had no measurable effect on results

## Relation to PM4H Challenges

This work directly addresses two challenges from the PM4H research agenda:
1. **Challenge 2 – Discover Beyond Discovery**: developing predictive capabilities in healthcare PM
2. **Challenge 4 – Deal with Reality**: applying PM to real-world, openly available EHR data (MIMIC-IV)^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:80-99]

The authors also highlight the need for standardised feature engineering guidelines for clinical PM, and propose that integrating PPM into Healthcare Information Systems (HISs) could complement existing clinical decision support.

## Comparison with Prior Work

| Study | Dataset | Method | Best AUROC |
|---|---|---|---|
| Su et al. | Proprietary (rectal cancer) | Random Forest | 0.889 |
| Inan et al. | MIMIC-III (11,000 stays) | ANN | 0.874 |
| Wu et al. | MIMIC-III (36,232 stays) | BERTopic + LSTM | 0.80 |
| Rojas et al. | MIMIC-III (24,885 transfers) | Gradient Boosting | 0.76 |
| Chen et al. | MIMIC-IV | PPM (process + clinical) | ~0.65 accuracy |
| **This study** | **MIMIC-IV (54K–61K admissions)** | **PPM (process + clinical + demographic)** | **0.99** |

This study is notable for targeting a *general hospital population* (not a specific clinical cohort), using a broader feature set, and demonstrating that process-aware PPM substantially outperforms prior approaches.^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:86-88]

## See Also
- [[narrative-based-predictive-process-monitoring-llm]]
- [[process-mining-oncology-care-pathways]]
- [[process-mining-psychiatric-pharmacotherapy]]
- [[event-log-extraction-clinical-narratives]]
- [[process-mining-workflow-documentation]]

## Key Data

- achieving AUROC = 0.80 and demonstrating improved performance over models using
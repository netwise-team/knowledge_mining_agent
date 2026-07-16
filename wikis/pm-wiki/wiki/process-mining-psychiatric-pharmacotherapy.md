---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:28:43'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Soleimani et al - Comparative
    Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant
    Depression.pdf
  hash: dc4685a53c0778a4a6bc1042f559fbae628c3748b698e95787200a1b4addaa9c
  ingested: '2026-07-14T07:28:43'
  size: 1234699
  truncated: true
status: active
tags:
- pharmacotherapy
- psychiatry
- treatment pathways
- care pathways
- process mining
- depression
- clinical data analysis
- heterogeneity
- observational study
- EHR
title: Process Mining for Psychiatric Pharmacotherapy
type: concept
---

# Process Mining for Psychiatric Pharmacotherapy

Process mining has been applied to psychiatric pharmacotherapy to uncover real-world treatment trajectories from electronic health records (EHRs), with a particular focus on major depressive disorder (MDD) and treatment-resistant depression (TRD). This application area extends [[process-mining-oncology-care-pathways|oncology-focused process mining]] and [[process-mining-healthcare-radiological-workflows|healthcare process mining]] into the domain of mental health, where care pathways are highly heterogeneous and poorly standardized.

## Motivation

Major depressive disorder affects over 280 million people worldwide and is a leading cause of disability. Treatment-resistant depression (TRD) — typically defined as inadequate response to at least two adequate antidepressant trials — affects 20–30% of MDD patients and is associated with higher mortality, greater healthcare resource utilization, and highly individualized treatment pathways. Despite the clinical burden of TRD, the detailed structure of real-world pharmacological trajectories has remained poorly characterized. Process mining offers a data-driven approach to reconstruct and compare these pathways at scale from EHR data.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:27-34]

## Case Study: TRD vs. Non-TRD Antidepressant Trajectories

Soleimani et al. (ICPM 2025 Workshops, Hasso Plattner Institute / Icahn School of Medicine at Mount Sinai) applied process mining to EHR data from 31,881 MDD patients (4,630 TRD; 27,251 non-TRD) with 415,641 antidepressant exposures drawn from the Mount Sinai Data Warehouse, structured under the OMOP Common Data Model (CDM).^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:13-16]

### Key Findings

- **Extreme heterogeneity in TRD**: 4,332 unique trace variants were identified among 4,630 TRD cases — nearly a one-to-one ratio of variants to cases. The most common TRD variant appeared in only 16 cases.
- **Homogeneity in non-TRD**: 74% of non-TRD patients (20,141/27,251) completed treatment within a single antidepressant category; the most frequent variant appeared in 2,943 cases.
- **Treatment duration**: Median case duration was 1,473 days in TRD versus 112 days in non-TRD.
- **Event counts**: Mean events per case were 40.0 (TRD) vs. 8.5 (non-TRD).
- **Switch patterns**: 58.9% of TRD and 55.7% of non-TRD category switches were same-day (zero-day delay), reflecting polypharmacy or immediate transitions during clinical encounters.
- **Initial treatment**: No major differences in starting drug categories between TRD and non-TRD; heterogeneity in TRD emerges later in the care pathway.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:15-23]

## Methodology

### Cohort Selection

Patients were required to have at least one year of clinical history prior to their first MDD diagnosis and no antidepressant exposure before diagnosis (with a 30-day buffer). MDD diagnoses were mapped from ICD-9/10 to SNOMED CT using the OMOP concept hierarchy, and antidepressant exposures were identified via RxNorm ingredient codes with descendant concept expansion.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:113-120]

### Event Log Generation

Prescription records were de-duplicated and semantically enriched by mapping each OMOP drug concept to its canonical ancestor (active ingredient), then abstracted to therapeutic class (SSRI, SNRI, atypical antidepressants, tricyclic antidepressants, MAOIs, augmentation agents, or others). TRD status was operationalized using the STAR*D definition: ≥2 failed adequate antidepressant trials, where an adequate trial was defined as ≥56 days of continuous exposure to the same ancestor drug. Separate XES event logs were generated for TRD and non-TRD cohorts using the PM4Py framework. This approach is consistent with best practices described in [[event-log-extraction-clinical-narratives|event log extraction]] literature.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:97-120]

### Process Discovery and Analysis

Directly-Follows Graphs (DFGs) were computed using PM4Py for both cohorts. Synthetic *Start* and *End* events were prepended/appended to each trace to enforce single-entry, single-exit structure. A 50-occurrence edge-frequency threshold was applied to filter low-frequency transitions for interpretability, reducing DFG edge coverage from 85% to 68% while retaining all *Start*/*End* edges. Trace variant analysis, case-length distributions, and temporal metrics (case duration, case dispersion) were computed via PM4Py's variant-analysis module.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:97-100]

## Methodological Challenges in Psychiatric Process Mining

- **High pathway variability**: Psychiatric treatment pathways are among the most heterogeneous in healthcare, making standard process discovery algorithms produce complex, difficult-to-interpret models.
- **Event abstraction**: Mapping individual drug prescriptions to therapeutic classes is essential for managing model complexity and improving clinical interpretability, as recommended by domain-specific event abstraction techniques.
- **TRD operationalization**: The STAR*D definition (≥2 failed trials of ≥56 days) is widely used but not universally accepted; alternative definitions may yield different cohort compositions.
- **Data completeness**: Prescription data from EHRs may be incomplete; dose changes within the same drug are not captured as switches in this framework.
- **Selection bias**: Requiring ≥1 year of prior history and excluding patients with pre-diagnosis antidepressant exposure may underrepresent chronic or recently transferred patients.
- **Absence of non-pharmacological data**: Psychotherapy, neuromodulation, and other interventions are not captured, limiting the completeness of the care pathway representation.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:36-41]

## Comparative Process Mining Techniques

The study establishes a reproducible baseline using DFGs and variant analysis, and identifies several advanced comparative techniques for future work:

- **Earth Mover's Distance** (Brockhoff et al., CAiSE 2024): quantifies differences between subprocesses via selection–projection structures.
- **Statistical testing on annotated transition systems** (Bolt et al., CAiSE 2016): highlights differences in activity frequencies and timing.
- **Stochastic-aware comparative process mining / P2CM** (Mazhar et al., BPM 2023): incorporates pathway likelihoods and automated cohort analysis.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:73-81]

These methods were not applied in the baseline study but are identified as essential for systematic cohort comparison in future psychiatric process mining research.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:79-81]

## Relation to Broader Healthcare Process Mining

This work extends the application of [[process-mining-healthcare-radiological-workflows|healthcare process mining]] to psychiatry, a domain previously underserved due to incomplete data and unclear clinical definitions. It complements [[process-mining-oncology-care-pathways|oncology care pathway mining]] by demonstrating that process mining can characterize pharmacological trajectories in chronic, relapsing conditions. The use of [[event-log-extraction-clinical-narratives|structured event log extraction]] from OMOP-standardized EHR data provides a reproducible pipeline applicable to multi-site validation.^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:35-41]

## Future Directions

- Integration of advanced comparative techniques (Earth Mover's Distance, overlay-based model comparison, cluster-based contrasts)
- Multi-site replication to assess generalizability across health systems
- Structured clinical validation of process models with domain experts
- Incorporation of psychotherapy, neuromodulation, comorbidity profiles, and sociodemographic data
- Predictive process monitoring for TRD outcomes, potentially leveraging approaches such as [[narrative-based-predictive-process-monitoring-llm|narrative-based LLM methods]]^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:20-23]

## References

- Soleimani, Z., Charney, A., Landi, I., Weske, M. (2025). *Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression: A Case Study.* ICPM 2025 International Workshops, Springer LNBIP.
- Berti, A., van Zelst, S.J., Schuster, D. (2023). PM4Py: A process mining library for Python. *Software Impacts*, 17, 100556.
- Munoz-Gama, J. et al. (2022). Process mining for healthcare: Characteristics and challenges. *J. Biomed. Informatics*, 127, 103994.

## Key Data

- TRD = treatment-resistant depression, non-TRD = non-treatment-resistant depres-
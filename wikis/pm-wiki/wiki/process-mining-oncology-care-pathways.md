---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:14:04'
lint_warnings:
- claim: A widely adopted framework for healthcare process mining projects is the
    PM² methodology (van Eck et al., 2015)
  concern: The PM² methodology for process mining in healthcare is attributed to van
    Eck et al., 2015, but the well-known PM² methodology is actually associated with
    Mans et al. or other authors. More importantly, 'PM²' is also widely known as
    a project management methodology developed by the European Commission. Attributing
    a specific 6-stage healthcare process mining framework to 'van Eck et al., 2015'
    with this name warrants scrutiny, as the citation details may be inaccurate or
    conflated with another framework.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Santos et al - Using Process
    Mining to Analyze Care Pathways in an Outpatient Oncology Clinic.pdf
  hash: 941002f098891b56614638d0ed26be4a6b1fab680c5e85aaccd0ca8875cb6a0a
  ingested: '2026-07-14T07:14:04'
  size: 778854
status: active
tags:
- process mining
- oncology
- care pathways
- patient flow
- Brazil
- chemotherapy
- radiotherapy
- process discovery
- healthcare efficiency
- event logs
title: Process Mining for Oncology Care Pathways
type: technology
---

# Process Mining for Oncology Care Pathways

Process mining has been applied to oncology settings to discover, analyze, and improve care pathways for cancer patients. Unlike general [[process-mining-healthcare-radiological-workflows|radiological workflow analysis]], oncology-focused process mining addresses the full patient journey — from initial multidisciplinary evaluation through treatment (chemotherapy, radiotherapy, surgery) to discharge — as well as the day-to-day departmental workflows within cancer treatment centers.

## Motivation

Oncology care is characterized by high complexity: patients may follow diverse treatment pathways depending on cancer type, stage, and individual response. Delays at any point in the care pathway can negatively impact clinical outcomes. Traditional management approaches based on personal judgment often fail to capture the true complexity of these workflows, even in digitalized institutions. Process mining enables evidence-based discovery of actual care flows, identification of bottlenecks, and detection of deviations from clinical protocols.^[Santos et al - Using Process Mining to Analyze Care Pathways in an Outpatient Oncology Clinic.pdf:26-45]

## PM² Methodology in Oncology

A widely adopted framework for healthcare process mining projects is the **PM² methodology** (van Eck et al., 2015), which structures a project into six stages:

1. **Planning** — Define research questions from organizational goals and identify relevant information systems.
2. **Extraction** — Retrieve event data from clinical information systems (e.g., EHR, billing modules) via SQL scripts.
3. **Data Processing** — Structure extracted data into standardized [[event-log-extraction-clinical-narratives|event logs]], enriched with attributes such as ICD-10 codes, therapeutic approach, age group, and gender.
4. **Mining and Analysis** — Apply process discovery and variant analysis techniques.
5. **Evaluation** — Assess findings against organizational goals.
6. **Process Improvement** — Implement and monitor changes.

In practice, many oncology case studies focus on the first four stages, leaving evaluation and improvement for future work.^[Santos et al - Using Process Mining to Analyze Care Pathways in an Outpatient Oncology Clinic.pdf:98-115]

## Case Study: Brazilian Outpatient Oncology Clinic

Santos et al. (ICPM 2025 Workshops) applied the PM² methodology at the **Centro Oncologico Mogi das Cruzes**, a Brazilian outpatient clinic treating all cancer types and receiving approximately 150 new cases per month with an average of 65 patients treated daily. The study was conducted in collaboration with Instituto Tecnológico de Aeronáutica and Compumedica Research & Innovation.^[Santos et al - Using Process Mining to Analyze Care Pathways in an Outpatient Oncology Clinic.pdf:55-57]

### Two Distinct Process Scopes

The study modeled two complementary business processes:

- **Department Workflow**: The patient's flow within the clinic during a single chemotherapy or radiotherapy session. Research questions focused on critical paths, average execution times, and deviations from institutional workflows.
- **Treatment Workflow**: The longitudinal care pathway from initial multidisciplinary evaluation to discharge, spanning January–May 2025. Research questions focused on the most common treatment pathway and differences across cancer types.

### Data Extraction and Event Logs

Event data were extracted from the clinic's proprietary management system (Firebird database) using SQL scripts validated by the IT team. No personal patient data were extracted; only event identifiers, activity names, timestamps, scheduled times, arrival times, executor identifiers, and resources used. The Department Workflow extraction yielded 13,400 rows; the Treatment Workflow yielded 67,469 rows. Data were stored in PostgreSQL and exported to CSV for analysis with **Fluxicon Disco**.

Event logs were enriched with ICD-10 codes, first-line therapeutic approach, age group, and gender to enable segmented analysis.

### Department Workflow Findings

Process discovery revealed three dominant daily flows:
1. **Radiotherapy**: Reception check-in → radiotherapy session (2,754 occurrences).
2. **Medical consultations**: Reception check-in → medical consultation (2,535 occurrences).
3. **Chemotherapy infusion**: Reception check-in → medication dispensing → drug administration (874 occurrences).

The average process execution time was **92.8 minutes**, with 94% of cases completed in under 1 hour and 43 minutes. Chemotherapy, the longest workflow (3–6 hours), accounted for only 16% of cases.

Significant deviations detected included:
- 57 patients (~1%) checking in at reception more than once.
- 24 patients proceeding directly to medication dispensing without reception check-in.
- 36 patients proceeding directly to medical consultation without check-in.

A **70% case coverage threshold** was used to manage the large number of process variants — only variants collectively covering 70% of cases were analyzed in detail.

### Treatment Workflow Findings

The most frequent treatment was **radiotherapy** (1,355 patients), reflecting the clinic's role as a regional reference center for this service. Chemotherapy was second (490 cases).

Comparisons across **breast, prostate, and digestive organ cancers** (together ~70% of cases) revealed distinct pathway patterns:
- **Prostate cancer**: More defined flow with radiotherapy as the predominant approach.
- **Digestive organ cancers**: Higher prevalence of chemotherapy and supportive therapy.
- Findings were consistent across time periods, age groups, and patient gender, suggesting these variables do not significantly affect treatment approach at this clinic.

## Historical Context and Related Work

Oncology was among the first healthcare domains to adopt process mining. Key milestones include:
- **Mans et al. (2008)**: Analysis of gynecological oncology patient flows in a Dutch hospital, examining control flow, organizational, and performance perspectives.
- **Pijnenborg et al. (2021)**: Process mining for palliative care in stomach and esophageal cancer using Netherlands Cancer Registry data.
- **Savino et al. (2023)**: Rectal cancer treatment adherence to European guidelines at an Italian hospital.
- **Iachecen et al. (2023)**: Lung cancer patient journey within a Brazilian health insurance provider.

Process discovery remains the dominant technique in oncology process mining (53% of studies per Santos Garcia et al.), reflecting its role as the essential first step before conformance checking or enhancement.^[Santos et al - Using Process Mining to Analyze Care Pathways in an Outpatient Oncology Clinic.pdf:59-96]

## Relationship to Broader Healthcare Process Mining

Oncology process mining shares foundational techniques with [[process-mining-healthcare-radiological-workflows|radiological workflow analysis]] and [[event-log-extraction-clinical-narratives|clinical event log extraction]], but is distinguished by:
- Longer case durations spanning months to years (treatment workflows).
- High pathway variability driven by cancer type, stage, and individual patient response.
- The need to compare pathways across tumor types for resource planning and guideline compliance.
- Integration of clinical data (ICD-10, therapeutic modality) rather than purely operational or imaging data.

## Applications and Future Directions

Process mining in oncology supports:
- **Operational management**: Right-sizing resources to match patient volumes per treatment type.
- **Quality assurance**: Detecting deviations from institutional or clinical guideline workflows.
- **Care planning**: Tailoring operational strategies to tumor-type-specific pathway patterns.
- **Conformance checking**: Future work can assess adherence to leading oncology guidelines (e.g., ESMO, NCCN).
- **[[sustainability-aware-process-mining|Sustainability]]**: Optimizing resource allocation to reduce waste in high-volume oncology settings.

The Santos et al. (2025) case study demonstrates that even with a relatively simple toolset (Fluxicon Disco, CSV exports), actionable insights can be generated for both clinical and operational teams in outpatient oncology settings.
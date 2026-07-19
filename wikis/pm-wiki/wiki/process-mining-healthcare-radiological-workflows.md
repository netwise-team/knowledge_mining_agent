---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T06:58:10'
lint_warnings:
- claim: radiology remains comparatively underexplored in process mining research
    compared to other medical specialties
  concern: This is a debatable characterization that may actually be inverted. Radiology
    is one of the more digitally mature specialties with rich structured data (DICOM,
    PACS, RIS), and there is a substantial body of process mining literature applied
    to radiology workflows. Claiming it is underexplored *compared to other specialties*
    is not a well-established fact and may contradict the broader literature.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Kantor et al - Applying Process
    Mining to Radiological Workflows A Clinical Case Study.pdf
  hash: 1ee62c2020b1da47a8af9173a5918813d87c7f95d2f0cfdb4d7c8c8a17ce0368
  ingested: '2026-07-14T06:58:10'
  size: 689792
status: active
tags:
- process mining
- healthcare
- radiology
- workflow analysis
- compliance monitoring
- bottleneck detection
- clinical quality
- interoperability
- data-driven analysis
- hospital operations
title: 'Process Mining for Healthcare: Radiological Workflows'
type: technology
---

# Process Mining for Healthcare: Radiological Workflows

Process Mining for Healthcare (PM4H) applies [[coordinated-projections-multi-faceted-process-exploration|process mining]] techniques to clinical workflows to enable data-driven analysis, compliance monitoring, and operational improvement. Radiology is an emerging application area where rich digital traceability — via systems such as DICOM, HL7, and PACS — makes process mining particularly tractable.

## Background and Motivation

The healthcare sector faces growing challenges related to resource efficiency and service quality. The **Integrating the Healthcare Enterprise (IHE)** initiative promotes interoperability among healthcare information systems using standards such as DICOM (for image transfer) and HL7 v2.x (for order and result messaging). Within radiology, IHE proposes the **Scheduled Workflow (SWF)** framework, which defines an integrated process for ordering, scheduling, acquisition, storage, and visualization of radiological images. Process mining can assess and improve compliance with this framework, identifying bottlenecks, inefficiencies, and deviations in clinical execution.^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:26-50]

Despite radiology's central diagnostic role and rich digital traceability, it remains comparatively underexplored in process mining research compared to other medical specialties.^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:87-91]

## Case Study: Hospital de Clínicas, Uruguay

Kantor, Delgado, and Calegari (ICPM 2025 Workshops) applied process mining to radiological workflows at **Hospital de Clínicas**, a large public university hospital in Uruguay, with two goals: (1) identify improvement opportunities, and (2) empirically validate PM4H characteristics and challenges in this context.^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:51-63]

### System Architecture

The hospital operates a distributed web-based Health Information System (HIS) integrating subsystems for Admissions, Appointment Scheduling, Medical History, Emergency Room, and Study Requests. The Radiology Information System (RIS) is embedded within the HIS. The system interoperates with radiological devices via DICOM for image management and HL7 v2.x for demographic data, orders, and reports. A **Worklist server** acts as a critical digital queue, transmitting scheduled patient and study data directly to imaging equipment in compliance with the SWF profile.^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:99-119]

### Methodology

The study followed the **PM² methodology**, aligning institutional objectives and ensuring active stakeholder participation. Key research questions addressed:

1. Differences in patient attention times between emergency and scheduled studies
2. Compliance with institutional time criteria (24 hours max for emergencies; one month for scheduled)
3. Impact of Worklist usage on efficiency
4. Degree of compliance with the SWF standard
5. Data inconsistencies affecting traceability

### Data Extraction and Processing

- **Period:** October 2021 – March 2024
- **Sources:** MySQL HIS database and PACS server
- **Modalities:** MRI (MR), CT, Mammography (MG), Radiography (CR)
- **Key events:** request creation, appointment scheduling, Worklist upload, study start/completion, report creation
- **Raw log:** 602,011 events in 103,198 cases and 12,713 variants (XES format)
- **Processed log:** 174,000 events in 30,024 cases and 999 variants (after quality filtering)

Data quality issues included duplicates, incomplete records, timestamp inconsistencies, and studies without corresponding images. Cross-referenced SQL queries linked patient events by Medical Record Number (MRN) and event date proximity.

### Key Findings

**Workflow disparities by modality:**
- **MRI:** Only 20% of appointments used the Worklist, generating significant delays
- **CT:** Most efficient modality — median 2.1 hours from study start to report generation
- **Radiography (CR):** 69% emergency-driven, only 4% with report generation — major bottleneck at final phase
- **Mammography (MG):** Fully scheduled but with reporting delays

**Compliance with institutional time criteria:**
- Emergency studies: median 1 hour 25 minutes from order to study start (within 24-hour limit)
- Scheduled studies: median 11 days (within one-month limit), but significant outliers exist

**Worklist usage:** 75% of studies use Worklists to some extent, but MRI emergency cases use it in only 38% of cases.

**SWF compliance:** Only **45.2% of cases** correctly complied with the SWF standard. Deviations included generating reports before study completion and accessing the Worklist mid-procedure, creating risks of diagnostic errors and loss of traceability.

**Data inconsistencies:** 11% of appointments were not linked to completed studies; 6.69% of emergency requests did not result in study initiation. A critical bug was discovered where 700 cases had multiple patients sharing a single appointment due to a recursive scheduling activity — a bug that had gone undetected for **14 years**.

### Improvements Implemented

- Immediate correction of the 14-year-old scheduling module bug
- Automated alerts for studies with pending reports
- Additional HIS restrictions to prevent redundant scheduling
- Training initiatives on Worklist usage for radiology practitioners
- Plans for mandatory Worklist controls and scheduling policy review

## PM4H Distinguishing Characteristics and Challenges

The case study was evaluated against the PM4H characteristics and challenges framework (Munoz-Gama et al., 2022):

| Characteristic | Manifestation |
|---|---|
| **D1: Substantial variability** | 16 frequent variants across >12,000 studies; wide temporal dispersion by modality and context |
| **D2: Infrequent behavior** | 700 double-booked agendas; MG in ER without clinical justification |
| **D3: Guidelines and protocols** | SWF adopted but 15% of studies lack reports; CR operates outside scheduling |
| **D4: Break-the-glass** | Uncontrolled workflow jumps; studies without Worklist or schedule validation |
| **D5: Multiple abstraction levels** | Required merging administrative, clinical, and technical (PACS) data layers |
| **D6: Multidisciplinary team** | Radiologists, technologists, HIS developers, and infrastructure staff collaborated |
| **D7: Patient focus** | Missing reports and modality mismatches affect diagnostic continuity and patient safety |
| **D8: White-box approaches** | Trace visualizations exposed incomplete flows and modality divergences |
| **D9: Sensitive/low-quality data** | Timestamp inconsistencies, duplicates, weak patient linkage, scheduler error |
| **D10: Rapid evolution** | HIS built for smaller volume; CT demonstrates achievable efficiency with best practices |

### Key Challenges Addressed

- **C1 (Tailored methodologies):** Separate analysis per modality and context required
- **C2 (Beyond discovery):** Conformance checking and enhancement complemented discovery
- **C3 (Concept drift):** Long-standing bugs and evolving practices call for drift-aware monitoring
- **C6 (Data quality):** Modality-specific clinical coherence checks needed
- **C9 (Complement HIS):** Process-aware validation rules and automated alerts must be embedded in the HIS

## Broader Research Context

Recent PM4H research trends include:
- Combining process mining with **process simulation** for what-if analyses
- Embedding process mining within **continuous improvement frameworks** (e.g., Kaizen)
- Extending process mining to **health equity monitoring** with fairness metrics
- End-to-end, cross-departmental pathway monitoring via advanced discovery techniques^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:77-86]

Foundational radiology-specific contributions include the use of standardized terminology to avoid ambiguity in event mapping (Helm, 2020) and analysis of heterogeneous PACS interaction patterns among radiologists (Forsberg et al., 2016).^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:91-97]

## Limitations and Future Work

The study acknowledges single-site validity threats, non-trivial event log reconciliation across data layers, and institution-specific KPIs limiting generalization. Future work includes:
- Formal conformance quantification against SWF
- Automated concept drift detection
- Real-time alerts and DIY dashboards for clinical teams
- Embedding process-aware rules directly into the HIS for continuous compliance
- Prospective evaluation of operational changes introduced

## References

- Kantor, J., Delgado, A., Calegari, D. (ICPM 2025 Workshops): *Applying Process Mining to Radiological Workflows: A Clinical Case Study*
- Munoz-Gama, J. et al. (2022): *Process mining for healthcare: Characteristics and challenges.* J. Biomed. Informatics 127, 103994
- van Eck, M.L. et al. (2015): *PM²: A process mining project methodology.* CAISE 2015
- Forsberg, D. et al. (2016): *Analyzing PACS usage patterns by means of process mining.* Journal of Digital Imaging 29, 47–58
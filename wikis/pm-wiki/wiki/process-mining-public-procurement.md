---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:52:21'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Artavia Pereira et al - Process
    Mining in a Public Procurement Process A Case Study.pdf
  hash: 0daa7e0c3e73358b968112bcbbe661546e611204f08083c0695e83ed8ab48e12
  ingested: '2026-07-14T07:52:21'
  size: 164384
status: active
tags:
- process mining
- public procurement
- conformance checking
- bottleneck analysis
- KPIs
- ETL
- event logs
- compliance
- Costa Rica
- case study
title: 'Process Mining in Public Procurement: University of Costa Rica Case Study'
type: concept
---

# Process Mining in Public Procurement: University of Costa Rica Case Study

This page covers the application of [[process-mining-data-science-in-action|process mining]] to public procurement processes, illustrated by a case study conducted at the **University of Costa Rica (UCR)**. The work was authored by Catalina Artavia Pereira, Silvia Solano Mora, Michael Arias, and Ana Lucía León Román, and accepted for presentation at the ICPM 2025 Workshops (Springer LNBIP series).

## Background and Motivation

Public procurement is a strategic institutional function responsible for acquiring goods and services necessary for operations. These processes are governed by legal frameworks and require strong internal controls and resource optimization. Despite the availability of digital systems, systematic data-driven analysis of procurement workflows has historically been limited. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:15-20]

At UCR, the **Procurement Office (OSUM)** manages procurement activities under Costa Rican public procurement law. This case study represents the first application of [[process-mining-data-science-in-action|process mining]] at OSUM, motivated by the need for a more comprehensive and evidence-based understanding of procurement execution. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:21-24]

## Data Sources and ETL

Data from 2023 and 2024 were extracted from two platforms:

- **SICOP** (Sistema Integrado de Compras Públicas): Costa Rica's national integrated public procurement system.
- **GECO**: UCR's internal procurement management platform.

The project followed three key stages:
1. **ETL process**: Extraction, transformation, and loading of event log data to address data quality and structural inconsistencies across platforms.
2. **KPI definition**: Identification of key performance indicators relevant to procurement procedure types.
3. **Process Mining tool application**: Discovery, conformance checking, and performance analysis.

Data governance and internal standardization were identified as critical prerequisites, as significant effort was required to reconcile data from heterogeneous institutional systems. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:24-28]

## Key Findings

### Reality vs. Design
Only **30% of cases conform** to the ideal (normative) process model. The analysis revealed structural inefficiencies caused by unplanned activities, demonstrating that real process execution frequently deviates from formal procedural design. This finding underscores the value of [[process-mining-data-science-in-action|process mining]] over purely document-based process analysis. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:30-34]

### Bottleneck Analysis by Procedure Type
The study identified bottlenecks associated with specific procurement categories:
- **Minor tenders** and **major tenders** exhibited average delays of up to **156 days**.
- Bottleneck patterns differed by procurement type, enabling targeted, procedure-specific interventions rather than generic process improvements. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:35-39]

### Compliance Diagnostics and Conformance Checking
Conformance checking was applied to evaluate adherence to the normative process model across years and procurement types:
- **Major tenders** showed improvement in compliance: from **8% (2023) to 40% (2024)**.
- **Small purchases** showed a decline: from **61% (2023) to 51% (2024)**.

These diverging trends highlight the importance of differentiating process improvement strategies by procurement category rather than applying uniform interventions. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:45-49]

### Data Management as a Core Enabler
Despite the availability of detailed event logs, the project required substantial ETL work to address data quality issues. This reinforces the broader process mining principle that **data governance and log quality** are foundational to reliable analysis. Strengthening internal standardization across institutional platforms was recommended as a priority. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:50-53]

## Contributions and Implications

The case study demonstrates how process mining can:
- **Quantify process conformance** in regulated public sector workflows.
- **Identify procurement-specific bottlenecks** with measurable time impacts.
- **Reveal execution variations** that affect efficiency and compliance.
- Provide OSUM staff with **actionable insights** for operational planning, control reinforcement, and evidence-based decision-making.

This work is part of a broader graduation project titled *Aplicación de minería de procesos para los procesos de contratación ordinaria en la UCR* (Chacón, Herrera & Matarrita, 2025), developed within the Industrial Engineering program at UCR. ^[Artavia Pereira et al - Process Mining in a Public Procurement Process A Case Study.pdf:54-58]

## Relation to Other Process Mining Applications

This case study shares methodological similarities with other public sector applications of process mining, such as [[process-mining-egovernment-collaborative-choreography|e-Government collaborative process choreography]], where inter-organizational processes are analyzed for compliance and efficiency. It also reflects challenges common to [[process-mining-workflow-documentation|process mining workflow documentation]], particularly around data quality and reproducibility in institutional settings.

## References

1. Hidalgo, R.C. (2022). Public procurement, a matter of principles? *Revista De Ciencias Jurídicas*, 159, pp. 1–33.
2. Van Der Aalst, W. (2016). Data science in action. In *Process Mining: Data Science in Action* (pp. 3–23). Springer Berlin Heidelberg.
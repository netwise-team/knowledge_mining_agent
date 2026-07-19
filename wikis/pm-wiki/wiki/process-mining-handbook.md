---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:09:10'
lint_warnings:
- claim: The Process Mining Manifesto (translated into 15+ languages)
  concern: The Process Mining Manifesto is widely cited as having been translated
    into over 20 languages, not merely '15+'. Understating the number is a factual
    inaccuracy relative to well-documented community records.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Process Mining Hanbook.pdf
  hash: db6e8f06959e9127febe8eb6f752f8cfeb43daf26aba42bb3c2132204570589e
  ingested: '2026-07-14T07:09:10'
  size: 153608
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/handbook2.pdf
  hash: b554a317f95114533fd75d1027c6e880b8dfc8bf0c4f2077d0dc42eb6afb375c
  ingested: '2026-07-14'
  size: 23933329
  truncated: true
status: active
tags:
- process mining
- event data
- process discovery
- conformance checking
- performance analysis
- process models
- control-flow
- open access
- tutorial
- business information processing
title: Process Mining Handbook (LNBIP 448)
type: technology
updated: '2026-07-14'
---

# Process Mining Handbook (LNBIP 448)

The *Process Mining Handbook* (Lecture Notes in Business Information Processing, Vol. 448) is an open-access reference work edited by **Wil M. P. van der Aalst** (RWTH Aachen University) and **Josep Carmona** (Universitat Politècnica de Catalunya), published by Springer Nature in 2022 (ISBN 978-3-031-08848-3, DOI: 10.1007/978-3-031-08848-3). It constitutes the core material of the first Summer School on Process Mining, organized by the IEEE Task Force on Process Mining in Aachen, Germany, July 4–8, 2022.^[Process Mining Hanbook.pdf:59-73]

The book is licensed under the Creative Commons Attribution 4.0 International License, making it freely available for use, sharing, and adaptation.^[Process Mining Hanbook.pdf:19-22]

## Background and Motivation

Process mining emerged as a discipline around the turn of the millennium, initially focused on discovering process models (e.g., Petri nets) from event traces. Over two decades, the field expanded to include conformance checking, performance analysis, multiple perspectives (time, resources, roles, costs), a wide range of process model notations (directly-follows graphs, Petri nets, declarative models, process trees, object-centric models, BPMN), and forward-looking techniques connecting process mining to simulation, machine learning, and automation.^[Process Mining Hanbook.pdf:38-50]

The IEEE Task Force on Process Mining, established in October 2009, drove key community outputs including the International Process Mining Conference (ICPM), the Process Mining Manifesto (translated into 15+ languages), the XES standard, and publicly available datasets. The handbook was conceived to fill the gap of a dedicated, comprehensive educational resource for the field.^[Process Mining Hanbook.pdf:62-69]

## Structure and Chapters

### Introduction
- **Process Mining: A 360 Degree Overview** (van der Aalst) — introduces basic concepts, types of process mining, process modeling notations, and event storage formats.

### Process Discovery
- **Foundations of Process Discovery** (van der Aalst) — covers directly-follows graphs, bottom-up and top-down discovery techniques producing Petri nets and BPMN models.
- **Advanced Process Discovery Techniques** (Augusto, Carmona, Verbeek) — state-based regions, language-based regions, split mining, and log skeleton-based approaches.
- **Declarative Process Specifications: Reasoning, Discovery, Monitoring** (Di Ciccio, Montali) — discovering and monitoring declarative specifications from event logs, and reasoning on declarative process models. See also [[sustainability-aware-process-mining]] for emerging extensions.

### Conformance Checking
- **Conformance Checking: Foundations, Milestones and Challenges** (Carmona, van Dongen, Weidlich) — framework for comparing modeled and observed behavior, applications, and open challenges.

### Data Preprocessing
- **Foundations of Process Event Data** (De Weerdt, Wynn) — event data structures, the data-preprocessing pipeline, the XES standard, and data quality problems.
- **A Practitioner's View on Process Mining Adoption, Event Log Engineering and Data Challenges** (Accorsi, Lebherz) — applied perspective on industry adoption, event log creation, best practices using the order-to-cash (O2C) process in SAP systems.

### Process Enhancement and Monitoring
- **Foundations of Process Enhancement** (de Leoni) — process extension and improvement, adding additional perspectives to process models.
- **Process Mining over Multiple Behavioral Dimensions with Event Knowledge Graphs** (Fahland) — constructing, querying, and aggregating event knowledge graphs for complex multi-entity processes. Related to [[object-centric-distance-metric]].
- **Predictive Process Monitoring** (Di Francescomarino, Ghidini) — techniques for predicting the future of ongoing process executions. See [[actor-enriched-throughput-time-forecasting]] for recent advances.

### Assorted Process Mining Topics
- **Streaming Process Mining** (Burattin) — techniques for processing streams of event data rather than fixed event logs.
- **Responsible Process Mining** (Mannhardt) — approaches for making process mining responsible by design using the FACT criteria: Fairness, Accuracy, Confidentiality, and Transparency.

### Industrial Perspective and Applications
- **Status and Future of Process Mining: From Process Discovery to Process Execution** (Reinkemeyer) — evolution of the field toward process execution management and business value.
- **Using Process Mining in Healthcare** (Martin, Wittig, Munoz-Gama) — overview of healthcare processes, healthcare process data, and common use cases. See also [[event-log-extraction-clinical-narratives]].
- **Process Mining for Financial Auditing** (Jans, Eulerich) — internal and external auditing applications of process mining.
- **Robotic Process Mining** (Dumas, La Rosa, Leno, Polyvyanyy, Maggi) — discovering repetitive routines for automation using robotic process automation (RPA) technology.

### Closing
- **Scaling Process Mining to Turn Insights into Actions** (van der Aalst, Carmona) — analysis of the current state of the discipline and outlook on future developments and challenges.

## Key Themes

1. **Breadth of process mining**: The handbook covers the full spectrum from foundational theory (process discovery, conformance checking) to applied domains (healthcare, financial auditing, RPA).
2. **Tool ecosystem**: By 2022, over 40 commercial process mining products existed alongside open-source tools such as ProM, PM4Py, and bupaR. The market was expected to double every 18 months.^[Process Mining Hanbook.pdf:51-58]
3. **Responsible and forward-looking process mining**: Increasing attention to fairness, confidentiality, transparency, and predictive/prescriptive capabilities.
4. **Object-centric and multi-entity perspectives**: Moving beyond single case-notion event logs to richer representations such as event knowledge graphs and object-centric models. See [[object-centric-distance-metric]] and [[veco-multimodal-process-mining-library]].
5. **Sustainability and societal impact**: Healthcare and auditing chapters highlight the societal value of process mining. See [[sustainability-aware-process-mining]] for environmental dimensions.

## Citation

van der Aalst, W. M. P., & Carmona, J. (Eds.). (2022). *Process Mining Handbook*. Lecture Notes in Business Information Processing, Vol. 448. Springer Nature. https://doi.org/10.1007/978-3-031-08848-3

## Chapter Structure and Contents

The handbook is organized into six thematic parts, as outlined in the preface by van der Aalst and Carmona:

- **Introduction**: Chapter 1 — *Process Mining: A 360 Degree Overview* (Wil M. P. van der Aalst) — introduces basic concepts, types of process mining, process modeling notations, and event data storage formats.
- **Process Discovery**: Chapter 2 — *Foundations of Process Discovery* (van der Aalst); Chapter 3 — *Advanced Process Discovery Techniques* (Adriano Augusto, Josep Carmona, Eric Verbeek); Chapter 4 — *Declarative Process Specifications: Reasoning, Discovery, Monitoring* (Claudio Di Ciccio, Marco Montali).
- **Conformance Checking**: Chapter 5 — *Conformance Checking: Foundations, Milestones and Challenges* (Josep Carmona, Boudewijn van Dongen, Matthias Weidlich).
- **Data Preprocessing**: Chapter 6 — *Foundations of Process Event Data* (Jochen De Weerdt, Moe Thandar Wynn); Chapter 7 — *A Practitioner's View on Process Mining Adoption, Event Log Engineering and Data Challenges* (Rafael Accorsi, Julian Lebherz).
- **Process Enhancement and Monitoring**: Chapter 8 — *Foundations of Process Enhancement* (Massimiliano de Leoni); Chapter 9 — *Process Mining over Multiple Behavioral Dimensions with Event Knowledge Graphs* (Dirk Fahland); Chapter 10 — *Predictive Process Monitoring* (Chiara Di Francescomarino, Chiara Ghidini).
- **Assorted Process Mining Topics**: Chapter 11 — *Streaming Process Mining* (Andrea Burattin); Chapter 12 — *Responsible Process Mining* (Felix Mannhardt).
- **Industrial Perspective and Applications**: Chapter 13 — *Status and Future of Process Mining: From Process Discovery to Process Execution* (Lars Reinkemeyer); Chapter 14 — *Using Process Mining in Healthcare* (Niels Martin, Nils Wittig, Jorge Munoz-Gama); Chapter 15 — *Process Mining for Financial Auditing* (Mieke Jans, Marc Eulerich); Chapter 16 — *Robotic Process Mining* (Marlon Dumas, Marcello La Rosa, Volodymyr Leno, Artem Polyvyanyy, Fabrizio Maria Maggi).
- **Closing**: Chapter 17 — *Scaling Process Mining to Turn Insights into Actions* (van der Aalst and Carmona).
^[handbook2.pdf:97-120]

## Chapter 1: Process Mining — A 360 Degree Overview

Chapter 1, authored by Wil M. P. van der Aalst, defines process mining as: *"process mining aims to improve operational processes through the systematic use of event data."* It positions process mining as the intersection of **data science** and **process science** (Fig. 1 in the chapter), drawing on disciplines including machine learning, statistics, operations research, workflow management, simulation, and business process management.

Key historical milestones noted include: process mining research beginning in the late 1990s; the first version of the open-source platform **ProM** released in 2004 with 29 plug-ins (now over 1,500); the first commercial tools appearing approximately 15 years before publication; and over 40 commercial tools in use at time of writing.^[handbook2.pdf:55-75]

### Process Model Notations

The chapter introduces several process model notations using a running "pizza process" example (activities: buy ingredients, create base, add tomato, add cheese, add salami, bake in oven, eat pizza, clean kitchen):

- **BPMN (Business Process Model and Notation)**: Uses parallel gateways (AND-split/AND-join) to express concurrency. The pizza process has 3! = 6 execution variants due to three concurrent topping activities.
- **Petri nets**: Places (circles) model states; transitions (squares) model activities; tokens flow through the net. The pizza process Petri net has 13 reachable markings.
- **Process trees**: A hierarchical representation using operators — **→** (sequence), **×** (exclusive choice), **∧** (parallel composition), and **↺** (redo loop). The pizza process is expressed as →(bi, cb, ∧(ac, at, as), bo, ep, ck). Used internally by several discovery algorithms.
- **Directly-Follows Graphs (DFGs)**: Show which activities directly follow each other. Commercial tools commonly use DFGs, but they tend to produce underfitting models by creating loops when activities occur in variable order, leading to "spaghetti-like" diagrams.
^[handbook2.pdf:55-67]

### The 360-Degree View of Process Mining

The chapter describes a high-level workflow (Fig. 2): event data are extracted from information systems (ERP, CRM, SCM systems such as SAP S/4HANA, Oracle E-Business Suite, Microsoft Dynamics 365, Salesforce CRM), then explored, filtered, and cleaned into an **event log**. Process discovery, conformance checking, and performance analysis are applied. Results feed into process improvement via simulation, operations research, and machine learning — ultimately triggering corrective actions.^[handbook2.pdf:55-67]

The chapter emphasizes that mainstream AI/ML (e.g., neural networks) cannot directly support process discovery or conformance checking; an explicit process model tightly connected to event data is required first. Process mining can then be used to *create* AI/ML problems (e.g., predicting remaining processing time, predicting compliance deviations, predicting ICU bed availability in healthcare).^[handbook2.pdf:55-67]
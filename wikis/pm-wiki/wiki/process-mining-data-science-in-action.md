---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:19:59'
lint_warnings:
- claim: Wil van der Aalst (Eindhoven University of Technology, Department of Mathematics
    and Computer Science)
  concern: By 2016 (the publication year of the second edition), Wil van der Aalst
    had moved to RWTH Aachen University. His affiliation with Eindhoven University
    of Technology (TU/e) was his earlier position; attributing TU/e as his affiliation
    for the 2016 second edition is likely incorrect.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Process Mining_ Data Science
    in Action ( PDFDrive ).pdf
  hash: f4728043c9640b642cba938b577657bf0b3b30440d7cb80d9b1a1e3992ff42e9
  ingested: '2026-07-14T07:19:59'
  size: 22442510
  truncated: true
status: active
tags:
- process mining
- data science
- event logs
- business processes
- ProM
- workflow
- BPM
- conformance checking
- process discovery
- Springer
title: 'Process Mining: Data Science in Action (Second Edition)'
type: technology
---

# Process Mining: Data Science in Action (Second Edition)

*Process Mining: Data Science in Action* (Second Edition) is a comprehensive textbook authored by **Wil van der Aalst** (Eindhoven University of Technology, Department of Mathematics and Computer Science), published by Springer-Verlag Berlin Heidelberg in 2016 (ISBN 978-3-662-49850-7, eBook ISBN 978-3-662-49851-4, DOI: 10.1007/978-3-662-49851-4). The first edition appeared in 2011 under the title *Process Mining: Discovery, Conformance and Enhancement of Business Processes*. The book is widely regarded as the definitive reference text for the field of [[process-mining-handbook|process mining]].^[Process Mining_ Data Science in Action ( PDFDrive ).pdf:11-17]

## Overview and Purpose

The book positions process mining as a bridge between traditional model-based process analysis (e.g., simulation and Business Process Management) and data-centric techniques such as machine learning and data mining. Its central thesis is that the omnipresence of event data, combined with process mining techniques, allows organizations to diagnose problems based on facts rather than assumptions. The subtitle "Data Science in Action" reflects the second edition's expanded framing of process mining as an integral component of data science.^[Process Mining_ Data Science in Action ( PDFDrive ).pdf:56-61]

The book is intended for practitioners, students, and academics, aiming to be both accessible to newcomers and rigorous enough to serve as a reference handbook for BPM and BI professionals.^[Process Mining_ Data Science in Action ( PDFDrive ).pdf:103-110]

## Key Additions in the Second Edition

Compared to the 2011 first edition, the second edition (2016) introduced several significant expansions:

- **Data Science context (Chapter 1):** Process mining is situated within the broader data science landscape, relating it to statistics, machine learning, Big Data, and predictive analytics.
- **Inductive Mining (Section 7.5):** Coverage of the family of inductive mining techniques, which handle large incomplete event logs with infrequent behavior while providing formal guarantees. The concept of *process trees* (Section 3.2.8) was also added.
- **Alignments (Section 8.3):** The conformance checking chapter was extended to introduce alignments as a key concept for relating observed behavior (event logs) to modeled behavior. Quality dimensions such as precision were formally defined alongside fitness.
- **Process Mining in the Large (Chapter 12):** A new chapter covering decomposition strategies (case-based and activity-based), process cubes, streaming process mining, and exploitation of modern distributed infrastructures.
- **Updated Tools chapter (Chapter 11):** Completely rewritten to cover commercial tools including Celonis Process Mining, Disco, Minit, myInvenio, Perceptive Process Mining, QPR ProcessAnalyzer, and others, alongside open-source platforms ProM and RapidProM.
- **Data Quality (Section 5.4):** A new section on conceptualizing event logs, classifying data quality issues, and guidelines for logging.^[Process Mining_ Data Science in Action ( PDFDrive ).pdf:111-120]

## Structure and Contents

The book is organized into six parts:

### Part I: Introduction
- **Chapter 1 – Data Science in Action:** Introduces the Internet of Events, the role of the data scientist, and the gap between process science and data science.
- **Chapter 2 – Process Mining: The Missing Link:** Covers limitations of pure modeling, the core concept of process mining, play-in/play-out/replay, and positioning process mining relative to BPM, data mining, Lean Six Sigma, BPR, Business Intelligence, CEP, GRC, and Big Data.

### Part II: Preliminaries
- **Chapter 3 – Process Modeling and Analysis:** Covers transition systems, Petri nets, workflow nets, YAWL, BPMN, EPCs, causal nets, and process trees. Includes model-based verification and performance analysis.
- **Chapter 4 – Data Mining:** Covers classification, regression, clustering, decision tree learning, k-means, association rule learning, sequence and episode mining, and model quality evaluation.

### Part III: From Event Logs to Process Models
- **Chapter 5 – Getting the Data:** Data sources, event log structure, the XES standard, data quality issues, and flattening reality into event logs.
- **Chapter 6 – Process Discovery: An Introduction:** Problem statement, the α-algorithm, rediscovering process models, representational bias, noise and incompleteness, and the four competing quality criteria (fitness, precision, generalization, simplicity).
- **Chapter 7 – Advanced Process Discovery Techniques:** Heuristic mining, genetic process mining, region-based mining, and inductive mining.

### Part IV: Beyond Process Discovery
- **Chapter 8 – [[conformance-checking-visualization-idioms|Conformance Checking]]:** Business alignment and auditing, token replay, alignments, footprint comparison, model repair, and evaluating discovery algorithms.
- **Chapter 9 – Mining Additional Perspectives:** Organizational mining (social network analysis, organizational structures, resource behavior), time and probabilities, and decision mining.
- **Chapter 10 – Operational Support:** The refined process mining framework (cartography, auditing, navigation), online process mining, detect/predict/recommend functions, concept drift, and the full process mining spectrum.

### Part V: Putting Process Mining to Work
- **Chapter 11 – Process Mining Software:** Taxonomy of tools, ProM as an open-source platform, commercial software landscape, strengths and weaknesses.
- **Chapter 12 – Process Mining in the Large:** Big event data, N=All principle, hardware/software developments, case-based and activity-based decomposition, process cubes, streaming process mining.
- **Chapter 13 – Analyzing "Lasagna Processes":** Structured, repetitive processes; use cases and a staged approach (plan, extract, create control-flow model, create integrated model, operational support); applications by functional area and sector.
- **Chapter 14 – Analyzing "Spaghetti Processes":** Highly variable, unstructured processes; approach and applications.

### Part VI: Reflection
- **Chapter 15 – Cartography and Navigation:** Business process maps, aggregation and abstraction, seamless zoom, and the analogy of process mining as a "TomTom for business processes".
- **Chapter 16 – Epilogue:** Process mining as a bridge between data mining and BPM, open challenges, and a call to action.

## Historical and Intellectual Context

Van der Aalst traces the intellectual roots of process mining to:
- **Anil Nerode (1958):** Synthesis of finite-state machines from example traces.
- **Carl Adam Petri (1962):** Introduction of Petri nets as the first modeling language adequately capturing concurrency.
- **Mark Gold (1967):** Systematic exploration of learnability.

The modern discipline of process mining is dated to a 1999 research project at TU/e titled "Process Design by Discovery: Harvesting Workflow Knowledge from Ad-hoc Executions," initiated by Van der Aalst and Ton Weijters (then called *workflow mining*). The first survey on process mining appeared in 2003.^[Process Mining_ Data Science in Action ( PDFDrive ).pdf:89-102]

## ProM and the Open-Source Ecosystem

The book is closely tied to the development of **ProM**, the leading open-source process mining platform. Key contributors acknowledged include Boudewijn van Dongen, Eric Verbeek, Christian Günther (Fuzzy Miner), Anne Rozinat (conformance checking, multi-perspective mining), Sander Leemans (inductive mining), and Peter van den Brand (ProM 6 architecture). Commercial spin-offs from the ProM ecosystem include Fluxicon (Disco) and Futura Process Intelligence (later acquired by Lexmark's Perceptive Software).^[Process Mining_ Data Science in Action ( PDFDrive ).pdf:38-42]

## Relationship to Other Works

This textbook is distinct from the later [[process-mining-handbook|Process Mining Handbook (LNBIP 448, 2022)]], which is an edited multi-author volume associated with the first IEEE Task Force Summer School on Process Mining. The 2016 book by Van der Aalst remains the primary single-author comprehensive treatment of the field and is a foundational reference for topics including [[data-quality-sensitivity-process-discovery|data quality in process mining]], [[conformance-checking-visualization-idioms|conformance checking]], [[actor-enriched-throughput-time-forecasting|predictive process monitoring]], and [[sustainability-aware-process-mining|sustainability-aware process mining]].
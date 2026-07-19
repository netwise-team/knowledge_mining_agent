---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:24:22'
lint_warnings:
- claim: This study is the first empirical investigation of those challenges.
  concern: This is a strong claim of novelty that is difficult to verify and likely
    overstated. Prior work on process mining education and its challenges exists in
    the literature, and claiming to be definitively 'the first empirical investigation'
    without exhaustive evidence is a common form of overstatement in academic writing
    that a skeptical editor should flag.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Tentina et al - Challenges
    in Teaching Process Mining Insights from Process Mining Educators.pdf
  hash: f0c540a87b176435c372a3651101a1b7357dd686abb3b2754f2364666a06657d
  ingested: '2026-07-14T07:24:22'
  size: 395636
  truncated: true
status: active
tags:
- process mining
- education
- teaching challenges
- focus groups
- event logs
- competencies
- academia
- industry training
- interdisciplinary
- business processes
title: Challenges in Teaching Process Mining
type: concept
---

# Challenges in Teaching Process Mining

This page summarizes the findings of an empirical study investigating the key challenges faced by process mining educators in both academic and industrial settings. The work was conducted by Irina Tentina and Boudewijn F. van Dongen (Eindhoven University of Technology) and Iris Beerepoot, Xixi Lu, Hajo A. Reijers, and Vinicius Stein Dani (Utrecht University), and was accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

[[process-mining-handbook|Process mining]] has gained traction in both academia and industry, enabling organizations to discover, monitor, and improve their work processes using event logs. As adoption grows, so does the demand for skilled professionals. However, developing process mining expertise is non-trivial, requiring a broad set of competencies spanning technical, analytical, and business-oriented skills. Despite the growing availability of educational offerings — university courses, vendor certifications (e.g., Celonis Academy, Fluxicon Camp), self-paced online courses, and internal company training — little was known about the specific challenges educators face. This study is the first empirical investigation of those challenges.^[Tentina et al - Challenges in Teaching Process Mining Insights from Process Mining Educators.pdf:9-58]

## Research Method

The study used **focus groups** as the primary data collection method, enabling observation of how perspectives from academia and industry align or diverge. Three focus groups were conducted online (via MS Teams), each lasting approximately 90 minutes, followed by a 45-minute validation session. In total, 13 participants took part: 8 from industry (consultants, process intelligence specialists, a director of process mining success) and 5 from academia (PhD candidates, assistant and associate professors). All participants conducted teaching activities mainly in Europe and had between 1 and 20 years of process mining experience.^[Tentina et al - Challenges in Teaching Process Mining Insights from Process Mining Educators.pdf:49-58]

Data analysis used qualitative thematic coding with iterative "in-vivo" coding by two researchers, resolving divergences through collaborative discussion. Saturation was confirmed after the third focus group, with 92 individual challenges aggregated into nine high-level themes.

## Nine Challenges in Teaching Process Mining

The challenges are organized into three categories of teaching tasks:

### Identifying Learners' Needs

**C1: Navigating divergent interpretations of process mining.**
Educators and learners conceptualize process mining differently — as a tool, a set of techniques, or a methodological framework. Industry participants tend toward a tooling-oriented perspective, while academics emphasize methodological foundations. An overly tool-centric approach may limit learners' deeper understanding and ability to apply process mining to novel, unstructured problems.

**C2: Aligning goals with diverse learner profiles.**
Learners come from varied backgrounds (computer science, business, data engineering, compliance management), each with distinct strengths and knowledge gaps. Computer science students may excel at data manipulation but lack business process understanding, while business students may have the reverse profile. In industry, technical and business-oriented learners have differing expectations, making it difficult to design courses that are simultaneously relevant, engaging, and appropriately challenging for all.^[Tentina et al - Challenges in Teaching Process Mining Insights from Process Mining Educators.pdf:29-44]

### Design and Development of Course Materials

**C3: Finding or generating suitable data and event logs.**
Sourcing realistic training data — including meaningful data quality issues — requires substantial effort. In academia, curated event logs are common; in industry, raw data distributed across multiple relational tables must be transformed into event log format, making realistic simulation even more demanding. This challenge is directly related to [[data-quality-sensitivity-process-discovery|data quality issues in process mining]].

**C4: Lacking reusable teaching materials.**
There is a limited availability of reusable resources including practical exercises, guided examples, case studies, and interactive sandbox environments. Learners need environments where they can experiment with filters, event log modifications, and algorithm choices, and immediately observe consequences — including the effects of mistakes.

**C5: Selecting an appropriate process mining tool.**
A wide range of tools exists (ProM, Disco, Apromore, Celonis, PM4Py, among others), each differing in features, usability, learning curve, and transparency of algorithms. Commercial platforms are increasingly preferred in industry but can overwhelm novice learners and obscure algorithmic details, often requiring supplementation with open-source tools for methodological grounding.^[Tentina et al - Challenges in Teaching Process Mining Insights from Process Mining Educators.pdf:84-100]

### Implementation and Evaluation of Courses

**C6: Balancing applicability and complexity.**
Oversimplification prioritizes ease of understanding but leaves learners unprepared for real-world complexity. Conversely, excessive technical depth increases cognitive load and risks disengaging learners, particularly in industry settings where course length is constrained.

**C7: Teaching the temporal aspect of the data.**
Conveying the importance of timestamps and temporal dynamics — critical for data preprocessing, event log quality assessment, and performance analysis — remains difficult. Misunderstandings lead to incorrect interpretations of process behavior. This is especially acute for advanced topics such as predictive process mining, where learners must reason about how time influences process outcomes.

**C8: Lacking potential value and use case examples.**
Students often lack familiarity with the types of questions practitioners pose and how process mining addresses concrete business problems. Commercial tools with integrated dashboards, process connectors, and predictive capabilities support a broader range of use cases than what is typically demonstrated in academic settings.

**C9: Validating process mining results.**
Validation goes beyond technical metrics such as fitness or precision; it requires interpretive effort considering organizational context, stakeholder feedback, and data limitations. Small changes in event log construction — case identifier selection, activity granularity, timestamp resolution — can significantly affect analysis results. Corporate training programs rarely have the flexibility for iterative validation cycles.^[Tentina et al - Challenges in Teaching Process Mining Insights from Process Mining Educators.pdf:25-44]

## Future Research Directions

**RD1: Develop process mining-oriented educational tools and environments.**
Future work should focus on sandbox environments or interactive tools that visualize the effects of incorrect assumptions, improper configurations, and algorithmic choices, supporting both theoretical and practical learning (addressing C3–C5, C7, C9).

**RD2: Develop adaptive and modular curriculum models for diverse learner profiles.**
Research should explore the skills required for teaching and learning [[process-mining-handbook|process mining]] and develop modular course structures with role-specific learning tracks bridging technical and organizational perspectives (addressing C1–C2).

**RD3: Bridge process mining education and real-world practice.**
Strategies are needed for integrating real-life complexity into educational settings through industry-sourced event logs and practice-driven case studies reflecting the full lifecycle of process mining projects, including data preparation and stakeholder communication (addressing C6, C8).^[Tentina et al - Challenges in Teaching Process Mining Insights from Process Mining Educators.pdf:49-58]

## Relation to Existing Resources

The [[process-mining-handbook|Process Mining Handbook]] and [[process-mining-data-science-in-action|Process Mining: Data Science in Action]] are among the primary reference texts used in academic process mining courses. The challenges identified in this study — particularly around data availability (C3), tool selection (C5), and validation (C9) — reflect broader issues also discussed in [[data-quality-sensitivity-process-discovery|data quality sensitivity research]] and [[ocpm-from-time-series-sensor-data|event log construction from raw data]].
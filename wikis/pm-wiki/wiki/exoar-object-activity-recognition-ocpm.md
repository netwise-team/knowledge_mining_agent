---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:59:53'
lint_warnings:
- claim: It was developed by Iris Beerepoot, Vinicius Stein Dani, and Xixi Lu at Utrecht
    University, and was accepted at the ICPM 2025 Workshops (Springer LNBIP series).
  concern: ICPM 2025 has not yet occurred at the time of established knowledge, making
    it impossible to verify acceptance. This claim about a future conference acceptance
    cannot be confirmed and may be speculative or premature.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Beerepoot et al - ExOAR Expert-Guided
    Object and Activity Recognition from Textual Data.pdf
  hash: 07122f9ee7df76a1ee9aac4982e42246d037d921a08d0c3b5ed2ace5f0d8114d
  ingested: '2026-07-14T07:59:53'
  size: 428039
  truncated: true
status: active
tags:
- process mining
- LLM
- expert-in-the-loop
- activity recognition
- object recognition
- unstructured text
- structured data
- human oversight
- textual data extraction
- workflow analysis
title: 'ExOAR: Expert-Guided Object and Activity Recognition for Object-Centric Process
  Mining'
type: technology
---

# ExOAR: Expert-Guided Object and Activity Recognition for Object-Centric Process Mining

ExOAR (Expert-Guided Object and Activity Recognition) is an interactive method and tool that combines [[llm-declarative-process-discovery-dcr-graphs|large language models (LLMs)]] with human expert validation to extract structured object-centric event data from unstructured textual sources. It was developed by Iris Beerepoot, Vinicius Stein Dani, and Xixi Lu at Utrecht University, and was accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

Object-centric process mining (OCPM) requires structured event logs — specifically Object-Centric Event Logs (OCELs) — in which events are explicitly linked to multiple object types and instances. However, many real-world data sources are unstructured or semi-structured text: physician notes, helpdesk tickets, maintenance logs, window tracking logs, and file names. Extracting meaningful object types, object instances, and activities from such sources is challenging because:

- Fully automated extraction methods fail due to domain-specific ambiguity and terminology.
- Fully manual labeling is too labor-intensive to scale.
- LLMs can suggest meaningful labels but produce inconsistent or overgeneralized outputs without domain context or oversight.

ExOAR addresses this gap through a human-in-the-loop design that interleaves LLM-generated suggestions with concise expert validation at each stage.^[6-20]

## Background: Object-Centric Process Mining

Unlike traditional [[process-mining-data-science-in-action|process mining]] based on XES event logs with a single case notion, OCPM allows events to be associated with multiple object types simultaneously, capturing the relational complexity of real-world processes. A prerequisite is a well-formed OCEL, which is difficult to derive from unstructured text because object types, their instances, and their relationships may all be unknown a priori. This is more demanding than conventional case recognition (which assumes a known case notion) and introduces challenges such as ambiguous object references, domain-specific terminology, and implicit relationships.^[67-111]

## The ExOAR Approach

ExOAR decomposes object and activity recognition into four iterative, modular steps, each involving an LLM prompt followed by user review and refinement:

### Step 1: Object Type Recognition
The user provides contextual input (e.g., their profession). The LLM generates a list of candidate object type categories (e.g., "courses", "research projects", "colleagues"). The user reviews, adds, or removes types before proceeding.

### Step 2: Activity Recognition
Using the verified object types and profession context, the LLM generates candidate activity labels semantically linked to those types (e.g., "supervise students", "manage research projects"). The user curates this list.

### Step 3: Object Recognition
The LLM is provided with the verified object types, activities, and a sample of raw textual data (e.g., frequent window titles). It identifies concrete object instances and assigns them to object types. The user reviews, edits labels, corrects type assignments, and removes duplicates or irrelevant entries.

### Step 4: Event Enrichment
The LLM associates each textual event (e.g., a window title) with specific verified objects and activities, producing event-object-activity tuples. A sample is presented to the user for final validation. Ambiguous events may be left unannotated. The result is a semantically grounded, human-verified dataset suitable for object-centric process analysis.

The approach prioritizes: (1) minimizing user effort, (2) economical use of LLM queries, and (3) modularity across data types and domains.^[50-61]

## Implementation and Demonstration

ExOAR was implemented as a Streamlit web application using OpenAI's GPT-4.1 model (chosen for its balance of cost, reasoning, and instruction-following). The tool was demonstrated using Active Window Tracking (AWT) data — logs of window titles, document names, and application metadata — from one of the authors over the full month of April 2025.

In the demonstration walkthrough:
- **Step 1** generated 13 candidate object types; the user added "conferences" and removed 3 irrelevant types, yielding a verified set.
- **Step 2** generated 20 candidate activities; all were retained and 4 more were added (e.g., "attend department meetings", "analyze research data"), totaling 24.
- **Step 3** generated 58 candidate object instances from the 500 most frequent window titles; after editing and removing duplicates, 39 objects were confirmed across 10 types (colleagues, students, courses, publications, conferences, research projects, etc.).
- **Step 4** enriched 100 frequent window titles; a sample of 10 was reviewed, with all correctly labeled, though activities were refined in several cases.

The full walkthrough cost approximately $0.08 in OpenAI API credits.^[14-20]

## Evaluation

A preliminary evaluation was conducted with four additional users: two academic staff members and two professionals (a bookkeeper and a self-employed business advisor), each using their own AWT data collected over at least one month.^[59-61]

Key findings (summarized across participants):

| Step | Observation |
|---|---|
| Object Types | High acceptance rate (93–100% kept as-is); minimal additions or removals |
| Activities | Very high acceptance (90–100% kept as-is); small additions by academics |
| Objects | More variability; 67–96% kept as-is; significant removals of duplicates/irrelevant entries |
| Event Enrichment | 30–80% kept as-is; most edits involved removing over-assigned activities |

A recurring issue was LLM over-generation of activities per event (e.g., listing "attend", "present at", and "organize conferences" for a single conference-related window title). Users typically retained only the most fitting activity. The authors note that erring toward overgeneration may be preferable, since it is easier to discard irrelevant suggestions than to conceive of missing ones.

Users also found it challenging to identify all relevant object types a priori, suggesting that future versions should offer a more diverse initial set of candidate types to reduce false negatives in downstream steps.^[15-20]

## Relation to Other Work

ExOAR extends prior work on LLM-based semantic recognition in several ways:
- Unlike single-case activity recognition approaches (e.g., for RPA or IoT logs), ExOAR handles multiple unknown object types simultaneously.
- Unlike the two-step LLM pipeline by Buss et al. (collector + refiner), ExOAR delineates multiple interpretation stages within extraction and evaluates on real-world rather than synthetic data.
- It complements [[wearable-data-event-log-enrichment|wearable data enrichment]] and other [[process-mining-workflow-documentation|process mining workflow]] efforts by the same Utrecht University group, all aimed at enriching event logs with richer contextual semantics.
- It shares the human-in-the-loop philosophy with [[teaching-process-mining-challenges|process mining education research]] from the same group, emphasizing the importance of domain expertise alongside automation.

## Limitations and Future Work

- The evaluation is preliminary (five users total) and focused on AWT data from a single data source type.
- Adding a new object type in Step 1 after Step 3 has begun requires re-running subsequent steps, which is costly.
- Prompt strategies for activity assignment need refinement to reduce over-generation.
- Future work will scale evaluations, improve object type suggestion diversity, and explore applications in healthcare, education, and legal services.^[15-20]
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T21:06:58'
lint_warnings:
- claim: PM is a methodology for uncovering patient circuits and treatment trajectories,
    enabling healthcare providers to better understand complex processes based on
    real-world data
  concern: Process Mining (PM) is a general methodology for analyzing business and
    organizational processes from event logs, not specifically designed for patient
    circuits and treatment trajectories. Describing it solely in healthcare terms
    overstates its scope and misrepresents its broader, domain-agnostic nature.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Gómez-Noé et al - Extraction
    and Identification of Medications from EHR Notes with LLMs - A Tool and a Case
    Study.pdf
  hash: 59c0007b17c936f3416845ead74d79b4ef2d2559bac36b5c33e56148838c19fa
  ingested: '2026-07-14T21:06:58'
  size: 450809
status: active
tags:
- medication extraction
- EHR
- LLM
- process mining
- NLP
- SNOMED-CT
- COPD
- Spanish-language dataset
- clinical NLP
- healthcare AI
title: GóMez Noé Et Al   Extraction And Identification Of Medications From Ehr Notes
  With Llms   A Tool And A Case Study
type: technology
---

# GóMez Noé Et Al   Extraction And Identification Of Medications From Ehr Notes With Llms   A Tool And A Case Study

Extraction and Identification of Medications from
EHR Notes with LLMs: A Tool and a Case Study
Alejandro Gómez-Noé1[0000−0002−9795−4358], Begoña
Martínez-Salvador2[0000−0001−5959−9415], Carlos
Fernández-Llatas1[0000−0002−2819−5597], and Mar Marcos2[0000−0001−9672−4190]
1 SABIEN-ITACA, Universitat Politècnica de València, Camino de Vera, S/N, 46022
Valencia, Spain{algono,cfllatas}@itaca.upv.es
2 Department of Computer Engineering and Science, Universitat Jaume I, Av. Vicent
Sos Baynat, s/n, 12071 Castellón, Spain{begona.martinez,mar.marcos}@uji.es
Abstract. Extracting medication data from Electronic Health Record
(EHR) notes plays a critical role in enhancing healthcare Process Min-
ing (PM) by enabling detailed analysis of patient treatment trajectories,
medication adherence, and clinical decision-making. However, accurate
extraction of information in general, and medication in particular, from
unstructured clinical texts remains challenging, particularly when work-
ing with non-English datasets and limited Natural Language Process-
ing (NLP) resources. To address these challenges and streamline the
process, accessible and efficient methods are needed to enable faster in-
house extraction of medication information while complying with privacy
regulations. In this paper, we present a case study involving patients
with Chronic Obstructive Pulmonary Disease (COPD) from a Spanish-
language EHR dataset. We explore the use of a prompt-based approach
leveraging an off-the-shelf Large Language Model (LLM) to extract med-
ication names from free-text EHR notes. We also present a tool that
enables interactive identification and validation of extracted medication
based on SNOMED-CT terminology. The extracted data was successfully
integrated into a PM model, demonstrating the practical feasibility and
utility of this method for improving the agility and depth of healthcare
data analysis workflows.
Keywords: LLMs · Medication Extraction · Electronic Health Records
· Process Mining
1 Introduction
Electronic Health Records (EHRs) are frequently recorded as unstructured, free-
text documents, making them both a rich source of clinical information and a
significant challenge for automated analysis. Extracting structured data—such
as medication mentions, diagnoses, or treatment actions—is critical for enabling
advanced applications in healthcare, including clinical decision-making, patient
monitoring, and Process Mining (PM). PM is a methodology for uncovering pa-
tient circuits and treatment trajectories, enabling healthcare providers to better
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
2 A. Gómez-Noé et al.
understand complex processes based on real-world data, identify non-standard
patients by analyzing infrequent behavior, and ultimately evolve clinical proto-
cols iteratively using these results [1]. However, the unstructured nature of EHRs
often creates barriers to integrating such data into PM workflows [3].
Existing Natural Language Processing (NLP) techniques have been explored
to extract structured information from clinical text [5], with many studies using
rule-based systems, machine learning models, and fine-tuned neural networks
[6], as well as the creation of specific NLP tooling [4]. While these methods
are powerful, they often require extensive manual annotation, domain-specific
expertise, and annotated datasets, making them inaccessible to many healthcare
IT teams. These barriers highlight the need for accessible, in-house solutions
that comply with data protection standards while enabling efficient information
extraction.
Recent advancements in large language models (LLMs), such as GPT-based
architectures, offer a promising alternative. LLMs have demonstrated strong per-
formance across a wide range of NLP tasks, including medical information ex-
traction, without requirin
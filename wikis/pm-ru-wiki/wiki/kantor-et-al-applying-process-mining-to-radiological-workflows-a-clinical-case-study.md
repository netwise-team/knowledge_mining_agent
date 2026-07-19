---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T19:41:55'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Kantor et al - Applying
    Process Mining to Radiological Workflows A Clinical Case Study.pdf
  hash: 1ee62c2020b1da47a8af9173a5918813d87c7f95d2f0cfdb4d7c8c8a17ce0368
  ingested: '2026-07-14T19:41:55'
  size: 689792
status: active
tags:
- process mining
- healthcare
- radiology
- clinical workflows
- compliance monitoring
- bottleneck analysis
- interoperability
- data-driven analysis
- hospital operations
- workflow optimization
title: Kantor Et Al   Applying Process Mining To Radiological Workflows A Clinical
  Case Study
type: technology
---

# Kantor Et Al   Applying Process Mining To Radiological Workflows A Clinical Case Study

Applying Process Mining to Radiological
Workflows: A Clinical Case Study
Jonathan Kantor1, Andrea Delgado 1 , and Daniel Calegari 2
1 Instituto de Computaci´ on, Facultad de Ingenier ´ ıa,Universidad de la Rep´ ublica
jthkantor@gmail.com, adelgado@fing.edu.uy
2 Universidad ORT Uruguay
calegari@ort.edu.uy
Abstract. Process mining has gained prominence in healthcare because
it provides data-driven methods for assessing and improving compliance
with established procedures. Nevertheless, the domain also presents dis-
tinctive characteristics and exposes several open challenges. This study
applies process mining to radiological workflows in a large university
hospital, with two complementary goals. First, to identify improvement
opportunities. We identified critical bottlenecks and significant temporal
deviations, and also demonstrated low compliance with the standard ref-
erence process. Second, the project served as an empirical validation of
how distinguishing characteristics and challenges manifest in this context
and how they provide guidance for future work. The findings demonstrate
the capability of process mining to uncover such actionable insights and
to drive evidence-based optimization of both operational and clinical
quality in hospital radiology services.^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:8-21]
Keywords: process mining, healthcare, radiological workflows, challenges
1 Introduction
In recent years, the healthcare sector has increasingly embraced technological in-
novations to address growing challenges related to resource efficiency and service
quality. For example, the Integrating the Healthcare Enterprise (IHE) initiative3
is a collaborative effort among healthcare professionals and industry stakehold-
ers aimed at enhancing interoperability among healthcare information systems.
IHE promotes the coordinated use of established standards such as DICOM
[11] and HL7 [6] version 2.x for order and result management to meet specific
clinical needs and support optimal patient care. The IHE initiative states that
systems developed in accordance with its guidelines demonstrate improved inter-
operability, are easier to implement, and enable healthcare providers to leverage
information more effectively, thereby helping to reduce operational costs and
ensure high-quality care [9].^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:24-35]
There is a growing interest in applying Process Mining [1] in the healthcare
domain [10,13], known as Process Mining for Healthcare (PM4H). It enables
3 https://www.ihe.net/
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
2 J. Kantor et at.
data-driven analysis of clinical workflows and support compliance monitoring
with established procedures. Radiology is one area where process mining ap-
plications are beginning to gain traction [7,5]. Within this context, the IHE
initiative proposes the Scheduled Workflow (SWF) framework [9], which de-
fines an integrated process for the ordering, scheduling, acquisition, storage, and
visualization of radiological images. The core goal of the SWF profile is to signif-
icantly improve the efficiency and outcomes of radiological procedures, thereby
enhancing the quality of care [9]. Process mining can play a key role in assessing
and improving compliance with this framework, facilitating the identification of
bottlenecks, inefficiencies, and deviations in clinical execution.^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:36-50]
However, the successful application of process mining for healthcare (PM4H)
requires addressing domain-specific challenges [10]. In this paper, we investigate
the application of process mining to radiological workflows within the context
of Hospital de Cl ´ ınicas, a public university hospital complex in Uruguay that
serves as a national reference. This case study is based on the analysis of event
data extracted from the Health Information System (HIS), which is designed to
interoperate with radiological devices using DICOM for image tra^[Kantor et al - Applying Process Mining to Radiological Workflows A Clinical Case Study.pdf:51-63]
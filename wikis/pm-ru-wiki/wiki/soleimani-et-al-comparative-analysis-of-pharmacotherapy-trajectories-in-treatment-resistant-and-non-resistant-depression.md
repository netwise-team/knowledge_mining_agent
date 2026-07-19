---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:22:25'
lint_warnings:
- claim: TRD, affecting 20–30% of patients, is typically defined as inadequate response
    to at least two antidepressant trials
  concern: The 20–30% figure conflates two different statistics. While roughly 20–30%
    of MDD patients may experience TRD depending on the definition used, this prevalence
    estimate is debated and some well-established sources (e.g., Rush et al., STAR*D)
    suggest closer to 10–30% with significant variability. More importantly, bundling
    the prevalence claim with the definition in one sentence risks implying a precision
    that is not well-established in the literature.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Soleimani et al - Comparative
    Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant
    Depression.pdf
  hash: dc4685a53c0778a4a6bc1042f559fbae628c3748b698e95787200a1b4addaa9c
  ingested: '2026-07-14T20:22:25'
  size: 1234699
  truncated: true
status: active
tags:
- psychiatry
- pharmacotherapy
- process mining
- depression
- clinical data analysis
- treatment trajectories
- EHR
- comparative analysis
- mental health
- ICPM 2025
title: Soleimani Et Al   Comparative Analysis Of Pharmacotherapy Trajectories In Treatment
  Resistant And Non Resistant Depression
type: concept
---

# Soleimani Et Al   Comparative Analysis Of Pharmacotherapy Trajectories In Treatment Resistant And Non Resistant Depression

Comparative Analysis of Pharmacotherapy
Trajectories in Treatment-Resistant and
Non-Resistant Depression
A Case Study
Zeinab Soleimani1, Alexander Charney2, Isotta Landi2, and Mathias Weske1
1 Hasso Plattner Institute for Digital Engineering, University of Potsdam, Potsdam,
Germany
{Zeinab.Soleimani, Mathias.Weske}@hpi.de
2 Icahn School of Medicine at Mount Sinai, NYC, U.S.A.
{Alexander.Charney, Isotta.Landi2}@mssm.edu
Abstract.Treatment-resistantdepression(TRD),definedasinadequate
response to at least two adequate trials of antidepressants, poses major
challenges in managing major depressive disorder (MDD). We applied
process mining to electronic health records of 31,881 patients (4,630
TRD, 27,251 non-TRD) with 415,641 antidepressant exposures. TRD
patients showed extreme heterogeneity, with nearly a one-to-one ratio
of trace variants to cases. They also underwent frequent switches across
antidepressant categories, whereas 74% of non-TRD patients completed
treatment within a single category. Median treatment duration was 1473
days in TRD versus 112 days in non-TRD. These results establish a re-
producible baseline for applying process mining in psychiatric pharma-
cotherapy and highlight the need for advanced comparative techniques
and multi-site validation. ^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:11-23]
Keywords:Major Depressive Disorder·Process Mining·Treatment-
Resistant Depression·Care Pathways
1 Introduction
Major depressive disorder (MDD) is a leading cause of disability worldwide, af-
fecting over 280 million people, and is often complicated by treatment failures,
including treatment-resistant depression (TRD) [10]. TRD, affecting 20–30% of
patients, is typically defined as inadequate response to at least two antidepres-
sant trials [19]. It is marked by poor response to standard therapies and highly
heterogeneous treatment pathways. While observational studies have highlighted
the burden of TRD, the detailed, real-world treatment trajectories of these pa-
tients remain poorly understood [7]. ^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:27-34]
Process mining is a promising approach for uncovering care pathways from
large electronic health record (EHR) datasets [14]. Although established in struc-
tured domains, its application in psychiatry is still emerging due to incomplete
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
2 Z. Soleimani et al.
data and unclear definitions [17]. As a result, the structure of individualized
treatment patterns in real-world psychiatric care is not well characterized. ^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:35-41]
To address this gap, we apply process mining to large-scale EHR data to com-
pare antidepressant treatment trajectories in patients with and without TRD.
The contributions of this paper are as follows:
–A reproducible analytic pipeline for process mining in psychiatric pharma-
cotherapy.
–Basic comparative analysis of TRD vs. non-TRD pathways, quantifying het-
erogeneity and timing.
–Discussion of methodological challenges and future directions for psychiatric
process mining.
Our research question is: How do antidepressant treatment pathways differ be-
tween TRD and non-TRD patients in real-world EHR data, in terms of structure
and timing? All analytic code and process models utilized to answer this question
are openly available (see Supplementary Materials 6). ^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:42-54]
2 Related Work
Several strands of research underpin this study, spanning observational analy-
ses of treatment-resistant depression (TRD), methodological developments in
healthcare process mining, and recent efforts to reconstruct psychiatric care
pathways from real-world data.
Howes et al. [10] reviewed definitions, prevalence, and challenges in treatment
resistance, while Ruhe et al. [19] examined staging methods and difficulties in
operationalizing TRD. Chan et al. [5] quantified excess mortality and healthcare
resource utilization in TRD, showing higher premature death risk and costs. ^[Soleimani et al - Comparative Analysis of Pharmacotherapy Trajectories in Treatment-Resistant and Non-Resistant Depression.pdf:60-63]
Process mining is widely a
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:39:26'
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Reiter et al - ContinuumConductor
    Decentralized Process Mining on the Edge-Cloud Continuum.pdf
  hash: 4b9f6d838d5eab1776e21662095f79c6c812288e7ab75f18b1072d23e75d4dcc
  ingested: '2026-07-14T20:39:26'
  size: 587318
  truncated: true
status: active
tags:
- process mining
- decentralization
- edge computing
- IoT
- privacy-preserving
- distributed computing
- event data
- resource efficiency
- edge-cloud continuum
- decision framework
title: Reiter Et Al   Continuumconductor Decentralized Process Mining On The Edge
  Cloud Continuum
type: technology
---

# Reiter Et Al   Continuumconductor Decentralized Process Mining On The Edge Cloud Continuum

ContinuumConductor : Decentralized Process
Mining on the Edge-Cloud Continuum
Hendrik Reiter1 , Janick Edinger2 , Martin Kabierski3 , Agnes Koschmider4
, Olaf Landsiedel1,5 , Arvid Lepsien1 , Xixi Lu6 , Andrea Marrella7 ,
Estefania Serral8 , Stefan Schulte5 , Florian Tschorsch9 , Matthias
Weidlich10 , and Wilhelm Hasselbring1
1 Kiel University, Kiel, Germany
{hendrik.reiter,hasselbring}@email.uni-kiel.de
2 University of Hamburg, Hamburg, Germany
3 University of Vienna, Vienna, Austria
4 University of Bayreuth, Bayreuth, Germany
5 Hamburg University of Technology, Hamburg, Germany
6 Utrecht University, Utrecht, Netherlands
7 Sapienza University of Rome, Rome, Italy
8 KU Leuven, Leuven, Belgium
9 Dresden University of Technology, Dresden, Germany
10 Humboldt University of Berlin, Berlin, Germany
Abstract. Process mining traditionally assumes centralized event data
collection and analysis. However, modern Industrial Internet of Things
(IIoT) systems increasingly operate over distributed, resource-constrained
edge-cloud infrastructures. This paper proposes a structured approach
for decentralizing process mining by enabling event data to be mined
directly within the IoT system's edge-cloud continuum. We introduce
ContinuumConductor a layered decision framework that guides when
to perform process mining tasks such as preprocessing, correlation, and
discovery centrally or decentrally. Thus, enabling privacy-preserving,
responsive and resource-efficient process mining. For each step in the
process mining pipeline, we analyze the trade-offs of decentralization
versus centralization across these layers and propose decision criteria. We
demonstrate ContinuumConductor at a real-world use-case of process
optimazition in inland ports. Our contributions lay the foundation for
computing-aware process mining in cyber-physical and IIoT systems.
Keywords: Process Mining · Distibuted Computing · IoT · Edge-Cloud
Continuum. ^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:18-34]

# 1 Introduction
TheproliferationofsensorsandactuatorsformsthebackboneofmodernIndustrial
Internet of Things (IIoT) environments. These systems leverage vast amounts
of sensor data to monitor processes, while actuators perform actions often in
direct response to the insights derived from this data. This complex interaction
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
2 H. Reiter et al.
requires the design of robust and efficient computing architectures that can meet
three critical objectives: firstly, responsive analysis ensuring that data analysis is
performed in real-time to allow timely actions; secondly, privacy-preservation,
particularly important in scenarios involving human interaction where sensitive
behavioral data, such as that captured by cameras, must be handled with care
and third resource-efficiency, since transferring and processing large data volume
may exceed the devices capacities. ^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:36-48]

The edge-cloud continuum [28] offers a promising solution to achieve real-time
responsiveness, enhanced privacy protection and resource-efficiency. By distribut-
ing computational tasks closer to the data source (edge) while leveraging the
scalability of centralized cloud resources, these architectures can mitigate latency,
reduce the exposure of sensitive information and minimize transferred data. In
this setting, process mining stands out as a powerful technique. Traditionally
applied to centralized event logs for retrospective business insights, process mining
in the dynamic, data-rich IIoT context requires a full pipeline, from preprocessing
raw sensor data to visualizing processes and extracting actionable insights. ^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:49-57]

This paper delves into the benefits and challenges of transforming the conven-
tional process mining pipeline into a distributed paradigm across the edge-cloud
continuum. Specifically, this paper contributes by:
1. Presenting a real-world use case that highlights the ^[Reiter et al - ContinuumConductor Decentralized Process Mining on the Edge-Cloud Continuum.pdf:58-67]
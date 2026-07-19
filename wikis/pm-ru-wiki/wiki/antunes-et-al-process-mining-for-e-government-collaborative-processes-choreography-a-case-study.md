---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:28:36'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Antunes et al - Process
    Mining for e-Government collaborative processes choreography a case study.pdf
  hash: f4f929f989507ffc222ceaa753f89d4274ab8530ba200b9864efcc29186eee3f
  ingested: '2026-07-14T20:28:36'
  size: 525930
  truncated: true
status: active
tags:
- process mining
- e-government
- choreography
- BPMN 2.0
- collaborative processes
- interoperability
- public sector
- Uruguay
- event log
- process discovery
title: Antunes Et Al   Process Mining For E Government Collaborative Processes Choreography
  A Case Study
type: technology
---

# Antunes Et Al   Process Mining For E Government Collaborative Processes Choreography A Case Study

Process Mining for e-Government collaborative
processes choreography: a case study
Lucía Antunes1, Andrea Delgado1 , and Laura González1
Instituto de Computación, Facultad de Ingeniería,Universidad de la República
{lucia.antunes,adelgado,lauragon}@fing.edu.uy
Abstract. Digital Government processes are distributed between sev-
eral public organizations that work together to provide services to cit-
izens. Integration of both internal orchestration-like processes and het-
erogeneous technologies is a key challenge for such collaborative pro-
cesses. The Uruguayan Digital Government Agency (AGESIC) provides,
among other components, a centralized Interoperability Platform (PDI),
which is an environment that facilitates integration and connectivity be-
tween participant organizations. Messages exchanged between collabo-
rative processes participants travel through the PDI, thus registering
process choreography data. In this paper, we present a case study we
carried out using messages data registered in the PDI to discover BPMN
2.0 choreography models for selected processes. We adapted an existing
correlation algorithm and generated a collaborative event log that in-
cludes participants with corresponding messages flow as attributes, from
which to obtain the choreography model. These choreography models
have proven to be useful for the business area in analyzing the real inter-
action between public organizations against the expected one, detecting
deviations from the intended use of the platform.^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:6-23]
Keywords: DigitalGovernmentprocesses ·collaborativeprocesses ·col-
laborative process choreography.
1 Introduction
Business processes (BPs) within organizations define the activities and their
sequence within an organizational and technological environment, that provides
expected results or outcomes to fulfill a business objective [16]. Traditional intra-
organizational BPs are also referred as orchestration-like processes, where the
control flow is in charge of the owner organization and within its limits. On
the other hand, collaborative inter-organizational BPs have gained increasingly
interest in the last decade, posing several challenges over orchestration-like pro-
cesses in all phases of the BPs lifecycle. Collaborative BPs involve more than
one organization that interacts with each other via message exchanges, to ob-
tain a global and coordinated result of interest. This type of processes, can have
different forms and distribution options between participant organizations [1].^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:27-37]
Digital Government processes are distributed between several public organi-
zations that work together to provide services to citizens. Integration of both
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
internal orchestration-like processes and heterogeneous technologies is a key
challenge for such collaborative processes. The Uruguayan Digital Government
Agency(AGESIC) 1 providesacentralizedInteroperabilityPlatform(PDI),which
is an environment that facilitates integration and connectivity between partici-
pant organizations. Messages exchanged between collaborative processes partic-
ipants travel through the PDI, enabling the registration of process choreography
metadata. Also, a traceability system component is used by participant organi-
zations to centrally register the activities they carry out within BPs execution.^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:38-48]
In previous work [5] we have analyzed orchestration-like and collaborative
processes from the traceability system, using real data provided by AGESIC to
get insights from their processes. If a BP contains an invocation from one partic-
ipant organization to another, it is expected that activities are registered within
the traceability system, and the message exchanges are carried out through the
PDI. In this context, the primary goal of this paper is to explore the feasibility
of applying pro^[Antunes et al - Process Mining for e-Government collaborative processes choreography a case study.pdf:49-59]
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:43:10'
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Götte et al - Process
    Mining for Object-oriented Processes with Dynamic-temporal Relations.pdf
  hash: 0a12739dc21ad79e32b222eadd13d396525aeeb930a6eecce08f8ea40f74d7f0
  ingested: '2026-07-14T20:43:10'
  size: 520671
status: active
tags:
- process mining
- object-centric
- collection objects
- hierarchical structures
- temporal relations
- split deliveries
- KPIs
- event logs
- supply chain
- ICPM 2025
title: GöTte Et Al   Process Mining For Object Oriented Processes With Dynamic Temporal
  Relations
type: technology
---

# GöTte Et Al   Process Mining For Object Oriented Processes With Dynamic Temporal Relations

Process Mining for Object-oriented Processes
with Dynamic-temporal Relations
Jost Götte1, Maximilian Harms1, and Henrik Leopold1
Kühne Logistics University, Hamburg, Germany{firstname.lastname}@klu.org
Abstract. Process mining analyzes and improves business processes us-
ing event data. Object-Centric Process Mining (OCPM) extends this by
capturing interactions between multiple object types. However, current
methods struggle with hierarchical structures where one object contains
multiple related objects, called collection objects. This paper formally
introduces collection objects within OCPM and identifies two key chal-
lenges: multi-level event execution and object lifecycle mismatches. We
proposeasplit-treeminingapproachthatmodelsdynamicsplitsincollec-
tion objects using hierarchical temporal relations. Our method preserves
relationships across object levels and time and, thus, enables accurate
performance analysis. We evaluate our approach using a simulated order-
to-delivery process with varying object complexity. The results show that
our approach outperforms traditional and existing OCPM techniques in
metrics such as lead time, average delivery time, and delivery spread.
This work establishes a foundation for extending object-centric analy-
sis to processes exhibiting dynamic, hierarchical behaviors, addressing
limitations of prior methods and improving process insights in complex
domains.
Keywords: OCPM · temporal relations · collection object · split deliv-
eries · KPIs.
1 Introduction
Process mining provides methods for analyzing and improving operational pro-
cesses using event data. It helps identify deviations, inefficiencies, and improve-
mentopportunitiesacrossdomainssuchasfinance[22],healthcare[8],andsupply
chain management [19]. Traditional techniques assume flat event logs with sin-
gle case identifiers. While effective, this structure poses limitations, particularly
when multiple process entities interact within a single execution [3].
Object-centric process mining (OCPM) addresses this by modeling multiple
interacting objects within a process. Rather than using a single case notion,
OCPM links events to all relevant objects, providing a more accurate and flexi-
ble representation of real-world processes [3]. However, most OCPM approaches
assume objects refer to singular items, like an invoice, an assumption that often
fails in practice.
In many domains, objects represent collections, i.e., aggregated entities con-
taining multiple, potentially heterogeneous items. We refer to these ascollection
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
2 J. Götte et al.
Order placed50 days Goods delivered100 days150 days200 days
Split
Goods delivered
SplitGoods delivered
Goods delivered
Order o1(100 x Material m1)Item i1(50 x Material m2)Item i2(80 x Material m1)Item i1-1(20 x Material m1)Item i1-2(30 x Material m2)Item i2-1(20 x Material m2)Item i2-2 Goods delivered
Fig. 1. An order-to-delivery process illustrating the dynamics resulting from collection
objects that change over time due to splits.
objects. Traditional mining often treats such relationships with type and quantity
attributes in events, but this oversimplifies the inherent complexity. In OCPM,
treating collections as atomic units can obscure important behaviors.
Toillustratethis,considertheorder-to-delivery(O2D)processfromabusiness-
to-business (B2B) setting shown in Figure 11. A customer places ordero1 con-
taining two items: itemi1 with 100 units of materialm1, and item i2 with 50
units of materialm2. Due to shipping delays, the supplier performs partial de-
liveries for both materials. On an object level, this results in itemi1 being split
into i1−1 and i1−2, and i2 into i2−1 and i2−2. The first of each pair is delivered
earlier; the second, later. Crucially, the order objecto1 is marked delivered only

## Key Data

- tuple L = (E, ET, O, OT, πetype, πtime, πotype, πtrace, O2O) consisting of:
- o1 = o2 → (o1, qual, o2) /∈ R+
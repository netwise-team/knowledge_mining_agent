---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:42:55'
lint_warnings:
- claim: Standard OCPM assumes each object refers to a singular entity (e.g., an invoice,
    a patient, an order).
  concern: This overstates the limitation of standard OCPM. Object-centric process
    mining was specifically designed to handle multiple objects of different types
    per event, moving beyond the single-case assumption of traditional process mining.
    The claim conflates the single-case assumption of classical process mining with
    OCPM's actual design.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Götte et al - Process Mining
    for Object-oriented Processes with Dynamic-temporal Relations.pdf
  hash: 0a12739dc21ad79e32b222eadd13d396525aeeb930a6eecce08f8ea40f74d7f0
  ingested: '2026-07-14T07:42:55'
  size: 520671
status: active
tags:
- process mining
- object-centric
- hierarchical structures
- temporal relations
- split deliveries
- KPIs
- event data
- supply chain
- business processes
- ICPM 2025
title: Object-Centric Process Mining with Collection Objects and Split-Tree Mining
type: technology
---

# Object-Centric Process Mining with Collection Objects and Split-Tree Mining

This page covers a methodology for extending [[object-centric-distance-metric|Object-Centric Process Mining (OCPM)]] to handle **collection objects** — hierarchical, compound entities that can undergo dynamic structural changes such as splits — using a **split-tree mining** approach with hierarchical temporal relations. The method was introduced by Jost Götte, Maximilian Harms, and Henrik Leopold (Kühne Logistics University, Hamburg) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

Standard [[object-centric-distance-metric|OCPM]] assumes each object refers to a singular entity (e.g., an invoice, a patient, an order). In many real-world domains — particularly supply chain and B2B logistics — objects represent **collections**: aggregated entities containing multiple, potentially heterogeneous items. For example, in an order-to-delivery (O2D) process, a single order may contain multiple item lines, each representing a quantity of a material. When partial deliveries occur, items are split into sub-items, creating dynamic, hierarchical object structures. ^[Götte et al - Process Mining for Object-oriented Processes with Dynamic-temporal Relations.pdf:38-52]

Existing OCPM approaches, including case-centric flattening and standard object-centric event log (OCEL) techniques, fail to capture two key challenges:

1. **Multi-level event execution**: Collection objects manage multiple lower-level objects with distinct behaviors. Meaningful analysis requires traceability across abstraction levels.
2. **Object lifecycle mismatch**: Splitting an item terminates its lifecycle and initiates those of new items, resulting in partially overlapping lifecycles that distort performance metrics such as delivery time. ^[Götte et al - Process Mining for Object-oriented Processes with Dynamic-temporal Relations.pdf:65-75]

## Formal Definitions

### Object-Centric Event Log

Building on OCEL 2.0 foundations, an object-centric event log is defined as a tuple:

`L = (E, ET, O, OT, π_etype, π_time, π_otype, π_trace, O2O)`

where E is a set of events, O is a set of objects, OT is a set of object types, and O2O is a set of qualified object-object relationships. ^[Götte et al - Process Mining for Object-oriented Processes with Dynamic-temporal Relations.pdf:99-110]

### Collection Object

An object `o ∈ O` is a **collection object** if it relates to multiple objects of the same type via a "consists of" qualifier in O2O. The set of all collection objects CO is formally defined to exclude circular containment. This allows analysis at different levels of abstraction — e.g., at the order level (aggregating over items) or at the item level (fine-grained per item). ^[Götte et al - Process Mining for Object-oriented Processes with Dynamic-temporal Relations.pdf:114-120]

### Collection Object Split

A **split** deletes a collection object `co` and creates `n ≥ 2` new collection objects of the same type. This is reflected in the OCEL via a dedicated "split" event or via "delete" and "create" events. Splits introduce hierarchical temporal relationships between the original and successor objects.

### Hierarchical Temporal Split Relation

The **split relation** `R_split ⊆ CO × U_qual × CO` captures successor relationships between collection objects after a split. Key properties:
- `(co1, qual, co2) ∈ R_split` indicates co2 is a successor of co1.
- A collection object cannot be its own successor (acyclicity enforced via transitive closure).
- `succ(co)` returns all successors of a given collection object.
- `CO_roots` denotes collection objects with no predecessors in the split relation.

Splits form a **directed acyclic graph (DAG)** — the **split tree** — where nodes are collection objects and edges represent split successions, evolving hierarchically over time.

## Split-Tree Mining Algorithm

Algorithm 1 implements a **breadth-first search** to extract split trees from an OCEL:

1. Starting from an object of interest, identify root collection objects via O2O.
2. For each root, initialize a tree and a queue.
3. Iteratively dequeue nodes, check for successors via `succ()`, and add children to both the tree and the queue.
4. Nodes with no successors are added as leaves.
5. Return all constructed split trees.

This approach enables analysis across object levels (addressing Challenge 1) and across mismatching lifecycles (addressing Challenge 2).

## KPI Computation from Split Trees

Algorithm 2 formalizes KPI computation over split trees:

- Given an object, a KPI function (e.g., delivery time), and an aggregation method (e.g., average), the algorithm retrieves all split trees for the object.
- It iterates over leaf nodes, applying the KPI function to events associated with each leaf.
- Results are aggregated at either the **upper level** (per order) or **lower level** (per item), depending on the desired analysis granularity.

A concrete example is **weighted delivery time**: the time difference between order placement and each item's delivery, computed by traversing the full split hierarchy to the leaf nodes.

## Evaluation

### Simulated Process

The method is evaluated on a simulated **order-to-delivery warehouse process** with partial deliveries and item splits. The BPMN process includes:
- "Place Order" → "Check Availability" → three paths: no availability (re-evaluate), full availability (pick/pack/ship), partial availability (split item and recurse).
- Splits can occur multiple times; each final delivery group becomes a leaf in the split tree.

### Data Generation

Ten simulation runs of 1,000 days each generate OCEL 2.0 logs with increasing average numbers of deliveries (AoD) per order, from 1 (no splits) to 10 (complex multi-shipment). Logs link events to Orders, Items, and Packages.

### Baselines

| Method | Description |
|---|---|
| **CCO** (Case-centric, Order as case) | Aggregates item events to order level; ignores item variability |
| **CCI** (Case-centric, Item as case) | Maximum item visibility; ignores order context; duplicates split events |
| **OCP** (OCPM + OC-PPINOT) | Traceability functions for single-level splits; fails at deeper hierarchies |
| **STO** (Split-tree, order level) | Proposed method aggregated at order level |
| **STI** (Split-tree, item level) | Proposed method aggregated at item level |

### Metrics

- **Lead time**: Duration from order placement to final delivery.
- **Average delivery time**: Mean duration from order placement to each individual delivery.
- **Delivery spread**: Time between first and final shipment.

### Results

The split-tree methods (STO, STI) consistently produce correct KPI values across all complexity levels:

- **Lead time**: CCI underestimates with increasing splits; STO/STI maintain accuracy by tracing full hierarchical lifecycles.
- **Average delivery time**: CCI truncates lifecycles and underestimates; STO/STI correctly relate each delivery to the initial order placement.
- **Delivery spread**: CCO always reports zero spread; CCI underestimates; only STO/STI capture the full temporal range by traversing the entire split hierarchy.
- **OCP** degrades with increasing split depth due to fixed-depth traceability, missing deeper levels and intermediate deliveries.

The split-tree approach remains stable and accurate regardless of the number of splits, demonstrating scalability and robustness in hierarchical, object-centric contexts.

## Relation to Existing OCPM Work

- **OCEL 2.0** and object-centric directly-follows graphs (OCDFG) provide the foundational event log structure extended by this work.
- **Object-centric Petri nets** and object continuation graphs are related model types but do not handle dynamic collection object splits.
- **OC-PPINOT** (Estrada-Torres et al.) introduced traceability functions for grouping related objects but lacks recursion for variable-depth split trees.
- **OPerA** (Park et al.) generalizes classical metrics to object-centric settings but assumes static object relationships.
- This work extends [[streaming-object-centric-process-mining|streaming and object-centric frameworks]] by introducing hierarchical temporal splits as a first-class concept.

## Limitations and Future Work

- Validation on real-world datasets is needed beyond the simulated O2D scenario.
- The current method assumes only split-based evolution; it does not yet handle collection objects that **grow**, **consolidate**, or involve KPI events occurring between splits.
- Extensions to conformance checking and predictive analytics are identified as future directions.
- Applicability to domains beyond supply chain management (e.g., healthcare, finance) remains to be explored.

## Key Concepts

- **Collection object**: A compound process object containing multiple related sub-objects of the same type.
- **Collection object split**: A dynamic structural change that terminates one collection object and creates two or more successors.
- **Split tree**: A directed acyclic graph representing the hierarchical succession of collection objects over time.
- **Hierarchical temporal split relation**: A formal relation capturing predecessor-successor relationships between collection objects across splits.
- **Split-tree-based KPI computation**: An algorithm that traverses split trees to compute accurate performance metrics across multi-level, dynamically evolving object lifecycles.

## Key Data

- tuple L = (E, ET, O, OT, πetype, πtime, πotype, πtrace, O2O) consisting of: ^[Götte et al - Process Mining for Object-oriented Processes with Dynamic-temporal Relations.pdf:100-110]
- o1 = o2 → (o1, qual, o2) /∈ R+
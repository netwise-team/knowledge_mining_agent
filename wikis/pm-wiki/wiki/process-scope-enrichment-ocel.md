---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:51:22'
lint_warnings:
- claim: The approach was introduced by Shahrzad Khayatbashi (Linköping University),
    Majid Rafiei, Jiayuan Chen, Timotheus Kampik, and Gregor Berg (SAP Signavio),
    and Amin Jalali (Stockholm University) in a paper accepted at the ICPM 2025 Workshops
    (Springer LNBIP series).
  concern: ICPM 2025 has not yet occurred at the time of established knowledge, making
    it impossible to verify that this paper was 'accepted' at ICPM 2025 Workshops.
    This claim cannot be confirmed and may be premature or fabricated.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Khayatbashi et al - Enriching
    Object-Centric Event Data with Process Scopes  A Framework for Aggregation and
    Analysis.pdf
  hash: 0878609f178a18ecd473ac350c4d331ca6cedf0141012aa454804330bec0d505
  ingested: '2026-07-14T07:51:22'
  size: 735319
  truncated: true
status: active
tags:
- process mining
- event log
- business process analysis
- data aggregation
- process abstraction
- value chain
- organizational analysis
- OCEL
- OCPM
- scope definition
title: Enriching Object-Centric Event Data with Process Scopes
type: concept
---

# Enriching Object-Centric Event Data with Process Scopes

This page covers a framework for embedding explicit, analyst-defined **process scopes** into [[streaming-object-centric-process-mining|Object-Centric Event Logs (OCEL)]], enabling structured multi-process analysis, aggregation, and inter-process interaction discovery. The approach was introduced by Shahrzad Khayatbashi (Linköping University), Majid Rafiei, Jiayuan Chen, Timotheus Kampik, and Gregor Berg (SAP Signavio), and Amin Jalali (Stockholm University) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

[[streaming-object-centric-process-mining|Object-Centric Process Mining (OCPM)]] enables analysis of complex operational behavior by capturing interactions among multiple business objects (orders, items, deliveries, etc.) within a single Object-Centric Event Log (OCEL). However, existing OCEL formats — including OCEL 2.0 — lack explicit support for defining **process scopes**: the boundaries that delineate what constitutes a distinct process within the log.^[Khayatbashi et al - Enriching Object-Centric Event Data with Process Scopes  A Framework for Aggregation and Analysis.pdf:11-15]

In practice, OCEL data often spans multiple interrelated processes connected through shared objects (e.g., a transport document linking an order management process to a goods management process). Without explicit scoping:

- Analysts must apply ad hoc manual filtering to isolate relevant subsets.
- Inter-process interactions, handovers, and dependencies remain implicit and hard to discover systematically.
- Analysis is restricted to a single level of granularity, preventing drill-down or roll-up across organizational process hierarchies.
- Process definitions are inherently subjective and context-dependent (varying by role, organizational unit, and analytical goal), making automated discovery insufficient.^[Khayatbashi et al - Enriching Object-Centric Event Data with Process Scopes  A Framework for Aggregation and Analysis.pdf:17-65]

## Core Concepts

### Scope-Enriched OCEL (POCEL)

The framework introduces the notion of a **scope-enriched OCEL (POCEL)**: an OCEL that contains objects of the reserved type `process`, each representing a specific analyst-defined process scope. Formally, a POCEL is an OCEL in which:

- At least one object `o` exists with `objtype(o) = process`.
- Events are linked to process objects via qualified event-to-object (E2O) relations.
- Process objects are interrelated via object-to-object (O2O) relations, enabling hierarchical and overlapping scope structures.

This makes process boundaries **transparent, reproducible, and machine-interpretable** while remaining fully compliant with the OCEL 2.0 standard.^[Khayatbashi et al - Enriching Object-Centric Event Data with Process Scopes  A Framework for Aggregation and Analysis.pdf:112-119]

### Hierarchical and Overlapping Scopes

Scopes can be defined at multiple levels of abstraction:

- **Fine-grained scopes** capture local subprocesses (e.g., individual operational tasks).
- **Coarse-grained scopes** aggregate multiple fine-grained scopes into higher-level processes (e.g., a value chain stage).
- Scopes may **overlap** when shared objects connect events across organizational functions.

This hierarchy supports **drill-down** (from strategic to operational) and **roll-up** (from operational to strategic) analysis, reflecting how different stakeholders — process owners, managers, analysts — view the same underlying event data differently.^[Khayatbashi et al - Enriching Object-Centric Event Data with Process Scopes  A Framework for Aggregation and Analysis.pdf:60-65]

## The Enrichment Language

To enable repeatable, domain-sensitive scope construction, the framework introduces a formal **grammar-based enrichment language** (a context-free grammar `G = (Σ, N, R, S)`).

### Grammar Structure

- **Terminal symbols (Σ):** `INCLUDE`, `EXCLUDE`, `AND`, `OR`, sets of object types, event types, attribute names, and values.
- **Non-terminals (N):** `ruleset`, `rule`, `statement`, `filteritem`, `entity`, `attribute`, `operator`, `value`.
- **Start symbol:** `ruleset`.

### Key Production Rules

```
<ruleset> ::= <rule> | (<ruleset> AND <ruleset>) | (<ruleset> OR <ruleset>)
<rule>    ::= INCLUDE <statement> | EXCLUDE <statement>
            | INCLUDE <statement> AND EXCLUDE <statement>
<statement> ::= { <filteritem> (, <filteritem>)* }
<filteritem> ::= (<entity>, ε, ε, ε) | (<entity>, <attribute>, <operator>, <value>)
<entity>  ::= an item ∈ Uotype ∪ Uetype
<operator> ::= < | > | = | ≠ | ...
```

A **ruleset** specifies inclusion and exclusion criteria over event types, object types, and their attribute values. Compound conditions support conjunctions, disjunctions, and nested expressions. The operator set is extensible.

### Enrichment Procedure

Given a valid ruleset, a deterministic transformation procedure:
1. Evaluates the ruleset over the original OCEL.
2. Filters relevant events and associated objects.
3. Instantiates a new `process` object with a unique identifier.
4. Links the process object to all selected entities via OCEL-compliant E2O and O2O relations.

The result is a POCEL in which the process scope is structurally embedded.

## Implementation Tools

### Procellar

**Procellar** is an open-source tool (JavaScript front-end, Python back-end) that allows analysts to:

- Import an existing OCEL log.
- Define process scope rulesets interactively via two modes:
  - **Basic mode:** Include/exclude object types without attribute filtering.
  - **Advanced mode:** Specify complex criteria combining event/object attributes, operators, and values.
- Apply rulesets to generate a scope-enriched OCEL (POCEL).
- Export both the enriched log and the rulesets for reproducibility and reuse.

Available at: [https://github.com/hudsonjychen/procellar](https://github.com/hudsonjychen/procellar)

### Business Execution Graph (BEG)

**Business Execution Graph (BEG)** is an open-source visualization and analysis tool that takes a scope-enriched OCEL as input and produces a **process interaction network** where:

- **Nodes** represent process scopes (sized by object count or object type diversity; colored by edge centrality).
- **Edges** represent object-type handovers between processes (labeled by object type, total shared objects, or average flow times).

The graph can be exported as PNG or in VOSviewer format for advanced network clustering. Available at: [https://github.com/hudsonjychen/business-execution-graph](https://github.com/hudsonjychen/business-execution-graph)

## Demonstration: Logistics Case Study

The approach was demonstrated on a publicly available logistics OCEL (from ocel-standard.org), covering an end-to-end scenario from customer order placement to long-distance carrier transport. Four process scopes were defined:

| Process Scope | Description | Events |
|---|---|---|
| **Order Management** | Order creation and management, issuing transport documents | 594 |
| **Goods Management** | Ordering containers, collecting/loading goods for dispatch | 13,155 |
| **Transportation Management** | Container movement between warehouses and terminals | 18,314 |
| **Export Management** | Scheduling and loading containers onto ships/trains | 2,132 |

The BEG visualization revealed:
- Order Management transmits **Transport Document** objects to Goods Management.
- Goods Management feeds both Transportation Management and Export Management.
- Transportation Management coordinates via **Container** and **Handling Unit** object types.
- Export Management depends on Transportation Management via **Forklift** usage.
- A loop pattern was detected: forklifts returning empty after container delivery.

All artifacts (scope-enriched OCEL, rulesets) are publicly available at [https://github.com/shahrzadkhayatbashi/Process-Level-OCPM](https://github.com/shahrzadkhayatbashi/Process-Level-OCPM).

## Relationship to Prior Work

The framework complements existing OCEL transformation operations (drill-down, roll-up, unfold, fold) that adjust log granularity in a data-centric manner. Unlike those approaches, process scope enrichment is **analyst-driven and semantically grounded**: it embeds domain knowledge about process boundaries directly into the log structure, rather than restructuring object types or event semantics. It also extends van der Aalst's earlier work on process interoperability patterns (chained execution, subcontracting, case transfer, capacity sharing, loosely coupled execution) by providing a concrete mechanism to represent and analyze such patterns within [[streaming-object-centric-process-mining|OCPM]] frameworks.

## Limitations and Future Work

- Process scope definitions are currently fully analyst-driven; automated or semi-automatic discovery of scopes is a direction for future work.
- The enrichment language does not yet support temporal constraints or behavioral patterns within scopes.
- Real-world practitioner evaluation of the scope-enriched approach has not yet been conducted.
- Future integration with enterprise modeling environments is planned to support strategic alignment and process governance.^[Khayatbashi et al - Enriching Object-Centric Event Data with Process Scopes  A Framework for Aggregation and Analysis.pdf:20-28]

## Key Contributions

1. **Formal definition** of scope-enriched OCEL (POCEL) as an extension of OCEL 2.0.
2. **Grammar-based enrichment language** for specifying analyst-defined process scopes.
3. **Procellar** tool for interactive scope definition and POCEL export.
4. **Business Execution Graph (BEG)** tool for visualizing inter-process interactions.
5. Open-source artifacts and a reproducible logistics case study demonstration.^[Khayatbashi et al - Enriching Object-Centric Event Data with Process Scopes  A Framework for Aggregation and Analysis.pdf:23-28]
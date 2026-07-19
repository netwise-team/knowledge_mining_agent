---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T06:56:24'
lint_warnings:
- claim: introduced by van den Elzen, Andrienko, Kerren, Resinas, Weber, and Yu (ICPM
    2025 Workshops)
  concern: ICPM 2025 has not yet occurred at the time of established knowledge, making
    it impossible to verify this citation. This could be a fabricated or speculative
    reference.
- claim: Road Traffic Fine Management event log (~561,470 events, 150,370 cases, 11
    activities, 12 data attributes, recorded 2000–2013 by an Italian police force)
  concern: The well-known Road Traffic Fine Management Process log from the 4TU repository
    has approximately 150,370 cases and 561,470 events, but is commonly cited as having
    around 11 activities and fewer than 12 data attributes. The specific figure of
    12 data attributes may be overstated compared to the standard published dataset
    description.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/van den Elzen et al - Coordinated
    Projections A New Approach to Multi-Faceted Process Exploration.pdf
  hash: d1628383d994850687e106253deb0a97c72188e0d0fbfa777a3968a2250d9ff6
  ingested: '2026-07-14T06:56:24'
  size: 6214133
  truncated: true
status: active
tags:
- process mining
- visual analytics
- dimensionality reduction
- multi-faceted exploration
- coordinated projections
- event log
- topic modeling
- brushing-and-linking
- control-flow
- process exploration
title: 'Coordinated Projections: Multi-Faceted Process Exploration'
type: technology
updated: '2026-07-14'
---

# Coordinated Projections: Multi-Faceted Process Exploration

Coordinated Projections is a visual analytics approach for multi-faceted process exploration in process mining, introduced by van den Elzen, Andrienko, Kerren, Resinas, Weber, and Yu (ICPM 2025 Workshops). It addresses a core limitation of traditional process exploration tools: the reliance on fixed-facet, single-perspective visualizations such as Directly-Follows Graphs (DFGs), which constrain analytical flexibility and obscure cross-perspective dependencies.^[13-26]

## Motivation

Process exploration is a fundamental task in process mining, particularly during the initial phases of a project when analysts familiarize themselves with event log data, formulate hypotheses, and uncover unexpected patterns. Traditional approaches encode process behavior primarily through the control-flow facet using DFGs, where nodes represent activities and edges represent direct succession. While additional visual channels (e.g., frequency, duration overlays) can enrich DFG-based views, the primary facet remains fixed.^[28-54]

Real-world analytical tasks require continuous shifts between facets—from case-centric to activity-centric, from control flow to resource flow, from process variants to attribute analysis. Fixing the facet can obscure relevant patterns, reduce user agency, and create cognitive mismatches between the visualization and the analyst's current mental model.^[59-66]

## Core Approach

The method integrates dimensionality reduction (DR) and topic modeling to generate coordinated views that dynamically link different facets of process data. The workflow proceeds through the following stages:

### A. Event Log Input
The approach is demonstrated using the publicly available Road Traffic Fine Management event log (~561,470 events, 150,370 cases, 11 activities, 12 data attributes, recorded 2000–2013 by an Italian police force).

### B. Attribute Derivation and Case Log Enrichment
The event log is transformed into an enriched case log using case predicates. Cases are assigned process outcomes: *fully paid*, *dismissed*, *credit collected*, or *unresolved*. Derived attributes such as `outstandingBalance` are computed.

### C. Defining Facets of Interest
Analysts select which process elements (cases, activities, variants, resources) and which attributes define the projection space. Facets may include:
- **Control-flow characteristics**: activity sequences, frequency patterns
- **Outcome-related indicators**: outstanding balance, dismissal codes
- **Contextual attributes**: vehicle class, notification type
- **Temporal aspects**: activity duration, case throughput time
- **Process variants**: distinct execution paths

### D. High-Dimensional Multi-Faceted Trace Encoding
Two main encoding strategies are used:

1. **Outcome-focused encoding**: Attributes such as `outstandingBalance > 0`, `totalPaymentAmount > 0`, dismissal code, and last activity are one-hot encoded.
2. **Control-flow sequence encoding**: Activity sequences are extracted, padded to uniform length, and one-hot encoded, producing an *n × m* matrix expanded into higher-dimensional format.

For topic modeling, event logs are represented as strings of activities (e.g., `A B C`) or transitions (e.g., `A_B B_C`), or a combination of both.

### E. Dimensionality Reduction and Topic Modeling
Non-linear DR techniques—**UMAP** and **t-SNE**—project high-dimensional encodings into 2D scatterplot space. **Latent Dirichlet Allocation (LDA)**-based topic modeling is applied to identify semantic themes within traces. DR preserves local similarity structure; topic modeling reveals semantic groupings. Together they provide both semantic structure and visual explorability.^[112-119]

### F. Visualization and Interaction
A **coordinated multiple views** framework connects two or more scatterplots through **brushing-and-linking**: selecting items in one view highlights corresponding items in all linked views. This enables cross-perspective exploration (e.g., correlating control-flow clusters with attribute clusters).^[112-119]

Key interaction techniques include:
- **Brushing-and-linking**: two-way selection across coordinated views
- **Focus+context**: close inspection of subsets while maintaining overview
- **Semantic zooming**: varying levels of detail by zoom level
- **Jittering**: alleviating overplotting in dense scatterplots
- **Attribute encoding**: color, shape, and size channels for additional facets^[23-25]

### G. Glyph-Based Encodings
To improve interpretability beyond positional encoding, the approach proposes replacing scatterplot dots with **glyphs** that encode multiple data attributes simultaneously. Glyph design for multi-faceted process data is identified as a key area for future work.

## Trace Encoding Categories

The paper situates its approach within three broad categories of trace encodings used in process mining:

| Category | Description | Examples |
|---|---|---|
| **Control-flow encodings** | Capture activity order and structure | n-grams, bags-of-activities, transition abstractions |
| **Data-aware encodings** | Incorporate case attributes, event data, resources, timing | Elapsed time, resource involvement |
| **Embedding-based encodings** | Dense vector representations via deep learning | LSTMs, Transformers, autoencoders |

^[98-111]

## Key Findings

Applied to the Road Traffic Fine log, the approach demonstrates:
- Clusters of similar traces (process variants) emerge in control-flow projections
- Attribute-based projections reveal clusters of similar outcome values
- Two-way brushing reveals that clusters of short traces (`{create fine, send fine}`) correspond to specific dismissal value structures in the attribute projection
- Topic modeling results are consistent with DR-based projections while substantially reducing dimensionality and improving interpretability

## Relationship to Multi-Perspective Process Mining

The approach aligns with multi-perspective process mining principles, enabling analysts to explore not only *what* happens (control flow) but also *how* and *why* it happens (data attributes, timing, resources). It extends the visual analytics paradigm in process mining, which emphasizes interactive, human-centered exploration over purely algorithmic output.^[80-85]

## Future Directions

- Representing activities and process variants (not just cases) as points in projections
- Systematic investigation of multi-faceted encodings for activities, variants, and traces
- Integration with process discovery algorithms to generate DFGs for selected subpopulations
- Ensemble methods combining multiple embedding approaches
- Expanded support for resource and relationship facets
- Formal evaluation of effectiveness and scalability

## References

van den Elzen, S., Andrienko, G., Kerren, A., Resinas, M., Weber, B., & Yu, P. (2025). *Coordinated Projections: A New Approach to Multi-Faceted Process Exploration*. In: Process Mining Workshops (ICPM 2025 Int. Workshops), Springer LNBIP.

## Workflow Steps in Detail

The Coordinated Projections approach follows a structured pipeline (Fig. 1 in the paper) consisting of seven stages:

### A. Original Dataset
The approach is demonstrated on the publicly available Road Traffic Fines event log (de Leoni & Mannhardt, 2015), which documents traffic fine handling by a local Italian police force. It contains approximately 561,470 events across 150,370 cases recorded between January 2000 and June 2013, involving 11 activities and 12 data attributes. The dataset supports exploration across control-flow, temporal, and data perspectives simultaneously.

### B. From Event Log to Enriched Case Log
The event log is transformed into a case log and enriched using case predicates. Each case is assigned one of four process outcomes: *fully paid*, *dismissed*, *credit collected*, or *unresolved*. Derived attributes such as `outstandingBalance` (sum of amounts plus expenses minus total payment amount) are computed and appended to the enriched case log.

### C. Define Facets of Interest
Users determine which process elements (cases, activities, variants, resources) will be represented as individual points in the projection space, and which attributes will define their position. Relevant dimensions include control-flow characteristics (activity sequences, frequency patterns), outcome-related indicators, contextual attributes, temporal aspects (duration, throughput time), and process variants.

### D. High-Dimensional Representation — Multi-Faceted Trace Encoding
Three categories of trace encoding are supported, consistent with the broader [[object-centric-distance-metric|process mining]] literature:

- **Control-flow encodings**: Capture activity order and structure using n-grams, bags-of-activities, or transition abstractions.
- **Data-aware encodings**: Enrich trace representations with case attributes, event-level data, resource involvement, and derived temporal attributes (e.g., elapsed time since previous event).
- **Embedding-based encodings**: Use deep learning models (LSTMs, Transformers, autoencoders) to learn dense vector representations of traces.

^[98-111]

For topic modeling, event logs are represented as sets of activities or sets of direct transitions (e.g., `A_B B_C`), or a combination of both. For dimensionality reduction, two encodings are constructed: one focused on outcome-relevant attributes (outstanding balance, total payment amount, dismissal code, last activity — with one-hot encoding for categorical fields), and one capturing the ordered activity sequence per case (padded to uniform length and one-hot encoded).

### E. Non-Linear Dimensionality Reduction and Topic Modeling
UMAP and t-SNE are applied to the multi-faceted trace encodings to project high-dimensional representations into two-dimensional scatterplots. Topic modeling (Latent Dirichlet Allocation) is applied in parallel, treating traces as textual documents. The two techniques are complementary: topic modeling reveals underlying semantic themes, while DR preserves local similarity structure. Three UMAP projections are generated based on topic weights, activity order, and case attributes respectively, and colored by process outcome and main topic to validate consistency across representations.

^[112-119]

### F. Visualization and Interaction
A **coordinated multiple views** framework connects two or more scatterplots through **brushing-and-linking**: selecting items in one view highlights corresponding items in all other views. This enables cross-perspective exploration — for example, selecting a cluster of similar traces in the control-flow projection reveals the corresponding attribute cluster structure in the outcome projection. Additional interaction techniques include:
- **Focus+context**: Close inspection of a data subset while maintaining an overview.
- **Semantic zooming**: Different levels of detail depending on zoom level.
- **Jittering**: Prevents overplotting in dense scatterplot regions.
- **Attribute encoding**: Color, shape, and size channels encode additional facets beyond position.

^[112-119]

### G. Glyph-Based Visual Encodings
To improve interpretability beyond position-only encodings (where only local distances are meaningful), the approach proposes replacing scatterplot dots with **glyphs**. Multiple data attributes can be encoded within a single glyph, representing multiple properties of a single entity or aggregate information across entities. Glyph types examined in prior literature include face-based and icon-based representations. The design of effective multi-facet glyphs for [[conformance-checking-visualization-idioms|process mining]] contexts is identified as a direction for future work.

## Relationship to Trace Encoding Research

The coordinated projections approach builds directly on the trace encoding literature. Comprehensive benchmarking of control-flow-focused encodings (Bose & van der Aalst, 2009) and multi-perspective encodings for classification, clustering, and anomaly detection (Rullo et al., 2025) inform the encoding design choices. The use of UMAP and t-SNE aligns with established visual analytics principles emphasizing coordinated views and multi-perspective representations to enhance analytical reasoning. ^[108-119]

## Future Work

Planned extensions to the system include:
- Alternative semantic representations for scatterplot points (activities, process variants) beyond cases.
- Systematic investigation of multi-faceted encoding strategies for different exploratory goals.
- Integration with existing [[sustainability-aware-process-mining|process discovery]] algorithms to generate DFGs for selected subpopulations.
- Expansion to additional facets including relationships, control-flow, and resources.
- Ensemble methods for embeddings, combining conceptually different embedding technologies or the same algorithm with varied hyperparameter settings.
- Formal evaluation of effectiveness and scalability across a wide range of analytical tasks and user needs.
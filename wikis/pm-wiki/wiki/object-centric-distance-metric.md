---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:08:03'
lint_warnings:
- claim: An object-centric event log is an ordered sequence of events L = ⟨(a1, O1),
    (a2, O2), …⟩, where each activity ai is associated with a set of involved objects
    Oi. Timestamps determine the total ordering of events.
  concern: 'Defining an event log as a sequence ordered by timestamps is a simplification
    that can be problematic: timestamps in real event logs are often not unique, leading
    to partial rather than total orderings. Claiming timestamps ''determine the total
    ordering'' overstates the precision typically available in practice and contradicts
    how event logs are formally handled in much of the process mining literature.'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Hildebrand et al - A Distance
    Metric for Object-Centric Process Mining.pdf
  hash: bdb840d84389041962084db1095b6e14293eccfe94b46be9ab2d42f1d1c522f8
  ingested: '2026-07-14T07:08:03'
  size: 428064
  truncated: true
status: active
tags:
- process mining
- object-centric
- distance metric
- graph-based weights
- cost minimization
- business objects
- clustering
- cohort identification
- event logs
- benchmarking
title: Distance Metric for Object-Centric Process Mining
type: technology
---

# Distance Metric for Object-Centric Process Mining

Object-centric process mining (OCPM) extends traditional [[coordinated-projections-multi-faceted-process-exploration|process mining]] by considering multiple interrelated business objects simultaneously, rather than focusing on the lifecycle of a single isolated object. A key analytical challenge in OCPM is comparing business objects in a meaningful way — for example, to cluster customers by behavior or identify resource usage patterns. This page covers a novel distance metric for object-centric event logs, introduced by Jonas Simon Hildebrand, Jan Niklas van Detten, and Sander J. J. Leemans (RWTH Aachen University / Celonis) in a paper accepted at the ICPM 2025 Workshops.

## Motivation

In traditional process mining, distance measures quantify dissimilarity between isolated object traces (e.g., sequences of activities for a single purchase order). In the object-centric setting, however, objects interact: a purchase order may be linked to multiple items, invoices, shipments, and customers. Clustering and cohort identification — common analysis tasks in OCPM — require distance measures that account for these interactions.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:31-54]

Existing approaches fall short in two main ways:
- Some methods focus exclusively on the events of the target object, ignoring related objects entirely.
- Others treat all related objects with equal weight, regardless of how directly or indirectly they interact with the compared objects.

These shortcomings can lead to flawed analytical results, such as failing to detect duplicate payments or unauthorized procurement patterns.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:63-71]

## Object-Centric Event Logs and Object Graphs

An **object-centric event log** is an ordered sequence of events `L = ⟨(a1, O1), (a2, O2), …⟩`, where each activity `ai` is associated with a set of involved objects `Oi`. Timestamps determine the total ordering of events.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:90-95]

The **object graph** `G = (Θ, E)` is an undirected graph where objects form vertices and edges connect objects that co-occur in at least one event. Two objects are *related* if they are transitively connected in this graph. Key graph-theoretic quantities include:
- `tra(o1, o2)`: shortest-path length between two objects (transitivity)
- `deg(o)`: node degree (number of direct connections)
^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:96-105]

## Five Axioms for Object-Centric Distance Measures

The authors identify five formal requirements (axioms) that a distance measure must satisfy to be meaningful in the object-centric setting:

| Axiom | Description |
|-------|-------------|
| **A1** | All objects related to either compared object must influence the distance (contextual completeness). |
| **A2** | Impact of related objects must decay with increasing graph distance (transitivity sensitivity). |
| **A3** | Objects with higher node degree (more connections) must have higher impact (connectivity sensitivity). |
| **A4** | The measure must be sensitive to the control flow (activity sequences) of related objects. |
| **A5** | The measure must be a proper metric (non-negativity, identity of indiscernibles, symmetry, triangle inequality). |

These axioms are grounded in established process modeling principles, including product-based process modeling (Dumas et al.) and data-driven process architectures (Weske).^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:55-62]

## The Proposed Distance Metric

### Object Impact Function

For a pair of objects `(o1, o2)`, the **impact** of a related object `o` is defined as:

```
I(o) = 0.5 × (Dnorm(o1)[o] + Cnorm(o1)[o])
```

where:
- **Dnorm**: normalized impact based on graph distance. For each related object `oi`, the weight is `δ^tra(o, oi) / norm1`, where `δ ∈ (0,1)` is a decay parameter and `norm1` is a normalizing constant. Closer objects receive higher weight.
- **Cnorm**: normalized impact based on node degree. For each related object `oi`, the weight is `deg(oi) / norm2`, where `norm2` is the sum of degrees of all related objects. More connected objects receive higher weight.

The combination of distance-decay and degree-weighting ensures axioms A2 and A3 are satisfied.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:72-81]

### Earth Mover's Distance Framework

The final distance between two objects is computed using the **Earth Mover's Distance (EMD)**, also known as the Wasserstein distance, with the **Levenshtein distance** as the ground truth metric on activity sequences:

```
dG(o1, o2) = min_{x≥0} Σ_i Σ_j lv(oi, oj) · x_ij
```

subject to:
- `Σ_i x_ij = I(oj)` for all j (impact of o2-related objects fully distributed)
- `Σ_j x_ij = I(oi)` for all i (impact of o1-related objects fully distributed)

The auxiliary variables `x_ij` represent how much of the impact of object `oi` (related to `o1`) is mapped to object `oj` (related to `o2`). The EMD finds the minimum-cost transport plan, where cost is the Levenshtein distance between activity sequences.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:72-81]

The EMD inherits metric properties from the Levenshtein ground distance, satisfying Axiom A5. Any metric ground distance is compatible with this framework.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:106-112]

### Theorem

The constructed `dG(o1, o2)` satisfies all five axioms A1–A5. The proof uses sensitivity analysis on the dual formulation of the EMD to show that the impact function correctly reflects the influence of each related object.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:72-81]

## Evaluation

### Clustering in a Purchase-to-Pay Process

The metric was applied to cluster 927 purchase requisitions from a publicly available purchase-to-pay (P2P) event log using DBSCAN (ε = 0.05). Eight interpretable clusters were identified, including:
- Standard P2P flows (one purchase, delivery, payment)
- Fragmented deliveries (high goods receipts per PO)
- Unauthorized purchases bypassing approval
- Duplicate payment events
- Delegated approval variants

The proposed metric achieved a silhouette score of 0.48 and successfully surfaced the duplicate payment anomaly — a finding that competing approaches missed.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:76-81]

### Comparison with Existing Methods

| Approach | A1 | A2 | A3 | A4 | A5 |
|----------|----|----|----|----|----|
| Ghahfarokhi et al. (object profiles) | ✗ | ✗ | ✗ | ✓ | ✓ |
| Faria Junior et al. (global identifier + Levenshtein) | ✓ | ✗ | ✗ | ✓ | ✓ |
| Jalali et al. (Markov multigraph) | ✗ | ✗ | ✗ | ✗ | ✗ |
| Zager et al. (graph similarity) | ✓ | ✗ | ✗ | ✗ | ✗ |
| Vitanyi et al. (normalized information distance) | ✓ | ✗ | ✗ | ✓ | ✓ |
| **Proposed metric** | ✓ | ✓ | ✓ | ✓ | ✓ |

The Ghahfarokhi approach (object profiles without graph structure) found only three clusters and missed the duplicate payment pattern. The Faria Junior approach (equal-weight Levenshtein) produced diverse clusters but could not isolate the duplicate payment anomaly reliably.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:63-71]

### Feasibility

Runtime was assessed on three OCEL logs:

| Log | Compared Type | Pairwise Comparisons | Median Related Objects | Runtime |
|-----|--------------|---------------------|----------------------|---------|
| Purchase-to-Pay | Purchase Requisition | 429,201 | 8 | 130s |
| Order-to-Cash | Orders | 1,999,000 | 7 | 1,000s |
| Sustainability | Customer | 10,731 | 101 | 2,200s |

Runtime scales with both the number of pairwise comparisons and the number of related objects. Mitigation strategies include EMD approximation heuristics and advanced case notions to reduce the object graph.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:76-81]

## Relationship to Other Process Mining Topics

This distance metric is broadly applicable beyond clustering, supporting:
- **Anomaly detection**: identifying objects with unusual interaction patterns
- **Process monitoring**: tracking behavioral drift across object populations
- **Optimization**: targeting interventions at high-impact object clusters

The approach complements [[sustainability-aware-process-mining|sustainability-aware process mining]], where object-level clustering could identify resource-intensive process variants, and [[actor-enriched-throughput-time-forecasting|actor-enriched throughput time forecasting]], where object interaction structure influences performance predictions.^[Hildebrand et al - A Distance Metric for Object-Centric Process Mining.pdf:79-81]

## Future Work

The authors plan to explore:
- Advanced case notions to reduce object graph complexity and improve scalability
- Approximation methods for the EMD to handle large-scale logs
- Extension to additional analysis tasks beyond clustering

## References

- Hildebrand, J. S., van Detten, J. N., & Leemans, S. J. J. (2025). *A Distance Metric for Object-Centric Process Mining*. ICPM 2025 Workshops, Springer LNBIP.
- Ghahfarokhi et al. (2023). Clustering object-centric event logs. DATA, SCITEPRESS.
- Faria Junior et al. Clustering analysis and frequent pattern mining for process profile analysis. ICPM Workshops, LNBIP.
- Jalali, A. (2022). Object type clustering using Markov directly-follow multigraph. IEEE Access.

## Key Data

- G = (Θ, E) is an undirected graph, representing the relations between objects
- i=1 δdi where n is the number of related objects and δ ∈ (0, 1) is a parameter
- i=1 deg(oi) where n is the number of related objects. Afterward, we
- norm2 = 8 and therefore Cnorm(O1) = [( O1, 0.25), (I1, 0.25),
- i
xij = IdG(o1,o2)(oj) ∀j,
- j
xij = IdG(o1,o2)(oi) ∀i.
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:23:12'
lint_warnings:
- claim: An event is published from a source only if the same behavior was observed
    for at least z − 1 other distinct cases within a time window of length Δt.
  concern: The standard z-anonymity definition requires at least z distinct cases
    (not z − 1) exhibiting the same behavior. The 'z − 1 others' phrasing would mean
    only z − 1 total cases are required, which understates the threshold by one and
    contradicts the typical formulation of group-based anonymity guarantees analogous
    to k-anonymity.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Weisenseel et al - Filtering
    at the Edge Exploring the Privacy-Utility Trade-Off.pdf
  hash: 0e20a3d85e9a01d68c3e907f65d851e320f5f9900f6abd0706fa24d5e80a00ee
  ingested: '2026-07-14T07:23:12'
  size: 574104
  truncated: true
status: active
tags:
- privacy
- process mining
- distributed filtering
- z-anonymity
- edge computing
- re-identification
- utility trade-off
- event logs
- k-anonymity
- differential privacy
title: Z-Anonymity Edge Filtering for Privacy-Preserving Process Mining
type: concept
---

# Z-Anonymity Edge Filtering for Privacy-Preserving Process Mining

This page covers a distributed data filtering approach for privacy-aware [[process-mining-data-science-in-action|process mining]], proposed by Maximilian Weisenseel, Fabian Sandkuhl, Florian Tschorsch (TU Dresden), Henrik Kirchmann, and Matthias Weidlich (Humboldt-Universität zu Berlin). The work was accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

Process mining applications increasingly extend beyond traditional centralized enterprise systems to distributed environments where event data is sensed close to process stakeholders and processed continuously for online process control. In such settings, privacy risks are heightened: individuals may be re-identified based on their behavioral characteristics through linkage with auxiliary data held by an adversary.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:27-38]

Existing privacy-preserving process mining techniques — including group-based guarantees (k-anonymity, t-closeness, l-diversity) and differential privacy — typically assume event data is available at a single central location. They also induce a privacy-utility trade-off: stronger privacy guarantees reduce the accuracy or certainty of process mining results.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:42-46]

The key insight motivating this work is that process event data often contains outliers and infrequent behavior that is routinely removed during data pre-processing regardless of privacy concerns, because most analysis techniques focus on behavior that holds for the majority of process executions. Filtering rare behavior at the edge therefore need not drastically reduce analytical utility, while simultaneously providing meaningful privacy guarantees.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:47-62]

## Approach: Filtering at the Edge

The proposed approach filters event streams **directly at distributed event sources** (the "edge") before data is transmitted to a central analysis location. This realizes two fundamental privacy design strategies:

- **Minimization**: Only filtered (non-rare) data propagates to the central analyzer.
- **Separation**: Outlying or rare behavior remains confined to the source where it was recorded.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:58-62]

### Z-Anonymity

The core privacy mechanism is **z-anonymity**, adapted from network data stream anonymization. An event is published from a source only if the same behavior was observed for at least *z − 1* other distinct cases within a time window of length Δt. Formally, for an event stream *S*:

- Events are tuples *e = (a, c, t, d)* over activities *A*, case IDs *C*, timestamps *T*, and payload data *D*.
- Behavioral predicates *β(E)* capture relevant behavioral features: single activity occurrences, conditioned activity occurrences (with specific payload), or sequences of activities (directly-follows n-grams of length 1, 2, or 3).
- **zanon(z, S)**: publishes event *e* only if at least *z* distinct cases (including *e*'s case) exhibit the same behavior within the time window Δt ending at *e*'s timestamp.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:63-71]

### Explicit Z-Anonymity

**Explicit z-anonymity (ezanon)** extends standard z-anonymity: when *z* distinct cases exhibit the same behavior within the time window, *all* events from *all z* contributing cases are published — not just those at or above the threshold. This makes the anonymity set explicit, releasing more data (higher utility) at the cost of slightly weaker re-identification protection compared to standard z-anonymity.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:67-74]

## Behavioral Predicates

Three notions of behavior are formalized:

1. **Activity occurrences** (1-grams): *βa(E)* — presence of a specific activity *a*.
2. **Conditioned activity occurrences**: *βa,d(E)* — activity *a* with specific payload value *d* (e.g., long duration, specific resource).
3. **Sequences of activities** (n-grams): *β⟨a1,...,an⟩(E)* — ordered sequence of activities occurring in direct succession.

Finer-grained behavioral definitions (longer n-grams) are harder to satisfy for the anonymity quota, resulting in greater information loss but potentially stronger privacy.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:63-74]

## Empirical Evaluation

### Datasets

Four real-world event logs were used, simulated as distributed streams by partitioning on organizational group or resource attributes:
- **Sepsis** event log
- **Environmental Permit** log (WABO, CoSeLoG project)
- **BPIC 2012 O** log
- **BPIC 2020 Prepaid Travel Costs (PTC)** log^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:75-82]

### Metrics

| Metric | Description |
|---|---|
| Ratio of Remaining Events (RRE) | Fraction of events retained after filtering |
| Ratio of Remaining Traces (RRT) | Fraction of traces retained |
| Ratio of Remaining Directly-Follows Relations (RDF) | Fraction of directly-follows pairs preserved |
| Fitness | Token-based replay fitness of anonymized log against model discovered from original log (Inductive Miner) |
| Re-identification Protection (A* Projection) | Complement of fraction of uniquely distinguishable traces based on sampled activity-timestamp patterns |

### Key Findings

- **Non-linear privacy-utility trade-off**: Increasing *z* raises re-identification protection but reduces retained events and traces non-linearly. For some datasets and configurations, meaningful privacy gains are achievable with minimal utility loss.
- **Dataset dependence**: The BPIC 2020 PTC log retains ~80% of events at *z = 5* (1-grams) while the Environmental Permit log loses ~80% of events at the same setting. Logs with more concurrent, repetitive behavior tolerate higher *z* values better.
- **N-gram size effect**: 2-gram and 3-gram behavioral definitions cause substantially more information loss than 1-grams, as longer sequences are rarer and harder to anonymize.
- **Z-anonymity vs. explicit z-anonymity**: Standard z-anonymity suppresses more events (lower utility) but provides stronger re-identification protection. Explicit z-anonymity retains more data with slightly weaker protection.
- **Favorable trade-off regions**: For the BPIC 2012 O log (and to a lesser degree Sepsis), privacy guarantees can be strengthened without significant utility degradation, suggesting Pareto-optimal operating points exist.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:75-82]

## Relation to Existing Privacy Techniques

The approach belongs to the family of **group-based privacy guarantees** for process mining, alongside k-anonymity, t-closeness, l-diversity, and differential privacy adaptations. Key distinctions:

- Unlike existing techniques that sanitize a centrally available event log, this approach operates on **distributed streaming data at the source**.
- Z-anonymity has been shown to provide k-anonymity with a desired probability.
- Data suppression (the transformation used here) can be complemented by aggregation (e.g., merging traces) or generalization (e.g., abstracting activities) in future extensions.
- Privacy risks from **continuous data release** (correspondence attacks, pattern-sensitive suppression) are identified as important future directions.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:42-46]

## Future Directions

- Predicting resulting utility for a given privacy guarantee and dataset characteristics.
- Studying the effect of z-anonymity on precision, generality, and simplicity of discovered process models.
- Systematic exploration of the temporal dimension (time window Δt) in relation to *z*.
- Achieving Pareto optimality for privacy and utility in specific deployment settings.
- Incorporating pattern-specific suppression for known sensitive behavioral patterns.^[Weisenseel et al - Filtering at the Edge Exploring the Privacy-Utility Trade-Off.pdf:75-82]

## References

- Weisenseel, M., Sandkuhl, F., Kirchmann, H., Weidlich, M., Tschorsch, F.: *Filtering at the Edge: Exploring the Privacy-Utility Trade-Off*. ICPM 2025 Workshops, Springer LNBIP (2025).
- Jha, N., Favale, T., Vassio, L., Trevisan, M., Mellia, M.: *z-anonymity: Zero-delay anonymization for data streams*. IEEE BigData 2020.
- Fahrenkrog-Petersen, S.A., van der Aa, H., Weidlich, M.: *Optimal event log sanitization for privacy-preserving process mining*. DKE 145 (2023).

## Key Data

- z = 3 and ∆t = 4. At time point T1, the square activity is performed in the
- E = {e} ∧ e(A) =a
- E = {e} ∧ e(A) =a ∧ e(D) =d
- E = {e1, . . . , en} ∧
- RDF =
( |DF(L)∩DF(L′)|
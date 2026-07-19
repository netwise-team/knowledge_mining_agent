---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:47:53'
lint_warnings:
- claim: Globally, roughly one-third of all food produced for human consumption goes
    to waste — over a billion tons per year.
  concern: The UN FAO estimates approximately 1.3 billion tonnes of food is wasted
    per year, which is consistent with 'over a billion tons,' but global food production
    is roughly 9-10 billion tonnes annually, meaning one-third would be closer to
    3 billion tonnes. The two figures (one-third and over a billion tons) are inconsistent
    with each other — one-third of global food production would be far more than one
    billion tons.
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Kalenkova et al - Discovering
    and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf
  hash: dc5a34f02d5bdd5f2ac98fa4579e7a0263a298e67a8d4bf9bc0799fda6f948fa
  ingested: '2026-07-14T07:47:53'
  size: 676449
  truncated: true
status: active
tags:
- food waste reduction
- process mining
- stochastic process discovery
- grocery retail
- supply chain optimization
- circular economy
- what-if analysis
- sustainability
- sales data
- object-centric
title: Stochastic Process Mining for Food Retail Waste Reduction
type: technology
---

# Stochastic Process Mining for Food Retail Waste Reduction

This page covers a novel methodology that integrates [[object-centric-distance-metric|Object-Centric Process Mining (OCPM)]] with stochastic process discovery and analysis to model grocery store dynamics and support food waste reduction strategies. The approach was introduced by Anna Kalenkova, Lu Xia (University of Adelaide), and Dirk Neumann (Albert-Ludwigs-University of Freiburg) in a paper accepted at the ICPM 2025 Workshops (Springer LNBIP series).

## Motivation

Globally, roughly one-third of all food produced for human consumption goes to waste — over a billion tons per year. Food waste occurs across the supply chain: during harvest, processing, and at the consumer/retail level due to oversupply. Reducing food waste aligns with circular economy principles, particularly the concept of *narrowing* material loops by optimizing logistics so that only the amount of food likely to be sold is purchased.^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:24-43]

[[sustainability-aware-process-mining|Sustainability-aware process mining]] has been identified as a promising tool for evidence-based analysis of such challenges. However, prior to this work, no specific process mining technique had been proposed specifically for food waste reduction. This paper addresses that gap by combining OCPM with stochastic process discovery.^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:44-57]

## Background Concepts

### Object-Centric Event Logs in Retail

Retail transaction data — including product identifiers, client identifiers, quantities, prices, and timestamps — can be represented as an [[object-centric-distance-metric|object-centric event log]] (OCEL). Formally, an event log is defined as a tuple L = (E, O, f_o, f_a, f_t), where:
- E is a set of events (transactions)
- O is a set of objects (products, clients)
- f_o maps events to subsets of objects
- f_a assigns attribute values (e.g., quantity, price) to events
- f_t assigns timestamps to events

The approach focuses on products as the primary objects of analysis.

### Continuous-Time Markov Chains (CTMCs)

The core process model used is a **finite-state continuous-time Markov chain (CTMC)**, defined as a pair CTMC = (λ, Q), where:
- λ is an initial state probability vector over states S = {0, 1, ..., k} (representing product quantity on shelves, from 0 to maximum capacity k)
- Q is a rate matrix where off-diagonal entries q_{i,j} ≥ 0 represent transition rates between states, and diagonal entries ensure rows sum to zero

At each moment, the process occupies one state. Transitions occur with exponentially distributed holding times. An **irreducible** CTMC is one where every state is reachable from every other state — a property important for steady-state analysis.

## Methodology

### Step 1: Mining Customer Purchasing Behavior (Algorithm 1)

For each product, the event log is filtered to extract a product-specific sublog. A CTMC is then discovered from this sublog:

1. States S = {0, ..., k} represent the number of product units on the shelf (0 = empty, k = full capacity).
2. The initial state probability vector λ is set to reflect the known starting quantity.
3. For each distinct purchase quantity Q observed in the data, events are ordered by timestamp and inter-event time intervals are computed.
4. The mean interval µ'_Q is calculated, and transition rates q_{i, i-Q} = 1/µ'_Q are set for all states i where Q ≤ i ≤ k (representing purchases of Q units reducing shelf quantity).
5. Undefined off-diagonal entries are set to 0; diagonal entries are set to ensure row sums equal zero.

The resulting CTMC models only customer purchasing behavior (forward/downward transitions in state space).

### Step 2: Enhancing with Supply Transitions

The discovered purchasing model is extended with **backward transitions** representing supply/restocking events. If a product is supplied in batches of Q_s units at rate q_s, backward transitions connect state i to state i + Q_s for all i where i + Q_s ≤ k.^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:11-20]

**Irreducibility Theorem:** If products are sold in quantities that include 1 (true for nearly all products in real data), then any supply strategy adding backward transitions between reachable states without exceeding capacity results in an irreducible CTMC. This is proven by showing that the maximum-capacity state k is reachable from any state via supply transitions, and any lower state is reachable from k via unit-purchase transitions.

### Step 3: Steady-State Analysis and What-If Evaluation

For an irreducible CTMC, **steady-state probabilities** π = (π_0, ..., π_k) are computed by solving the global balance equation πQ = 0 subject to Σπ_i = 1. These probabilities represent the long-run fraction of time the system spends with each quantity of product on the shelf.

Steady-state distributions enable:
- **Undersupply assessment:** Probability of being in low-stock states (e.g., states 0–3)
- **Oversupply/waste assessment:** Expected surplus above a waste threshold (e.g., quantities > 70 units)
- **What-if analysis:** Comparing different supply rates (e.g., 0.25, 0.30, 0.35, 0.40 per hour) to identify the optimal balance between food waste and product availability^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:11-20]

## Case Study

The approach was implemented and tested on a real-world grocery store dataset (Kaggle) containing 7,829 transactions across 300 unique products. Key findings:

- Nearly all products (292 of 300) had at least one transaction with quantity = 1, enabling irreducible CTMC construction.
- For a representative fruit product (purchased in quantities 1–4, capacity = 100, batch size = 10), steady-state analysis across four supply rates revealed a clear trade-off:
  - Higher supply rates reduce undersupply probability (from 18.67% at rate 0.25 to 0.31% at rate 0.40)
  - Higher supply rates increase expected surplus/waste (from 1.02 to 12.10 units above a threshold of 70)
  - Expected shelf quantities ranged from 27.77 to 77.31 units across the four scenarios^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:11-20]

The framework provides a quantitative basis for selecting supply strategies that minimize food waste while avoiding stockouts.

## Relationship to Broader Process Mining Research

This work sits at the intersection of several active research areas:

- **[[sustainability-aware-process-mining|Sustainability-aware process mining]]:** Directly addresses food waste as a sustainability challenge using process mining techniques.
- **[[object-centric-distance-metric|Object-Centric Process Mining]]:** Uses OCEL-style event logs with products and clients as objects; connects to the broader OCPM research agenda including stochastic OCPM.
- **[[streaming-process-mining-event-streams|Streaming process mining]]:** Retail transaction data shares characteristics with continuous event streams from operational systems.
- **Stochastic process discovery:** Extends prior work on discovering stochastic Petri nets and stochastic directly-follows models by applying CTMC discovery to object-centric retail data.^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:87-93]

## Future Directions

The authors identify several planned extensions:
1. Optimization of supply processes across all products simultaneously (recognizing that supply rates are often synchronized across products)
2. Explicit incorporation of food waste states into the CTMC model, linked to product quantity and shelf time
3. Generalization to non-exponential (semi-Markov) time distributions
4. Incorporation of financial factors and sustainable supply strategy parameters

## Implementation

The implementation is publicly available at: https://github.com/akalenkova/foodwaste

## Key Data

- CTMC = (λ, Q), where:
- s1 = i, sm = j, and qsl,sl+1 is positive for all1 ≤ l < m.
- L = (E, O, fo, fa, ft) is filtered, and a sublog for each product is extracted.
- pj = 0if j ̸= i, and pi = 1.
- Q = {e′ ∈ E′ | f ′
- Q = [f ′
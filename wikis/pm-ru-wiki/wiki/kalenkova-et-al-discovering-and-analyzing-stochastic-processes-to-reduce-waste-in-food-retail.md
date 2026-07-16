---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:48:48'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Kalenkova et al - Discovering
    and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf
  hash: dc5a34f02d5bdd5f2ac98fa4579e7a0263a298e67a8d4bf9bc0799fda6f948fa
  ingested: '2026-07-14T20:48:48'
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
title: Kalenkova Et Al   Discovering And Analyzing Stochastic Processes To Reduce
  Waste In Food Retail
type: concept
---

# Kalenkova Et Al   Discovering And Analyzing Stochastic Processes To Reduce Waste In Food Retail

Discovering and Analyzing Stochastic Processes
to Reduce Waste in Food Retail ⋆
Anna Kalenkova1[0000−0002−5088−7602], Lu Xia1[0009−0000−0979−8053],
Dirk Neumann2[0000−0003−2178−3705]
1 School of Computer and Mathematical Sciences,
The University of Adelaide, Australia
{anna.kalenkova@,lu.xia@student.}adelaide.edu.au
2 Information Systems Research,
Albert-Ludwigs-University of Freiburg, Germany
dirk.neumann@is.uni-freiburg.de
Abstract. This paper proposes a novel method for analyzing food retail
processes with a focus on reducing food waste. The approach integrates
object-centric process mining (OCPM) with stochastic process discovery
and analysis. First, a stochastic process in the form of a continuous-time
Markov chain is discovered from grocery store sales data. This model
is then extended with supply activities. Finally, a what-if analysis is
conducted to evaluate how the quantity of products in the store evolves
over time. This enables the identification of an optimal balance between
customer purchasing behavior and supply strategies, helping to prevent
both food waste due to oversupply and product shortages.
Keywords: Food Waste Reduction· Grocery Store Sales Data· Object-
Centric Process Mining· Stochastic Process Discovery
1 Introduction
Globally, it is estimated that roughly one-third of all food produced for human
consumption goes to waste [11]. This staggering figure represents more than
a billion tons of food lost every year, exposing the inefficiencies of our current
food system. Such waste occurs at various stages along the food life cycle: during
harvest (due to poor storage or transport), in processing (where food may not
meet quality standards), and at the consumer level (where oversupply may lead
to unnecessary disposal). Food waste is a significant sustainability challenge,
contributing to the growing pressures on environmental and social systems. ^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:24-31]
Sustainability is achieved through the implementation ofcircular economy
principles, which aim to minimize waste, reduce resource consumption, and pro-
mote regenerative systems. In [13], circular economy is defined as "a regenera-
tive system in which resource input and waste, emission, and energy leakage are
minimized by slowing, closing, and narrowing material and energy loops". While
⋆ The authors thank the support from Freiburg - Adelaide Partnership Fund.
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
2 A. Kalenkova et al.
slowing and closing food retail loops refer to extending product use or enabling
recycling and donations to charities, narrowing primarily involves optimizing
logistics to purchase only the amount of food likely to be sold [6]. In this paper,
we study models that support the optimization of food supply (narrowing). ^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:32-43]
Since data describing retail processes often comes as a collection of sales
events with timestamps and additional contextual information, process min-
ing [1] emerges as a promising tool for analyzing these processes. It provides a
comprehensive set of techniques [16] to support sustainability initiatives by en-
abling data-driven insights and process analysis. Although food waste reduction
has been discussed within the realm of process mining [23,29,39,41], no specific
process mining technique for food waste reduction has been proposed. ^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:44-50]
In [12], a 5 phase approach for process mining research strategy in sustain-
ability area was proposed. This paper focuses on the first three stages: modeling
(discovery), analysis, and process improvement and optimization. We introduce
methods for discovering stochastic processes that capture the dynamics of store
capacity, specifically the amount of products on the shelves. We then provide
analytical tools for performing what-if analysis on the discovered models, which
can support process optimization and food waste reduction strategies. ^[Kalenkova et al - Discovering and Analyzing Stochastic Processes to Reduce Waste in Food Retail.pdf:51-57]
The pap
---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:30:20'
lint_warnings:
- claim: Prior solutions addressed Trace-Prob on Petri nets using linear optimisation,
    probabilistic grammar sampling, or Petri net playout.
  concern: This characterization of prior work may be incomplete or imprecise, but
    more notably 'probabilistic grammar sampling' is not a well-established standard
    technique for Trace-Prob on Petri nets — this phrasing conflates grammar-based
    approaches (more associated with process trees) with Petri net methods, potentially
    misrepresenting the prior literature.
- claim: PPTs extend them with weight-based probability semantics while retaining
    translation to weighted stochastic Petri nets.
  concern: Process trees in general (not just PPTs) can be translated to Petri nets.
    Claiming this as a distinctive feature of PPTs specifically is potentially overstated,
    as the translation property belongs to the underlying process tree formalism rather
    than being something PPTs uniquely 'retain.'
orphan: true
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Burke et al - Trace Probability
    Calculation on Probabilistic Process Trees.pdf
  hash: f351a8fea52d433bcd7217ee021832a49650349fc9cec6bbb94fb9283294a71a
  ingested: '2026-07-14T07:30:20'
  size: 491327
status: active
tags:
- stochastic process mining
- trace probability
- process trees
- weighted automata
- process models
- Petri nets
- stochastic languages
- approximation bounds
- process discovery
- formal methods
title: Trace Probability Calculation on Probabilistic Process Trees
type: technology
---

# Trace Probability Calculation on Probabilistic Process Trees

Trace probability calculation on Probabilistic Process Trees (PPTs) is a core problem in **stochastic process mining** — the subfield of [[process-mining-handbook|process mining]] concerned with quantifying the likelihood of observed behaviour under a probabilistic process model. This page covers the formal framework and closed-form solutions introduced by Adam T. Burke (Queensland University of Technology), Sander J.J. Leemans (RWTH Aachen), and Moe T. Wynn (Queensland University of Technology), accepted at the ICPM 2025 Workshops.

## Motivation: The Trace-Prob Problem

Stochastic process models extend conventional process models with probability information, enabling precise descriptions of how likely any given sequence of activities (a *trace*) is under the model. The central computational challenge is the **Trace-Prob** problem: given a process model and a trace, compute the probability that the model generates that trace.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:14-16]

Trace-Prob underpins many stochastic process quality metrics — including those based on the Earth Mover's Distance — and can be embedded within stochastic discovery algorithms. Prior solutions addressed Trace-Prob on Petri nets using linear optimisation, probabilistic grammar sampling, or Petri net playout. This work provides solutions directly on two data structures heavily used in [[process-mining-handbook|process mining]]: Weighted Stochastic Finite Automata (WSFAs) and Probabilistic Process Trees (PPTs).^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:17-28]

Process trees are particularly important because they are the native output of the **Inductive Miner** family of discovery algorithms, and PPTs extend them with weight-based probability semantics while retaining translation to weighted stochastic Petri nets.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:20-28]

## Weighted Stochastic Finite Automata (WSFAs)

A **Weighted Stochastic Finite Automaton** (WSFA) is a five-tuple *(S, Act, →, s₀, sω)* where:
- *S* is a finite set of states,
- *Act ⊆ A ∪ {τ}* is the set of activities including silent transitions,
- *→ ⊂ S × Act × S → ℝ⁺* is a weight function,
- Transition probabilities are derived from weights: *P(s₁, x, s₂) = w / W_T* where *W_T* is the total outgoing weight from *s₁*,
- *s₀* is the unique initial state (no incoming arcs), *sω* is the unique terminal deadlock state.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:57-71]

Three compositional operators are defined on WSFAs:
- **Concatenation (` `)**: two automata execute serially by merging the final state of the first with the initial state of the second.
- **Union (\)**: exactly one operand executes, chosen by weighted probability; initial and final states of operands are merged.
- **Race (||)**: two automata progress in parallel; at each step the next transition is chosen by weighted race across all enabled arcs, producing a Cartesian product state space.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:106-108]

All three operators are associative; union and race are also commutative, enabling extension to *n*-ary operators by composition.

## Probabilistic Process Trees (PPTs)

PPTs extend standard process trees (as used in the Inductive Miner) with weight annotations on each node. Each node *x: w* carries a weight *w ∈ ℝ⁺*. The operators are:

| Operator | Symbol | Semantics |
|---|---|---|
| Sequence | →  | Children execute serially (WSFA concatenation) |
| Choice | × | Exactly one child executes (WSFA union), weighted by child weights |
| Concurrency | ∧ | Children execute in parallel (WSFA race) |
| Fixed loop | ⟳ⁿ | Body executes exactly *m* times (sequence of *m* copies) |
| Probabilistic loop | ⟳ᵖ | Body repeats geometrically with parameter *ρ* |

The semantics function *wa: PPT → WSFA* recursively translates any PPT into an equivalent WSFA, providing a formal grounding for probability calculations.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:17-24]

## Trace Probability on WSFAs

The function *π^ϵ_st(σ, E, s, ϵ, p, seen)* computes trace probability for trace *σ* starting from state *s* in WSFA *E*, within approximation bound *ϵ*:

- For a non-empty trace *⟨a⟩ + σ*: sum over activity arcs matching *a* (weighted probability × recursive call on suffix) plus, if *p > ϵ*, sum over silent arcs (weighted probability × recursive call on full trace).
- For the empty trace at terminal state *sω*: return 1.
- For the empty trace at a non-terminal state: follow silent arcs if *p > ϵ*, else return 0.
- **Silent loop handling**: the function tracks visited states (*seen*) and cumulative probability (*p*). When entering a new state, the suppression threshold *ϵ* is scaled down proportionally; when revisiting a state, *ϵ* is unchanged. This ensures that in a silent loop, cumulative probability monotonically decreases while the threshold stays fixed, guaranteeing termination.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:7-11]

The overall trace probability is *π^w_ϵ(σ, E, ϵ) = π^ϵ_st(σ, E, s₀, ϵ, 1, ∅)*.

## Trace Probability on PPTs

The function *πϵ(σ, u, ϵ)* computes trace probability directly on PPT nodes by structural recursion:

- **Leaf nodes**: probability 1 if the trace exactly matches the leaf activity (or empty trace for *τ*), else 0.
- **Choice (×)**: weighted sum over children — *πϵ(σ, ×(x₁:w₁,...), ϵ) = (1/W_T) Σ wᵢ · πϵ(σ, xᵢ:wᵢ, wᵢ·ϵ/W_T)*.
- **Concurrency (∧)**: delegates to the WSFA calculation via *wa*, due to state-space explosion from interleaving.
- **Sequence (→)**: considers all two-way splits of the input trace, summing products of prefix and suffix probabilities across children.
- **Fixed loop (⟳ⁿ)**: treated as a sequence of *m* copies of the body.
- **Probabilistic loop (⟳ᵖ)**: approximated by loop unrolling. The loop executes *i* times with probability *(1/ρ)·((ρ−1)/ρ)ⁱ*. Choose *k* such that *((ρ−1)/ρ)^(k+1) / (1 − (ρ−1)/ρ) ≤ ϵ*, then sum the first *k+1* terms. The approximation error is bounded by *ϵ*.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:7-11]

### Approximation Bound Propagation

A key property is that the approximation bound does not increase when a subtree is embedded in a larger tree: conditional probability multiplies by a value ≤ 1, so the bound *ϵ* is preserved throughout the recursion.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:22-24]

## Complexity

The trace probability calculation builds a conceptual *path tree* of possible execution paths. Worst-case time complexity is **O(|σ|² · nₜ)** where *nₜ* is the size of the path tree. For concurrent subtrees, the state space is exponential in the number of concurrent children, giving an overall bound of **O(n · k · 2ᵐ)** where *n* is the number of PPT nodes, *k* is the loop unrolling bound, and *m* is the size of the largest concurrent subtree.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:7-11]

In practice, complexity is sensitive to model quality: precise models with small concurrent regions are significantly cheaper to evaluate than imprecise flower-model-style structures.

## Relation to Stochastic Process Quality Metrics

A stochastic language maps traces to probabilities and is potentially infinite for models with loops. Stochastic quality metrics — including Earth Mover's Stochastic Conformance — require finite approximations of stochastic languages. The bounded approximation approach here provides a principled, quantitative criterion for excluding traces below a probability threshold *ϵ*, enabling practical computation of stochastic languages for use in [[data-quality-sensitivity-process-discovery|process model quality assessment]] and discovery.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:22-24]

## Related Work

- **Trace-Prob on Petri nets**: Leemans et al. (2022) use linear optimisation on labelled Petri nets; Burke et al. (2021) use Petri net playout with genetic miners.
- **Earth Mover's Stochastic Conformance**: Leemans, van der Aalst et al. (2021) defined Trace-Prob as a prerequisite for this metric.
- **Alternative PPT extension**: Horváth, Ballarini & Cry (2024) associate nodes with fixed probabilities rather than weights, deliberately avoiding Petri net translation, and include an approximate trace probability calculation bounded by maximum loop length rather than probability threshold.
- **Grammar-based approaches**: Watanabe et al. (2022) use probabilistic grammar sampling for conformance checking.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:25-28]

The PPT framework retains translation to weighted stochastic Petri nets, which is a deliberate design choice to maintain interoperability with the broader [[process-mining-handbook|process mining]] ecosystem.^[Burke et al - Trace Probability Calculation on Probabilistic Process Trees.pdf:25-28]
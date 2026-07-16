---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:12:33'
lint_warnings:
- claim: Attack Flow is a domain-specific language built on top of STIX (Structured
    Threat Information Expression)
  concern: Attack Flow is developed by MITRE and uses STIX as a serialization/exchange
    format, but it is not accurately described as 'built on top of STIX.' It is a
    separate language/schema that can be expressed in STIX, not a direct extension
    or superset of STIX.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Rodríguez et al - Process
    mining-driven automated generation of threat intelligence artifacts.pdf
  hash: 59cfdbb7016f07c13519dded4a4644c120f68ac2a443a28ae1c3fdf3d452083c
  ingested: '2026-07-14T07:12:33'
  size: 534436
  truncated: true
status: active
tags:
- process mining
- cybersecurity
- threat intelligence
- attacker behavior
- TTPs
- ransomware
- automation
- behavioral analysis
- threat modeling
- domain-specific language
title: 'Process Mining for Cybersecurity: Attack Flow Generation'
type: technology
---

# Process Mining for Cybersecurity: Attack Flow Generation

Process mining (PM) has emerged as a valuable technique for uncovering behavioral patterns in attack traces extracted from cybersecurity system logs. Rather than analyzing isolated events, PM provides a comprehensive view of attack processes as end-to-end sequences. A key challenge, however, is that the notation used in PM is not standard in the cybersecurity community. This page covers a method proposed by Rodríguez, Betarte, and Calegari (Universidad de la República / Universidad ORT Uruguay) — accepted at the ICPM 2025 Workshops — for automatically generating **Attack Flow** models from PM-discovered process models.^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:8-23]

## Background: PM-Based Attacker Profiling

The authors' prior work established a four-phase PM-based method for attacker profiling:

1. **Enactment** — attack strategies are executed in a controlled or real environment.
2. **Extraction** — system logs are processed to create event logs labeled with the **MITRE ATT&CK** taxonomy (tactics, techniques, and procedures — TTPs).
3. **Discovery** — process discovery algorithms (specifically the **Inductive Miner**) are applied to produce process models of attacker behavior.
4. **Analysis** — cybersecurity experts analyze the resulting models.

^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:71-76]

The MITRE ATT&CK framework categorizes adversarial activities: *tactics* are strategic goals, *techniques* are methods to achieve them, and *procedures* are real-world implementations. By mapping low-level system events to ATT&CK labels, the method raises the abstraction level for attacker profiling. Experiments used the PWNJUTSU dataset (human attackers) and a WannaCry ransomware case study.^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:43-51]

The Inductive Miner algorithm is favored in this context due to favorable results in cybersecurity settings. It produces **Process Trees** — abstract representations of block-structured workflow nets — which are then used as the basis for Attack Flow translation.

## The Attack Flow Language

**Attack Flow** is a domain-specific language built on top of **STIX** (Structured Threat Information Expression) for formalizing how attackers combine and sequence offensive techniques. Its key elements are:^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:99-104]

| Element | Description |
|---|---|
| Attack Flow | Represents the general flow of the attack |
| Attack Action | A specific action within attacker behavior (often mapped to ATT&CK techniques) |
| Attack Asset | An object targeted or affected by an action |
| Attack Operator | Combines multiple attack paths using Boolean logic (AND/OR) |
| Attack Condition | A state or outcome resulting from an action; enables flow splits |

OR operators require one path to be active; AND operators require all paths. Conditions allow bifurcation based on success/failure and can contextualize actions without implying a decision.^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:109-116]

## Mapping Control-Flow Patterns to Attack Flow

The translation from PM process models to Attack Flow models is grounded in **control-flow patterns** — abstract descriptions of process control-flow behavior. The authors focus on patterns supported by the Inductive Miner:^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:58-61]

### Basic Patterns

- **Sequence**: A task proceeds only after a preceding task completes. In Attack Flow, this is represented as directed connections between actions with arrows indicating transition.
- **Parallel Split**: A branch diverges into two or more concurrent branches. In Attack Flow, multiple arrows originate from an initial action, leading to parallel attack paths.
- **Synchronization**: Two or more branches converge into one, requiring all preceding branches to complete. Represented in Attack Flow using the AND operator.
- **Exclusive Choice**: A single path branches into alternatives, with control transferred to only one. Modeled in Attack Flow using Condition objects with true/false branches — useful for representing attacker reactions to success or failure.
- **Simple Merge**: Two or more branches merge into one; only one incoming branch needs to be active. Since Attack Flow lacks an explicit exclusive-OR convergence operator, the OR operator (preceded by a Condition object) is used.

### Advanced Patterns

- **Multi-Choice**: Execution flow is selectively split into multiple concurrent threads based on a decision mechanism. Modeled using independent Condition objects per branch.
- **Structured Synchronizing Merge**: Convergence of branches previously forked by a Multi-Choice. Requires synchronization of all previously selected paths; represented with AND operators.
- **Structured Loop**: Repeated execution of a process or sub-process with a pre- or post-test control condition. Infrequent in standard Attack Flow examples but observed in attacker behavior models, particularly for human attackers using trial-and-error cycles.
- **Implicit Termination**: Process instance ends when no pending work items remain. Expressed in Attack Flow using a Condition object to delineate the termination criterion for malicious activity.

## Case Study: WannaCry Ransomware

WannaCry is a ransomware first identified in a worldwide attack in May 2017. The authors registered five distinct instances of WannaCry execution and applied the Inductive Miner to produce a Petri net capturing seven distinct activities aligned with ATT&CK tactics:^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:83-89]

- **Persistence** (T1543): Creates malicious service `mssecsvc2.0`
- **Impact** (T1486, T1490, T1489): Encrypts files, disables OS recovery, kills services
- **Command and Control** (T1573): Uses Tor for C2 traffic
- **Lateral Movement** (T1210, T1570, T1563): Exploits SMBv1, copies itself to remote systems
- **Discovery** (T1083, T1120, T1018, T1016): Searches files, scans network, identifies drives
- **Defense Evasion** (T1222): Hides files and grants full access
- **Execution** (T1047): Uses `wmic` to delete shadow copies

The discovered Petri net shows expected ransomware behavior: first disabling defenses, then executing persistence, privilege escalation, lateral movement, and impact in a continuous cycle — reflecting the inherent looping nature of ransomware (searching for new files to encrypt, reconnecting to C2).

The Attack Flow model derived from this Petri net begins with an "Infected Machine" condition representing initial compromise. Tactical actions are aligned with ATT&CK tactics. AND connectors express simultaneous conditions; OR connectors indicate alternative routes. The full model and Python prototype (using **PM4Py** and **Stix2** libraries) are available at the authors' GitLab repository.

## Limitations and Future Work

- **Data perspective**: Current PM models focus only on control flow, neglecting data aspects. Preconditions and postconditions must currently be provided manually by cybersecurity analysts. The authors suggest exploring [[object-centric-distance-metric|object-centric process mining]] to partially derive conditions from object behavior.
- **Asset integration**: Automatically including Attack Asset objects requires detailed analysis of attack execution data — challenging due to information extraction, semantic correlation, and log contextualization difficulties.
- **Dataset scarcity**: A consistent obstacle is the lack of suitable cybersecurity datasets with usable system logs for process mining.
- **Decision mining**: Exclusive-Choice and Multi-Choice patterns appear frequently in attacker models, but the criteria for path selection are not captured. Decision mining is proposed as a future strategy to infer logical rules from data.
- **Evaluation**: Further quantitative and qualitative evaluation is needed to validate transformation correctness and model usefulness.

## Relation to Other Work

Related approaches include:
- Konsta et al. (2025): PM-based method for generating **attack trees** (differs in using ATT&CK taxonomy and targeting Attack Flow).
- Cheh et al. (2025): Automated framework for modeling attack paths with Attack Flow, highlighting challenges of manual effort.
- Attack Flow 3.0.0: Includes a defensive posture usage guide using Windows event logs (Sysmon), but relies on manual construction.

This work is part of the broader [[process-mining-handbook|process mining]] research landscape and was accepted at the ICPM 2025 Workshops, to appear in the Springer LNBIP series.^[Rodríguez et al - Process mining-driven automated generation of threat intelligence artifacts.pdf:39-39]
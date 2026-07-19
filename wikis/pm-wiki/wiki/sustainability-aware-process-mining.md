---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:00:59'
lint_warnings:
- claim: Rubio, Delgado, and García (ICPM 2025 Workshops)
  concern: Citing a 2025 workshop paper as an established source is problematic for
    a wiki claiming to document well-established facts — this is a future-dated or
    at best very recent unpublished/forthcoming work, and its findings cannot yet
    be considered verified or peer-reviewed in the traditional sense, making it an
    unreliable foundation for encyclopedic claims.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Rubio et al - Enabling Sustainability-Aware
    Process Mining A Systematic approach for Measurement and Registration of Sustainability
    Data.pdf
  hash: 001987af8ae27c46ea760e6c6aa83e3c96c556d6d8817d9749a0f45291f1e8a6
  ingested: '2026-07-14T07:00:59'
  size: 780068
status: active
tags:
- process mining
- sustainability
- business processes
- Green BPM
- event logs
- XES
- sustainability measures
- environmental impact
- measurement taxonomy
- ICPM 2025
title: Sustainability-Aware Process Mining
type: concept
---

# Sustainability-Aware Process Mining

Sustainability-aware process mining is an emerging research area that integrates environmental, economic, and social sustainability measures into [[coordinated-projections-multi-faceted-process-exploration|process mining]] workflows, enabling organizations to conduct evidence-based analysis of the sustainability impact of their business processes. It sits at the intersection of Green Business Process Management (Green BPM) and process mining, using execution data captured in event logs to quantify and monitor sustainability dimensions.

## Motivation

Organizations are increasingly concerned with the environmental impact of their daily operations and seek to incorporate sustainable practices into their business processes. While sustainability measures for business processes have been proposed in the literature, few approaches address how to systematically capture, derive, and register sustainability data from process execution in a form suitable for process mining analysis. Existing proposals typically embed resulting values as event log attributes without clearly explaining how values are registered or calculated, and without distinguishing between estimated and actually measured data — undermining transparency in a critical domain. ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:47-59]

Process mining serves as a key enabler for sustainability assessment by providing the basis for evidence-based process analysis and improvement, linking sustainability indicators directly to process activities and cases. ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:49-51]

## Conceptual Framework

The approach proposed by Rubio, Delgado, and García (ICPM 2025 Workshops) defines a systematic method comprising:

- **Specific sustainability measures** with concrete formulae and required parameters
- **A method for registering and capturing sustainability values** in event logs via a defined XES extension
- **A measurement taxonomy** that explicitly differentiates between estimated and measured values ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:60-64]

The framework focuses on organizational business processes whose execution is supported by information systems, including traditional systems and Business Process Management Systems (BPMS). ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:115-117]

## System Architecture

The systematic approach includes the following components:

1. **Information system / BPMS**: Supports business process execution and stores sustainability parameters in its database.
2. **Sustainability data registration tools**: Invoked by tasks during execution to capture parameter values and optionally calculated measure results.
3. **Sustainability calculator**: A microservices-based component with a REST API that calculates sustainability measures at runtime or offline, either using own formulae or by invoking existing online calculators.
4. **Log extraction component**: Collects process execution data and generates XES event logs enriched with sustainability attributes.
5. **Log enrichment component**: Post-processes generated event logs to add missing measure result values by invoking the sustainability calculator offline.
6. **Sustainability dashboard**: Visualizes sustainability measures data alongside process mining results, offering breakdowns by category and measurement type. ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:110-120]

## Sustainability Measures and Categories

Sustainability measures are organized along the three dimensions of the UN Sustainable Development Goals (SDGs): environmental, economic, and social. The environmental dimension — the primary focus — includes the following categories:

- **Energy**: Energy consumed (J), energy consumed by device, energy consumed by cloud services
- **Emissions**: CO₂ emissions per km (kg)
- **Material**: Kg of paper consumed, fuel consumed per time
- **Water**: Liters of water consumed
- **Waste**: Recycled volume
- **Software**: Energy consumed per CPU usage, per software execution, per programming language ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:80-85]

Each measure is defined with its formula, required parameters (with units), and measurement type.

## Measurement Taxonomy

A key contribution is a taxonomy that differentiates sustainability measurements by their degree of empiricism:

### Instrument-based Measurement (IB)
Captures environmental data directly through instrumentation, offering the highest degree of empiricism. Includes hardware instrumentation (power meters, gas analyzers), domain-specific sensors (CO₂, particulate, noise sensors), and platform-integrated monitoring. Precise and traceable but often intrusive, costly, and less scalable.

### Empirical Model-based Estimation (EE)
Infers impact from operational data (telemetry, logs) combined with empirically validated models or conversion factors. Examples include utilization-based models using CPU/memory traces, empirically calibrated analytical models, and hybrid approaches multiplying observed activity by emission factors (e.g., gCO₂/kWh). Balances accuracy and feasibility but depends on robust data and calibration.

### Theoretical Model-based Estimation (TE)
Relies on static assumptions, literature-based coefficients, or expert knowledge, applied when runtime data is unavailable. Examples include fixed grid emission factors or design-time mappings embedded in process models. Lightweight and easy to apply but less reliable.

## XES Extension for Sustainability

A dedicated XES extension is defined to register sustainability data in [[event-log-extraction-clinical-narratives|event logs]]. The extension structure is:

- An **event** can include a **sustainability category** attribute (with a name and a list of sustainability measures)
- Each **sustainability measure** has a name and a list of **sustainability parameters** (name, unit, value)
- Each measure can include a **result** (name, unit, value)
- Each measure carries a **measurement type**: instrument-based, empirically estimated, or theoretically estimated ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:60-64]

This extension is designed to be translatable to object-centric event logs (OCEL 2.0). ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:100-103]

## Proof of Concept

The approach was validated using a patient transportation process (picking up patients from care homes to take them to hospital), implemented in Camunda 7 as the BPMS. Selected sustainability measures included:

| Task | Measure | Calculation Type |
|---|---|---|
| Generate patient documentation | Paper waste generated (kg) | Runtime calculator |
| Retrieve patient clinical history | Energy consumed per software execution (J) | Runtime measurement |
| Evaluate request | Energy consumed per device (J) | Post-processing calculator |
| Get optimal route | Energy consumed in cloud services | Runtime calculator |
| Update patient documentation | Energy consumed per programming language (J) | Runtime calculator |
| Complete travel data | Emissions per km (kgCO₂) | Post-processing calculator |

A purpose-built sustainability library, microservices-based calculator, and analysis dashboard were implemented in Python. The dashboard links emissions, energy, material, and software indicators to the measurement taxonomy and incorporates process mining perspectives. ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:64-68]

## Relation to Green BPM

Green BPM has emerged to provide organizations with a vision in which sustainability is a business objective. Sustainability-aware process mining operationalizes this vision by grounding sustainability assessment in actual process execution data, enabling continuous monitoring and evidence-based improvement rather than one-off assessments. ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:40-42]

## Limitations and Future Work

The authors note that measuring sustainability indicators alone does not automatically lead to meaningful improvement of a business process's environmental impact. Organizations must undertake prior stages of the process lifecycle to identify applicable measures and define corresponding improvement actions. Future work includes extending support to additional sustainability measures and translating the registration and extension method to object-centric event data. ^[Rubio et al - Enabling Sustainability-Aware Process Mining A Systematic approach for Measurement and Registration of Sustainability Data.pdf:69-74]

## Key References

- Rubio, M., Delgado, A., García, F.: *Enabling Sustainability-Aware Process Mining: A Systematic Approach for Measurement and Registration of Sustainability Data*. ICPM 2025 Workshops, Springer LNBIP.
- van der Aalst, W.M.P.: *Process Mining – Data Science in Action*, 2nd ed. Springer (2016).
- vom Brocke, J., Seidel, S., Recker, J. (eds.): *Green Business Process Management – Towards the Sustainable Enterprise*. Springer (2012).
- Graves, N., Koren, I., van der Aalst, W.M.: *Rethink Your Processes! A Review of Process Mining for Sustainability*. ICT4S 2023.
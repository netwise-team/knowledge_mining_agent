---
aliases: []
confidence: medium
created: '2026-07-16T06:50:36'
lint_warnings:
- claim: 'Published: March 16, 2026'
  concern: This date is in the future relative to any plausible knowledge cutoff,
    making it impossible to verify as a real publication. The arXiv ID format '2603.15351'
    would correspond to March 2026, which is suspicious and cannot be confirmed as
    an established fact.
orphan: true
resource: https://github.com/fit-process-mining/PMAx-evaluation
sources:
- file: https://github.com/fit-process-mining/PMAx-evaluation
  hash: 28dba1d36955ae90f32e0b8c8c606f167053067c2564d4b93f29a263a903c64c
  ingested: '2026-07-16T06:50:36'
  size: 53
status: active
tags:
- process mining
- AI agents
- LLM
- automation
- multi-agent system
- business intelligence
- event log analysis
- reproducibility
- research
- visualization
title: 'PMAx: An Agentic Framework for AI-Driven Process Mining'
type: technology
updated: '2026-07-16'
---

# PMAx: An Agentic Framework for AI-Driven Process Mining

**arXiv:** [2603.15351](https://arxiv.org/abs/2603.15351) | **Published:** March 16, 2026 | **Venue:** EMMSAD 2026 (Tool Demonstration, preprint)

**Authors:** Anton Antonov, Humam Kourani, Alessandro Berti, Gyunam Park, Wil M.P. van der Aalst

**Affiliations:** Fraunhofer Institute for Applied Information Technology FIT (Sankt Augustin) & RWTH Aachen University

## Summary

PMAx — это автономный, конфиденциальный агентный фреймворк, действующий как **виртуальный аналитик процессов**. Он соединяет бизнес-вопросы на естественном языке с точным анализом Process Mining — без отправки сырых журналов событий во внешние сервисы ИИ.

Ключевая идея: вместо того чтобы LLM напрямую рассуждал над данными событий (что приводит к галлюцинациям и утечкам приватности), PMAx заставляет LLM **писать и исполнять локальный Python-код** с использованием проверенных библиотек (PM4Py, Pandas). Вычисление и интерпретация разделены между двумя специализированными агентами.

## Problem Statement

Традиционный Process Mining требует экспертизы в:
- Специализированных языках запросов (PQL, PM4Py API)
- Инструментах Data Science
- Предметных знаниях для содержательной интерпретации

Коммерческие решения (Celonis AI Copilot, SAP Signavio, Apromore) существуют, но проприетарны и требуют отправки данных в внешние API. Существует **исследовательский пробел для открытых, прозрачных, локально развёртываемых фреймворков**.

### Ключевые вызовы

1. **Галлюцинации LLM на метриках** — LLM не могут надёжно вычислять throughput time, количество вариантов, показатели conformance; они генерируют правдоподобные, но неверные числа
2. **Конфиденциальность данных** — реальные журналы событий содержат чувствительные данные организации; передача во внешние API нарушает политики data governance
3. **Безопасность генерируемого кода** — исполнение непроверенных LLM-скриптов несёт риски безопасности

## Architecture

### Four Design Pillars

1. **Secure Data Handling** — только лёгкие структурные метаданные (имена столбцов, типы данных, примеры атрибутов) отправляются в LLM; сырые данные не покидают локальную среду
2. **Multi-Agent Workflow** (разделяй и властвуй) — два специализированных агента: **Engineer** (синтез кода) + **Analyst** (интерпретация результатов)
3. **Reliable Execution** — статический слой верификации + автономный цикл самокоррекции, захватывающий runtime-ошибки и возвращающий их агентам
4. **Open-Source & Extensible** — построен на стандартной экосистеме Python (PM4Py, Pandas); полностью инспектируем и локально развёртываем

### Engineer Node

- Специализированный LLM-агент для генерации кода
- Инициализируется с ролевым промптом ("специализированный Data Engineer")
- Получает: абстракцию схемы журнала событий, доменные знания (case ID, timestamp, activity), спецификацию разрешённого API
- Генерирует: исполняемые Python-скрипты с использованием PM4Py + Pandas + NumPy + Matplotlib/Plotly/Seaborn
- Статическая верификация кода перед исполнением (синтаксис + ограничения безопасности)

**Whitelist категорий PM4Py API:**
- `FILTERING`: filter_time_range, filter_case_performance, filter_variants, filter_activity
- `DISCOVERY`: discover_petri_net, discover_process_tree, discover_dfg, discover_bpmn
- `CONFORMANCE`: compute_fitness_token_replay, compute_precision, check_conformance
- `STATISTICS`: get_variants, get_case_duration_stats, compute_service_time, compute_waiting_time
- `VISUALIZATION`: выводы как Matplotlib/Plotly figures

### Analyst Node

- Интерпретирует артефакты, созданные Engineer (process models, таблицы, графики)
- Изолирован от технических деталей кода (изолированная история диалога)
- Генерирует комплексные отчёты, сочетающие нарративные инсайты с визуальными доказательствами
- Никогда не видит сырые данные — только артефакты и метаданные

### Collaborative Memory State

- Общее состояние между узлами Engineer и Analyst
- Реализует строгое **разделение ответственности** через изолированные истории диалогов
- Действует как фильтрованный канал, передающий только существенный межузловой контекст

## Tool Demonstration: Loan Application Process

Статья демонстрирует PMAx на **процессе рассмотрения заявок на кредит**:

**Пример запроса пользователя:** "What are the most common process variants and how do they compare in terms of cycle time?"

**Рабочий процесс PMAx:**
1. Engineer извлекает схему журнала (столбцы, типы данных)
2. Engineer генерирует Python-код для вычисления вариантов + статистики производительности через PM4Py
3. Код статически верифицируется, затем исполняется локально
4. Analyst получает выходные данные (таблицы, графики) и составляет отчёт на естественном языке
5. UI показывает панель синтеза кода в реальном времени + итоговую панель отчёта

## Implementation

- **GitHub (основной):** https://github.com/fit-process-mining/ProMoAI (реализован как расширение в ProMoAI)
- **GitHub (артефакты):** https://github.com/fit-process-mining/PMAx-evaluation
- **Язык:** Python (98%+)
- **Ключевые библиотеки:** PM4Py, Pandas, NumPy, Matplotlib, Plotly, Seaborn, Streamlit
- **AI-провайдеры:** конфигурируемые (пользователь выбирает провайдера + API-ключ при запуске)
- **Интерфейс:** разговорный UI с панелью мониторинга синтеза кода

## Related Work

PMAx строится на:
- **ProMoAI** (Kourani et al., IJCAI 2024) — генерация BPMN/Petri net из текста через LLM
- **Rebmann et al.** — систематическая оценка LLM для семантических задач (предсказание активностей, обнаружение аномалий)
- **Фреймворки для OCEL** — разговорный анализ объектно-ориентированных журналов
- **AutoGen, LIDA** — общие агентные фреймворки Data Science
- **Vu et al. (2025)** — опрос практиков, подтверждающий высокий интерес к агентному BPM

## Key Contributions

1. Новая **двухагентная архитектура** разделяющая синтез кода (Engineer) и семантическую интерпретацию (Analyst)
2. **Privacy-preserving** дизайн через метаданные-only экспозицию для LLM
3. **Статический слой верификации** для безопасности генерируемого кода
4. **Цикл самокоррекции** для автономного восстановления после ошибок
5. **Open-source** интеграция в пакет ProMoAI

## See Also

- [[promoai-pmax-ai-process-mining-suite]] — родительский инструментарий (ProMoAI + PMAx)
- [[knowledge-driven-hallucination-llm-process-modeling]] — проблема галлюцинаций, которую решает PMAx
- [[object-centric-process-mining-ai-enabler]] — смежная работа van der Aalst по LLM + PM (2025)
- [[llm-declarative-process-discovery-dcr-graphs]] — альтернативный подход LLM для Process Mining

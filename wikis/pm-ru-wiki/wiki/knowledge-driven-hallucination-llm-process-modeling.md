---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T20:26:49'
lint_warnings:
- claim: Авторы — Humam Kourani, Anton Antonov, Alessandro Berti и Wil M.P. van der
    Aalst (Fraunhofer FIT и RWTH Aachen)
  concern: Wil van der Aalst is primarily affiliated with RWTH Aachen, but attributing
    all listed authors jointly to both Fraunhofer FIT and RWTH Aachen may be an overstatement
    — individual affiliations can differ, and presenting this as a single shared affiliation
    for all authors could be inaccurate without verification of each author's specific
    institutional affiliation.
- claim: все последовательные зависимости в модели инвертированы; порядок событий
    в трассах журнала обращён
  concern: Completely inverting all sequential dependencies in a realistic business
    process model (e.g., one with parallel gateways, loops, and XOR splits) does not
    straightforwardly produce a valid Petri net or coherent process model, making
    the claim that this was done cleanly across all four processes — including complex
    ones like Internal Audit with 63 nodes — likely overstated without significant
    caveats about structural validity.
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Kourani et al - Knowledge-Driven
    Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf
  hash: c082f0fd7351eab62a3b23d5cb87777a0af65b131fd8d95ac9f3772daf272a38
  ingested: '2026-07-14T20:26:49'
  size: 625152
  truncated: true
status: active
tags:
- hallucination
- LLMs
- process modeling
- BPM
- generative AI
- trustworthy AI
- empirical study
- pre-trained knowledge
- evidence fidelity
- ICPM 2025
title: Знание-обусловленные галлюцинации LLM при моделировании процессов
type: concept
---

# Знание-обусловленные галлюцинации LLM при моделировании процессов

Знание-обусловленные галлюцинации (knowledge-driven hallucination) в больших языковых моделях (LLM) — явление, при котором модель генерирует выходные данные, противоречащие явным входным свидетельствам, поскольку её обобщённые внутренние знания, полученные в ходе предобучения, подавляют предоставленные факты. Данная проблема исследована в контексте автоматизированного моделирования бизнес-процессов — задачи, тесно связанной с [[process-mining-overview]].^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:12-31]

## Постановка проблемы

LLM широко применяются для автоматической генерации формальных моделей бизнес-процессов из текстовых описаний и журналов событий. Ключевое преимущество таких моделей — способность интерпретировать неоднозначные входные данные и восполнять пробелы на основе предобученных знаний. Однако именно эта способность порождает критический риск: когда предоставленные свидетельства противоречат «здравому смыслу» модели о типичном ходе процесса, модель может «исправить» выходные данные в соответствии со своими внутренними схемами, игнорируя реальные входные данные.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:45-52]

Многие базовые бизнес-процессы — такие как «закупка-к-оплате» (purchase-to-pay), «заказ-к-оплате» (order-to-cash) или управление инцидентами — следуют стандартизированным паттернам, хорошо представленным в обучающих корпусах LLM. Это создаёт идеальный контекст для изучения конфликта между предоставленными свидетельствами и предобученными схемами.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:64-72]

## Методология эксперимента

Авторы — Humam Kourani, Anton Antonov, Alessandro Berti и Wil M.P. van der Aalst (Fraunhofer FIT и RWTH Aachen) — разработали контролируемый эксперимент в три этапа.

### Генерация артефактов

Для четырёх бизнес-процессов из существующего бенчмарка были подготовлены стандартные артефакты: модель (M⁺), текстовое описание (D⁺) и симулированный журнал событий (L⁺). Процессы охватывали различные структуры управляющего потока:

- **Sales Order** (8 активностей, 26 узлов сети Петри)
- **Booking System** (13 активностей, 49 узлов; решения, циклы, параллелизм)
- **Complaint Handling** (9 активностей, 21 узел; решения)
- **Internal Audit** (24 активности, 63 узла; решения, циклы, параллелизм)

Для каждого процесса были созданы два набора конфликтующих артефактов:

- **Обращённые артефакты (M⁻, L⁻, D⁻)**: все последовательные зависимости в модели инвертированы; порядок событий в трассах журнала обращён; текстовое описание скорректировано соответственно.
- **Перемешанные артефакты (M∗, L∗, D∗)**: метки активностей случайным образом переставлены по структуре модели при сохранении управляющего потока; журнал и описание адаптированы аналогично.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:73-82]

### Генерация моделей с помощью LLM

Эксперимент охватывал десять LLM различных классов: command-r, gemini-2.5-flash, gemini-2.5-pro, gpt-4.1-nano, grok-3-fast, grok-3-mini-fast, kimi-k2, o3, o4-mini, qwen3-235b-a22b. Для генерации моделей использовался фреймворк **ProMoAI**, формирующий модели на языке **POWL** с последующей конвертацией в сети Петри или BPMN-диаграммы. Журналы событий преобразовывались в текстовые абстракции с помощью библиотеки **PM4Py**.

Каждый эксперимент проводился в двух режимах:
- **Стандартный промпт**: оригинальный оптимизированный промпт ProMoAI.
- **Промпт строгого следования**: стандартный промпт с явной инструкцией игнорировать фоновые знания и полностью опираться на предоставленные входные данные.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:73-82]

### Протокол оценки

Для каждой сгенерированной модели вычислялась семантическая схожесть с тремя эталонными моделями (M⁺, M⁻, M∗) на основе метрики **behavioral footprint similarity** из библиотеки PM4Py. Цель — определить, к какому из трёх эталонов ближе сгенерированная модель: к соответствующему источнику свидетельств или к стандартной модели процесса.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:73-82]

## Результаты

### Подтверждение гипотезы о галлюцинациях

Результаты убедительно подтвердили центральную гипотезу: все протестированные LLM демонстрировали знание-обусловленные галлюцинации при работе с нетипичными структурами процессов. Ни одна модель не достигла полного следования нетипичным свидетельствам. При стандартных промптах зафиксировано 27 явных случаев галлюцинаций при работе с текстовыми описаниями и 20 — при работе с журналами событий.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:24-31]

### Влияние строгого промпта

Явная инструкция придерживаться входных данных снизила число галлюцинаций с 27 до 13 (текстовые описания) и с 20 до 10 (журналы событий). Однако полностью устранить проблему не удалось ни для одной модели. Модель **o3** показала наибольшее улучшение при строгом промпте, тогда как **grok-3-fast** продолжал галлюцинировать даже при явных инструкциях.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:24-31]

### Влияние типа входного артефакта

Журналы событий вызывали меньше галлюцинаций, чем текстовые описания (30 против 40 случаев суммарно по обоим типам промптов). Структурированный и однозначный формат журнала событий служит более весомым свидетельством для LLM по сравнению с естественным языком. Тем не менее галлюцинации сохранялись и при работе с журналами, что свидетельствует об устойчивости внутренних схем модели.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:24-31]

### Сравнение LLM

Лучшие результаты по метрике средней диагональной схожести (diag) показали **o4-mini** и **o3**. Наибольшее отставание от лидера продемонстрировали **command-r** и **gpt-4.1-nano**. Примечательно, что прямой зависимости между размером модели (числом параметров) и устойчивостью к галлюцинациям обнаружено не было.

Даже в случаях корректного следования нетипичной структуре качество сгенерированных моделей (по значению схожести) оставалось ниже, чем для стандартных процессов. Это указывает на то, что внутренние схемы LLM ухудшают производительность даже без полной галлюцинации.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:24-31]

## Связь с другими направлениями

Данное исследование пересекается с несколькими областями [[process-mining-overview]]:

- **Автоматическое обнаружение процессов**: LLM используются как альтернатива классическим алгоритмам майнинга для генерации моделей из журналов событий.
- **Предиктивный мониторинг**: схожие проблемы надёжности LLM актуальны для [[narrative-based-predictive-process-monitoring-llm]].
- **Конформанс-чекинг**: оценка соответствия сгенерированных моделей реальному поведению процессов.

Исследование также связано с более широкой проблематикой доверенного ИИ (Trustworthy AI) в доменах с нормативными требованиями, где отклонение от стандартных паттернов является намеренным и значимым.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:28-31]

## Практические выводы

1. **Валидация обязательна**: артефакты, сгенерированные LLM в доменах с устоявшимися паттернами, требуют строгой проверки на соответствие исходным свидетельствам.
2. **Промпт-инжиниринг помогает, но недостаточен**: явные инструкции снижают число галлюцинаций примерно вдвое, но не устраняют их полностью.
3. **Журналы событий надёжнее текста**: структурированные данные в формате журналов событий обеспечивают более высокую точность следования свидетельствам по сравнению с текстовыми описаниями.
4. **Нетипичные процессы особенно уязвимы**: организации с нестандартными процессами подвергаются наибольшему риску получить вводящие в заблуждение модели от LLM.

Все артефакты и результаты эксперимента опубликованы в открытом доступе на GitHub: https://github.com/antonov1/process-hallucinations.^[Kourani et al - Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling.pdf:24-31]
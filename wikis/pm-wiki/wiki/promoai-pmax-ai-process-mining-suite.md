---
aliases: []
confidence: medium
created: '2026-07-16T06:49:41'
lint_warnings:
- claim: Поддерживаются Python 3.9 и 3.10.
  concern: Это утверждение, скорее всего, занижает реальную поддержку версий Python.
    Современные Python-библиотеки, как правило, поддерживают более широкий диапазон
    версий (например, 3.9–3.12), и ограничение только версиями 3.9 и 3.10 выглядит
    подозрительно узким без дополнительного подтверждения из официальной документации
    проекта.
orphan: false
resource: https://github.com/fit-process-mining/ProMoAI
sources:
- file: https://github.com/fit-process-mining/ProMoAI
  hash: 180e4c5bc8a65e0460ef24f8b3c63747f5da66774f22ac337fd87716c9f09546
  ingested: '2026-07-16T06:49:41'
  size: 45
status: active
tags:
- process mining
- AI
- LLM
- BPMN
- Petri nets
- autonomous agents
- event logs
- natural language processing
- model generation
- open source
title: 'ProMoAI и PMAx: AI-инструментарий для Process Mining'
type: technology
---

# ProMoAI и PMAx: AI-инструментарий для Process Mining

**ProMoAI** — это AI-инструментарий для [[process-mining-handbook|Process Mining]], разработанный группой fit-process-mining (Fraunhofer Institute FIT и RWTH Aachen University). Инструментарий использует большие языковые модели (LLM) для преобразования естественного языка в формальные процессные модели и включает автономную агентную систему **PMAx** для анализа журналов событий и генерации аналитических отчётов. ^[ProMoAI:113-116]

Проект опубликован на GitHub по адресу `fit-process-mining/ProMoAI` (лицензия AGPL-3.0) и доступен в виде облачного приложения на `promoai.streamlit.app`, а также как Python-библиотека (`pip install promoai`).

## Архитектура: два основных модуля

Инструментарий состоит из двух взаимодополняющих модулей: ^[ProMoAI:117-120]

### ProMoAI: генерация и уточнение процессных моделей

Модуль ProMoAI решает задачу автоматического построения формальных процессных моделей на основе текстовых описаний или журналов событий. Он поддерживает следующие режимы работы: ^[ProMoAI:118-119]

- **Text-to-Model («текст → модель»):** генерация моделей в форматах BPMN или PNML (сети Петри) из описаний на естественном языке.
- **Уточнение модели:** загрузка существующей BPMN-диаграммы или сети Петри и её интерактивное изменение или расширение с помощью LLM через диалоговый интерфейс.
- **Discovery Baseline («базовое обнаружение»):** загрузка XES-журнала событий для автоматического обнаружения начальной модели с последующим уточнением при помощи языковой модели.

Подход ProMoAI к генерации моделей связан с проблемой [[knowledge-driven-hallucination-llm-process-modeling|knowledge-driven hallucination]], исследованной той же научной группой: LLM может подменять информацию из входного источника своими обобщёнными знаниями, что особенно критично при построении точных процессных моделей.

### PMAx: агентный Process Mining

PMAx — автономная мультиагентная система, функционирующая как виртуальный аналитик процессов. Её ключевые характеристики: ^[ProMoAI:115-116]

- **Архитектура «разделяй и властвуй»:** система использует специализированных агентов — **Engineer** (инженер) и **Analyst** (аналитик), — которые совместно обрабатывают высокоуровневые бизнес-вопросы.
- **Защита конфиденциальности данных:** LLM получает только лёгкие метаданные (названия и типы столбцов); необработанные данные журнала событий не покидают локальную среду пользователя.
- **Детерминированная точность:** система генерирует и выполняет локальный Python-код с использованием разрешённых библиотек предобработки данных для вычисления точных метрик, что позволяет избежать галлюцинаций LLM при работе с числовыми показателями.
- **Комплексная отчётность:** автоматическая генерация таблиц, статистических диаграмм и нарративных выводов на основе бизнес-вопросов пользователя.

## Техническая реализация

Приложение реализовано на Python (98,1% кодовой базы) с использованием фреймворка Streamlit. Поддерживаются Python 3.9 и 3.10. Репозиторий содержит: ^[ProMoAI:88-109]

- `app.py` — единый интерфейс (ProMoAI + PMAx);
- `promoai_standalone.py` — устаревший автономный интерфейс ProMoAI;
- `pmax.py` — модуль агентной аналитики;
- `promoai/` — основной пакет библиотеки;
- `example_online_shop/` — пример использования для интернет-магазина.

Инструментарий интегрируется с различными LLM-провайдерами, включая OpenAI, Google Gemini и GitHub Copilot.

## Публикации и цитирование

Основная научная публикация, описывающая модуль ProMoAI:

> Humam Kourani, Alessandro Berti, Daniel Schuster, Wil M. P. van der Aalst. *ProMoAI: Process Modeling with Generative AI*. Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI 2024), pp. 8708–8712. ijcai.org, 2024.

Авторы — исследователи Fraunhofer Institute FIT и RWTH Aachen University, той же группы, которая изучала [[knowledge-driven-hallucination-llm-process-modeling|knowledge-driven hallucination в LLM для моделирования процессов]].

## Связанные темы

- [[process-mining-handbook|Process Mining]] — область, для которой разработан инструментарий.
- [[knowledge-driven-hallucination-llm-process-modeling|Knowledge-Driven Hallucination в LLM]] — проблема, которую PMAx решает через детерминированное выполнение кода.
- [[llm-declarative-process-discovery-dcr-graphs|LLM-Based Discovery of Declarative Processes]] — смежный подход к извлечению процессных моделей с помощью LLM.
- [[veco-multimodal-process-mining-library|VeCo]] — другая библиотека, связывающая мультимодальные данные компании с LLM для задач Process Mining.
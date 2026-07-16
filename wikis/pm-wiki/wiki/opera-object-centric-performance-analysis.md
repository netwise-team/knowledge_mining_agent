---
aliases: []
confidence: medium
created: '2026-07-16T05:30:58'
lint_warnings:
- claim: алгоритм Inductive Miner Directly-Follows (Leemans, 2018)
  concern: The cited Leemans 2018 paper ('Scalable process discovery and conformance
    checking') describes the general scalable Inductive Miner framework, not specifically
    the Inductive Miner Directly-Follows (IMf) variant. IMf was introduced in an earlier
    2013/2014 paper by Leemans et al. Attributing IMf specifically to the 2018 paper
    is inaccurate.
orphan: false
resource: https://github.com/gyunamister/OPerA
sources:
- file: https://github.com/gyunamister/OPerA
  hash: 3f262f44dacdfe9edddd650ee8d9aace17c2e29315343e1c2ae1d74202804472
  ingested: '2026-07-16T05:30:58'
  size: 36
status: active
tags:
- process mining
- object-centric
- performance analysis
- Petri nets
- event logs
- token-based replay
- conformance checking
- process discovery
- visualization
- open source
title: 'OPerA: Инструмент объектно-ориентированного анализа производительности процессов'
type: technology
updated: '2026-07-16'
---

# OPerA: Инструмент объектно-ориентированного анализа производительности процессов

**OPerA** (Object-centric Performance Analysis) — интерактивный инструмент с открытым исходным кодом, реализующий объектно-ориентированный анализ производительности бизнес-процессов. Репозиторий доступен на GitHub по адресу `gyunamister/OPerA` и распространяется под лицензией GPL-3.0. Инструмент разработан Гюнамом Парком (Gyunam Park) и ориентирован на работу с объектно-центрическими журналами событий в рамках парадигмы [[process-mining-handbook|process mining]].

## Назначение и возможности

OPerA предоставляет полный конвейер для анализа производительности процессов на основе объектно-центрических данных:

- **Импорт объектно-центрических журналов событий** в форматах OCEL JSON, OCEL XML и CSV.
- **Обнаружение объектно-центрических сетей Петри (OCPN)** на основе общего подхода ван дер Аалста и Берти (2020) с применением алгоритма Inductive Miner Directly-Follows (Leemans, 2018). Базовая статья: [[object-centric-petri-nets-discovery]].
- **Воспроизведение токенов с временны́ми метками** на OCPN с использованием подхода token-based replay (Berti и van der Aalst, 2021).
- **Вычисление объектно-центрических показателей производительности** на основе результатов воспроизведения: вхождений событий и посещений токенов.
- **Визуализация OCPN** с наложением показателей производительности.

## Теоретическая основа

Инструмент опирается на три ключевые научные работы:

1. **van der Aalst, W.M.P., Berti, A.** «Discovering object-centric Petri nets». *Fundamenta Informaticae* 175(1–4), 1–40 (2020) — базовый подход к построению объектно-центрических сетей Петри. Страница в wiki: [[object-centric-petri-nets-discovery]].
2. **Leemans, S.J.J., Fahland, D., van der Aalst, W.M.P.** «Scalable process discovery and conformance checking». *Software & Systems Modeling* 17(2), 599–631 (2018) — алгоритм Inductive Miner для масштабируемого обнаружения процессов.
3. **Berti, A., van der Aalst, W.M.P.** «A novel token-based replay technique to speed up conformance checking and process enhancement». *Transactions on Petri Nets and Other Models of Concurrency* 15, 1–26 (2021) — техника воспроизведения токенов для ускорения проверки соответствия.

Объектно-центрические сети Петри (OCPN) расширяют классические сети Петри, позволяя моделировать процессы, в которых одно событие может быть связано с несколькими объектами разных типов. Это устраняет ограничения традиционного [[process-mining-handbook|process mining]], предполагающего единственный идентификатор случая.

## Архитектура и развёртывание

OPerA реализована как веб-приложение на Python (98,7% кодовой базы) с использованием фреймворка Dash. Архитектура включает:

- **Бэкенд** с очередью задач на базе Celery и RabbitMQ.
- **База данных**, запускаемая через Docker Compose.
- **Веб-интерфейс**, доступный по адресу `127.0.0.1:8050`.

### Автоматическое развёртывание (Docker)

```bash
git clone https://github.com/gyunamister/OPerA.git
cd src/
docker-compose up
```

После запуска веб-сервис доступен по адресу `127.0.0.1/8050`. Логин по умолчанию: `admin`, пароль: `test123`.

### Ручное развёртывание

Требования: Graphviz (бинарный файл) и Python 3.8.8.

```bash
# Shell 1: база данных
cd src/backend/db && docker-compose up

# Shell 2: Celery worker
export OPERA_PATH=<path_to_project_root>
cd src/backend && ./run_celery.sh

# Shell 3: веб-сервер
export OPERA_PATH=<path_to_project_root>
cd src/backend && ./run_opera.sh
```

## Связанные инструменты и библиотеки

- [[object-centric-petri-nets-discovery]] — фундаментальная статья ван дер Аалста и Берти (2020), алгоритм OCPN из которой реализован в OPerA.
- [[ocpa]] (github.com/ocpm/ocpa) — Python-библиотека для объектно-ориентированного процессного майнинга от тех же авторов (Adams, Park, van der Aalst); является более полным пакетом, включающим OCPN discovery, conformance checking, performance analysis и predictive monitoring.
- [[object-centric-streaming-process-discovery-liss]] — потоковое расширение обнаружения OCPN.
- [[streaming-object-centric-process-mining]] — потоковая обработка объектно-центрических процессов.

---

*Источник: репозиторий github.com/gyunamister/OPerA; связанная статья arXiv:2204.10662 (OPerA: Object-Centric Performance Analysis, Gyunam Park et al., ICPM 2022).*

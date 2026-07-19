---
aliases: []
confidence: medium
created: '2026-07-16T02:17:39'
lint_warnings:
- claim: Последний релиз | v2.0.3 (июнь 2026)
  concern: A release date of June 2026 is in the future relative to any plausible
    knowledge cutoff, making this claim unverifiable and almost certainly fabricated
    or erroneous.
orphan: false
resource: https://github.com/beamline/pybeamline
sources:
- file: https://github.com/beamline/pybeamline
  hash: 31c8133c932cc93827404766d1eb2170921f56a7d79f75a89e7faf9b3927c281
  ingested: '2026-07-16T02:17:39'
  size: 38
status: active
tags:
- streaming process mining
- ReactiveX
- RxPY
- event-based programming
- observable sequences
- Python library
- open source
- process mining framework
- asynchronous programming
- object-centric
title: pyBeamline
type: technology
---

# pyBeamline

**pyBeamline** — это Python-реализация фреймворка Beamline для [[streaming-process-mining-event-streams|потокового процессного майнинга]]. Библиотека позволяет встраивать операторы процессного майнинга в конвейеры обработки событий в реальном времени и поддерживает как классический, так и [[streaming-object-centric-process-mining|объектно-ориентированный процессный майнинг]].^[pybeamline:102-107]

## Архитектура и технологическая основа

pyBeamline построен на базе **ReactiveX** и его Python-привязки **RxPY** — библиотеки для составления асинхронных и событийно-ориентированных программ с использованием наблюдаемых последовательностей (observable sequences) и конвейерных операторов запросов. Такой подход позволяет декларативно описывать потоки событий и применять к ним операторы процессного майнинга в виде composable-компонентов.^[pybeamline:108-108]

Фреймворк наследует идеи и принципы оригинального Beamline, однако реализован на Python и ориентирован на иную технологическую экосистему.^[pybeamline:105-107]

## Возможности

- **Классический потоковый процессный майнинг**: обнаружение процессных моделей из непрерывных потоков событий в режиме реального времени.
- **Объектно-ориентированный процессный майнинг**: поддержка [[object-centric-streaming-process-discovery-liss|объектно-центричного обнаружения процессов]] из потоков событий, что соответствует современным подходам к работе с [[process-scope-enrichment-ocel|объектно-центричными журналами событий (OCEL)]].
- Интеграция операторов процессного майнинга в реактивные конвейеры обработки данных.^[pybeamline:108-108]

## Установка

Библиотека доступна через PyPI и устанавливается стандартной командой:

```
pip install pybeamline
```
^[pybeamline:111-112]

## Документация и обучающие материалы

Полная документация размещена на сайте [beamline.cloud/pybeamline](https://www.beamline.cloud/pybeamline/). Репозиторий содержит Jupyter-ноутбуки с примерами:

- **tutorial.ipynb** — классический процессный майнинг;
- **tutorial_oc.ipynb** — объектно-ориентированный процессный майнинг.^[pybeamline:109-117]

## Техническая информация

| Параметр | Значение |
|---|---|
| Язык | Python (30,9%), Jupyter Notebook (69,1%) |
| Лицензия | Apache-2.0 |
| Последний релиз | v2.0.3 (июнь 2026) |
| Репозиторий | github.com/beamline/pybeamline |

## Связь с исследовательским сообществом

pyBeamline используется в академических исследованиях по потоковому процессному майнингу. В частности, работы по [[streaming-object-centric-process-mining|потоковому объектно-центричному процессному майнингу (SOCPM)]] и [[object-centric-streaming-process-discovery-liss|объектно-центричному потоковому обнаружению процессов]] опираются на схожие концепции реактивной обработки потоков событий, которые реализованы в pyBeamline на практике.
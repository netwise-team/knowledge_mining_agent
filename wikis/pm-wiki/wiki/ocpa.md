---
aliases: []
confidence: medium
created: '2026-07-16T05:17:46'
lint_warnings:
- claim: Традиционный процессный майнинг анализирует один процесс на основе однородных
    последовательностей событий.
  concern: Traditional process mining typically works with event logs containing traces
    (sequences of events) associated with a single case notion, but it is not strictly
    limited to 'homogeneous sequences' — this characterization oversimplifies the
    field and could be considered misleading as a general statement about traditional
    process mining.
orphan: false
resource: https://github.com/ocpm/ocpa
sources:
- file: https://github.com/ocpm/ocpa
  hash: ffeb7a492d46fb731acc6ccb14f0a9e821b6d704e03f604532477f8412de9ad6
  ingested: '2026-07-16T05:17:46'
  size: 28
status: active
tags:
- object-centric process mining
- process discovery
- conformance checking
- predictive process monitoring
- event log management
- Python library
- heterogeneous event graphs
- performance analysis
- open source
- research
title: 'ocpa: Python-библиотека для объектно-ориентированного процессного майнинга'
type: technology
---

# ocpa: Python-библиотека для объектно-ориентированного процессного майнинга

**ocpa** (Object-Centric Process Analysis) — это Python-библиотека с открытым исходным кодом, предназначенная для поддержки [[process-mining-handbook|объектно-ориентированного процессного майнинга]]. Библиотека разработана **Jan Niklas Adams**, **Gyunam Park** и **Wil M.P. van der Aalst** (RWTH Aachen University) и опубликована в журнале *Software Impacts* (2022, DOI: 10.1016/j.simpa.2022.100438). Репозиторий доступен на GitHub по адресу `ocpm/ocpa` и распространяется под лицензией GPL-3.0.^[ocpa:114-120]

Традиционный [[process-mining-data-science-in-action|процессный майнинг]] анализирует один процесс на основе однородных последовательностей событий. Однако многие реальные процессы состоят из нескольких взаимодействующих подпроцессов, а события могут затрагивать несколько объектов одновременно. ocpa обобщает классические техники процессного майнинга, переходя от однородных последовательностей событий к гетерогенным графам событий.^[ocpa:101-102]

## Основные функциональные возможности

ocpa охватывает следующие направления [[process-mining-handbook|объектно-ориентированного процессного майнинга]]:

- **Управление объектно-ориентированными журналами событий** — импорт и экспорт данных;
- **Извлечение выполнений процессов** (object-centric cases);
- **Обнаружение процессов** — построение объектно-ориентированных сетей Петри;
- **Расчёт вариантов** и их визуализация;
- **Проверка соответствия** (conformance checking) — точность и полнота воспроизведения;
- **Мониторинг ограничений** (constraint monitoring);
- **Улучшение процессов** — анализ производительности;
- **Предиктивный мониторинг процессов** — извлечение признаков, кодирование и предобработка.^[ocpa:100-102]

## Управление журналами событий

ocpa поддерживает импорт объектно-ориентированных данных о событиях из нескольких форматов:

- **CSV-файлы** — с указанием типов объектов, названий активностей и временных меток;
- **JSON OCEL / XML OCEL** — форматы стандарта [[ocpm-personal-health-management|OCEL]];
- **OCEL 2.0** — включая формат SQLite.

Экспорт поддерживается в формат JSON OCEL. Интерфейс импортёра позволяет гибко настраивать параметры обработки журнала.^[ocpa:127-137]

## Извлечение выполнений процессов

Выполнения процессов (process executions) извлекаются из журнала событий с помощью настраиваемых техник. По умолчанию используется метод связных компонент (connected components). Также поддерживается метод ведущего типа (leading type). Для каждого выполнения доступны: список событий, список объектов и граф выполнения процесса.^[ocpa:139-144]

## Обнаружение объектно-ориентированных процессов

ocpa реализует алгоритм обнаружения [[partial-order-powl-process-discovery|процессных моделей]] в виде **объектно-ориентированных сетей Петри** (Object-Centric Petri Nets, OCPN). Полученные модели могут быть визуализированы непосредственно в библиотеке.^[ocpa:145-147]

### Расчёт и визуализация вариантов

Варианты определяются как эквивалентные по управляющему потоку выполнения процессов. Поскольку выполнение процесса представляет собой граф, эквивалентность устанавливается через изоморфизм графов с аннотацией узлов атрибутом активности. ocpa предлагает два метода:

- **TWO_PHASE** — сначала вычисляются лексикографические представления графов, затем выполняется уточнение; как правило, работает быстрее;
- **ONE_PHASE** — прямая проверка изоморфизма один к одному.

По умолчанию используется приближённый расчёт вариантов через лексикографическое представление. Визуализация вариантов реализована, в частности, на платформе OCpi (www.ocpi.ai).^[ocpa:148-155]

## Проверка соответствия

### Точность и полнота воспроизведения

ocpa позволяет вычислять **точность** (precision) и **полноту воспроизведения** (fitness) путём сравнения объектно-ориентированной сети Петри с объектно-ориентированным журналом событий. Полнота воспроизведения определяется как доля событий, которые могут быть воспроизведены в сети Петри.^[ocpa:156-159]

### Мониторинг ограничений

ocpa поддерживает проверку соответствия журнала событий пользовательским ограничениям, описывающим:

- **Ограничения управляющего потока** (control-flow constraints) — например, параллельное или причинно-следственное выполнение активностей;
- **Ограничения на вовлечённость объектов** (object-involvement constraints) — например, обязательное или запрещённое присутствие объектов определённого типа;
- **Ограничения производительности** (performance constraints).

Ограничения задаются с помощью класса `ConstraintGraph`, включающего узлы активностей (`ActivityNode`), узлы типов объектов (`ObjectTypeNode`) и рёбра (`ControlFlowEdge`, `ObjectRelationEdge`, `PerformanceEdge`).^[ocpa:160-195]

## Анализ производительности

ocpa реализует объектно-ориентированный анализ производительности, учитывающий взаимодействие объектов в бизнес-процессах. Поддерживаемые метрики включают:

- **Время ожидания** (waiting time);
- **Время обслуживания** (service time);
- **Время пребывания** (sojourn time);
- **Время синхронизации** (synchronization time);
- **Время объединения** (pooling time);
- **Время запаздывания** (lagging time);
- **Время потока** (flow time).

Эти метрики обеспечивают более точную оценку производительности по сравнению с классическими подходами, поскольку учитывают объектно-ориентированную природу данных.^[ocpa:196-206]

## Предиктивный мониторинг процессов

ocpa предоставляет расширенную поддержку предиктивного мониторинга процессов через:

- **Извлечение признаков** (feature extraction) — на основе графовой структуры объектно-ориентированных данных о событиях;
- **Кодирование признаков** (feature encoding) — в табличном, последовательном или графовом формате;
- **Предобработку** — нормализацию и разбиение на обучающую и тестовую выборки.

Извлечённые признаки хранятся в структуре `Feature Storage`, содержащей список графов признаков. Каждый граф представляет одно выполнение процесса, каждый узел — одно событие. Предопределённые функции признаков включают оставшееся время (`EVENT_REMAINING_TIME`), прошедшее время (`EVENT_ELAPSED_TIME`), количество предшествующих событий определённого типа и предшествующие активности.^[ocpa:207-220]

## Установка

Библиотека устанавливается через pip:

```
pip install ocpa
```

Либо клонированием репозитория с GitHub:

```
git clone https://github.com/ocpm/ocpa.git
cd ocpa
pip install .
```

Документация доступна на ReadTheDocs. Библиотека совместима с существующими стандартами объектно-ориентированных журналов событий (OCEL) и легко интегрируется с другими инструментами процессного майнинга.^[ocpa:103-105]

## Цитирование

При использовании ocpa в научных работах рекомендуется ссылаться на следующую публикацию:

Adams, J. N., Park, G., & van der Aalst, W. M. P. (2022). ocpa: A Python library for object-centric process analysis. *Software Impacts*, 100438. https://doi.org/10.1016/j.simpa.2022.100438^[ocpa:109-120]

## Key Data

- title = {ocpa: A Python library for object-centric process analysis},
- journal = {Software Impacts},
- pages = {100438},
- year = {2022},
- issn = {2665-9638},
- doi = {https://doi.org/10.1016/j.simpa.2022.100438},
- url = {https://www.sciencedirect.com/science/article/pii/S2665963822001221},
- author = {Jan Niklas Adams and Gyunam Park and Wil M.P. {van der Aalst}},
- filename = "sample_logs/csv/BPI2017-Final.csv"
- object_types = ["application", "offer"]
- parameters = {"obj_names":object_types,
- ocel = ocel_import_factory.apply(file_path= filename,parameters = parameters)
- filename = "sample_logs/jsonocel/p2p-normal.jsonocel"
- ocel = ocel_import_factory.apply(filename)
- filename = "sample_logs/ocel2/sqlite/running-example.sqlite"
- filename = "../../sample_logs/jsonocel/p2p-normal.jsonocel"
- parameters = {"execution_extraction": "leading_type",
- ocel = ocel_import_factory.apply(file_path=filename)
- ocpn = ocpn_discovery_factory.apply(ocel, parameters={"debug": False})
- variant_layouting = variants_visualization_factory.apply(ocel)
- ocpn = ocpn_discovery_factory.apply(ocel, parameters = {"debug":False})
- filename = "<path-to-your-log>"
- ocpn = ocpn_discovery_factory.apply(ocel)
- diag = performance_factory.apply(ocpn, ocel, parameters=diag_params)
- cg1 = ConstraintGraph('Example1')
- act_vm = ActivityNode('Verify Material')
- act_pgi = ActivityNode('Plan Goods Issue')
- cf1 = ControlFlowEdge(act_vm, act_pgi, 'concur', 'MATERIAL', 0.1)
- cg2 = ConstraintGraph('Example2')
- act_cpr = ActivityNode('Create Purchase Requisition (CPR)')
- act_cpo = ActivityNode('Create Purchase Order (CPO)')
- cf2 = ControlFlowEdge(act_cpr, act_cpo, 'causal', 'PURCHREQ', 0.99)
- cg3 = ConstraintGraph('Example3')
- cf3 = ControlFlowEdge(act_cpr, act_cpr, 'skip', 'PURCHREQ', 0)
- cg4 = ConstraintGraph('Example4')
- obj_node1 = ObjectTypeNode('PURCHORD')
- or1 = ObjectRelationEdge(obj_node1, act_pgi, 'absent', 0)
- cg5 = ConstraintGraph('Example5')
- obj_node2 = ObjectTypeNode('MATERIAL')
- or2 = ObjectRelationEdge(obj_node2, act_pgi, 'present', 0)
- cg6 = ConstraintGraph('Example6')
- or3 = ObjectRelationEdge(obj_node1, act_cpo, 'singular', 0.99)
- cg7 = ConstraintGraph('Example7')
- act_cpo = ActivityNode('Plan Goods Issue')
- or4 = ObjectRelationEdge(obj_node2, act_cpo, 'multiple', 0.7)
- filename = "./sample_logs/jsonocel/p2p-normal.jsonocel"
- gviz = ocpn_vis_factory.apply(
- activities = list(set(ocel.log.log["event_activity"].tolist()))
- feature_set = [(predictive_monitoring.EVENT_REMAINING_TIME, ()),
- feature_storage = predictive_monitoring.apply(ocel, feature_set, [])
- table = tabular.construct_table(feature_storage)
- sequences = sequential.construct_sequence(feature_storage)
- train_table = tabular.construct_table(
- test_table = tabular.construct_table(
- model = LinearRegression()
- y_pred = model.predict(x_test)
- avg_rem = sum(y_train)/len(y_train)^[ocpa:114-120]
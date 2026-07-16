---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T21:12:28'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Ansari et al - On the Simplification
    of Neural Network Architectures for Predictive Process Monitoring.pdf
  hash: a957dcea86e11a8b3cead362baaef2bc27e9aac5adba649f335c4b312433ad17
  ingested: '2026-07-14T21:12:28'
  size: 1386650
  truncated: true
status: active
tags:
- deep learning
- process mining
- neural network simplification
- model compression
- event logs
- self-attention
- RNN
- NLP
- scalability
- efficiency
title: Упрощение архитектур нейронных сетей для предиктивного мониторинга процессов
type: technology
---

# Упрощение архитектур нейронных сетей для предиктивного мониторинга процессов

Упрощение архитектур нейронных сетей для предиктивного мониторинга процессов (Predictive Process Monitoring, PPM) — направление исследований в области [[process-mining-overview]], изучающее, насколько можно сократить сложность глубоких моделей (количество параметров и глубину архитектуры) без существенной потери предсказательной точности. Работа Ансари, Кирхдорфера и Хадиан (SAP Signavio / Университет Мангейма, 2025) демонстрирует, что значительное сжатие моделей возможно при минимальных потерях качества.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:1-21]

## Мотивация и контекст

Современные подходы к [[class-balanced-focal-loss-next-activity-prediction|PPM]] опираются на глубокое обучение: рекуррентные сети (LSTM) и Transformer-модели. Несмотря на высокую точность, эти модели требуют значительных вычислительных ресурсов, что затрудняет их промышленное применение. Поставщики решений по процессному майнингу — SAP Signavio, Celonis, Apromore — вынуждены обучать и поддерживать отдельные модели для каждого клиента и процесса, что порождает высокие затраты и ограничивает масштабируемость.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:41-48]

Предшествующие работы по повышению эффективности PPM фокусировались на:
- **сокращении обучающих данных** (выборка информативных подмножеств журналов событий),
- **инкрементальном обучении** (обновление модели без полного переобучения),
- **альтернативных архитектурах** (свёрточные нейронные сети вместо LSTM),
- **модификациях кодирования последовательностей** (трейс-кодирование вместо префиксного).

Вопрос о том, можно ли достичь эффективности за счёт непосредственного упрощения самой архитектуры модели, оставался малоизученным.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:108-120]

## Исследуемые архитектуры

### Transformer-модели

- **MTLFormer** — исходная многозадачная Transformer-модель (Wang et al., 2023) с пятью параллельными потоками энкодеров (два для активностей, два для ролей, один для временного контекста) и тремя головами предсказания на основе многослойных перцептронов (MLP). Расширена авторами для предсказания ролей и времени ожидания.
- **MTLFormerlight** — облегчённый вариант: сохраняет пятипоточную архитектуру, но заменяет MLP-головы одиночными линейными слоями и уменьшает гиперпараметры (размер эмбеддинга, число голов внимания, размерность прямого прохода). Сокращение параметров — **85%** (со 136 412 до 19 823).
- **Transformersimple** — наиболее компактный вариант: единственный Transformer-энкодер обрабатывает токены активностей и ролей совместно; три одиночных линейных головы предсказания. Параметры: ~20 264.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:56-61]

### LSTM-модели

- **LSTM** (Camargo et al., 2019) — общий LSTM-слой как основа, три параллельные задачно-специфичные головы, каждая из которых содержит LSTM-слой и небольшой MLP.
- **LSTMlight** — сохраняет общий LSTM-слой, но заменяет головы одиночными линейными проекциями. Сокращение параметров — **77%** (с 75 876 до 17 193).^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:62-65]

## Задачи PPM и метрики

Авторы рассматривают пять стандартных задач PPM на основе префиксов трасс журнала событий:

1. **Предсказание следующей активности (NAP)** — метрика F1.
2. **Предсказание следующей роли (NRP)** — метрика F1.
3. **Предсказание времени ожидания следующего события (NWTP)** — MAE в днях.
4. **Предсказание длительности следующего события (NDP)** — MAE в днях.
5. **Предсказание оставшегося времени (RTP)** — MAE в днях.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:25-30]

Эти задачи пересекаются с тематикой [[actor-enriched-throughput-time-forecasting]] и [[class-balanced-focal-loss-next-activity-prediction]].

## Экспериментальная установка

Оценка проводилась на пяти журналах событий из различных доменов (финансовые услуги, закупки, производство):

| Журнал | Тип | Трассы | События | Активности | Ресурсы |
|---|---|---|---|---|---|
| Production | реальный | 225 | 4 503 | 24 | 41 |
| BPIC2012W | реальный | 8 616 | 59 302 | 6 | 52 |
| P2P | синтетический | 608 | 9 119 | 21 | 27 |
| Confidential 1000 | синтетический | 1 000 | 38 160 | 42 | 14 |
| Confidential 2000 | синтетический | 2 000 | 77 418 | 42 | 14 |

Данные разбивались хронологически: 70% — обучение, 10% — валидация, 20% — тест. Для многозадачного обучения применялось взвешивание потерь по неопределённости (uncertainty weighting).^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:13-21]

## Ключевые результаты

### Transformer-модели

- **MTLFormerlight** при сокращении параметров на 85% теряет лишь **1,4% F1** по NAP (0,70 → 0,69) и **2,8% F1** по NRP (0,71 → 0,69). MAE по NWTP возрастает на 6,3%; NDP не изменяется; RTP — на 0,7%.
- **Transformersimple** сопоставим с MTLFormerlight по временны́м задачам, однако уступает ему примерно на **3 п.п. F1** по NAP (0,66 против 0,69), что обусловлено главным образом большим разрывом на датасете BPI12W.
- MTLFormerlight нередко сходится **быстрее** полного MTLFormer, что свидетельствует о том, что компактность модели не препятствует, а порой ускоряет оптимизацию.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:56-61]

### LSTM-модели

- **LSTMlight** при сокращении параметров на 77% теряет **2,9% F1** по NAP и NRP (0,70 → 0,68). Однако временны́е ошибки растут заметнее: MAE по NWTP увеличивается на **13%**, по RTP — на 3%.
- По сравнению с Transformersimple, LSTMlight использует на 15% меньше параметров и незначительно превосходит его по NAP (0,68 против 0,66 F1), но показывает на **26,8% более высокую ошибку RTP** (20,80 против 16,40 MAE).^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:62-65]

### Сравнительный вывод

Transformer-архитектуры демонстрируют бо́льшую устойчивость к сжатию, чем LSTM, особенно в задачах предсказания времени. Единственный Transformer-энкодер (Transformersimple) способен конкурировать с более сложными моделями при значительно меньшем числе параметров.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:16-21]

## Методология отбора моделей

Для выбора оптимальной конфигурации авторы вводят составной показатель:

$$S_M = p_M + \lambda \cdot \ell_M$$

где $p_M$ — относительное число параметров модели $M$ по сравнению с лучшей моделью по валидационной потере, $\ell_M$ — относительное отклонение валидационной потери, $\lambda = 2$ (акцент на качестве предсказания). Модель с наименьшим $S_M$ выбирается для каждого типа архитектуры и датасета.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:49-55]

## Связь с другими подходами к эффективности PPM

Работа дополняет существующие стратегии повышения эффективности PPM:
- [[llm-domain-adaptation-peft-ppm]] — параметрически эффективная дообучка LLM для данных процессов (PEFT).
- [[narrative-based-predictive-process-monitoring-llm]] — использование LLM для нарративного предсказания исходов.
- [[actor-enriched-throughput-time-forecasting]] — обогащение моделей данными об акторах для прогнозирования времени выполнения.

В отличие от этих подходов, данная работа фокусируется не на смене парадигмы (переход к LLM), а на **прунинге существующих архитектур** глубокого обучения.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:49-55]

## Направления будущих исследований

- Архитектурно-осознанный прунинг и поиск нейронных архитектур (NAS).
- Расширение на долгосрочные задачи PPM: предсказание суффиксов трасс и итогов процессов.
- Исследование обобщаемости лёгких моделей на новые домены.
- Интеграция облегчённых моделей в системы PPM реального времени.^[Ansari et al - On the Simplification of Neural Network Architectures for Predictive Process Monitoring.pdf:19-21]

## Key Data

- pM = #params(M)
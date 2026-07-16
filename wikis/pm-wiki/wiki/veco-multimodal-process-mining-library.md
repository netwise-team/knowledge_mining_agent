---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T07:05:02'
lint_warnings:
- claim: audio is transcribed via OpenAI Whisper
  concern: OpenAI Whisper is an open-source model that can be run locally, but describing
    it as 'OpenAI Whisper' in the context of a tool emphasizing local/private processing
    could be misleading. However, the more concrete concern is that the page elsewhere
    emphasizes local LLMs and privacy, yet Whisper could imply an API call to OpenAI
    — though Whisper itself is open-source and can run locally, so this is potentially
    just imprecise naming rather than a clear factual error. This concern is borderline.
- claim: No prior tool existed for embedding and persistently storing multimodal company
    knowledge in a vector database and making it accessible to LLMs for downstream
    process mining tasks.
  concern: This is an overstated absolute claim. General-purpose multimodal RAG (Retrieval-Augmented
    Generation) frameworks and vector database tools (e.g., LlamaIndex, LangChain
    with multimodal support, Weaviate) existed prior to VeCo and support embedding
    multimodal data for LLM access. The claim that 'no prior tool existed' for this
    purpose is clearly overstated, even if no tool was specifically tailored to process
    mining.
orphan: false
resource: https://github.com/MatthiasPohlAmberg/VeCo
sources:
- file: /home/meyurin-2135327/wikis/pm-wiki/raw_sources/Zisgen et al - Vectorizing
    the Company Leveraging Multimodal Data for Process Mining.pdf
  hash: 3a9383bd2770d9c8d9f94293e1a563cf951f21b834c085be1c47a21f66992ba3
  ingested: '2026-07-14T07:05:02'
  size: 706163
- file: https://github.com/MatthiasPohlAmberg/VeCo
  hash: 4c33c78c4b5ba878d9e013daa7ce543d1ebbc90d2f526b9baa49c81f1a13bf9c
  ingested: '2026-07-16'
  size: 42
status: active
tags:
- process mining
- multimodal data
- LLM
- vector database
- embeddings
- generative AI
- open-source
- conformance checking
- process discovery
- knowledge injection
title: 'VeCo: Multimodal Data Vectorization Library for Process Mining'
type: technology
updated: '2026-07-16'
---

# VeCo: Multimodal Data Vectorization Library for Process Mining

VeCo is an open-source Python library developed by Yorck Zisgen and Agnes Koschmider (University of Bayreuth) and Matthias Pohl (ames wiring GmbH) that streamlines the vectorization of multimodal company data and connects it to local Large Language Models (LLMs) to enhance [[coordinated-projections-multi-faceted-process-exploration|process mining]] tasks. The library was presented at the ICPM 2025 Workshops and is available on GitHub. ^[Zisgen et al - Vectorizing the Company Leveraging Multimodal Data for Process Mining.pdf:3-71]

## Motivation

Process mining techniques such as process discovery, [[deviation-desirability-assessment|conformance checking]], and process enhancement typically rely on structured event log data. However, companies store substantial domain knowledge in non-textual and heterogeneous formats — PowerPoint presentations, PDFs, images, audio recordings, and videos — that are inaccessible to conventional process mining pipelines. The emergence of Generative AI and LLMs creates an opportunity to tap into this previously unused multimodal data. ^[Zisgen et al - Vectorizing the Company Leveraging Multimodal Data for Process Mining.pdf:8-14]

Existing LLM-based process mining approaches focus predominantly on text data and natural language interfaces. No prior tool existed for embedding and persistently storing multimodal company knowledge in a vector database and making it accessible to LLMs for downstream process mining tasks. ^[Zisgen et al - Vectorizing the Company Leveraging Multimodal Data for Process Mining.pdf:36-43]

## Architecture and Pipeline

The VeCo pipeline consists of the following stages:

1. **Input ingestion**: The user provides files in various formats.
2. **Modality decomposition**: VeCo internally determines the file type and applies the appropriate extraction strategy.
3. **Text extraction and description**: Text is extracted directly from documents; images are described by a local multimodal LLM (e.g., Gemma3 12B); audio is transcribed via OpenAI Whisper; video files currently have their audio layer extracted and transcribed, with frame sampling planned for future releases.
4. **Vectorization and storage**: Extracted text is embedded and stored in a JSON-based vector database for persistent retrieval.
5. **LLM connection**: VeCo connects to local LLMs via the Ollama API, injecting relevant domain knowledge into prompts to improve process mining outputs. ^[Zisgen et al - Vectorizing the Company Leveraging Multimodal Data for Process Mining.pdf:44-52]

The library is designed to be LLM-agnostic (satisfying an explicit design requirement), allowing organizations to choose their preferred local model.

## Supported File Formats

VeCo supports the following formats:
- **Text/documents**: `.txt`, `.pdf`, `.doc`, `.docx`, `.pptx`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.bmp`
- **Audio**: `.mp3`, `.wav`
- **Video**: `.mp4`, `.avi`, `.mov`, `.mkv`

The modular, encapsulated design allows extension to additional proprietary or third-party formats.

## Design Requirements

The library was designed around four explicit requirements:
- **Req 1**: Support common office and image formats.
- **Req 2**: Handle audio and video formats.
- **Req 3**: Be extensible to additional file formats.
- **Req 4**: Be LLM-agnostic.

## Use Cases

### Use Case 1: Process Discovery and Event Log Completeness

In process discovery, incomplete event logs lead to incomplete and meaningless process models. VeCo demonstrated that an LLM without domain knowledge fails to identify custom SAP database tables (e.g., `ZSOCD`) relevant to a premium customer rapid delivery process. After vectorizing a voicemail recording in which an employee described a customization request, the LLM correctly identified the custom table, enabling a more complete event log and a more accurate discovered process model. ^[Zisgen et al - Vectorizing the Company Leveraging Multimodal Data for Process Mining.pdf:54-58]

This use case is particularly relevant to [[event-log-extraction-clinical-narratives|event log extraction]] challenges more broadly, where identifying all relevant data sources is critical.

### Use Case 2: Conformance Checking with Outdated Process Models

In [[deviation-desirability-assessment|conformance checking]], alignment-based methods may flag legitimate process behavior as deviations when the reference model is outdated. VeCo demonstrated this with a simplified procurement process: an 'Approval by Manager' activity appeared as a log move (fitness = 0.88) against an outdated process model. Without domain knowledge, the LLM confirmed the deviation as correct. After vectorizing a PowerPoint presentation informing employees of a process update (manager approval required for orders exceeding €50,000), the LLM correctly identified that the reference model was incomplete — recommending a model update rather than employee retraining. ^[Zisgen et al - Vectorizing the Company Leveraging Multimodal Data for Process Mining.pdf:58-62]

## Technical Dependencies

- **Ollama**: Interface for running local LLMs (ensures LLM-agnosticism)
- **OpenAI Whisper**: Speech-to-text conversion for audio files (requires Python 3.10.11 due to `numba`/`llvmlite` dependencies)
- **FFmpeg**: Audio/video conversion
- **Local multimodal LLM**: For image description (e.g., Gemma3 12B)
- Tested LLMs: Gemma3 12B and Llama3.1 8B

## Relationship to Existing Process Mining Tools

VeCo complements existing Python-based process mining infrastructure. PM4Py and PM4Py.LLM provide process mining algorithms and some LLM integration, but neither handles multimodal data vectorization or persistent domain knowledge storage. VeCo fills this gap by acting as a domain knowledge layer that feeds contextual information into LLM-assisted process mining workflows. ^[Zisgen et al - Vectorizing the Company Leveraging Multimodal Data for Process Mining.pdf:116-120]

## Limitations and Future Work

- Video processing currently extracts only the audio layer; full audiovisual frame sampling is planned.
- The vector database is currently JSON-based; integration with dedicated vector databases (e.g., Weaviate) is planned.
- The impact of LLM choice, database type, and document format/modality on performance has not yet been systematically studied.
- Fine-tuning local LLMs on domain-specific examples (shown to improve performance significantly after ~120 examples) has not yet been explored within VeCo.

## References

Zisgen, Y., Pohl, M., & Koschmider, A. (2025). Vectorizing the Company: Leveraging Multimodal Data for Process Mining. In *Process Mining Workshops (ICPM 2025 Int. Workshops)*, Springer LNBIP. GitHub: https://github.com/MatthiasPohlAmberg/VeCo

## Key Data

- veco = Ve ct or iz e ( d e f a u l t _ m o d e l = " llama3 .1 " )
- process = "Procurement Process"
- ref_model = "'Receive Material Shortage Note', 'Calculate Material Quantity', 'In-
- trace = "'Receive Material Shortage Note', 'Calculate Material Quantity', 'Approval
- move = "Log Moves (log only): ['Approval by Manager']"

## Техническая архитектура и возможности библиотеки

Библиотека распространяется под именем пакета **veco-ai** и поддерживает Python версий 3.10 и 3.11. Центральным классом является `Vectorize`, реализующий следующий конвейер обработки данных:

1. **Определение типа входных данных** — автоматическое распознавание формата файла.
2. **Извлечение текста** — с использованием специализированных библиотек в зависимости от типа: `pdfplumber` (PDF), `python-docx` (Word), `python-pptx` (PowerPoint), `pytesseract` (изображения/OCR), `moviepy` и `whisper` (аудио и видео).
3. **Опциональное сжатие** — генерация резюме через локальные модели Ollama (хранятся отдельно и не используются как входные данные для эмбеддингов).
4. **Разбиение на фрагменты** — разделение текста на перекрывающиеся сегменты, готовые для RAG.
5. **Векторизация** — создание эмбеддингов с помощью `sentence-transformers`.
6. **Хранение** — индекс FAISS в сочетании с одним из бэкендов: JSON (резервный, автономный), SQLite или MongoDB.
7. **RAG-запросы** — вспомогательный метод `query()` извлекает релевантный контекст и передаёт его локальной модели Ollama для генерации ответа.
^[VeCo:95-98]

## Поддерживаемые типы данных

VeCo обрабатывает широкий спектр форматов корпоративных документов: текстовые файлы, PDF, документы Word, презентации PowerPoint, изображения (с OCR и опциональным описанием через `veco_pic_describe`), аудиозаписи и видеофайлы. Опциональный модуль `veco_diarization.py` обеспечивает диаризацию дикторов для аудио- и видеоматериалов. Такой охват форматов делает библиотеку особенно ценной для задач [[veco-multimodal-process-mining-library|мультимодального процессного майнинга]], где корпоративные данные существуют в разнородных форматах.
^[VeCo:95-119]

## Установка и использование

Библиотека устанавливается через PyPI:

```bash
pip install veco_ai
```

Пример базового использования:

```python
from veco_ai import Vectorize

# Инициализация с JSON-бэкендом
veco = Vectorize(preload_json_path="vector_db.json")

# Векторизация файла
veco.vectorize("path/to/file.pdf", use_compression=True)

# Сохранение базы данных
veco.save_database("vector_db.json")

# RAG-запрос (требуется Ollama)
res = veco.query(
    database="vector_db.json",
    question="О чём этот документ?",
    llm_model="gemma3:12b",
)
print(res["answer"])
```

Для работы с GPU необходимо отдельно настроить PyTorch согласно официальному руководству; по умолчанию устанавливаются CPU-версии пакетов.

## Лицензия и доступность

Проект опубликован на GitHub под лицензией **CC0 1.0 Universal** (общественное достояние). Репозиторий поддерживается Matthias Pohl (ames wiring GmbH) под именем пользователя MatthiasPohlAmberg.
^[VeCo:40-43]

## Key Data

- veco
=
Vectorize
- preload_json_path
=
"vector_db.json"
- database
=
"vector_db.json"
- question
=
"What is this document about?"
- llm_model
=
"gemma3:12b"
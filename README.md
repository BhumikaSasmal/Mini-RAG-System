# Mini-RAG-System Week 5

The purpose of Week 5 is to build on the existing Week 4 implementation by connecting semantic retrieval with answer generation, source display, and a clean user-facing question-answering flow.

## Week 5 Scope
- Connect semantic retrieval output with an answer-generation layer.
- Prepare a structured prompt using retrieved chunks as context.
- Add an LLM service or approved mock response service for answer generation.
- Display answers with supporting source details such as file name, page number, and chunk identifier.
- Improve the Streamlit flow so uploaded documents can be queried in a clear chat-style or question-answer format.
- Create a manual test log covering retrieval, answer quality, source display, and edge cases.
- Update README with Week 4 setup, workflow, completed scope, limitations, and next steps.
---

## Tools and Libraries Used
- Python
- PyMuPDF (`fitz`)
- Chroma DB
- Sentence Transformers
- Virtual Environment
- pip
- VS Code
- Streamlit
- Git and GitHub

---

## Setup Instructions

1. Create and activate a virtual environment.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Upload either:
- `sample_policy.txt`
- `sample_report.pdf`

5. Click:

```text
Build / Rebuild Vector Index
```

6. Run semantic search queries from the UI.

---

## How to Test Week 5

1. Launch the Streamlit application.

2. Upload a TXT or PDF document.

3. Verify:
- chunk preview
- metadata
- page handling
- JSON export

4. Build the vector index using the indexing button.

5. Run semantic search queries such as:
- "What is the purpose of a sample policy?"
- "Why is communication important?"
- "What are the review requirements?"

6. Verify:
- Answer generation
- Source attribution
- Metadata display
- Retrieved context preview
- Insufficient-context handling: The UI should notify if the uploaded document does not have enough context to answer the query.


8. Run retrieval evaluation manually:

```bash
python src/retrieval_test.py
```

8. Check generated results:

```text
outputs/retrieval_test_results.md
```

---

## Folder Structure

```text
mini-rag-system/
├── app.py
├── README.md
├── requirements.txt
├── data/
│ └── sample_docs/
│ ├── sample_policy.txt
│ ├── sample_report.pdf
│ └── sample_scanned.pdf
| └── README.md
├── outputs/
│ ├── chunks_preview_txt.json
│ ├── chunks_preview_pdf.json
│ ├── week4_sample_outputs.md
│ └── retrieval_test_results.md
├── src/
│ ├── __init__.py
│ ├── config.py
│ ├── document_loader.py
│ ├── text_cleaning.py
│ ├── chunking.py
│ ├── embedding_service.py
│ ├── vector_store.py
│ ├── index_chunks.py
│ ├── llm_service.py
│ ├── rag_pipeline.py
│ ├── prompt_template.py
│ └── pipeline.py
├── tests/
│ ├── manual_test_log.md
│ └── week3_manual_test_log.md
│ └── week4_manual_test_log.md
└── legacy/
  ├── text_processing.py
  ├── sample.txt
  └── run_text_demo.py
```

---

## Embedding Strategy

### Local Sentence Transformers

Model used:

```text
all-MiniLM-L6-v2
```

### Pros
- No API key required
- No usage cost
- Works offline after initial model download
- Easy to test locally

### Limitations
- First model load can be slow
- Performance depends on local hardware
- Retrieval quality is still basic and depends heavily on chunking quality

---

## Chunk Metadata

Each chunk stores metadata used during retrieval and debugging.

### chunk_id

Example:

```text
sample_report.pdf_p3_c12
```

Meaning:
- `sample_report.pdf` → source file
- `p3` → page number
- `c12` → global chunk number

NOTE: page number metadata is only applicable for PDF files. For .txt files, there is no page number in chunk_id.

Example:

```text
sample_policy.txt_c3
```

### chunk_index

Represents the local chunk position within a page or document section.

Example:
- `0`
- `1`
- `2`

---

## Vector Store Persistence

Chroma DB uses persistent storage.

This allows:

- Indexed documents to remain available after application restart
- Previously indexed documents to remain searchable
- Multi-document retrieval across sessions

Duplicate chunks are not added when an already-indexed document is processed again.

---



## OCR and Scanned PDF Note

The current implementation works only with machine-readable PDFs.

Scanned PDFs require OCR (Optical Character Recognition), which is currently out of scope unless added in a future version.

Example:
- sample_report.pdf → supported
- sample_scanned.pdf → not supported yet

## LLM Service Modes
### Mock Mode

Used for local testing and demonstrations.

Benefits:

- No API access required
- Deterministic behavior
- Suitable for coursework demonstrations

#### Generating an answer using the configured LLM mode
In mock mode, no LLM inference is performed. The response is an
extractive answer formed from the first retrieved context sentences
and is intended only for testing the RAG pipeline.

Rather than generating a response from the prompt, this method
returns the first one or two sentences from the retrieved context.
This provides a deterministic, extractive answer and should not be
interpreted as true LLM reasoning.

The prompt in prompt_template.py is unused in mock mode. The prompt is designed to be consistent with the production LLM workflow.
In mock mode, it is intentionally ignored because the response is generated directly from the retrieved context.

Mock mode does not send a prompt to an LLM.

NOTE: Currently, no API mode has been added.

## Limitations and Planned Improvements

| Current Limitation | Planned Improvement |
|-------------------|---------------------|
| Retrieval quality depends on chunk quality | Improved ranking and retrieval strategies |
| Simple chunking approach | More advanced sentence-aware chunking |
| Limited answer generation in mock mode | Full LLM integration |
| No OCR support | OCR pipeline for scanned PDFs |
| Basic retrieval filtering | Relevance thresholds and reranking |
| Local embedding model only | Optional cloud embedding providers |

---

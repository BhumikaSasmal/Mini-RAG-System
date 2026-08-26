# Mini-RAG-System Week 5

The Week 5 assignment begins from the current Week 4 codebase. The existing modules for document
ingestion, chunking, embeddings, vector storage, retrieval, prompt creation, answer generation, source
display, and manual testing are expected to remain as the foundation for this phase.

## Week 5 Scope
- Refine the RAG answer-generation flow so that the response structure is consistent across the
application, test outputs, and documentation.
- Improve source handling so that every displayed answer is traceable to retrieved chunks with clear file
name, page value, chunk ID, and preview text.
- Clarify the difference between mock answer generation and API-based LLM answer generation in the
application and README.
- Improve index management, including duplicate handling and clear rebuild behavior.
- Strengthen testing evidence using expected result, actual result, status, and remarks for each test case.
- Prepare the project for Week 6 enhancements such as better UI polish, optional real LLM integration,
evaluation metrics, and deployment readiness.
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

4. Click **Build / Update Vector Index** to index the processed chunks.

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
- Mock Mode Clarification: The UI should notify when answers are retrieved using Mock Mode.
- Duplicate Indexing: The UI should notify when the same file is indexed again and no new chunks are added.


8. Run retrieval evaluation manually:

```bash
python src/retrieval_test.py
```

9. Check generated results:

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
├── WorkLog_Week5.xlsm
├── vector_store/
├── data/
│ └── sample_docs/
│ ├── sample_policy.txt
│ ├── sample_report.pdf
│ └── sample_scanned.pdf
| └── README.md
├── outputs/
│ ├── chunks_preview_txt.json
│ ├── chunks_preview_pdf.json
│ ├── week5_sample_outputs.md
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
│ └── week5_manual_test_log.md
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

#### NOTE: Currently, no API mode has been added.
#### NOTE: UI will show a notification when a query is run in mock mode.

## Limitations and Planned Improvements

| Current Limitation | Planned Improvement |
|-------------------|---------------------|
| Retrieval quality depends on chunk quality | Improved ranking and retrieval strategies |
| Simple chunking approach | More advanced sentence-aware chunking |
| Limited answer generation in mock mode | Full LLM integration |
| No OCR support | OCR pipeline for scanned PDFs |
| Local embedding model only | Optional cloud embedding providers |

---

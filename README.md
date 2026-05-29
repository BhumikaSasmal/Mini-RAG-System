# Mini-RAG-System Week 3

The aim of Week 3 is to convert document chunks into embeddings and store them in a persistent vector database.

## Week 3 Scope
- Raw document text that can be cleaned and chunked before indexing
- Reduces noise before embeddings are generated
- Controls the size and quality of text units sent to the embedding model
- Allows search results to show source file, page number, chunk index, and other context
- Streamlit upload/preview flow extended to include indexing status and semantic search
- Retrieval testing added for evaluating search quality
- README and work log updated with embedding choices, setup steps, and retrieval testing

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

## How to Test Week 3

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

6. Run retrieval evaluation manually:

```bash
python src/retrieval_test.py
```

7. Check generated results:

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
├── outputs/
│ ├── chunks_preview_txt.json
│ ├── chunks_preview_pdf.json
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
│ └── pipeline.py
├── tests/
│ ├── manual_test_log.md
│ └── week3_manual_test_log.md
└── legacy/
  ├── text_processing.py
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

### `chunk_id`

Example:

```text
sample_report.pdf_p3_c12
```

Meaning:
- `sample_report.pdf` → source file
- `p3` → page number
- `c12` → global chunk number

### `chunk_index`

Represents the local chunk position within a page or document section.

Example:
- `0`
- `1`
- `2`

---

## Vector Index Behavior

The current indexing flow rebuilds the Chroma collection during indexing.

This means:
- Existing indexed chunks are removed
- Only the latest indexed dataset remains available

This behavior is intentional for Week 3 testing and debugging.

Future versions may support:
- incremental indexing
- multi-document persistence
- append-only indexing

---



## OCR and Scanned PDF Note

The current implementation works only with machine-readable PDFs.

Scanned PDFs require OCR (Optical Character Recognition), which is currently out of scope unless added in a future version.

Example:
- `sample_report.pdf` → supported
- `sample_scanned.pdf` → not fully supported yet

## Current Limitations and Planned Fixes

| Current Limitation | Planned Improvement |
|---|---|
| Retrieval quality is still basic | Improve chunking and ranking |
| Chunk overlap is simple word overlap | Sentence-aware chunking improvements |
| Only local embeddings are supported | Add optional cloud embedding APIs |
| Scanned PDFs are not processed correctly | Add OCR pipeline later |
| Rebuilding index removes previous data | Add incremental indexing |
| Initial model loading is slow | Add Streamlit caching and optimization |

---

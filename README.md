# Mini-RAG-System Week 6

The Week 6 release builds upon the foundational retrieval pipeline by integrating active LLM-backed answer generation via Google Gemini, introducing system mode toggling, establishing strict prompt-grounding controls, and implementing comprehensive automated unit testing.

---

## Week 6 Scope & Highlights

* **Google Gemini Integration (`gemini-3.6-flash`):** Replaced mock-only extractions with live, grounded natural language synthesis via the `google-genai` SDK.
* **Dual Execution Modes:** Seamless switching between `gemini` (LLM-backed answer synthesis) and `mock` (offline extractive fallback) modes via UI controls and configuration.
* **Strict Prompt Grounding & Fallback:** Enforced strict RAG system prompt constraints to eliminate hallucinations. Queries without sufficient document context cleanly trigger a safety message.
* **Source Traceability & Metadata:** Clear display of source attributions (file name, page number, chunk ID, and snippet preview) for every generated answer.
* **API Error Handling & Resilience:** Non-blocking UI warnings for missing `GEMINI_API_KEY` credentials and graceful exception handling for provider/API failures.
* **Automated & Manual Testing Evidence:** Unit testing suite covering `LLMService` using `pytest`, paired with comprehensive manual test logs for answer quality, source traceability, and mode comparison.

---

## Tools and Libraries Used

* **Language & Runtime:** Python 3.10+
* **LLM Provider:** Google Gemini API (`gemini-3.6-flash`) via `google-genai` SDK
* **UI Framework:** Streamlit
* **Vector Store & Embeddings:** Chroma DB & Sentence Transformers (`all-MiniLM-L6-v2`)
* **PDF Processing:** PyMuPDF (`fitz`)
* **Testing:** `pytest` & `unittest.mock`
* **Environment Management:** `python-dotenv`

---

## Setup & Configuration

### 1. Environment Setup

Create a `.env` file in the project root directory:

```env
LLM_MODE=gemini
GEMINI_API_KEY=your_actual_gemini_api_key_here
LLM_MODEL_NAME=gemini-3.6-flash

## Setup & Configuration

### 1. Environment Setup

Create a `.env` file in the project root directory:

```env
LLM_MODE=gemini
GEMINI_API_KEY=your_actual_gemini_api_key_here
LLM_MODEL_NAME=gemini-3.6-flash

```

* `LLM_MODE`: Set to `gemini` for live LLM response generation, or `mock` for deterministic extraction testing.
* `GEMINI_API_KEY`: Required when `LLM_MODE=gemini`.
* `LLM_MODEL_NAME`: Set to `gemini-3.6-flash`.

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Run the Streamlit Application

```bash
streamlit run app.py

```

---

## Week 6 Testing

### Running Automated Unit Tests

Execute the unit test suite covering `LLMService` mode switching, prompt formatting, and error handling:

```bash
python -m pytest tests/test_llm_service.py

```

### Manual Testing Workflow

1. **Upload Documents:** Upload `sample_policy.txt` or `sample_report.pdf` in the sidebar and click **Build / Update Vector Index**.
2. **Select Mode:** Toggle between `LLM (Gemini)` and `Mock` modes in the sidebar UI.
3. **Run Grounded Queries:**
* Query: *"What is a sample policy?"*
* Observe: Gemini mode synthesizes a natural, multi-sentence definition; sources display matching chunk IDs and page numbers (`N/A` for TXT, numeric for PDF).


4. **Test Insufficient Context:**
* Query: *"Who wrote Harry Potter?"*
* Observe: System correctly triggers the safety fallback string: *"The available document context is insufficient to answer this question."*


5. **Verify API Resilience:**
* Unset `GEMINI_API_KEY` in `.env` and switch to `gemini` mode.
* Observe: Application displays a non-blocking warning banner without crashing.



---

## Folder Structure

```text
mini-rag-system/
├── app.py
├── README.md
├── requirements.txt
├── vector_store/
├── data/
│   └── sample_docs/
│       ├── sample_policy.txt
│       ├── sample_report.pdf
│       └── sample_scanned.pdf
├── outputs/
│   ├── week6_evaluation_summary.md
│   ├── week6_sample_outputs.md
│   └── retrieval_test_results.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── document_loader.py
│   ├── chunking.py
│   ├── embedding_service.py
│   ├── vector_store.py
│   ├── llm_service.py
│   ├── rag_pipeline.py
│   └── prompt_template.py
└── tests/
    ├── test_llm_service.py
    └── week6_manual_test_log.md

```

---

## Execution Modes

| Feature | Mock Mode | Gemini Mode (`gemini-3.6-flash`) |
| --- | --- | --- |
| **Inference Source** | None (Deterministic extraction) | Google Gemini API |
| **Response Style** | First 1–2 raw sentences from context | Synthesized, well-formatted natural prose |
| **API Key Required** | No | Yes (`GEMINI_API_KEY`) |
| **Use Case** | Pipeline structure testing & offline development | Production RAG answer generation |
| **Grounding Enforcement** | Exact chunk subset | Strict system prompt instructions + fallback |

---

## Chunk Metadata & Vector Persistence

Chroma DB persists indexed vector embeddings across restarts. Chunks store granular metadata for strict source attribution:

* **PDF Chunk Format:** `sample_report.pdf_p1_c0` (`p1` = Page 1, `c0` = Chunk 0)
* **TXT Chunk Format:** `sample_policy.txt_c0` (Page is displayed as `N/A`)

Duplicate document uploads are detected during ingestion to prevent redundant chunk storage in the database.


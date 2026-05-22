# Mini-RAG-System Week 3

The aim of week 3 is to convert document chunks into embeddings and store them in a persistent vector database.

## Week 3 Scope
- Raw document text that can be cleaned and chunked before indexing
- Reduces noise before embeddings are generated
- Controls the size and quality of text units sent to the embedding model
- Allows search results to show source file, page number, chunk index, and other context
- Streamlit upload/preview flow will be extended to include indexing status and test retrieval
- README and work log started. Will be updated with embedding choices, setup steps, and test results

## Tools and Libraries Used
-  Python
-  fitz
-  Chroma DB
-  Sentence Transformer
-  Virtual Environment 
-  pip
-  VS Code
-  Streamlit
-  Git and GitHub

## Setup Instructions
- Install Python 3.10 or above and verify with: python --version.
- Install Visual Studio Code and add the Python extension.
- Create a Python virtual environment using: python -m venv venv.
- Activate the environment. On Windows, use: venv/Scripts/activate. On Mac/Linux use: source venv/bin/activate.
- Install initial packages: pip install streamlit pandas numpy python-dotenv.

## Streamlit App 
- Navigate to app.py, open the terminal, and run it using: streamlit run app.py
  
## Folder Structure
mini-rag-system/
- app.py
- requirements.txt
- README.md
- legacy/ #contains files from previous week that may not be relevant to week 2 updates
  - run_text_demo.py
  - sample.txt
- data/
  - sample_docs/
    - sample_policy.txt
    - sample_report.pdf
    - sample_scanned.pdf
    - README.md
- notebooks/
- outputs/
  - chunks_preview.json
  - retrieval_test_results.md
- src/
  - __init__.py
  - document_loader.py
  - text_cleaning.py
  - chunking.py
  - schemas.py
  - config.py
  - embedding_service.py
  - vector_store.py
  - index_chunks.py
  - retrieval_test.py
- tests/
  - week3_manual_test_log.md

## Known Limitations
- Chunks generated may not be very consistent
- The results for queries may not be very accurate
- The Streamlit app is taking a long time to load when first opened.

## Next Steps
- Advanced OCR for scanned PDFs
- Cloud deployment
- Production-grade UI design

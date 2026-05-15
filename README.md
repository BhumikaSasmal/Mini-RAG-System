# Mini-RAG-System Week 2

The aim is to have a working document ingestion pipeline. The system should accept simple
text and PDF documents, extract usable text, clean the extracted content, split it into searchable chunks, and attach metadata
to every chunk, and show the results in a basic Streamlit interface.

## Problem Statement
- Build the foundation that will be used for embeddings and vector search in Week 3.
- Keep the implementation simple, modular, and testable.
- Do not focus on chatbot answers yet. Week 2 is about preparing high-quality document text for retrieval.
- Document every design decision so the next stage is easy to continue.

## Week 2 Scope
- Read .txt and .pdf files
- Clean and normalize extracted text
- Create text chunks with overlap
- Attach chunk metadata
- Show upload and chunk preview
- Write README and testing notes

## Tools and Libraries Used
-  Python
-  pypdf
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
  - text_processing.py
- data/
  - sample_docs/
    - sample_policy.txt
    - sample_report.pdf
    - sample_scanned.pdf
    - README.md
- notebooks/
- outputs/
  - chunks_preview_pdf.json
  - chunks_preview_scanned.json
  - chunks_preview_txt.json
- src/
  - __init__.py
  - document_loader.py
  - text_cleaning.py
  - text_processing.py
  - chunking.py
  - schemas.py
  - pipeline.py
- tests/
  - manual_test_log.md

## Known Limitations
- Content in scanned PDFs is not recognised, whether it is printed or handwritten.
- In .txt files, the system is unable to differentiate between pages and paragraphs. If a file has 10 paragraphs, it shows 10 for both paragraph and page count => Fixed: System displays N/A for page count in .txt files.
- Messily formatted PDFs produce more inconsistent chunks, but the text extraction is still fine.
- UI is still very basic.

## Next Steps
- Vector database integration
- Advanced OCR for scanned PDFs
- Cloud deployment
- Production-grade UI design

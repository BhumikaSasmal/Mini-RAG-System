# Mini-RAG-System

Week 1 focuses on building the foundation of a mini RAG system.
Users can upload documents, and the system extracts and processes the text for use.
Basic keyword-based search is implemented to answer user queries from the document.

## Problem Statement
Week 1 is the foundation phase of the Mini RAG System project. The objective is not to build the final AI chatbot
yet. The objective is to ensure understanding of the project workflow, have the correct development
setup, process basic text with Python, run a simple Streamlit interface, and maintain clean
documentation and version control.

## Week 1 Scope
- Set up a reproducible Python project environment using a virtual environment and requirements.txt.
- Read, clean, and search text using Python.
- Create a basic Streamlit app with file upload and user input fields.
- Use Git for basic version control: status, add, commit, and repository hygiene.
- Prepare professional documentation: README, setup notes, work log, and issue tracker.

## Tools and Libraries Used
-  Basic Python file handling
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
- mini-rag-system/
  - data/
  - notebooks/
  - src/
    - text_processing.py
  - tests/
  - app.py
  - requirements.txt
  - sample.txt
  - README.md
  - .gitignore

## Known Limitations
- Query search is based only on keywords. Semantics cannot be recognised by the system yet.
- Results may not always return the most relevant chunks first.
- UI is very basic and lacks features like history, highlighting, or source referencing.

## Next Steps
- Implement semantic search using embeddings for better accuracy.
- Add chunking strategy to improve retrieval from large documents.
- Improve UI with chat history and better formatting.

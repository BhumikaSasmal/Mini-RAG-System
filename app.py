import streamlit as st
import tempfile
import os
import json
from src.pipeline import process_document

st.title("Mini RAG System - Document Inspector")
st.write("Upload a TXT or PDF file to inspect extracted chunks.")

uploaded_file = st.file_uploader("Upload file", type=["txt", "pdf"])

if uploaded_file is not None:
    
    file_name = uploaded_file.name
    file_type = file_name.split(".")[-1]
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name
    
    result = process_document(temp_path)
    
    if isinstance(result, dict) and "error" in result:
        st.error(result["error"])
    else:
        chunks = result
        
        total_chars = sum(c["char_count"] for c in chunks)
        pages = set(c["page_number"] for c in chunks)
        
        st.subheader("File Details")
        st.write(f"File Name: {file_name}")
        st.write(f"File Type: {file_type}")
        st.write(f"Total Characters: {total_chars}")
        page_count = "N/A" if file_type == "txt" else len(pages)
        st.write(f"Page Count: {page_count}")
        st.write(f"Chunk Count: {len(chunks)}")
        
        st.subheader("Chunk Preview")
        
        for c in chunks[:5]:
            with st.expander(f"{c['chunk_id']} (Page {c['page_number']})"):
                st.write(c["text"])
        
        json_data = json.dumps(chunks, indent=2, ensure_ascii=False)
        
        st.download_button(
            label="Download chunks_preview.json",
            data=json_data,
            file_name="chunks_preview.json",
            mime="application/json"
        )
    
    os.remove(temp_path)

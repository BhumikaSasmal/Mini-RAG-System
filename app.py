import streamlit as st
from src.text_processing import *

st.title("Mini RAG System - Week 1 Prototype")
st.write("Upload a text file and ask questions to find relevant parts of the document.")


uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    clean_text = basic_clean_text(text)
    st.subheader("Text Preview (First 1000 characters)")
    st.write(text[:1000])
    stats = count_text_stats(clean_text)
    paragraphs = split_into_paragraphs(text)
    st.subheader("Document Statistics")
    st.write(f"Characters: {stats['characters']}")
    st.write(f"Words: {stats['words']}")
    st.write(f"Sentences: {stats['sentences']}")
    st.write(f"Paragraphs: {len(paragraphs)}")
    query = st.text_input("Enter your question:")
    if st.button("Search Document"):
        if not query.strip():
            st.error("Please enter a question.")      
        else:
            results = keyword_search(clean_text, query)
            st.subheader("Results")
            if results:
                for i, res in enumerate(results, 1):
                    st.write(f"{i}. {res}")
            else:
                st.warning("No matching paragraph found.")

else:
    st.error("Please upload a .txt file to proceed.")
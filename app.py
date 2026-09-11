import streamlit as st
import tempfile
import os
import json

from src.pipeline import process_document
from src.rag_pipeline import RAGPipeline
from src.index_chunks import run_indexing

st.set_page_config(
    page_title="Mini RAG System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Mini RAG System")


st.sidebar.header("Pipeline Configuration")

selected_mode = st.sidebar.radio(
    "Select Answer Mode:",
    options=["gemini", "mock"],
    format_func=lambda x: "LLM Mode (Google Gemini)" if x == "gemini" else "Mock Mode (Extraction)",
    help="Gemini Mode uses gemini-2.5-flash for answer synthesis; Mock Mode extracts sentences strictly."
)


if selected_mode == "gemini" and not os.getenv("GEMINI_API_KEY"):
    st.sidebar.error(" `GEMINI_API_KEY` is not set in your environment!")
else:
    st.sidebar.success(f"Active Mode: **{selected_mode.upper()}**")


st.header("1. Upload & Inspect Document")

uploaded_file = st.file_uploader(
    "Upload TXT or PDF document",
    type=["txt", "pdf"]
)

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_type = file_name.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    try:
        chunks, summary = process_document(temp_path, source_name=file_name)

        if not chunks:
            error_message = summary.get("error", "Processing failed.")
            st.error(error_message)
        else:
            st.session_state.chunks = chunks
            st.session_state.summary = summary
            st.session_state.file_type = file_type

            total_chars = sum(c.get("char_count", 0) for c in chunks)
            pages = "N/A" if file_type == "txt" else len({
                c.get("page_number") for c in chunks if c.get("page_number") is not None
            })

            st.subheader("File Details")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Chunks", len(chunks))
            col2.metric("Characters", total_chars)
            col3.metric("Pages", pages)
            col4.metric("Avg Chunk Size", int(summary.get("average_char_count", 0)))

            st.subheader("Chunk Preview")
            for c in chunks[:5]:
                chunk_id = c.get("chunk_id", "unknown")
                page_number = c.get("page_number")
                title = chunk_id if file_type == "txt" else f"{chunk_id} | Page {page_number}"
                
                with st.expander(title):
                    st.text(c.get("text", ""))

            json_data = json.dumps(chunks, indent=2, ensure_ascii=False)
            st.download_button(
                label="Download Chunks JSON",
                data=json_data,
                file_name="chunks_preview.json",
                mime="application/json"
            )

    except Exception as e:
        st.error(f"Processing error: {str(e)}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)



st.header("2. Build Vector Index")

if st.button("Build / Update Vector Index"):
    if st.session_state.chunks is None:
        st.warning("Upload and process a document first.")
    else:
        try:
            with st.spinner("Building vector index..."):
                stats = run_indexing(st.session_state.chunks)

            if stats["added"] == 0:
                st.info("No new chunks were added. Document is already indexed.")
            else:
                st.success(f"Added {stats['added']} chunks. Collection size: {stats['total']}.")
        except Exception as e:
            st.error(f"Indexing failed: {str(e)}")



st.header("3. Semantic Search & Answer Generation")

query = st.text_input("Enter your question")

if st.button("Submit Question"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        try:
            
            pipeline = RAGPipeline(llm_mode=selected_mode)

            if pipeline.store.count() == 0:
                st.info("No documents indexed. Upload and index a document first.")
            else:
                with st.spinner(f"Processing in **{selected_mode.upper()}** mode..."):
                    response = pipeline.answer_question(query)

                st.subheader("Generated Answer")
                st.write(response["answer"])

                
                if response.get("mode") == "mock":
                    st.warning("⚠️ **Mock Mode Active:** Answer extracted from context without LLM reasoning.")
                else:
                    st.caption("🤖 Answer generated using LLM based on retrieved context.")

                
                sources = response.get("sources", [])
                if sources:
                    st.subheader("Sources")
                    for src in sources:
                        st.markdown(
                            f"**File:** `{src.get('source_file')}` | "
                            f"**Page:** `{src.get('page_number')}` | "
                            f"**Chunk ID:** `{src.get('chunk_id')}`"
                        )
                        st.caption(f"Preview: {src.get('preview')}...")
                        st.divider()

                
                answer_context = response.get("answer_context", [])
                if answer_context:
                    with st.expander("Inspect Retained Context Chunks"):
                        for i, result in enumerate(answer_context):
                            meta = result.get("metadata", {})
                            page_val = meta.get("page_number")
                            if page_val in [-1, None]:
                                page_val = "N/A"

                            st.markdown(f"**Chunk {i+1}** | File: {meta.get('source_file')} | Page: {page_val}")
                            st.text_area(
                                label=f"Chunk Text ({meta.get('chunk_id', i)})",
                                value=result.get("text", ""),
                                height=150,
                                key=f"ctx_{i}"
                            )

        except Exception as e:
            st.error(f"Search/Generation failed: {str(e)}")

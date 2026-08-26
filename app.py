import streamlit as st
import tempfile
import os
import json

from src.pipeline import process_document
from src.rag_pipeline import RAGPipeline
from src.index_chunks import run_indexing


st.set_page_config(
    page_title="Mini RAG System",
    layout="wide"
)

st.title("Mini RAG System")

st.info(
    "The first embedding/model load may take some time."
)

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "file_type" not in st.session_state:
    st.session_state.file_type = None

st.header("1. Upload & Inspect Document")

uploaded_file = st.file_uploader(
    "Upload TXT or PDF",
    type=["txt", "pdf"]
)

if uploaded_file is not None:

    file_name = uploaded_file.name

    file_type = file_name.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{file_type}"
    ) as tmp:

        tmp.write(uploaded_file.read())

        temp_path = tmp.name

    try:
        chunks, summary = process_document(
            temp_path,
            source_name=file_name
        )

        if not chunks:

            error_message = summary.get(
                "error",
                "Processing failed."
            )

            st.error(error_message)

        else:
            st.session_state.chunks = chunks
            st.session_state.summary = summary
            st.session_state.file_type = file_type

            total_chars = sum(
                c.get("char_count", 0)
                for c in chunks
            )

            if file_type == "txt":
                pages = "N/A"
            else:
                pages = len(
                    {
                        c.get("page_number")
                        for c in chunks
                        if c.get("page_number") is not None
                    }
                )

            st.subheader("File Details")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Chunks", len(chunks))
            col2.metric("Characters", total_chars)
            col3.metric("Pages", pages)
            col4.metric(
                "Avg Chunk Size",
                int(summary.get("average_char_count", 0))
            )

            st.subheader("Chunk Preview")

            preview_chunks = chunks[:5]

            for c in preview_chunks:

                chunk_id = c.get("chunk_id", "unknown")
                page_number = c.get("page_number")
                text = c.get("text", "")

                if file_type == "txt":
                    expander_title = chunk_id
                else:
                    expander_title = f"{chunk_id} | Page {page_number}"

                with st.expander(expander_title):
                    st.text(text)

            json_data = json.dumps(
                chunks,
                indent=2,
                ensure_ascii=False
            )

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
                st.info(
                    "No new chunks were added. "
                    "This document appears to have already been indexed."
                )
            else:
                st.success(
                    f"Added {stats['added']} chunks. "
                    f"Collection now contains {stats['total']} chunks."
                )

        except Exception as e:
            st.error(f"Indexing failed: {str(e)}")

st.header("3. Semantic Search")

query = st.text_input("Enter a query")

if st.button("Search Relevant Chunks"):

    if not query.strip():
        st.warning("Enter a query first.")

    else:
        try:
            pipeline = RAGPipeline()

            if pipeline.store.count() == 0:
                st.info(
                    "No documents have been indexed yet. "
                    "Upload a document and build the vector index first."
                )

            else:
                with st.spinner(
                    "Retrieving document context and generating answer..."
                ):
                    response = pipeline.answer_question(query)

                results = response.get("retrieved_results", [])

                if response.get("status") == "insufficient_context":
                    st.warning(
                        "The available document context is insufficient "
                        "to answer this question."
                    )
                    st.subheader("Answer")
                    st.text(response["answer"])

                else:
                    results = sorted(
                        results,
                        key=lambda x: x.get("score", float("inf"))
                    )

                    st.subheader("Answer")
                    st.text(response["answer"])

                mode = response.get("mode", "unknown")

                if mode == "mock":
                    st.warning(
                        "Mock Mode: Answers are extraction-based and do not use full LLM reasoning."
                    )
                else:
                    st.caption(f"Mode: {mode}")

                st.subheader("Sources")

                for source in response.get("sources", []):

                    st.markdown(f"""
                        **Source File:** {source.get('source_file')}

                        **Page:** {source.get('page_number')}

                        **Chunk ID:** {source.get('chunk_id', 'N/A')}
                        
                        **Preview:** {source["preview"]}
                        
                        """)
                    
                answer_context = response.get("answer_context", [])

                if answer_context:

                    with st.expander("Context Used for Answer Generation"):

                        for i, result in enumerate(answer_context):

                            metadata = result.get("metadata", {})

                            page_value = metadata.get("page_number")

                            if page_value == -1:
                                page_value = "N/A"

                            st.markdown(f"### Context {i + 1}")

                            st.write(
                                f"Source File: {metadata.get('source_file')}"
                            )

                            st.write(f"Page: {page_value}")

                            st.write(
                                f"Chunk ID: {metadata.get('chunk_id', 'N/A')}"
                            )

                            st.text_area(
                                label="Context Text",
                                value=result.get("text", ""),
                                height=220,
                                key=f"context_{i}"
                            )

                            st.markdown("---")

                                      

                with st.expander("Retrieved Results"):

                    for i, r in enumerate(results):

                        metadata = r.get("metadata", {})
                        distance = r.get("score", 0)

                        similarity = round(1 / (1 + distance), 4)

                        st.markdown(f"### Result {i + 1}")

                        col1, col2, col3 = st.columns(3)

                        col1.metric(
                            "Similarity",
                            similarity
                        )

                        page_value = metadata.get("page_number")

                        if page_value == -1:
                            page_value = "N/A"

                        col2.metric(
                            "Page",
                            page_value
                        )

                        col3.metric(
                            "Chunk",
                            metadata.get("chunk_index")
                        )

                        st.write(
                            f"Source File: {metadata.get('source_file')}"
                        )

                        st.text_area(
                            label="Retrieved Text",
                            value=r.get("text", ""),
                            height=220,
                            key=f"result_{i}"
                        )

                        st.markdown("---")

        except Exception as e:
            st.error(f"Search failed: {str(e)}")

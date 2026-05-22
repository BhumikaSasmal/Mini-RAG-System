import streamlit as st
import tempfile
import os
import json

from src.pipeline import process_document
from src.index_chunks import run_indexing
from src.vector_store import VectorStore

st.set_page_config(
    page_title="Mini RAG System",
    layout="wide"
)

st.title("Mini RAG System")

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "summary" not in st.session_state:
    st.session_state.summary = None

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
        chunks, summary = process_document(temp_path)

        if not isinstance(chunks, list):
            st.error("Processing failed.")
        else:
            st.session_state.chunks = chunks
            st.session_state.summary = summary

            total_chars = sum(
                c.get("char_count", 0)
                for c in chunks
            )

            pages = sorted(
                list(
                    set(
                        c.get("page_number", 1)
                        for c in chunks
                    )
                )
            )

            st.subheader("File Details")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Chunks", len(chunks))
            col2.metric("Characters", total_chars)
            col3.metric("Pages", len(pages))
            col4.metric(
                "Avg Chunk Size",
                int(summary.get("average_char_count", 0))
            )

            st.subheader("Chunk Preview")

            preview_chunks = chunks[:5]

            for c in preview_chunks:
                chunk_id = c.get("chunk_id", "unknown")
                page_number = c.get("page_number", "?")
                text = c.get("text", "")

                with st.expander(
                    f"{chunk_id} | Page {page_number}"
                ):
                    st.text(text)

            json_data = json.dumps(
                chunks,
                indent=2,
                ensure_ascii=False
            )

            st.download_button(
                label="Download chunks JSON",
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

if st.button("Build / Rebuild Vector Index"):

    if st.session_state.chunks is None:
        st.warning("Upload and process a document first.")

    else:
        try:
            with st.spinner("Building vector index..."):
                run_indexing(st.session_state.chunks)

            st.success(
                f"Successfully indexed {len(st.session_state.chunks)} chunks."
            )

        except Exception as e:
            st.error(f"Indexing failed: {str(e)}")

st.header("3. Semantic Search")

query = st.text_input(
    "Enter a query"
)

if st.button("Search Relevant Chunks"):

    if not query.strip():
        st.warning("Enter a query first.")

    else:
        try:
            store = VectorStore()

            results = store.query(
                query,
                top_k=3
            )

            results = sorted(
                results,
                key=lambda x: x.get("score", float("inf"))
            )

            if not results:
                st.warning("No relevant results found.")

            else:
                st.subheader("Top Matches")

                for i, r in enumerate(results):

                    metadata = r.get("metadata", {})

                    distance = r.get("score", 0)
                    similarity = round(
                        1 / (1 + distance),
                        4
                    )

                    st.markdown(
                        f"### Result {i + 1}"
                    )

                    col1, col2, col3 = st.columns(3)

                    col1.metric(
                        "Similarity",
                        similarity
                    )

                    col2.metric(
                        "Page",
                        metadata.get("page_number")
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

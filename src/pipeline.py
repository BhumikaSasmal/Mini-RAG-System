import os
import json
import csv

from src.document_loader import load_txt, load_pdf
from src.text_cleaning import clean_text
from src.chunking import process_chunks


def process_document(file_path):
    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        raw_records = load_txt(file_path)

    elif ext == "pdf":
        raw_records = load_pdf(file_path)

    else:
        return [], {"error": "Unsupported file type"}

    cleaned = clean_text(raw_records)

    chunks, summary = process_chunks(cleaned)

    return chunks, summary


def export_to_json(chunks, output_path="outputs/chunks.json"):
    os.makedirs("outputs", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)


def export_to_csv(chunks, output_path="outputs/chunks.csv"):
    os.makedirs("outputs", exist_ok=True)

    keys = [
        "source_file",
        "file_type",
        "page_number",
        "chunk_id",
        "chunk_index",
        "char_count",
        "text"
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(chunks)

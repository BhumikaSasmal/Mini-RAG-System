import os
import json
import csv
from src.document_loader import load_txt, load_pdf
from src.text_cleaning import clean_text
from src.chunking import chunk_text

def process_document(file_path):
    ext = file_path.split(".")[-1].lower()
    
    if ext == "txt":
        records = load_txt(file_path)
    elif ext == "pdf":
        records = load_pdf(file_path)
    else:
        return {"error": "Unsupported file type"}
    
    if isinstance(records, dict) and "error" in records:
        return records
    
    all_chunks = []
    file_name = os.path.basename(file_path).split(".")[0]
    
    for record in records:
        cleaned = clean_text(record["text"])
        chunks = chunk_text(cleaned)
        
        for i, chunk in enumerate(chunks, start=1):
            chunk_id = f"{file_name}_p{record['page_number']}_c{i}"
            
            all_chunks.append({
                "source_file": record["source_file"],
                "file_type": record["file_type"],
                "page_number": record["page_number"],
                "chunk_id": chunk_id,
                "chunk_no": i,
                "char_count": chunk["char_count"],
                "text": chunk["text"]
            })
    
    return all_chunks


def export_to_json(chunks, output_path="outputs/chunks.json"):
    os.makedirs("outputs", exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)


def export_to_csv(chunks, output_path="outputs/chunks.csv"):
    os.makedirs("outputs", exist_ok=True)
    
    keys = ["source_file", "file_type", "page_number", "chunk_id", "chunk_no", "char_count", "text"]
    
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(chunks)
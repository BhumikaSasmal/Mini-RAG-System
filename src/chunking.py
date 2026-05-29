import json
import os
import re
from src.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

def normalize_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()


def split_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()

    if not words:
        return []

    chunks = []
    start = 0

    sentence_endings = {".", "!", "?", ".\"", "!\"", "?\""}

    while start < len(words):
        end = min(start + chunk_size, len(words))

        if end < len(words):
            extended_end = min(end + 20, len(words))

            for i in range(end, extended_end):
                word = words[i].strip()

                if any(word.endswith(se) for se in sentence_endings):
                    end = i + 1
                    break

        chunk_words = words[start:end]

        chunk_text = " ".join(chunk_words).strip()

        if chunk_text:
            chunks.append(chunk_text)

        start += chunk_size - overlap

    return chunks


def create_chunks(records, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    global_index = 0

    for record in records:
        if not isinstance(record, dict):
            continue

        text = record.get("text", "")

        if isinstance(text, list):
            if len(text) > 0 and isinstance(text[0], dict):
                text = " ".join(item.get("text", "") for item in text)
            else:
                text = " ".join(str(item) for item in text)

        if not isinstance(text, str):
            continue

        text = normalize_text(text)

        if not text:
            continue

        source_file = os.path.basename(
            record.get("source_file", "unknown")
        )

        file_type = record.get("file_type", "unknown")
        page_number = record.get("page_number")

        text_chunks = split_text(
            text,
            chunk_size=chunk_size,
            overlap=overlap
        )

        for chunk_index, chunk_text in enumerate(text_chunks):
            chunk_id = f"{source_file}_p{page_number}_c{global_index}"

            chunks.append({
                "chunk_id": chunk_id,
                "text": chunk_text,
                "source_file": source_file,
                "file_type": file_type,
                "page_number": page_number,
                "chunk_index": chunk_index,
                "char_count": len(chunk_text)
            })

            global_index += 1

    return chunks


def clean_chunks(chunks, min_length=50):
    seen = set()
    cleaned = []

    for chunk in chunks:
        if not isinstance(chunk, dict):
            continue

        text = chunk.get("text", "").strip()

        if not text:
            continue

        if len(text) < min_length:
            continue

        normalized = text.lower()

        if normalized in seen:
            continue

        seen.add(normalized)
        cleaned.append(chunk)

    return cleaned


def validate_chunks(chunks):
    total = len(chunks)

    empty_chunks = sum(
        1 for c in chunks
        if not c.get("text", "").strip()
    )

    ids = [
        c.get("chunk_id")
        for c in chunks
        if isinstance(c, dict)
    ]

    duplicate_ids = len(ids) - len(set(ids))

    avg_char_count = (
        sum(c.get("char_count", 0) for c in chunks) / total
        if total > 0 else 0
    )

    return {
        "total_chunks": total,
        "average_char_count": avg_char_count,
        "empty_chunks": empty_chunks,
        "duplicate_id_count": duplicate_ids
    }


def save_chunks(chunks, output_path="outputs/chunks_clean.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)


def process_chunks(records, output_path="outputs/chunks_clean.json"):
    chunks = create_chunks(records)
    chunks = clean_chunks(chunks)

    summary = validate_chunks(chunks)

    save_chunks(chunks, output_path)

    return chunks, summary

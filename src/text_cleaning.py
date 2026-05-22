def clean_text(records):
    cleaned = []

    for record in records:
        text = record.get("text", "")

        if isinstance(text, list):
            text = " ".join([str(t) for t in text])

        if not isinstance(text, str):
            continue

        text = text.strip()

        if len(text) == 0:
            continue

        cleaned.append({
            "text": text,
            "page_number": record.get("page_number", 1),
            "source_file": record.get("source_file", "unknown"),
            "file_type": record.get("file_type", "unknown")
        })

    return cleaned

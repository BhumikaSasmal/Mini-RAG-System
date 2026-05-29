def clean_text(records):
    cleaned = []

    for record in records:
        if not isinstance(record, dict):
            continue

        text = record.get("text", "")

        if isinstance(text, list):
            text = " ".join(str(t) for t in text)

        if not isinstance(text, str):
            continue

        text = text.strip()

        if not text:
            continue

        paragraphs = []

        for paragraph in text.split("\n"):
            paragraph = " ".join(paragraph.split())

            if paragraph:
                paragraphs.append(paragraph)

        text = "\n\n".join(paragraphs)

        cleaned.append({
            **record,
            "text": text
        })

    return cleaned

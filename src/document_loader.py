import fitz


def normalize_text(text):
    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        cleaned_lines.append(line)

    text = " ".join(cleaned_lines)

    text = " ".join(text.split())

    return text.strip()


def load_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        text = normalize_text(text)

        return [{
            "text": text,
            "page_number": 1,
            "source_file": file_path,
            "file_type": "txt"
        }]

    except Exception as e:
        return {"error": str(e)}


def load_pdf(file_path):
    try:
        doc = fitz.open(file_path)

        records = []

        for i, page in enumerate(doc):
            text = page.get_text("text")

            text = normalize_text(text)

            if not text:
                continue

            records.append({
                "text": text,
                "page_number": i + 1,
                "source_file": file_path,
                "file_type": "pdf"
            })

        return records

    except Exception as e:
        return {"error": str(e)}

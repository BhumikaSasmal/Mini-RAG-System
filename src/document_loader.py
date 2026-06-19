import fitz


def normalize_text(text):
    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.rstrip()

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()


def load_txt(file_path, source_name=None):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        text = normalize_text(text)

        return [{
            "text": text,
            "page_number": None,
            "source_file": source_name or file_path,
            "file_type": "txt"
        }]

    except UnicodeDecodeError:
        return [{
            "error": "Encoding issue: unable to decode TXT file."
        }]

    except Exception as e:
        return [{
            "error": f"Failed to read TXT file: {str(e)}"
        }]

def load_pdf(file_path, source_name=None):
    try:
        doc = fitz.open(file_path)

        records = []

        for i, page in enumerate(doc):
            text = page.get_text("text")

            text = normalize_text(text)

            if not text.strip():
                continue

            records.append({
                "text": text,
                "page_number": i + 1,
                "source_file": source_name or file_path,
                "file_type": "pdf"
            })
        if not records:
            return [{
                "error": (
                    "PDF contains no extractable text. "
                    "It may be a scanned PDF requiring OCR."
                )
            }]

        return records

    except Exception as e:
        return [{
            "error": f"Unreadable PDF: {str(e)}"
        }]

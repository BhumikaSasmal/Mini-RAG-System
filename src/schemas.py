def create_document_schema(source_file, file_type, text, page_number=None):
    return {
        "source_file": source_file,
        "file_type": file_type,
        "page_number": page_number,
        "text": text
    }

def build_document_records(source_file, file_type, text=None, pages=None):

    records = []

    if file_type == "txt":
        records.append({
            "source_file": source_file,
            "file_type": file_type,
            "page_number": "N/A",
            "text": text
        })

    else:
        for page in pages:
            records.append({
                "source_file": source_file,
                "file_type": file_type,
                "page_number": page["page_number"],
                "text": page["text"]
            })

    return records

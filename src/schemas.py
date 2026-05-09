def create_document_schema(source_file, file_type, text, page_number=None):
    """
    Returns a standardized document record.
    """
    return {
        "source_file": source_file,
        "file_type": file_type,
        "page_number": page_number,
        "text": text
    }

def build_document_records(source_file, file_type, paragraphs):
    records = []
    
    for i, para in enumerate(paragraphs, start=1):
        record = {
            "source_file": source_file,
            "file_type": file_type,
            "page_number": i, 
            "text": para
        }
        records.append(record)
    
    return records
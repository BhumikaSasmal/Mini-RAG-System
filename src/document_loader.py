from src.schemas import build_document_records,create_document_schema
from src.text_processing import split_into_paragraphs
from pypdf import PdfReader

def load_txt(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return {"error": "File not found."}
    except Exception as e:
        return {"error": str(e)}

    if not text.strip():
        return {"error": "The uploaded file is empty."}
    
    paragraphs = split_into_paragraphs(text)
    
    records = build_document_records(
        source_file=file_path,
        file_type="txt",
        text=text,
        pages=None
    )
    
    return records

def load_pdf(file_path):
    
    records = []
    
    try:
        reader = PdfReader(file_path)
    except FileNotFoundError:
        return {"error": "File not found."}
    except Exception as e:
        return {"error": str(e)}

    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text()
            
            if text is None:
                text = ""
                print(f"Warning: No text found on page {i}")
        
        except Exception:
            text = ""
            print(f"Warning: Failed to extract page {i}")
        
        record = create_document_schema(
            source_file=file_path,
            file_type="pdf",
            page_number=i,
            text=text
        )
        
        records.append(record)
    
    return records

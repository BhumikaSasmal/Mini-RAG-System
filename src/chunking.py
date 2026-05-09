def chunk_text(text, chunk_size=1000, overlap=150):
    chunks = []
    start = 0
    chunk_id = 1
    
    text_length = len(text)
    
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        
        if end < text_length:
            last_period = chunk.rfind(".")
            if last_period != -1:
                end = start + last_period + 1
                chunk = text[start:end]
        
        chunk = chunk.strip()
        
        if chunk:
            chunks.append({
                "chunk_id": chunk_id,
                "text": chunk,
                "char_count": len(chunk)
            })
            chunk_id += 1
        
        start = end - overlap
    
    return chunks
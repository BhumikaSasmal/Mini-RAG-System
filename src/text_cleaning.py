import re

def clean_text(text):
    if not text:
        return ""
    
    text = text.replace("\r\n", "\n")
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    
    lines = text.split("\n")
    cleaned_lines = [line.strip() for line in lines]
    
    text = "\n".join(cleaned_lines)
    
    return text.strip()
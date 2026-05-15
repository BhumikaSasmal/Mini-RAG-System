def read_text_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."

def basic_clean_text(text):
    lines = text.splitlines()               
    cleaned_lines = [line.strip() for line in lines if line.strip() != ""]  
    return " ".join(cleaned_lines)             


def count_text_stats(text):
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    return {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count
    }

def split_into_paragraphs(text):
    text = text.replace("\r\n", "\n")
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if p.strip() != ""]

def keyword_search(text, query):
    sentences = text.split('.')   
    matches = [s.strip() for s in sentences if query.lower() in s.lower()]
    return matches


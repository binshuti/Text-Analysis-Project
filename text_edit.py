STOPWORDS = ["the", "and", "a", "an", "of", "to", "in", "is", "it", "for", "on", 
             "with", "that", "at", "by", "this", "be", "as", "from", "are", 
             "was", "were", "but", "not", "have", "has", "had", "he", "she", 
             "they", "them", "his", "her", "their", "you", "your", "i", "we", "our"]

def clean_text(text):
    """Making the text lowercase and removing both complex and strange characters and symbols."""
    text = text.lower()
    simple_text = ""
    for char in text:
        if char.isalpha() or char == " ":
            simple_text += char
        else:
            simple_text += " "
    return simple_text

def make_words(text):
    """Spliting  text into words."""
    words = text.split()
    return words

def remove_stopwords(words):
    """Take out common stopwords."""
    cleaned = []
    for w in words:
        if w not in STOPWORDS:
            cleaned.append(w)
    return cleaned

def split_sentences(text):
    """Roughly split sentences when we see a period."""
    sentences = text.split(".")
    new_list = []
    for s in sentences:
        s = s.strip()
        if len(s) > 0:
            new_list.append(s)
    return new_list

def full_clean(raw_text):
    """Do all cleaning steps and return words and sentences."""
    cleaned_text = clean_text(raw_text)
    sentences = split_sentences(raw_text)
    words = make_words(cleaned_text)
    final_words = remove_stopwords(words)
    return final_words, sentences

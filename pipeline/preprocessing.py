import spacy
import string

# Load SpaCy's English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """
    Tokenizes, removes stopwords, punctuation, and lemmatizes the text.
    """
    doc = nlp(text)
    tokens = []
    
    for token in doc:
        if not token.is_stop and token.text not in string.punctuation:
            tokens.append(token.lemma_)
    
    return tokens

def clean_and_preprocess_file(filename):
    """
    Reads a text file and preprocesses its content.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return preprocess_text(content)

# Example usage:
if __name__ == "__main__":
    preprocessed_tokens = clean_and_preprocess_file('web_data.txt')
    print(preprocessed_tokens)

import nltk
import string
import contractions
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def initialize_nltk():
    resources = ['punkt', 'stopwords', 'wordnet', 'omw-1.4', 'punkt_tab']
    for resource in resources:
        nltk.download(resource, quiet=True)

initialize_nltk()

def preprocess_text(text):
    """
    Text processing pipeline for normalization and token extraction.
    
    Pipeline stages:
    1. Case normalization
    2. Contraction expansion
    3. Punctuation filtering (preserving technical suffixes like ++, #, .NET)
    4. Tokenization (Punkt)
    5. Lexical filtration (Stopword removal)
    6. Morphological normalization (WordNet lemmatization)
    
    Returns:
        tuple: (list of tokens, space-separated normalized string)
    """
    if not isinstance(text, str):
        return [], ""

    # 1 Lowercase
    text = text.lower()

    # 2 Contractions
    text = contractions.fix(text)

    # 3 Remove Punctuation

    preserved_chars = "+#."
 
    # string.punctuation contains
    all_punct = string.punctuation
    for char in preserved_chars:
        all_punct = all_punct.replace(char, '')
    
    text = text.translate(str.maketrans('', '', all_punct))

    # 4 Tokenization
    tokens = word_tokenize(text)

    # 5 Stopword Removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w not in stop_words]

    # 6 Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]

    # Reconstruct cleaned text for phrase matching
    cleaned_text = " ".join(lemmatized_tokens)

    return lemmatized_tokens, cleaned_text

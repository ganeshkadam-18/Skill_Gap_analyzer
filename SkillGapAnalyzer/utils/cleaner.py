from .nlp_processor import preprocess_text

def clean_text(text):
    """
    Normalizes raw text input for downstream analysis.
    Executes the full NLP transformation pipeline including noise reduction,
    tokenization, and morphological normalization.
    """
    if not isinstance(text, str):
        return ""
    
    # Use the centralized NLP processor
    tokens, cleaned_text = preprocess_text(text)
    
    return cleaned_text

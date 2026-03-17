"""NLP preprocessing pipeline for Resume Skill Gap AI (Milestone 2).

This module implements the STRICT preprocessing workflow:

    Lowercase → Remove punctuation → Tokenization
    → Stopword Removal → Lemmatization

The goal is to transform raw text into a clean, normalized token list
that downstream components (skill extractor, matcher) can use.
"""

from __future__ import annotations

import re
import string
from dataclasses import dataclass
from typing import List

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


_NLTK_RESOURCES = [
    ("punkt", "tokenizers/punkt"),
    ("punkt_tab", "tokenizers/punkt_tab"),
    ("stopwords", "corpora/stopwords"),
    ("wordnet", "corpora/wordnet"),
    ("omw-1.4", "corpora/omw-1.4"),
]


def _ensure_nltk_resources_downloaded() -> None:
    """Download required NLTK resources if they are missing.

    This keeps setup simple for educational environments
    like internship projects and lab machines.
    """
    for resource_name, resource_path in _NLTK_RESOURCES:
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(resource_name, quiet=True)


_ensure_nltk_resources_downloaded()


_STOP_WORDS = set(stopwords.words("english"))
_LEMMATIZER = WordNetLemmatizer()
_PUNCT_TRANSLATION = str.maketrans("", "", string.punctuation)


@dataclass
class PreprocessingResult:
    """Container for preprocessing outputs.

    Attributes:
        original_text: The unmodified input text.
        cleaned_text: Text after lowercasing and punctuation removal.
        tokens: Final token list after stopword removal and lemmatization.
    """

    original_text: str
    cleaned_text: str
    tokens: List[str]


def _normalize_whitespace(text: str) -> str:
    """Collapse multiple spaces/newlines into a single space."""
    return re.sub(r"\s+", " ", text).strip()


def preprocess_text(text: str) -> PreprocessingResult:
    """Run the complete NLP preprocessing pipeline on `text`.

    Steps (in order):
        1. Lowercase
        2. Remove punctuation
        3. Tokenization
        4. Stopword removal
        5. Lemmatization

    Args:
        text: Raw input text.

    Returns:
        `PreprocessingResult` with original text, cleaned text, and final tokens.
    """
    original = text

    # 1. Lowercase
    lowered = text.lower()

    # 2. Remove punctuation
    no_punct = lowered.translate(_PUNCT_TRANSLATION)

    # Normalize whitespace to keep tokens readable
    cleaned_text = _normalize_whitespace(no_punct)

    # 3. Tokenization
    raw_tokens = word_tokenize(cleaned_text)

    # 4. Stopword removal
    tokens_no_stop = [t for t in raw_tokens if t not in _STOP_WORDS]

    # 5. Lemmatization
    lemmatized_tokens = [_LEMMATIZER.lemmatize(t) for t in tokens_no_stop]

    return PreprocessingResult(
        original_text=original,
        cleaned_text=cleaned_text,
        tokens=lemmatized_tokens,
    )


__all__ = ["PreprocessingResult", "preprocess_text"]


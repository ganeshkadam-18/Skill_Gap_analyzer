"""Skill extraction logic for Resume Skill Gap AI (Milestone 2).

This module converts preprocessed text into a set of detected skills.

Key design decisions:
    - Uses BOTH token-level information and the full cleaned text.
    - Supports multi-word skills (e.g. "machine learning").
    - Relies on the central skill database for consistency.
"""

from __future__ import annotations

from typing import Iterable, Set

from skill_database import ALL_SKILLS
from preprocessing import PreprocessingResult


def _extract_single_word_skills(tokens: Iterable[str]) -> Set[str]:
    """Extract skills that consist of a single word.

    Approach:
        - Look at each token.
        - If the token exactly matches a known single-word skill, keep it.
    """
    single_word_skills = {s for s in ALL_SKILLS if " " not in s}
    token_set = set(tokens)
    return token_set.intersection(single_word_skills)


def _extract_multi_word_skills(cleaned_text: str) -> Set[str]:
    """Extract multi-word skills by substring search on cleaned text.

    The cleaned text has already been lowercased and stripped of
    punctuation, which makes simple substring checks reliable for
    phrase detection in this educational project.
    """
    text = cleaned_text.lower()
    multi_word_skills = {s for s in ALL_SKILLS if " " in s}

    found: Set[str] = set()
    for skill in multi_word_skills:
        if skill in text:
            found.add(skill)

    return found


def extract_skills(preprocessed: PreprocessingResult) -> Set[str]:
    """High-level entry point for skill extraction.

    Args:
        preprocessed: Output from the NLP preprocessing pipeline.

    Returns:
        A set of detected skills (subset of `ALL_SKILLS`).
    """
    single_word = _extract_single_word_skills(preprocessed.tokens)
    multi_word = _extract_multi_word_skills(preprocessed.cleaned_text)

    return single_word.union(multi_word)


__all__ = ["extract_skills"]


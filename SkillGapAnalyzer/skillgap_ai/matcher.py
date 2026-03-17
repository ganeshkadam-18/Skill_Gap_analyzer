"""Skill matching and scoring engine for Resume Skill Gap AI (Milestone 2).

This module is responsible for:
    - Comparing resume skills and job description skills.
    - Computing overlaps and gaps using set operations.
    - Calculating an intuitive match score.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Set


@dataclass
class MatchResult:
    """Container for all matching outputs."""

    resume_skills: Set[str]
    jd_skills: Set[str]
    matched_skills: Set[str]
    missing_skills: Set[str]
    extra_skills: Set[str]
    match_score: float


def match_skills(resume_skills: Set[str], jd_skills: Set[str]) -> MatchResult:
    """Perform set-based skill comparison and compute a match score.

    Set operations:
        matched_skills = resume_skills ∩ jd_skills
        missing_skills = jd_skills - resume_skills
        extra_skills   = resume_skills - jd_skills

    Match score:
        If the job description specifies N skills and the resume covers K
        of them, then:

            score = (K / N) * 100

        If the job description has no skills (N = 0), the score is 0.0.
    """
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills.difference(resume_skills)
    extra = resume_skills.difference(jd_skills)

    if jd_skills:
        score = (len(matched) / len(jd_skills)) * 100.0
    else:
        score = 0.0

    return MatchResult(
        resume_skills=resume_skills,
        jd_skills=jd_skills,
        matched_skills=matched,
        missing_skills=missing,
        extra_skills=extra,
        match_score=round(score, 2),
    )


__all__ = ["MatchResult", "match_skills"]


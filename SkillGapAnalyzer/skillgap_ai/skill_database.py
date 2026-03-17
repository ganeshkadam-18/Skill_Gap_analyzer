"""Central skill database for Resume Skill Gap AI (Milestone 2).

This module defines a curated list of technical and soft skills.
Both single-word and multi-word skills are supported.

The skill extractor and matcher operate purely on these canonical
skill strings, which makes the system easy to extend:

    - To add a new skill, simply add it to `ALL_SKILLS`.
    - To group skills by category (optional), use `SKILL_CATEGORIES`.
"""

from __future__ import annotations

from typing import Dict, List, Set


# NOTE: All skills are stored in lowercase for consistent matching.
ALL_SKILLS: Set[str] = {
    # Programming languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "sql",
    "r",

    # Web / frameworks
    "html",
    "css",
    "react",
    "node.js",
    "django",
    "flask",
    "spring boot",

    # Data / ml / analytics
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "data analysis",

    # Devops / tools
    "git",
    "github",
    "docker",
    "kubernetes",
    "linux",

    # Cloud
    "aws",
    "azure",
    "gcp",

    # Soft skills
    "communication",
    "teamwork",
    "leadership",
    "problem solving",
    "time management",
}


SKILL_CATEGORIES: Dict[str, List[str]] = {
    "programming_languages": [
        "python",
        "java",
        "c",
        "c++",
        "c#",
        "javascript",
        "typescript",
        "r",
        "sql",
    ],
    "web_and_frameworks": [
        "html",
        "css",
        "react",
        "node.js",
        "django",
        "flask",
        "spring boot",
    ],
    "data_and_ml": [
        "pandas",
        "numpy",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "natural language processing",
        "nlp",
        "data analysis",
    ],
    "devops_and_tools": [
        "git",
        "github",
        "docker",
        "kubernetes",
        "linux",
    ],
    "cloud": [
        "aws",
        "azure",
        "gcp",
    ],
    "soft_skills": [
        "communication",
        "teamwork",
        "leadership",
        "problem solving",
        "time management",
    ],
}


__all__ = ["ALL_SKILLS", "SKILL_CATEGORIES"]


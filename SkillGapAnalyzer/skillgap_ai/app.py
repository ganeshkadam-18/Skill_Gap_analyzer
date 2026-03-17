"""Entry point for Resume Skill Gap AI (Milestone 2).

This script wires together all modules to implement the full workflow:

    Resume File → Text Extraction
    Job Description → Text Extraction
    ↓
    NLP Preprocessing
    (Lowercase → Remove punctuation → Tokenization
     → Stopword Removal → Lemmatization)
    ↓
    Skill Keyword Extraction
    ↓
    Skill Matching Engine
    ↓
    Match Score Calculation
    ↓
    Output (console report)
"""

from __future__ import annotations

from pathlib import Path

from tabulate import tabulate

from extractor import extract_text
from matcher import MatchResult, match_skills
from preprocessing import preprocess_text
from skill_extractor import extract_skills


def _print_header(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def _print_skill_set(title: str, skills: set[str]) -> None:
    _print_header(title)
    if not skills:
        print("None")
        return

    # Display one skill per row for readability
    table = [[s] for s in sorted(skills)]
    print(tabulate(table, headers=["Skill"], tablefmt="github"))


def _print_match_summary(result: MatchResult) -> None:
    _print_header("Match Score Summary")

    print(f"Total JD skills    : {len(result.jd_skills)}")
    print(f"Skills in resume   : {len(result.resume_skills)}")
    print(f"Matched skills     : {len(result.matched_skills)}")
    print(f"Missing skills     : {len(result.missing_skills)}")
    print(f"Extra resume skills: {len(result.extra_skills)}")
    print()
    print(f"Overall Match Score: {result.match_score:.2f} %")


def run_pipeline(resume_path: str, jd_path: str) -> MatchResult:
    """Run the full skill gap analysis pipeline."""
    # 1. Text extraction
    resume_raw = extract_text(resume_path)
    jd_raw = extract_text(jd_path)

    # 2. NLP preprocessing (strict order)
    resume_pre = preprocess_text(resume_raw)
    jd_pre = preprocess_text(jd_raw)

    # 3. Skill keyword extraction
    resume_skills = extract_skills(resume_pre)
    jd_skills = extract_skills(jd_pre)

    # 4. Skill matching engine + score
    result = match_skills(resume_skills, jd_skills)

    # 5. Reporting
    _print_skill_set("Skills detected in RESUME", result.resume_skills)
    _print_skill_set("Skills required in JOB DESCRIPTION", result.jd_skills)
    _print_skill_set("Matched skills (present in both)", result.matched_skills)
    _print_skill_set("Missing skills (required but not in resume)", result.missing_skills)
    _print_skill_set("Extra skills (present in resume only)", result.extra_skills)
    _print_match_summary(result)

    return result


def _prompt_for_path(label: str) -> str:
    """Simple user prompt with validation for file paths."""
    while True:
        raw = input(f"Enter path to {label} file (.txt/.pdf): ").strip().strip('"')
        if not raw:
            print("Path cannot be empty. Please try again.")
            continue

        p = Path(raw)
        if not p.exists():
            print(f"File does not exist: {p}. Please try again.")
            continue

        return str(p)


def main() -> None:
    print("=== Resume Skill Gap AI – Milestone 2 (NLP Enhanced) ===")
    resume_path = _prompt_for_path("RESUME")
    jd_path = _prompt_for_path("JOB DESCRIPTION")

    run_pipeline(resume_path, jd_path)


if __name__ == "__main__":
    main()


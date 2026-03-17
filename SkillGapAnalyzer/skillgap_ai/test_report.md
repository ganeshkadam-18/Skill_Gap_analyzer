## Milestone 2 – NLP Resume Skill Gap Analyzer  
### Test Report

This document records basic functional tests for the Milestone 2 system.

---

### 1. Environment & Setup

- **Python version**: 3.10+ (recommended)
- **Dependencies installation**

```bash
cd skillgap_ai
pip install -r requirements.txt
```

When the app is run for the first time, NLTK resources are downloaded automatically if missing (internet connection required once).

---

### 2. Test Cases

#### Test Case 1 – Simple overlap (TXT files)

- **Input files**
  - `samples/resume_simple.txt`
    - Mentions: `Python`, `Java`, `SQL`, `Git`, `Teamwork`
  - `samples/jd_simple.txt`
    - Requires: `Python`, `SQL`, `Git`, `Docker`, `Communication`

- **Expected behavior**
  - Resume skills include at least: `python`, `java`, `sql`, `git`, `teamwork`
  - JD skills include at least: `python`, `sql`, `git`, `docker`, `communication`
  - Matched skills: `python`, `sql`, `git`
  - Missing skills: `docker`, `communication`
  - Extra skills: `java`, `teamwork`
  - Match score:
    - JD skills = 5 (python, sql, git, docker, communication)
    - Matched = 3
    - Score = 3 / 5 × 100 = **60.00 %**

- **Observed result**
  - Output table lists skills exactly as expected.
  - Printed **Overall Match Score**: `60.00 %`
  - **Status**: ✅ Pass

---

#### Test Case 2 – Multi-word skills (TXT files)

- **Input files**
  - `samples/resume_ml.txt`
    - Mentions: `Machine learning`, `Deep learning`, `Python`, `Pandas`
  - `samples/jd_ml.txt`
    - Requires: `Machine learning`, `Natural language processing`, `Python`

- **Expected behavior**
  - System recognizes multi-word skills:
    - `machine learning`
    - `deep learning`
    - `natural language processing`
  - Matched skills: `python`, `machine learning`
  - Missing skills: `natural language processing`
  - Extra skills: `deep learning`, `pandas`
  - JD skills = 3 → Matched = 2 → Score ≈ **66.67 %**

- **Observed result**
  - Multi-word skills correctly detected via phrase search.
  - Printed **Overall Match Score**: `66.67 %`
  - **Status**: ✅ Pass

---

#### Test Case 3 – PDF resume and JD

- **Input files**
  - `samples/resume_dev.pdf`
  - `samples/jd_dev.pdf`
  - Both PDFs created from text (not scanned images).

- **Expected behavior**
  - Text successfully extracted from both PDFs.
  - Skills are detected similar to the equivalent `.txt` versions.
  - No crashes or exceptions in extraction.

- **Observed result**
  - Console output shows detected skills and score.
  - No PyPDF2 errors for standard text-based PDFs.
  - **Status**: ✅ Pass

---

#### Test Case 4 – Empty or very short JD

- **Input files**
  - `samples/resume_simple.txt` (non-empty)
  - `samples/jd_empty.txt` (contains only stopwords / almost no skills)

- **Expected behavior**
  - JD skill set is empty or near-empty.
  - Match score falls back to **0.0 %** when JD has zero skills.
  - No division-by-zero error.

- **Observed result**
  - JD skills set size: `0`
  - Printed **Overall Match Score**: `0.00 %`
  - **Status**: ✅ Pass

---

### 3. Notes & Future Improvements

- The current skill database is curated but limited; adding more domain-specific skills (e.g. for cloud, data engineering, cybersecurity) will improve coverage.
- Multi-word skills are detected via simple substring search on cleaned text; for production use, a more advanced phrase chunking or tagging approach (e.g. using spaCy noun chunks) could be explored.
- Additional evaluation metrics (e.g. weighting critical vs. optional skills) can make the match score more realistic for real hiring scenarios.


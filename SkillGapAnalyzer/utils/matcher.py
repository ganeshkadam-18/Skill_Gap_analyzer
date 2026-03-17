from .skills import PREDEFINED_SKILLS
import re

def extract_skills(cleaned_text):
    """
    Identifies technical competencies by cross-referencing normalized text
    against the established skill taxonomy.
    """
    found_skills = set()
    
    for skill in PREDEFINED_SKILLS:
        skill_clean = skill.lower()
        
        # Exact match with word boundaries in cleaned text
        escaped_skill = re.escape(skill_clean)
        pattern = r'(?:^|\s)' + escaped_skill + r'(?:\s|$)'
        
        if re.search(pattern, cleaned_text):
            found_skills.add(skill.lower())
            
    return found_skills

def analyze_skill_gap(resume_clean, jd_clean):
    """
    Computes set-based overlap between candidate profile and requirement vector.
    Calculates match index and identifies specific lexical deltas.
    """
    # Extract skills text
    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)
    
    # Matching using Set Operations
    matching_skills = jd_skills.intersection(resume_skills)
    missing_skills = jd_skills.difference(resume_skills)
    
    # Calculate match score
    total_jd_skills = len(jd_skills)
    if total_jd_skills > 0:
        match_percentage = round((len(matching_skills) / total_jd_skills) * 100, 2)
    else:
        match_percentage = 0.0
        
    return {
        "matching_skills": sorted(list(matching_skills)),
        "missing_skills": sorted(list(missing_skills)),
        "match_percentage": match_percentage,
        "resume_skills": sorted(list(resume_skills)),
        "jd_skills": sorted(list(jd_skills))
    }

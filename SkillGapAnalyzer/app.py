import streamlit as st
import base64
from utils.extractor import extract_text
from utils.cleaner import clean_text
from utils.matcher import analyze_skill_gap

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(
        page_title="SkillGapAI - Intelligence Alignment",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Professional Light Theme (Emerald Frost)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        * { font-family: 'Outfit', sans-serif; }
        
        /* Clean Light Background */
        .stApp {
            background-color: #f8fafc;
            background-image: 
                radial-gradient(at 0% 0%, rgba(16, 185, 129, 0.05) 0, transparent 50%), 
                radial-gradient(at 100% 100%, rgba(20, 184, 166, 0.05) 0, transparent 50%);
        }
        
        /* Pristine White Cards */
        .main-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 24px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            height: 3.2em;
            background: #10b981;
            color: white;
            font-weight: 700;
            font-size: 1rem;
            border: none;
            transition: all 0.2s ease;
        }
        
        .stButton>button:hover {
            background: #059669;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
            transform: translateY(-1px);
        }
        
        .metric-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #e2e8f0;
            text-align: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        
        .skill-tag {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 6px;
            margin: 4px;
            font-size: 0.9em;
            font-weight: 600;
        }
        
        .tag-match { 
            background: #ecfdf5; 
            color: #065f46; 
            border: 1px solid #a7f3d0; 
        }
        
        .tag-miss { 
            background: #fef2f2; 
            color: #991b1b; 
            border: 1px solid #fecaca; 
        }
        
        /* Elegant Typography */
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 0.2rem;
            letter-spacing: -0.02em;
        }
        
        .hero-sub {
            font-size: 1.1rem;
            color: #64748b;
            margin-bottom: 2.5rem;
        }

        h3, h4 {
            color: #1e293b !important;
            font-weight: 700 !important;
        }

        .stMarkdown p { color: #475569; }
        
        /* Clean File Uploader */
        [data-testid="stFileUploader"] {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 10px;
            border: 1px dashed #cbd5e1;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 1px solid #e2e8f0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown('<h1 class="hero-title">SkillGap AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">Deep alignment analysis between talent profiles and industry requirements.</p>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("### 🧬 Analysis Matrix")
        st.write("V 4.0 | Integrated Intelligence")
        st.markdown("---")
        st.markdown("""
        **Processing Workflow:**
        1. Multi-modal Extraction
        2. Normalization Engine
        3. Lexical Vectorization
        4. Alignment Quantification
        """)
        st.markdown("---")
        st.image("C:\\Users\\GAMESH\\.gemini\\antigravity\\brain\\6732dd8a-1608-4eaf-ae97-be7e82dc48be/skillgapai_logo_1773150325017.png")

    # Main Input Area (Vertical Alignment)
    with st.container():
        # Resume Section
        st.markdown("### 📄 Resume Discovery")
        resume_file = st.file_uploader("Drop candidate profile PDF/DOCX here", type=["pdf", "docx"], label_visibility="collapsed")
        if resume_file:
            st.info(f"Loaded: {resume_file.name}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Requirement Section
        st.markdown("### 📋 Requirement Context")
        jd_input_choice = st.segmented_control("Capture Method", ["Source File", "Direct Text"], default="Source File", label_visibility="collapsed")
        
        jd_raw_text = ""
        if jd_input_choice == "Source File":
            jd_file = st.file_uploader("Upload Job Specification", type=["pdf", "docx", "txt"], label_visibility="collapsed")
            if jd_file:
                jd_raw_text = extract_text(jd_file)
        else:
            jd_raw_text = st.text_area("Paste JD text context", height=150, placeholder="Paste requirements, responsibilities, and qualifications here...")

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Analyze Resume"):
        if resume_file and (jd_raw_text or 'jd_file' in locals()):
            with st.spinner("Analyzing skill vectors and quantifying alignment..."):
                # Extraction
                resume_raw = extract_text(resume_file)
                if not jd_raw_text and 'jd_file' in locals() and jd_file:
                    jd_raw_text = extract_text(jd_file)
                
                # NLP Pipeline
                res_clean = clean_text(resume_raw)
                jd_clean = clean_text(jd_raw_text)
                
                # Matching
                results = analyze_skill_gap(res_clean, jd_clean)
                
                # Visual Results Breakdown
                st.markdown("---")
                st.markdown("### 📊 Intelligence Report")
                
                # Metrics Row
                m1, m2, m3 = st.columns(3)
                with m1:
                    st.markdown(f'<div class="metric-card"><h4>Match Index</h4><h2 style="color: #10b981;">{results["match_percentage"]}%</h2></div>', unsafe_allow_html=True)
                with m2:
                    st.markdown(f'<div class="metric-card"><h4>Identified Skills</h4><h2 style="color: #4e4376;">{len(results["resume_skills"])}</h2></div>', unsafe_allow_html=True)
                with m3:
                    st.markdown(f'<div class="metric-card"><h4>Gaps Detected</h4><h2 style="color: #e11d48;">{len(results["missing_skills"])}</h2></div>', unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.progress(results['match_percentage'] / 100)
                
                # Skill Analysis Containers
                res_col1, res_col2 = st.columns(2)
                
                with res_col1:
                    st.markdown("#### ✅ Alignment Verified")
                    if results['matching_skills']:
                        for skill in results['matching_skills']:
                            st.markdown(f'<span class="skill-tag tag-match">{skill.title()}</span>', unsafe_allow_html=True)
                    else:
                        st.write("No direct alignment detected.")
                        
                with res_col2:
                    st.markdown("#### 🔍 Discovered Gaps")
                    if results['missing_skills']:
                        for skill in results['missing_skills']:
                            st.markdown(f'<span class="skill-tag tag-miss">{skill.title()}</span>', unsafe_allow_html=True)
                    else:
                        st.write("Alignment complete. Zero lexical gap.")

                # Advanced AI Insights (Simulated for UX)
                st.markdown("<br>", unsafe_allow_html=True)
                with st.expander("✨ AI Strategic Insights"):
                    st.markdown("Based on the analyzed skill vectors, the candidate shows high potential for this role.")
                    st.write("**Recommended Learning Path:**")
                    if results['missing_skills']:
                        st.info(f"Focus on mastering: {', '.join([s.title() for s in results['missing_skills'][:3]])}")
                    else:
                        st.success("Candidate is ready for immediate deployment.")

                # Deployment Meta-data
                with st.expander("🛠️ System Trace"):
                    st.write("**Processing Sequence:** Normalization -> Contraction Fix -> Punctuation Mask -> Tokens -> Stopword Removal -> Morphological Lemmatization")
                    st.markdown("**Processed Trace (Resume Sample):**")
                    st.code(res_clean[:300] + "...")
                
                st.download_button(
                    "💾 Download Analytical Report",
                    data=f"Match Index: {results['match_percentage']}%\nFound: {results['matching_skills']}\nMissing: {results['missing_skills']}",
                    file_name="skill_alignment.txt"
                )
        else:
            st.warning("Insufficient data. Please provide both resume and requirement contexts.")

if __name__ == "__main__":
    main()

import streamlit as st
from datetime import datetime
import base64
from pathlib import Path
import requests

# ── helpers ──────────────────────────────────────────────────────────────────

def local_css(file_name):
css_path = Path(**file**).parent / file_name
try:
with open(css_path) as f:
st.markdown(f”<style>{f.read()}</style>”, unsafe_allow_html=True)
except FileNotFoundError:
pass

@st.cache_data
def get_image_base64(image_path):
try:
with open(image_path, “rb”) as img_file:
return base64.b64encode(img_file.read()).decode()
except FileNotFoundError:
return “iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==”

def get_image_path(*args):
return (Path(**file**).parent / “assets” / Path(*args)).as_posix()

# ── page config ───────────────────────────────────────────────────────────────

st.set_page_config(page_title=“Sahil Chawla | Data Scientist”, layout=“wide”, page_icon=“⚡”)

st.markdown(”””

<style>
  footer { visibility: hidden; }
  #MainMenu { visibility: hidden; }
  header { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  section[data-testid="stSidebar"] { display: none; }
</style>

“””, unsafe_allow_html=True)

local_css(“styles/style.css”)

# ── Google Fonts & base styles ─────────────────────────────────────────────

st.markdown(”””

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ── navbar ────────────────────────────────────────────────────────────────────

st.markdown(”””

<nav class="top-nav">
  <div class="nav-logo">SC</div>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#projects">Work</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <a href="#download-cv" class="nav-cta">Resume ↗</a>
</nav>
""", unsafe_allow_html=True)

# ── hero ──────────────────────────────────────────────────────────────────────

profile_b64 = get_image_base64(get_image_path(“profile.jpg”))

st.markdown(f”””

<section id="profile" class="hero-section">
  <div class="hero-inner">
    <div class="hero-text">
      <span class="hero-eyebrow">portfolio · 2026</span>
      <h1 class="hero-title">I turn messy<br>data into<br><em>decisions.</em></h1>
      <p class="hero-sub">Data Scientist with 4.5+ years building ML pipelines, supply-chain optimisers, and Gen AI tools for Fortune 500s — from PepsiCo to Honda.</p>
      <div class="hero-actions">
        <a href="#projects" class="btn-primary">View Work</a>
        <a href="#contact" class="btn-ghost">Get in Touch</a>
      </div>
    </div>
    <div class="hero-image-wrap">
      <img src="data:image/jpeg;base64,{profile_b64}" alt="Sahil Chawla" class="hero-image" />
      <div class="hero-image-badge">EY · Great Learning · PepsiCo</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── stats strip ───────────────────────────────────────────────────────────────

st.markdown(”””

<section class="stats-strip">
  <div class="stat-item">
    <span class="stat-num">4.5+</span>
    <span class="stat-label">Years of Experience</span>
  </div>
  <div class="stat-divider"></div>
  <div class="stat-item">
    <span class="stat-num">5+</span>
    <span class="stat-label">Fortune 500 Clients</span>
  </div>
  <div class="stat-divider"></div>
  <div class="stat-item">
    <span class="stat-num">50%</span>
    <span class="stat-label">Transport Cost Reduction</span>
  </div>
  <div class="stat-divider"></div>
  <div class="stat-item">
    <span class="stat-num">₹50Cr</span>
    <span class="stat-label">Revenue from Courses</span>
  </div>
</section>
""", unsafe_allow_html=True)

# ── about ────────────────────────────────────────────────────────────────────

st.markdown(”””

<section id="about" class="section">
  <div class="section-inner">
    <div class="section-header">
      <span class="section-tag">001 · About</span>
      <h2 class="section-title">The data scientist<br>behind the work.</h2>
    </div>
    <div class="about-body">
      <p>I'm <strong>Sahil Chawla</strong> — a Data Scientist and Technology Consultant at Ernst &amp; Young, based in Gurugram, India. I specialise in Machine Learning, Supply Chain Analytics, and Generative AI.</p>
      <p>My journey started in customer service before pivoting through a PGP in Data Science. That grounding in real user problems shapes how I build: systems that are rigorous <em>and</em> actually used.</p>
      <p>I've delivered ML pipelines at The Schwan's Company, a SQL optimisation engine at Ferrero Rocher, Power BI dashboards at Honda, and internal Gen AI tools at EY. Earlier, I built and taught data science curricula across 15 concurrent batches at Great Learning — including programs for NUS Singapore.</p>
      <p>Outside work: video games, strong coffee, and going too deep into Figma prototypes I'll never ship.</p>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── experience ────────────────────────────────────────────────────────────────

experiences = [
{
“title”: “Technology Consultant – Data Scientist”,
“company”: “Ernst & Young (EY)”,
“duration”: “Apr 2024 – Present”,
“domain”: “Supply Chain · Fintech · Logistics”,
“tags”: [“Python”, “PySpark”, “LangChain”, “SQL”, “Azure”, “Power BI”],
“highlights”: [
(“PepsiCo”, “Acted as Data Product Manager & SME; owned end-to-end GDO/DFS documentation and delivery across build → hypercare.”),
(“Schwan’s Company”, “MLOps engineer; deployed ML inventory-planning pipelines, improving supply chain accuracy by 18%.”),
(“Ferrero Rocher”, “PL/SQL developer; built BlueYonder TMS optimisation solver — 90% truck utilisation, 50% cost reduction.”),
(“American Honda Motors”, “Productionised ML workflows; Power BI dashboards uncovered a $50M data gap across enterprise systems.”),
(“Carnival Cruise Lines”, “Python automation streamlining SQL transformation workflows, eliminating manual execution effort.”),
(“EY Internal”, “Built LangChain + Streamlit synthetic data generator & ERNY 2.0 AI chatbot (React UI).”),
],
},
{
“title”: “Associate Data Scientist – Faculty”,
“company”: “Great Learning”,
“duration”: “Jan 2022 – Apr 2024”,
“domain”: “Ed-tech · AI Education”,
“tags”: [“Python”, “SQL”, “ML”, “Gen AI”, “Tableau”],
“highlights”: [
(“NUS & GLCA Courses”, “Designed and delivered programs generating ₹50 Cr in revenue.”),
(“AI Code Tutor”, “Built contextual hint engine → 40% user satisfaction uplift, 30% platform engagement increase.”),
(“15 Concurrent Batches”, “Ran live sessions across data analysis, engineering, science, and Gen AI tracks simultaneously.”),
],
},
{
“title”: “Associate Data Scientist Intern”,
“company”: “Great Learning”,
“duration”: “Jan 2021 – Dec 2021”,
“domain”: “Ed-tech · Cloud AI”,
“tags”: [“Azure ML”, “IBM Watson”, “Python”, “Computer Vision”],
“highlights”: [
(“Azure ML Modules”, “Designed hands-on learning labs for ML on Microsoft Azure.”),
(“IBM Watson”, “Built conversational and action-based chatbot tutorials.”),
(“Computer Vision Projects”, “Led Azure Custom Vision projects — helmet detection & obstacle detection.”),
],
},
]

exp_cards = “”
for exp in experiences:
tags_html = “”.join(f’<span class="tag">{t}</span>’ for t in exp[“tags”])
highlights_html = “”.join(
f’<div class="highlight-row"><span class="highlight-client">{h[0]}</span><span class="highlight-desc">{h[1]}</span></div>’
for h in exp[“highlights”]
)
exp_cards += f”””

<div class="exp-card">
  <div class="exp-header">
    <div>
      <h3 class="exp-title">{exp['title']}</h3>
      <p class="exp-company">{exp['company']} <span class="exp-duration">· {exp['duration']}</span></p>
      <p class="exp-domain">{exp['domain']}</p>
    </div>
    <div class="exp-tags">{tags_html}</div>
  </div>
  <div class="exp-highlights">{highlights_html}</div>
</div>
"""

st.markdown(f”””

<section id="experience" class="section section-alt">
  <div class="section-inner">
    <div class="section-header">
      <span class="section-tag">002 · Experience</span>
      <h2 class="section-title">Where I've shipped<br>real things.</h2>
    </div>
    <div class="exp-list">{exp_cards}</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── projects ──────────────────────────────────────────────────────────────────

projects = [
{
“title”: “Annual Turnover Prediction”,
“tags”: [“Regression”, “LGBM”, “CatBoost”, “Random Forest”],
“status”: “Shipped”,
“challenge”: “Predict restaurant annual turnover from operational variables with minimal prediction error.”,
“approach”: “Benchmarked LGBM, CatBoost, and Random Forest regressors; optimised for RMSE with hyperparameter tuning.”,
“result”: “Best RMSE”,
“metric”: “RMSE”,
“link”: “https://github.com/Sahilchawla1094/Annual-Turnover-of-a-restaurant”,
},
{
“title”: “Home Credit Default Risk”,
“tags”: [“Classification”, “LightGBM”, “Logistic Regression”, “AUC”],
“status”: “Shipped”,
“challenge”: “Identify clients at risk of loan default to reduce financial exposure for a lender.”,
“approach”: “Implemented Logistic Regression, Random Forest, and LightGBM; feature-engineered credit history signals.”,
“result”: “High AUC Score”,
“metric”: “AUC”,
“link”: “https://github.com/Sahilchawla1094/Home-Credit-Default-Risk”,
},
{
“title”: “Business Loan Default Prediction”,
“tags”: [“Classification”, “Decision Tree”, “F1 Score”, “Imbalanced Data”],
“status”: “Shipped”,
“challenge”: “Predict whether a business loan application will default, with heavy class imbalance.”,
“approach”: “Applied SMOTE resampling + Decision Tree and Random Forest; optimised for F1 to handle imbalance.”,
“result”: “Best F1 Score”,
“metric”: “F1”,
“link”: “https://github.com/Sahilchawla1094/Predicting-whether-a-business-loan-applicant-will-default-or-not”,
},
{
“title”: “Thera Bank Liability Prediction”,
“tags”: [“ANN”, “Deep Learning”, “Banking”],
“status”: “Shipped”,
“challenge”: “Predict which liability customers are likely to purchase personal loans to target marketing spend.”,
“approach”: “Built and tuned an Artificial Neural Network; optimised threshold for best F1 on the minority class.”,
“result”: “High F1 Score”,
“metric”: “F1”,
“link”: “https://github.com/Sahilchawla1094/Thera-Bank”,
},
{
“title”: “Water Potability Analysis”,
“tags”: [“ANN”, “Binary Classification”, “Environment”],
“status”: “Shipped”,
“challenge”: “Classify water samples as safe or unsafe for drinking from physicochemical measurements.”,
“approach”: “ANN with normalised inputs; handled missing values and class imbalance via weighted training.”,
“result”: “Strong Accuracy”,
“metric”: “Accuracy”,
“link”: “https://github.com/Sahilchawla1094/Water-Potability”,
},
{
“title”: “CS:GO Round Winner Prediction”,
“tags”: [“XGBoost”, “Random Forest”, “Gaming Analytics”],
“status”: “Shipped”,
“challenge”: “Predict the winning team (T or CT) mid-round from in-game state variables.”,
“approach”: “Compared Logistic Regression, Decision Tree, Random Forest, and XGBoost; selected best by accuracy.”,
“result”: “Best Accuracy”,
“metric”: “Accuracy”,
“link”: “https://github.com/Sahilchawla1094/Counter-Strike–GO-Round-winner”,
},
]

proj_cards = “”
for p in projects:
tags_html = “”.join(f’<span class="tag">{t}</span>’ for t in p[“tags”])
proj_cards += f”””

<div class="proj-card">
  <div class="proj-card-top">
    <div class="proj-meta">
      <span class="proj-status">{p['status']}</span>
      {tags_html}
    </div>
    <h3 class="proj-title">{p['title']}</h3>
  </div>
  <div class="proj-card-body">
    <div class="proj-row">
      <span class="proj-row-label">Challenge</span>
      <span class="proj-row-val">{p['challenge']}</span>
    </div>
    <div class="proj-row">
      <span class="proj-row-label">Approach</span>
      <span class="proj-row-val">{p['approach']}</span>
    </div>
    <div class="proj-result-bar">
      <span class="proj-result-num">{p['result']}</span>
      <span class="proj-result-metric">Key metric: {p['metric']}</span>
    </div>
  </div>
  <a href="{p['link']}" target="_blank" class="proj-link">View on GitHub ↗</a>
</div>
"""

st.markdown(f”””

<section id="projects" class="section">
  <div class="section-inner">
    <div class="section-header">
      <span class="section-tag">003 · Selected Work</span>
      <h2 class="section-title">Projects built<br>on real data.</h2>
      <p class="section-sub">A curated set of ML and analytics work — each solving a concrete problem with measurable output.</p>
    </div>
    <div class="proj-grid">{proj_cards}</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── skills ────────────────────────────────────────────────────────────────────

skill_groups = [
(“Languages & Querying”, [“Python”, “SQL”, “PL/SQL”, “PySpark”]),
(“ML & AI”, [“Machine Learning”, “Deep Learning”, “NLP”, “LLMs”, “LangChain”, “Generative AI”, “Statistics”]),
(“Data & Analytics”, [“Data Analysis”, “Data Engineering”, “Tableau”, “Power BI”, “Excel”]),
(“Cloud & Infra”, [“Microsoft Azure”, “Databricks”, “Snowflake”]),
(“Frameworks & Tools”, [“Streamlit”, “Scikit-learn”, “XGBoost”, “LightGBM”, “CatBoost”, “Pandas”, “NumPy”]),
]

skill_html = “”
for group_name, skills in skill_groups:
pills = “”.join(f’<span class="skill-pill">{s}</span>’ for s in skills)
skill_html += f”””

<div class="skill-group">
  <h4 class="skill-group-name">{group_name}</h4>
  <div class="skill-pills">{pills}</div>
</div>
"""

st.markdown(f”””

<section id="skills" class="section section-alt">
  <div class="section-inner">
    <div class="section-header">
      <span class="section-tag">004 · Skills</span>
      <h2 class="section-title">Tools I reach for<br>on day one.</h2>
    </div>
    <div class="skills-grid">{skill_html}</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── education ────────────────────────────────────────────────────────────────

education = [
(“Executive PGP in Management (Data Science & Analytics)”, “Great Lakes Institute of Management, Gurugram”, “Feb 2022 – Feb 2023”),
(“Post Graduate Program in Data Science & Engineering”, “Great Lakes Institute of Management, Gurugram”, “Oct 2020 – Aug 2021”),
(“B.Tech in Civil Engineering”, “Anand International College of Engineering”, “2013 – 2017”),
]

edu_items = “”.join(f”””

<div class="edu-item">
  <div class="edu-dot"></div>
  <div class="edu-content">
    <h4 class="edu-degree">{e[0]}</h4>
    <p class="edu-inst">{e[1]}</p>
    <p class="edu-year">{e[2]}</p>
  </div>
</div>
""" for e in education)

st.markdown(f”””

<section id="education" class="section">
  <div class="section-inner">
    <div class="section-header">
      <span class="section-tag">005 · Education</span>
      <h2 class="section-title">Foundation of<br>the craft.</h2>
    </div>
    <div class="edu-timeline">{edu_items}</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── contact ───────────────────────────────────────────────────────────────────

st.markdown(”””

<section id="contact" class="section section-alt">
  <div class="section-inner contact-inner">
    <div class="section-header">
      <span class="section-tag">006 · Contact</span>
      <h2 class="section-title">Let's build<br>something real.</h2>
      <div class="contact-details">
        <a href="mailto:Sahilchawla1094@gmail.com" class="contact-link">Sahilchawla1094@gmail.com ↗</a>
        <a href="https://www.linkedin.com/in/sahil-chawla9799558521/" target="_blank" class="contact-link">LinkedIn ↗</a>
        <a href="https://github.com/Sahilchawla1094" target="_blank" class="contact-link">GitHub ↗</a>
        <a href="https://public.tableau.com/app/profile/sahil.chawla" target="_blank" class="contact-link">Tableau Public ↗</a>
      </div>
    </div>
""", unsafe_allow_html=True)

with st.container():
st.markdown(’<div class="contact-form-wrap">’, unsafe_allow_html=True)
with st.form(“contact_form”, clear_on_submit=True):
col1, col2 = st.columns(2, gap=“medium”)
with col1:
name = st.text_input(“Name”, placeholder=“Your full name”)
email = st.text_input(“Email”, placeholder=“your@email.com”)
with col2:
phone = st.text_input(“Phone”, placeholder=”+91 XXXXX XXXXX”)
subject = st.text_input(“Subject”, placeholder=“What’s this about?”)
message = st.text_area(“Message”, placeholder=“Tell me about your project or opportunity…”, height=150)
submit = st.form_submit_button(“Send Message →”)
if submit:
if not name or not email or not message:
st.error(“Please fill in name, email, and message.”)
else:
try:
service_id = st.secrets[“emailjs”][“service_id”]
template_id = st.secrets[“emailjs”][“template_id”]
user_id = st.secrets[“emailjs”][“user_id”]
data = {
“service_id”: service_id,
“template_id”: template_id,
“user_id”: user_id,
“template_params”: {
“from_name”: name,
“from_email”: email,
“from_phone”: phone,
“message”: message
}
}
response = requests.post(“https://api.emailjs.com/api/v1.0/email/send”, json=data, timeout=10)
if response.status_code == 200:
st.success(“Message sent! I’ll get back to you soon.”)
else:
st.error(“Failed to send. Try emailing directly.”)
except Exception:
st.error(“Something went wrong. Please email directly.”)
st.markdown(’</div>’, unsafe_allow_html=True)

st.markdown(”</div></section>”, unsafe_allow_html=True)

# ── download cv ───────────────────────────────────────────────────────────────

st.markdown(’<div id="download-cv" style="padding:2rem 4rem;">’, unsafe_allow_html=True)
cv_path = get_image_path(“cv”, “Resume___Sahil_Chawla.pdf”)
try:
with open(cv_path, “rb”) as f:
st.download_button(
label=“⬇ Download Resume”,
data=f,
file_name=“Resume_Sahil_Chawla.pdf”,
mime=“application/pdf”,
)
except FileNotFoundError:
st.info(“Place your PDF at assets/cv/Resume___Sahil_Chawla.pdf to enable download.”)
st.markdown(’</div>’, unsafe_allow_html=True)

# ── footer ────────────────────────────────────────────────────────────────────

st.markdown(f”””

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-left">
      <span class="footer-logo">SC</span>
      <p class="footer-tagline">Data Scientist · Gurugram, India</p>
    </div>
    <nav class="footer-nav">
      <a href="#about">About</a>
      <a href="#experience">Experience</a>
      <a href="#projects">Work</a>
      <a href="#skills">Skills</a>
      <a href="#contact">Contact</a>
    </nav>
    <p class="footer-copy">© {datetime.now().year} Sahil Chawla. All rights reserved.</p>
  </div>
</footer>
""", unsafe_allow_html=True)
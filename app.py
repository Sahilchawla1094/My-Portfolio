import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import requests
import base64
from pathlib import Path
import streamlit.components.v1 as components


def local_css(file_name):
    css_path = Path(__file__).parent / file_name
    try:
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file '{file_name}' not found at {css_path}.")


@st.cache_data
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="


def get_image_path(*args):
    return (Path(__file__).parent / "assets" / Path(*args)).as_posix()


# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Sahil Chawla | Data Scientist", layout="wide")

st.markdown("""
<style>
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

local_css("styles/style.css")

st.markdown(
    '<meta name="description" content="Sahil Chawla — Data Scientist portfolio. ML, Generative AI, Supply Chain.">',
    unsafe_allow_html=True
)

# ── Navbar ─────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="navbar">
    <ul>
        <li><a href="#profile"         title="Profile">🏠</a></li>
        <li><a href="#about"           title="About">👨‍💼</a></li>
        <li><a href="#education"       title="Education">🎓</a></li>
        <li><a href="#experience"      title="Experience">💼</a></li>
        <li><a href="#skills"          title="Skills">🛠️</a></li>
        <li><a href="#projects"        title="Projects">📂</a></li>
        <li><a href="#other-platforms" title="Platforms">🔗</a></li>
        <li><a href="#contact"         title="Contact">📞</a></li>
        <li><a href="#download-cv" class="download-cv" title="Download CV">📄</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)


# ── Animation injector (particles + scroll reveal + skill bars) ────────────────
def inject_animations():
    components.html("""
    <script>
    (function () {
        const p = window.parent;

        /* ── Particle canvas ── */
        if (!p.document.getElementById('sc-particles')) {
            const canvas = p.document.createElement('canvas');
            canvas.id = 'sc-particles';
            canvas.style.cssText =
                'position:fixed;top:0;left:0;width:100vw;height:100vh;' +
                'z-index:0;pointer-events:none;';
            p.document.body.appendChild(canvas);

            const ctx = canvas.getContext('2d');
            function resize() {
                canvas.width  = p.window.innerWidth;
                canvas.height = p.window.innerHeight;
            }
            resize();
            p.window.addEventListener('resize', resize);

            const pts = Array.from({ length: 65 }, () => ({
                x:  Math.random() * canvas.width,
                y:  Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.38,
                vy: (Math.random() - 0.5) * 0.38,
                r:  Math.random() * 1.4 + 0.5,
                a:  Math.random() * 0.35 + 0.08
            }));

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                pts.forEach(pt => {
                    pt.x += pt.vx; pt.y += pt.vy;
                    if (pt.x < 0 || pt.x > canvas.width)  pt.vx *= -1;
                    if (pt.y < 0 || pt.y > canvas.height)  pt.vy *= -1;
                    ctx.beginPath();
                    ctx.arc(pt.x, pt.y, pt.r, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(0,212,255,${pt.a})`;
                    ctx.fill();
                });
                for (let i = 0; i < pts.length; i++) {
                    for (let j = i + 1; j < pts.length; j++) {
                        const dx = pts[i].x - pts[j].x;
                        const dy = pts[i].y - pts[j].y;
                        const d  = Math.sqrt(dx * dx + dy * dy);
                        if (d < 105) {
                            ctx.beginPath();
                            ctx.strokeStyle = `rgba(0,212,255,${0.12 * (1 - d / 105)})`;
                            ctx.lineWidth = 0.5;
                            ctx.moveTo(pts[i].x, pts[i].y);
                            ctx.lineTo(pts[j].x, pts[j].y);
                            ctx.stroke();
                        }
                    }
                }
                p.requestAnimationFrame(draw);
            }
            draw();
        }

        /* ── Scroll reveal + skill bar trigger ── */
        function setupObservers() {
            const revealObs = new p.IntersectionObserver(entries => {
                entries.forEach(e => {
                    if (e.isIntersecting) e.target.classList.add('sc-visible');
                });
            }, { threshold: 0.1 });

            p.document.querySelectorAll('.sc-reveal, .sc-reveal-left')
                .forEach(el => revealObs.observe(el));

            const barObs = new p.IntersectionObserver(entries => {
                entries.forEach(e => {
                    if (e.isIntersecting) {
                        e.target.querySelectorAll('.skill-bar-fill')
                            .forEach(b => b.classList.add('animated'));
                    }
                });
            }, { threshold: 0.2 });

            p.document.querySelectorAll('.skills-container')
                .forEach(el => barObs.observe(el));
        }

        setTimeout(setupObservers, 800);
        setTimeout(setupObservers, 2200);
    })();
    </script>
    """, height=0, scrolling=False)


# ── Stats counters component ───────────────────────────────────────────────────
def show_stats():
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;800&family=JetBrains+Mono:wght@500;700&display=swap');
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: transparent; font-family: 'Inter', sans-serif; }

    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        padding: 28px 0 4px;
    }
    .card {
        background: #0f1628;
        border: 1px solid #1a2a4a;
        border-radius: 14px;
        padding: 22px 14px 18px;
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: transform .3s, box-shadow .3s, border-color .3s;
    }
    .card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00d4ff, #7b2ff7);
    }
    .card::after {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 50% 0%, rgba(0,212,255,0.06) 0%, transparent 70%);
        opacity: 0;
        transition: opacity .3s;
    }
    .card:hover { transform: translateY(-5px); border-color: #00d4ff; box-shadow: 0 0 22px rgba(0,212,255,.2); }
    .card:hover::after { opacity: 1; }

    .num {
        font-family: 'JetBrains Mono', monospace;
        font-size: 40px;
        font-weight: 700;
        background: linear-gradient(135deg, #00d4ff, #7b2ff7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }
    .suffix { font-size: 26px; }
    .lbl {
        font-size: 10px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        margin-top: 8px;
        font-weight: 600;
    }
    @media (max-width: 580px) {
        .grid { grid-template-columns: repeat(2,1fr); }
    }
    </style>
    </head>
    <body>
    <div class="grid">
        <div class="card">
            <div class="num"><span class="cnt" data-t="4.5" data-d="1">0</span><span class="suffix">+</span></div>
            <div class="lbl">Years Experience</div>
        </div>
        <div class="card">
            <div class="num"><span class="cnt" data-t="5" data-d="0">0</span><span class="suffix">+</span></div>
            <div class="lbl">Enterprise Clients</div>
        </div>
        <div class="card">
            <div class="num"><span class="cnt" data-t="6" data-d="0">0</span></div>
            <div class="lbl">ML Projects</div>
        </div>
        <div class="card">
            <div class="num">₹<span class="cnt" data-t="50" data-d="0">0</span><span class="suffix">Cr</span></div>
            <div class="lbl">Revenue Generated</div>
        </div>
    </div>

    <script>
    function animateCount(el) {
        const target = parseFloat(el.dataset.t);
        const dec    = parseInt(el.dataset.d) || 0;
        const dur    = 1800;
        const start  = performance.now();
        (function tick(now) {
            const p = Math.min((now - start) / dur, 1);
            const v = (1 - Math.pow(1 - p, 3)) * target;
            el.textContent = dec ? v.toFixed(dec) : Math.floor(v);
            if (p < 1) requestAnimationFrame(tick);
        })(start);
    }
    const obs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.querySelectorAll('.cnt').forEach(animateCount);
                obs.unobserve(e.target);
            }
        });
    }, { threshold: 0.4 });
    document.querySelectorAll('.grid').forEach(g => obs.observe(g));
    </script>
    </body>
    </html>
    """, height=170)


# ── Profile ────────────────────────────────────────────────────────────────────
def show_profile():
    st.markdown("<div id='profile'></div>", unsafe_allow_html=True)

    profile_b64 = get_image_base64(get_image_path("profile.jpg"))

    col1, col2 = st.columns([1, 1.9], gap="large")

    with col1:
        st.markdown(f"""
        <div class="profile-img-wrapper sc-reveal-left">
            <img src="data:image/jpeg;base64,{profile_b64}" alt="Sahil Chawla" />
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="sc-reveal" style="padding-top:16px;">
            <p class="hero-greeting">// Hello, I'm</p>
            <h1 class="hero-name">Sahil Chawla</h1>
            <div style="margin:10px 0 18px;">
                <span class="typing-text">Data Scientist</span>
            </div>
            <p class="hero-bio">
                With <span class="highlight-text">4.5+ years</span> of experience in
                <span class="highlight-text">Machine Learning</span> and
                <span class="highlight-text">Generative AI</span>, I build intelligent
                solutions for global enterprise clients across Supply Chain and Ed-tech.
            </p>
            <div style="display:flex;gap:14px;margin-top:26px;flex-wrap:wrap;">
                <a href="#contact"     class="btn-primary">Contact Me</a>
                <a href="#download-cv" class="btn-outline">Download CV</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    show_stats()


# ── About ──────────────────────────────────────────────────────────────────────
def show_about():
    st.markdown("<div id='about'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Get To Know More</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">About Me</h1>', unsafe_allow_html=True)

    p1 = 'I am a Data Scientist with <span class="highlight-text">4.5+ years</span> of experience delivering Machine Learning and Generative AI solutions, currently working as a <span class="highlight-text">Technology Consultant at Ernst &amp; Young (EY)</span>. I have supported global enterprise clients including <span class="highlight-text">PepsiCo, American Honda Motors, Carnival Cruise Lines, Ferrero Rocher, and The Schwan\'s Company</span>, driving measurable improvements in cost efficiency, planning accuracy, and operational performance.'
    p2 = 'Previously at <span class="highlight-text">Great Learning</span>, I designed and delivered data science, data engineering, and Generative AI courses across 15 concurrent batches, created programs for <span class="highlight-text">NUS (National University of Singapore)</span> and the Great Learning Career Academy, generating <span class="highlight-text">INR 50 crore in revenue</span>.'
    p3 = 'My passion lies in building intelligent systems — from ML pipelines and supply chain optimisation solvers to AI chatbots and synthetic data generators — leveraging <span class="highlight-text">Python, SQL, PySpark, LangChain</span>, and cloud platforms like <span class="highlight-text">Microsoft Azure</span>.'
    st.markdown(
        f'<div class="about-card sc-reveal"><p>{p1}</p><p>{p2}</p><p>{p3}</p></div>',
        unsafe_allow_html=True
    )


# ── Education ──────────────────────────────────────────────────────────────────
def show_education():
    st.markdown("<div id='education'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Academic Background</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Education</h1>', unsafe_allow_html=True)

    education = [
        {
            'degree': 'Executive PGP in Management (Data Science & Analytics)',
            'institution': 'Great Lakes Institute of Management, Gurugram',
            'duration': 'Feb 2022 – Feb 2023',
        },
        {
            'degree': 'Post Graduate Program in Data Science & Engineering',
            'institution': 'Great Lakes Institute of Management, Gurugram',
            'duration': 'Oct 2020 – Aug 2021',
        },
        {
            'degree': 'Bachelor of Technology in Civil Engineering',
            'institution': 'Anand International College of Engineering',
            'duration': '2013 – 2017',
            'percentage': '65%',
        },
        {
            'degree': '12th – PCMB',
            'institution': 'National Institute of Open Schooling',
            'duration': '2011 – 2012',
            'percentage': '65%',
        },
        {
            'degree': '10th Grade',
            'institution': 'St. Anselms Sr. Sec. School',
            'duration': '2009 – 2010',
            'percentage': '8.6 CGPA',
        },
    ]

    for edu in education:
        pct = (f' <span style="color:#00d4ff;font-size:11px;font-family:\'JetBrains Mono\',monospace;">'
               f'· {edu["percentage"]}</span>') if 'percentage' in edu else ''
        st.markdown(f"""
        <div class="edu-card sc-reveal">
            <div class="edu-degree">{edu['degree']}</div>
            <div class="edu-institution">{edu['institution']}</div>
            <div class="edu-duration">{edu['duration']}{pct}</div>
        </div>
        """, unsafe_allow_html=True)


# ── Experience ─────────────────────────────────────────────────────────────────
def show_experience():
    st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Work History</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Experience</h1>', unsafe_allow_html=True)

    experience = [
        {
            'title': 'Associate Data Scientist Intern',
            'company': 'Great Learning, Gurugram',
            'duration': 'Jan 2021 – Dec 2021',
            'domain': 'Ed-tech',
            'technologies': ['Python', 'SQL', 'Excel', 'Microsoft Azure', 'IBM Watson'],
            'bullets': [
                'Designed and delivered hands-on AI and ML learning modules using Microsoft Azure ML.',
                'Built IBM Watson Assistant tutorials for conversational and action-based chatbots.',
                'Led live project support sessions; implemented Azure Custom Vision projects including helmet and obstacle detection.',
            ],
        },
        {
            'title': 'Associate Data Scientist – Faculty',
            'company': 'Great Learning, Gurugram',
            'duration': 'Jan 2022 – Apr 2024',
            'domain': 'Ed-tech',
            'technologies': ['Python', 'SQL', 'Excel', 'Tableau', 'Machine Learning', 'Generative AI'],
            'bullets': [
                'Designed and delivered data analysis, data engineering, data science, and Generative AI courses across 15 concurrent batches.',
                'Created courses for NUS (National University of Singapore) and GLCA, generating INR 50 crore in revenue.',
                'Built an AI code tutor providing real-time contextual hints → 40% increase in user satisfaction, 30% uplift in platform engagement.',
            ],
        },
        {
            'title': 'Technology Consultant – Data Scientist',
            'company': 'Ernst & Young (EY), Gurugram',
            'duration': 'Apr 2024 – Present',
            'domain': 'Supply Chain',
            'technologies': ['Python', 'SQL', 'PL/SQL', 'PySpark', 'LangChain', 'Power BI', 'Microsoft Azure'],
            'bullets': [
                'Data Product Manager for PepsiCo — acted as SPOC/SME, owned GDO and DFS/DRD documentation, led end-to-end delivery across build, UT, FT, SIT, and hypercare.',
                'MLOps engineer for The Schwan\'s Company — deployed ML pipelines for inventory planning, improving supply chain accuracy by 18%.',
                'PL/SQL developer for Ferrero Rocher — built supply chain optimisation solver for BlueYonder TMS: +90% truck utilisation, −50% transport cost.',
                'MLOps engineer for American Honda Motors — productionised ML workflows; Power BI dashboards identified a $50M data gap across enterprise systems.',
                'Python developer for Carnival Cruise Lines — automation to streamline SQL transformation workflows and reduce manual execution effort.',
                'Internal EY AI assets: GenAI synthetic data tool (LangChain + Streamlit) and ERNY 2.0 internal chatbot (LangChain + React UI).',
            ],
        },
    ]

    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    for exp in experience:
        chips   = ''.join(f'<span class="tech-chip">{t}</span>' for t in exp['technologies'])
        bullets = ''.join(f'<li>{b}</li>' for b in exp['bullets'])
        st.markdown(f"""
        <div class="timeline-item sc-reveal">
            <div class="timeline-title">{exp['title']}</div>
            <div class="timeline-company">{exp['company']}</div>
            <div class="timeline-meta">
                <span class="timeline-tag">📅 {exp['duration']}</span>
                <span class="timeline-tag purple">🏷 {exp['domain']}</span>
            </div>
            <ul class="timeline-desc">{bullets}</ul>
            <div style="margin-top:14px;">{chips}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── Skills ─────────────────────────────────────────────────────────────────────
def show_skills():
    st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Technical Proficiency</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Skills</h1>', unsafe_allow_html=True)

    technical_skills = {
        'Python': 90, 'SQL': 85, 'PySpark': 75, 'Data Analysis': 90,
        'Data Engineering': 80, 'Machine Learning': 85, 'Deep Learning': 75,
        'Statistics': 80, 'Generative AI': 75, 'LLMs & LangChain': 70,
        'NLP': 70, 'Tableau': 70, 'Power BI': 75, 'Microsoft Azure': 70,
        'Databricks': 65, 'Snowflake': 65, 'PL/SQL': 65, 'Excel': 90, 'Streamlit': 80,
    }

    col_chart, col_bars = st.columns([1, 1], gap="large")

    with col_chart:
        skills = list(technical_skills.keys())
        values = list(technical_skills.values())
        fig = go.Figure(data=[go.Scatterpolar(
            r     = values + [values[0]],
            theta = skills + [skills[0]],
            fill  = 'toself',
            name  = 'Proficiency',
            line  = dict(color='#00d4ff', width=2),
            fillcolor = 'rgba(0, 212, 255, 0.08)',
            marker    = dict(color='#00d4ff', size=4),
        )])
        fig.update_layout(
            polar=dict(
                bgcolor='rgba(15,22,40,0.6)',
                radialaxis=dict(
                    visible=True, range=[0, 100],
                    tickmode='linear', tick0=0, dtick=20,
                    gridcolor='rgba(0,212,255,0.08)',
                    linecolor='rgba(0,212,255,0.08)',
                    tickfont=dict(color='#4a5568', size=8),
                ),
                angularaxis=dict(
                    gridcolor='rgba(0,212,255,0.06)',
                    linecolor='rgba(0,212,255,0.06)',
                    tickfont=dict(color='#94a3b8', size=10),
                ),
            ),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=55, r=55, t=55, b=55),
            height=430,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_bars:
        bars_html = '<div class="skills-container">'
        for name, pct in technical_skills.items():
            bars_html += f"""
            <div class="skill-bar-item">
                <div class="skill-bar-header">
                    <span class="skill-bar-name">{name}</span>
                    <span class="skill-bar-pct">{pct}%</span>
                </div>
                <div class="skill-bar-track">
                    <div class="skill-bar-fill" style="--target-width:{pct}%;"></div>
                </div>
            </div>"""
        bars_html += '</div>'
        st.markdown(bars_html, unsafe_allow_html=True)

    st.markdown(
        '<p style="margin-top:16px;font-family:\'JetBrains Mono\',monospace;font-size:13px;">'
        '<span style="color:#00d4ff;">Languages:</span>'
        ' <span style="color:#e2e8f0;">English</span>'
        ' <span style="color:#4a5568;"> · </span>'
        ' <span style="color:#e2e8f0;">Hindi</span></p>',
        unsafe_allow_html=True
    )


# ── Projects ───────────────────────────────────────────────────────────────────
def show_projects():
    st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Projects</h1>', unsafe_allow_html=True)

    projects = [
        {
            'title': 'Annual Turnover Prediction for Restaurant',
            'description': 'Predict the annual turnover of a restaurant based on provided variables. Utilised LGBM Regressor, CatBoost Regressor, and Random Forest Regressor to achieve optimal RMSE.',
            'image': 'project1.jpg',
            'link': 'https://github.com/Sahilchawla1094/Annual-Turnover-of-a-restaurant',
            'tags': ['LGBM', 'CatBoost', 'Regression', 'RMSE'],
        },
        {
            'title': 'Home Credit Default Risk',
            'description': 'Identify if a new client shows risk of loan default. Implemented Logistic Regression, Random Forest, and LightGBM to achieve a strong AUC score.',
            'image': 'project2.jpg',
            'link': 'https://github.com/Sahilchawla1094/Home-Credit-Default-Risk',
            'tags': ['LightGBM', 'Classification', 'AUC', 'Risk'],
        },
        {
            'title': 'Business Loan Default Prediction',
            'description': 'Determine if a business loan application will default. Employed Logistic Regression, Decision Tree, and Random Forest to predict the best F1 score.',
            'image': 'project3.jpg',
            'link': 'https://github.com/Sahilchawla1094/Predicting-whether-a-business-loan-applicant-will-default-or-not',
            'tags': ['Random Forest', 'F1 Score', 'Finance', 'Decision Tree'],
        },
        {
            'title': 'Thera Bank Liability Prediction',
            'description': 'Predict the likelihood of a liability customer buying personal loans using Artificial Neural Networks (ANN) to achieve the best F1 score.',
            'image': 'project4.jpg',
            'link': 'https://github.com/Sahilchawla1094/Thera-Bank',
            'tags': ['ANN', 'Deep Learning', 'Banking', 'F1 Score'],
        },
        {
            'title': 'Water Potability Analysis',
            'description': 'Identify whether water is safe for drinking based on provided variables. Utilised Artificial Neural Networks (ANN) to achieve the best accuracy score.',
            'image': 'project5.jpg',
            'link': 'https://github.com/Sahilchawla1094/Water-Potability',
            'tags': ['ANN', 'Binary Classification', 'Environment'],
        },
        {
            'title': 'Counter-Strike: GO Round Winner Prediction',
            'description': 'Predict the round winner using game-state variables. Implemented Logistic Regression, Decision Tree, Random Forest, and XGBoost to achieve the best accuracy.',
            'image': 'project6.jpg',
            'link': 'https://github.com/Sahilchawla1094/Counter-Strike--GO-Round-winner',
            'tags': ['XGBoost', 'Multi-model', 'Sports Analytics'],
        },
    ]

    for project in projects:
        img_b64 = get_image_base64(get_image_path("projects", project['image']))
        tags_html = ''.join(f'<span class="tech-chip">{t}</span>' for t in project['tags'])
        st.markdown(f"""
        <div class="project-card sc-reveal">
            <div class="project-img-wrapper">
                <img src="data:image/jpeg;base64,{img_b64}" alt="{project['title']}" />
            </div>
            <div class="project-content">
                <div class="project-title">{project['title']}</div>
                <p class="project-desc">{project['description']}</p>
                <div style="margin-bottom:16px;">{tags_html}</div>
                <a href="{project['link']}" target="_blank" class="project-link">
                    View on GitHub &nbsp;→
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── Other Platforms ────────────────────────────────────────────────────────────
def show_other_platforms():
    st.markdown("<div id='other-platforms'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Find Me Online</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Other Platforms</h1>', unsafe_allow_html=True)

    platforms = [
        {'title': 'GitHub',        'description': 'All things code',              'image': 'github.png',   'link': 'https://github.com/Sahilchawla1094'},
        {'title': 'LinkedIn',      'description': 'Connect professionally',       'image': 'linkedin.png', 'link': 'https://www.linkedin.com/in/sahil-chawla9799558521/'},
        {'title': 'Tableau Public','description': 'Data visualisations & dashboards', 'image': 'tableau.png',  'link': 'https://public.tableau.com/app/profile/sahil.chawla'},
    ]

    cols = st.columns(3, gap="medium")
    for idx, platform in enumerate(platforms):
        img_b64 = get_image_base64(get_image_path("icons", platform['image']))
        with cols[idx]:
            st.markdown(f"""
            <a href="{platform['link']}" target="_blank" style="text-decoration:none;">
                <div class="platform-card sc-reveal">
                    <img src="data:image/png;base64,{img_b64}" alt="{platform['title']}" />
                    <h3>{platform['title']}</h3>
                    <p>{platform['description']}</p>
                </div>
            </a>
            """, unsafe_allow_html=True)


# ── Contact ────────────────────────────────────────────────────────────────────
def show_contact():
    st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Get In Touch</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Contact Me</h1>', unsafe_allow_html=True)

    col_form, col_info = st.columns([1.3, 1], gap="large")

    with col_form:
        with st.form("contact_form"):
            c1, c2 = st.columns(2)
            with c1:
                name  = st.text_input("Name",    placeholder="Your full name")
                email = st.text_input("Email",   placeholder="your@email.com")
            with c2:
                phone   = st.text_input("Phone",   placeholder="+91 XXXXX XXXXX")
                address = st.text_input("Address", placeholder="Your city")
            message = st.text_area("Message", placeholder="Your message...", height=120)
            submit  = st.form_submit_button("Send Message  →")

        if submit:
            if not name or not email or not phone or not address or not message:
                st.error("Please fill in all fields.")
            else:
                try:
                    service_id  = st.secrets["emailjs"]["service_id"]
                    template_id = st.secrets["emailjs"]["template_id"]
                    user_id     = st.secrets["emailjs"]["user_id"]
                    data = {
                        "service_id": service_id, "template_id": template_id, "user_id": user_id,
                        "template_params": {
                            "from_name": name, "from_email": email,
                            "from_phone": phone, "from_address": address, "message": message,
                        },
                    }
                    response = requests.post(
                        "https://api.emailjs.com/api/v1.0/email/send", json=data, timeout=10
                    )
                    if response.status_code == 200:
                        st.success("Message sent successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to send message. Please try again.")
                except Exception:
                    st.error("An error occurred while sending the message.")

    with col_info:
        contact_details = [
            {'icon': 'phone.png',   'label': 'Phone',   'value': '+919799558521'},
            {'icon': 'email.png',   'label': 'Email',   'value': '<a href="mailto:Sahilchawla1094@gmail.com">Sahilchawla1094@gmail.com</a>'},
            {'icon': 'address.png', 'label': 'Address', 'value': 'A45 B HKM Nagar, Alwar (Raj)'},
        ]
        items_html = ''
        for d in contact_details:
            icon_b64 = get_image_base64(get_image_path("icons", d['icon']))
            items_html += f"""
            <div class="info-item">
                <img src="data:image/png;base64,{icon_b64}" alt="{d['label']}" class="contact-icon" />
                <p><strong style="color:#e2e8f0;">{d['label']}:</strong>&nbsp; {d['value']}</p>
            </div>"""
        st.markdown(f'<div class="contact-info-card sc-reveal">{items_html}</div>', unsafe_allow_html=True)


# ── Download CV ────────────────────────────────────────────────────────────────
def download_cv():
    st.markdown("<div id='download-cv'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Resume</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Download CV</h1>', unsafe_allow_html=True)

    cv_path = get_image_path("cv", "Resume___Sahil_Chawla.pdf")
    try:
        with open(cv_path, "rb") as file:
            _, col_btn, _ = st.columns([1, 1, 1])
            with col_btn:
                st.download_button(
                    label="⬇  Download CV",
                    data=file,
                    file_name="Resume___Sahil_Chawla.pdf",
                    mime="application/pdf",
                    key="download_cv_button",
                )
    except FileNotFoundError:
        st.warning("CV file not found. Ensure 'Resume___Sahil_Chawla.pdf' is in assets/cv/.")


# ── Footer ─────────────────────────────────────────────────────────────────────
def show_footer():
    github_b64   = get_image_base64(get_image_path('icons', 'github.png'))
    linkedin_b64 = get_image_base64(get_image_path('icons', 'linkedin.png'))
    email_b64    = get_image_base64(get_image_path('icons', 'email.png'))

    st.markdown(f"""
    <footer>
        <p>&copy; {datetime.now().year} &nbsp;·&nbsp; Sahil Chawla &nbsp;·&nbsp; Data Scientist &nbsp;·&nbsp; Built with Streamlit</p>
        <div>
            <a href="https://github.com/Sahilchawla1094" target="_blank">
                <img src="data:image/png;base64,{github_b64}" alt="GitHub" />
            </a>
            <a href="https://www.linkedin.com/in/sahil-chawla9799558521/" target="_blank">
                <img src="data:image/png;base64,{linkedin_b64}" alt="LinkedIn" />
            </a>
            <a href="mailto:Sahilchawla1094@gmail.com" target="_blank">
                <img src="data:image/png;base64,{email_b64}" alt="Email" />
            </a>
        </div>
    </footer>
    """, unsafe_allow_html=True)


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    inject_animations()
    show_profile()
    show_about()
    show_education()
    show_experience()
    show_skills()
    show_projects()
    show_other_platforms()
    show_contact()
    download_cv()
    show_footer()


if __name__ == "__main__":
    main()

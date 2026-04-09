# CLAUDE.md — Portfolio Project Reference

## Project Overview

This is **Sahil Chawla's personal portfolio website** built with **Streamlit**. It is a single-page application (`app.py`) that presents a professional data science portfolio with multiple sections rendered via custom HTML/CSS injected into Streamlit.

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Streamlit |
| Charts | Plotly (radar chart for skills) |
| Email | EmailJS via REST API (`requests`) |
| Styling | Custom CSS (`styles/style.css`) |
| Images | Base64-encoded (loaded locally, cached with `@st.cache_data`) |
| Theme | Light (configured in `.streamlit/config.toml`) |

## File Structure

```
My-Portfolio/
├── app.py                          # Main application (single entry point)
├── styles/
│   └── style.css                   # All custom CSS
├── assets/
│   ├── profile.jpg                 # Profile photo
│   ├── cv/
│   │   └── Resume___Sahil_Chawla.pdf
│   ├── projects/
│   │   ├── project1.jpg through project6.jpg
│   └── icons/
│       ├── phone.png, email.png, address.png
│       ├── github.png, linkedin.png, tableau.png
├── requirements.txt                # streamlit, plotly, requests
├── .streamlit/
│   └── config.toml                 # base="light" theme
├── diagram.txt                     # ASCII project structure diagram
└── .gitignore                      # Ignores venv/, .env, __pycache__, etc.
```

## app.py Architecture

The app is structured as a series of section functions called in sequence from `main()`:

| Function | Section | Key Details |
|---|---|---|
| `show_profile()` | Profile/Hero | Profile photo (base64), name, title, CTA buttons |
| `show_about()` | About | Bio paragraph, 4.5+ years experience |
| `show_education()` | Education | 5 entries from 10th grade to executive PGP |
| `show_experience()` | Experience | 3 roles at Great Learning (intern → faculty) and EY |
| `show_skills()` | Skills | Plotly Scatterpolar radar chart, 19 skills rated 65–90% |
| `show_projects()` | Projects | 6 ML projects with GitHub links and images |
| `show_other_platforms()` | Platforms | GitHub, LinkedIn, Tableau Public cards |
| `show_contact()` | Contact | Streamlit form → EmailJS API + contact info display |
| `download_cv()` | CV Download | `st.download_button` for the PDF CV |
| `show_footer()` | Footer | Copyright + social icons (base64) |

### Navigation
A fixed right-side emoji navbar is injected as raw HTML. On mobile (<576px) it collapses to a bottom bar.

### Image Handling
- All images are read from disk and base64-encoded via `get_image_base64()` (cached).
- `get_image_path()` builds paths using `pathlib.Path` with `.as_posix()` for cross-platform compatibility.

### Contact Form (EmailJS)
- Credentials stored in Streamlit secrets: `st.secrets["emailjs"]["service_id"]`, `template_id`, `user_id`.
- POSTs to `https://api.emailjs.com/api/v1.0/email/send`.
- Template params: `from_name`, `from_email`, `from_phone`, `from_address`, `message`.

## About Sahil Chawla (Portfolio Subject)

- **Current Role:** Technology Consultant – Data Scientist at Ernst & Young (EY), Gurugram
- **Experience:** 4.5+ years in Data Science & ML
- **Domains:** Supply Chain (EY), Ed-tech (Great Learning)

### Key Clients at EY
- **PepsiCo** – Data Product Manager (GDO/DFS/DRD documentation, end-to-end delivery)
- **The Schwan's Company** – MLOps (ML pipelines for inventory planning, +18% accuracy)
- **Ferrero Rocher** – PL/SQL developer (BlueYonder TMS optimizer: +90% truck utilization, -50% transport cost)
- **American Honda Motors** – MLOps + Power BI (identified $50M data gap)
- **Carnival Cruise Lines** – Python developer (SQL transformation automation)

### Notable Achievements at Great Learning
- Delivered courses across 15 concurrent batches
- Designed courses for NUS (National University of Singapore) and GLCA
- Generated INR 50 crore revenue through designed/delivered courses
- Built AI code tutor → +40% user satisfaction, +30% platform engagement

## Skills (Proficiency %)

Python 90, Data Analysis 90, Excel 90, SQL 85, Machine Learning 85, Data Engineering 80, Statistics 80, Streamlit 80, PySpark 75, Deep Learning 75, Power BI 75, Generative AI 75, LLMs & LangChain 70, NLP 70, Tableau 70, Microsoft Azure 70, PL/SQL 65, Databricks 65, Snowflake 65

## Projects (6 ML Projects on GitHub)

1. **Annual Turnover Prediction for Restaurant** — LGBM, CatBoost, Random Forest (RMSE)
2. **Home Credit Default Risk** — Logistic Regression, RF, LightGBM (AUC)
3. **Business Loan Application Default Prediction** — Logistic Regression, DT, RF (F1)
4. **Thera Bank Liability Prediction** — ANN (F1)
5. **Water Portability Analysis** — ANN (Accuracy)
6. **Counter-Strike: GO Round Winner Prediction** — LR, DT, RF, XGBoost (Accuracy)

All projects link to `https://github.com/Sahilchawla1094`.

## Contact Info

- **Phone:** +919799558521
- **Email:** Sahilchawla1094@gmail.com
- **Address:** A45 B HKM Nagar, Alwar (Raj)
- **LinkedIn:** https://www.linkedin.com/in/sahil-chawla9799558521/
- **GitHub:** https://github.com/Sahilchawla1094
- **Tableau:** https://public.tableau.com/app/profile/sahil.chawla

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Requires a `.streamlit/secrets.toml` with:
```toml
[emailjs]
service_id = "..."
template_id = "..."
user_id = "..."
```

## CSS Design Notes

- Font: Helvetica Neue (Google Fonts)
- Primary color: `#0071e3` (Apple-like blue)
- Background: white (`#FFFFFF`)
- Body text: `#666666`, headers: `#000000`
- Buttons: rounded (`border-radius: 25px`), blue with hover darkening
- Navbar: fixed right-side, emoji icons, circular hover effect
- Download CV button in navbar: green (`#28a745`)
- Platform cards: hover lifts with box-shadow
- Responsive breakpoints: 992px and 576px

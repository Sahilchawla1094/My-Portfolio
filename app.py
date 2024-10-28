import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import requests
import base64
from pathlib import Path

# Function to load local CSS
def local_css(file_name):
    css_path = Path(__file__).parent / file_name
    try:
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file '{file_name}' not found at {css_path}.")

# Function to encode images in Base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return encoded
    except FileNotFoundError:
        st.warning(f"Image not found at path: {image_path}")
        # Return a transparent pixel if image is not found
        return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII="

# Helper function to get image paths with forward slashes
def get_image_path(*args):
    return (Path(__file__).parent / "assets" / Path(*args)).as_posix()

# Set page configuration
st.set_page_config(page_title="Sahil Chawla | Data Scientist", layout="wide")

# Hide Streamlit default footer
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Inject custom CSS
local_css("styles/style.css")

# Inject meta description for SEO
st.markdown(
    """
    <meta name="description" content="Sahil Chawla's professional Data Scientist portfolio showcasing projects, skills, and contact information.">
    """,
    unsafe_allow_html=True
)

# Side Navigation Bar (Implemented as fixed right-hand side)
navbar = """
<nav class="navbar">
    <ul>
        <li><a href="#profile" title="Profile">🏠</a></li>
        <li><a href="#about" title="About">👨‍💼</a></li>
        <li><a href="#education" title="Education">🎓</a></li>
        <li><a href="#experience" title="Experience">💼</a></li>
        <li><a href="#skills" title="Skills">🛠️</a></li>
        <li><a href="#projects" title="Projects">📂</a></li>
        <li><a href="#other-platforms" title="Platforms">🔗</a></li>
        <li><a href="#contact" title="Contact">📞</a></li>
        <li><a href="#download-cv" class="download-cv" title="Download CV">📄</a></li>
    </ul>
</nav>
"""
st.markdown(navbar, unsafe_allow_html=True)

# Profile Section
def show_profile():
    st.markdown("<div id='profile'></div>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns([1, 2], gap="medium")
        
        with col1:
            # Load local profile image and encode it in Base64
            profile_image_path = get_image_path("profile.jpg")
            profile_image_base64 = get_image_base64(profile_image_path)
            st.markdown(
                f"""
                <img src="data:image/jpeg;base64,{profile_image_base64}" alt="Profile Image" style="width:100%; border-radius:10px;" />
                """,
                unsafe_allow_html=True
            )
        
        with col2:
            st.markdown("<h2>Hello, I'm</h2>", unsafe_allow_html=True)
            st.markdown("<h1>Sahil Chawla</h1>", unsafe_allow_html=True)
            st.markdown("<h3>Data Scientist</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <p>With over 3.5 years of professional experience, I specialize in Data Science within the Ed-tech and Supply Chain domains. My enthusiasm for Generative AI and Cloud technologies drives my passion to automate processes and simplify complex tasks, ensuring efficiency and innovation in every project I undertake.</p>
                <div style='text-align: left; margin-top: 20px; display: flex; gap: 15px;'>
                    <a href="#contact">
                        <button class="btn_color">Contact Info</button>
                    </a>
                    <a href="#download-cv">
                        <button class="btn_color">Download CV</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

# About Section
def show_about():
    st.markdown("<div id='about'></div>", unsafe_allow_html=True)
    st.markdown("<h2>Get To Know More</h2>", unsafe_allow_html=True)
    st.markdown("<h1>About Sahil Chawla</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown(
            """
            <div style='max-width: 800px; margin: auto; text-align: left;'>
                <p>I am an accomplished Associate Data Scientist with over 3.5 years of experience, renowned for delivering impactful results in the Ed-tech and Supply Chain domains. My journey has been marked by a deep expertise in Data Analysis and Data Engineering, coupled with a relentless pursuit of innovation through Generative AI and Cloud technologies.</p>
                <p>At Great Learning, I have spearheaded the development of numerous Data Science courses, including the prestigious Applications of Artificial Intelligence, PGP Data Science and Engineering, PGP Data Engineering, and the Great Learning Career Academy programs. My role involves comprehensive project management, strategic planning, and the creation of cutting-edge educational content that pushes the boundaries of traditional learning.</p>
                <p>My passion lies in automating processes to make tasks easier and more efficient, leveraging tools like Python, SQL, Spark, and cloud platforms like Microsoft Azure. This enthusiasm drives me to continuously explore and integrate new technologies into my work, ensuring that I stay at the forefront of the Data Science field.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Education Section
def show_education():
    st.markdown("<div id='education'></div>", unsafe_allow_html=True)
    st.markdown("<h2>My</h2>", unsafe_allow_html=True)
    st.markdown("<h1>Education</h1>", unsafe_allow_html=True)
    
    education = [
        {
            'degree': 'Executive PGP in Management (Data Science & Analytics)',
            'institution': 'Great Lakes Institute of Management, Gurugram',
            'duration': 'Feb 2022 - Feb 2023',
        },
        {
            'degree': 'Post Graduate Program in Data Science & Engineering',
            'institution': 'Great Lakes Institute of Management, Gurugram',
            'duration': 'Oct 2020 - Aug 2021',
        },
        {
            'degree': 'Bachelor of Technology in Civil Engineering',
            'institution': 'Anand International College of Engineering',
            'duration': '2013 - 2017',
            'percentage': '65%',
        },
        {
            'degree': '12th - PCMB',
            'institution': 'National Institute of Open Schooling',
            'duration': '2011 - 2012',
            'percentage': '65%',
        },
        {
            'degree': '10th Grade',
            'institution': 'St. Anselms Sr. Sec. School',
            'duration': '2009 - 2010',
            'percentage': '8.6 CGPA',
        }
    ]
    
    with st.container():
        for edu in education:
            edu_content = f"""
            <div style='margin-bottom: 1.5rem;'>
                <h3>{edu['degree']}</h3>
                <p><strong>{edu['institution']}</strong></p>
                <p>{edu['duration']}</p>
            """
            if 'percentage' in edu:
                edu_content += f"<p><strong>Percentage:</strong> {edu['percentage']}</p>"
            edu_content += "</div>"
            st.markdown(edu_content, unsafe_allow_html=True)
            st.markdown("---")

# Experience Section
def show_experience():
    st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
    st.markdown("<h2>My</h2>", unsafe_allow_html=True)
    st.markdown("<h1>Experience</h1>", unsafe_allow_html=True)
    
    experience = [
        {
            'title': 'Associate Data Scientist - Intern',
            'company': 'Great Learning, Gurugram',
            'duration': 'Aug 2021 - Dec 2021',
            'domain': 'Ed-tech',
            'technologies': ['Python', 'SQL', 'Excel', 'Tableau', 'Microsoft Azure'],
            'description': """
            - Worked closely with students to help them learn and apply cutting-edge technologies in data science.
            - Developed and taught courses on Microsoft Azure ML for creating new projects on Artificial Neural Networks (ANNs).
            - Created learning content on IBM Watson Assistant to help students understand and create Conversational/Action-based chatbots.
            - Managed the PGP-Data Engineering program, showcasing the ability to take ownership of complex programs.
            """
        },
        {
            'title': 'Associate Data Scientist',
            'company': 'Great Learning, Gurugram',
            'duration': 'Jan 2022 - Apr 2024',
            'domain': 'Ed-tech',
            'technologies': ['Python', 'SQL', 'Excel', 'Tableau', 'Machine Learning'],
            'description': """
            - Renowned for a strong track record in New Product Development (NPD), particularly in creating and spearheading Data Science courses.
            - Architect of significant programs such as Applications of Artificial Intelligence, PGP Data Science and Engineering, PGP Data Engineering, and the Great Learning Career Academy.
            - Demonstrates exceptional ownership, strategic foresight, and a commitment to developing cutting-edge educational content that pushes the boundaries of traditional learning.
            - Successfully orchestrated the operations of 25 running batches of the Great Learning Career Academy program, impacting over 7,000 student careers worldwide.
            - Utilizes platforms such as Excel, Tableau, and programming in Python (with libraries like Matplotlib and Seaborn) for deep data analysis and decision-making.
            - Developed an AI-code tutor providing real-time, contextual hints to users, leading to a 40% increase in user satisfaction and a 30% uplift in platform engagement metrics.
            """
        },
        {
            'title': 'Technology Consultant - Data Scientist',
            'company': 'Ernst & Young',
            'duration': 'Apr 2024 - Present',
            'domain': 'Supply Chain',
            'technologies': ['Excel', 'SQL', 'PL/SQL', 'Python', 'Langchain'],
            'description': """
            - Leveraged predictive analytics to streamline inventory management, minimizing stockouts and improving supply chain accuracy by 18% for Schwan’s company.
            - Developed an advanced Generative AI solution using Langchain to generate high-quality synthetic data, addressing data privacy and availability challenges.
            - Architected and implemented a custom Supply Chain Planning and Optimization (SCPO) Solver for BlueYonder's Transportation Management System using Oracle PL/SQL.
            - Created multi-condition loading processes and source shifting algorithms that increased truck utilization by 90% and reduced transportation costs by 50% for Ferrero Rocher.
            - Developed sophisticated truck loading optimization algorithms incorporating multiple constraints (stackability, weight limits, priority shipments), resulting in maximized asset utilization and improved operational efficiency.
            - clientele: 'The Schwans company', 'Ferrero Rocher', 'Carnival Cruise Line', 'BlueYonder'.
            """
        }
    ]
    
    with st.container():
        for exp in experience:
            technologies_used = ", ".join(exp['technologies'])
            # Split the description into list items
            description_items = [item.strip() for item in exp['description'].split('\n') if item.strip()]
            exp_content = f"""
            <div style='margin-bottom: 1.5rem;'>
                <h3>{exp['title']} - <em>{exp['company']}</em></h3>
                <p><strong>Duration:</strong> {exp['duration']}</p>
                <p><strong>Domain:</strong> {exp['domain']}</p>
                <p><strong>Technologies Used:</strong> {technologies_used}</p>
                <ul>
                    {''.join([f"<li>{item}</li>" for item in description_items])}
                </ul>
            </div>
            """
            st.markdown(exp_content, unsafe_allow_html=True)
            st.markdown("---")

# Skills Section with Plotly Radar Chart
def show_skills():
    st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
    st.markdown("<h2>My</h2>", unsafe_allow_html=True)
    st.markdown("<h1>Skills</h1>", unsafe_allow_html=True)
    
    # Technical Skills Data (Percentage)
    technical_skills = {
        'Python': 90,
        'SQL': 85,
        'Spark': 70,
        'Data Analysis': 90,
        'Data Engineering': 80,
        'Machine Learning': 80,
        'Deep Learning': 75,
        'Statistics': 80,
        'Tableau': 70,
        'Power BI': 70,
        'Looker Studio': 60,
        'Microsoft Azure': 70,
        'Excel': 90,
        'NLP': 70,
        'IBM Watson': 60,
        'Langchain': 50,
        'PL/SQL': 65,
        'Predictive Analytics': 80,
        'Generative AI': 60
    }
    
    # Languages
    languages = ['English', 'Hindi']
    
    # Prepare data for Radar Chart
    skills = list(technical_skills.keys())
    proficiency = list(technical_skills.values())
    
    # Radar charts require the data to loop back to the start
    skills += [skills[0]]
    proficiency += [proficiency[0]]
    
    fig = go.Figure(
        data=[
            go.Scatterpolar(
                r=proficiency,
                theta=skills,
                fill='toself',
                name='Proficiency',
                line=dict(color='#0071e3')
            )
        ]
    )
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickmode='linear',
                tick0=0,
                dtick=20
            )
        ),
        showlegend=False,
        title=dict(
            text='Technical Skills Proficiency',
            x=0.5,
            y=0.95,
            font=dict(size=20)
        ),
        margin=dict(l=50, r=50, t=100, b=50),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Display the Plotly Radar Chart
    st.plotly_chart(fig, use_container_width=True)
    
    # Display Languages
    st.markdown("### Languages")
    languages_col1, languages_col2 = st.columns([1, 1], gap="small")
    
    with languages_col1:
        for language in languages[:len(languages)//2]:
            st.markdown(f"- {language}")
    
    with languages_col2:
        for language in languages[len(languages)//2:]:
            st.markdown(f"- {language}")
    
    st.markdown("---")

# Projects Section
def show_projects():
    st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
    st.markdown("<h2>My</h2>", unsafe_allow_html=True)
    st.markdown("<h1>Projects</h1>", unsafe_allow_html=True)
    
    projects = [
        {
            'title': 'Annual Turnover Prediction for Restaurant',
            'description': 'Predict the Annual Turnover of a Restaurant based on provided variables. Utilized LGBM Regressor, CATBOOST Regressor, and Random Forest Regressor to achieve optimal RMSE.',
            'image': 'project1.jpg',
            'link': 'https://github.com/Sahilchawla1094/Annual-Turnover-of-a-restaurant'
        },
        {
            'title': 'Home Credit Default Risk',
            'description': 'Identify if a new client shows any risk of loan default based on provided variables. Implemented Logistic Regression, Random Forest Classifier, and LightGBM Classifier to achieve a good AUC score.',
            'image': 'project2.jpg',
            'link': 'https://github.com/Sahilchawla1094/Home-Credit-Default-Risk'
        },
        {
            'title': 'Business Loan Application Default Prediction',
            'description': 'Determine if a new business loan application will default based on provided variables. Employed Logistic Regression, Decision Tree Classifier, and Random Forest Classifier to predict the best F1 score.',
            'image': 'project3.jpg',
            'link': 'https://github.com/Sahilchawla1094/Predicting-whether-a-business-loan-applicant-will-default-or-not'
        },
        {
            'title': 'Thera Bank Liability Prediction',
            'description': 'Predict the likelihood of a liability customer buying personal loans using Artificial Neural Networks (ANN) to achieve the best F1 score.',
            'image': 'project4.jpg',
            'link': 'https://github.com/Sahilchawla1094/Thera-Bank'
        },
        {
            'title': 'Water Portability Analysis',
            'description': 'Identify whether water is safe for drinking based on provided variables. Utilized Artificial Neural Networks (ANN) to achieve the best Accuracy score.',
            'image': 'project5.jpg',
            'link': 'https://github.com/Sahilchawla1094/Water-Potability'
        },
        {
            'title': 'Counter-Strike: GO Round Winner Prediction',
            'description': 'Predict the match winner (terrorist or counter-terrorist) using variables from the dataset. Implemented Logistic Regression, Decision Tree Classifier, Random Forest Classifier, and XG Boost to achieve the best Accuracy score.',
            'image': 'project6.jpg',
            'link': 'https://github.com/Sahilchawla1094/Counter-Strike--GO-Round-winner'
        }
    ]
    
    with st.container():
        for project in projects:
            st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
            cols = st.columns([1, 2], gap="medium")
            with cols[0]:
                project_image_path = get_image_path("projects", project['image'])
                project_image_base64 = get_image_base64(project_image_path)
                st.markdown(
                    f"""
                    <img src="data:image/jpeg;base64,{project_image_base64}" alt="{project['title']} Image" style="width:100%; border-radius:10px;" />
                    """,
                    unsafe_allow_html=True
                )
            with cols[1]:
                st.markdown(f"### {project['title']}")
                st.write(project['description'])
                st.markdown(f"**[View Project]({project['link']})**")
        st.markdown("---")

# Other Platforms Section
def show_other_platforms():
    st.markdown("<div id='other-platforms'></div>", unsafe_allow_html=True)
    st.markdown("<h2>Explore My</h2>", unsafe_allow_html=True)
    st.markdown("<h1>Other Platforms</h1>", unsafe_allow_html=True)
    
    platforms = [
        {
            'title': 'GitHub',
            'description': 'All things code',
            'image': 'github.png',
            'link': 'https://github.com/Sahilchawla1094'
        },
        {
            'title': 'LinkedIn',
            'description': 'Connect with me professionally',
            'image': 'linkedin.png',
            'link': 'https://www.linkedin.com/in/sahil-chawla9799558521/'
        },
        {
            'title': 'Tableau Public',
            'description': 'Check out my data visualizations',
            'image': 'tableau.png',
            'link': 'https://public.tableau.com/app/profile/sahil.chawla'
        }
    ]
    
    with st.container():
        cols = st.columns(3, gap="medium")
        for idx, platform in enumerate(platforms):
            with cols[idx]:
                platform_image_path = get_image_path("icons", platform['image'])
                platform_image_base64 = get_image_base64(platform_image_path)
                st.markdown(
                    f"""
                    <a href="{platform['link']}" target="_blank" style='text-decoration: none; color: inherit;'>
                        <div class="platform-card">
                            <img src="data:image/png;base64,{platform_image_base64}" alt="{platform['title']} Icon" width="50" height="50" />
                            <h3>{platform['title']}</h3>
                            <p>{platform['description']}</p>
                        </div>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
    st.markdown("---")

# Contact Section
def show_contact():
    st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
    st.markdown("<h1>Contact Me</h1>", unsafe_allow_html=True)
    
    with st.container():
        # Contact Form
        with st.form("contact_form"):
            col1, col2 = st.columns([1, 1], gap="small")
            with col1:
                name = st.text_input("Name", placeholder="Enter your full name")
                email = st.text_input("Email", placeholder="Enter your email")
            with col2:
                phone = st.text_input("Phone", placeholder="+919799558521")
                address = st.text_input("Address", placeholder="A45 HKM Nagar, Alwar (Raj)")
            message = st.text_area("Message", placeholder="Your message...")
            submit = st.form_submit_button("Send Message")
        
        if submit:
            if not name or not email or not phone or not address or not message:
                st.error("Please fill in all fields.")
            else:
                try:
                    service_id = st.secrets["emailjs"]["service_id"]
                    template_id = st.secrets["emailjs"]["template_id"]
                    user_id = st.secrets["emailjs"]["user_id"]
                    
                    data = {
                        "service_id": service_id,
                        "template_id": template_id,
                        "user_id": user_id,
                        "template_params": {
                            "from_name": name,
                            "from_email": email,
                            "from_phone": phone,
                            "from_address": address,
                            "message": message
                        }
                    }
                    
                    response = requests.post("https://api.emailjs.com/api/v1.0/email/send", json=data)
                    
                    if response.status_code == 200:
                        st.success("Message sent successfully!")
                        st.experimental_rerun()
                    else:
                        st.error("Failed to send message. Please try again.")
                except Exception as e:
                    st.error("An error occurred while sending the message.")
    
    with st.container():
        # Contact Information with Icons
        st.markdown(
            """
            <div style='max-width: 800px; margin: 2rem auto; text-align: left;'>
                <h2>Contact Information</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        contact_details = [
            {
                'icon': 'phone.png',
                'alt': 'Phone Icon',
                'label': 'Phone',
                'value': '+919799558521'
            },
            {
                'icon': 'email.png',
                'alt': 'Email Icon',
                'label': 'Email',
                'value': '<a href="mailto:Sahilchawla1094@gmail.com">Sahilchawla1094@gmail.com</a>'
            },
            {
                'icon': 'address.png',
                'alt': 'Address Icon',
                'label': 'Address',
                'value': 'A45 HKM Nagar, Alwar (Raj)'
            }
        ]
        
        for detail in contact_details:
            icon_path = get_image_path("icons", detail['icon'])
            icon_base64 = get_image_base64(icon_path)
            st.markdown(
                f"""
                <div class='info-item'>
                    <img src="data:image/png;base64,{icon_base64}" alt="{detail['alt']}" class="contact-icon" />
                    <p><strong>{detail['label']}:</strong> {detail['value']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Download CV Section
def download_cv():
    st.markdown("<div id='download-cv'></div>", unsafe_allow_html=True)
    cv_path = get_image_path("cv", "Sahil_Chawla_CV.pdf")
    try:
        with open(cv_path, "rb") as file:
            st.download_button(
                label="Download CV",
                data=file,
                file_name="Sahil_Chawla_CV.pdf",
                mime="application/pdf",
                key="download_cv_button"
            )
    except FileNotFoundError:
        st.warning("CV file not found. Please ensure 'Sahil_Chawla_CV.pdf' is placed in the 'assets/cv/' directory.")

# Footer Section with Base64 Images
def show_footer():
    github_img = get_image_base64(get_image_path('icons', 'github.png'))
    linkedin_img = get_image_base64(get_image_path('icons', 'linkedin.png'))
    email_img = get_image_base64(get_image_path('icons', 'email.png'))
    footer_html = f"""
    <footer>
        <p>&copy; {datetime.now().year} Sahil Chawla. All Rights Reserved.</p>
        <div>
            <a href="https://github.com/Sahilchawla1094" target="_blank">
                <img src="data:image/png;base64,{github_img}" alt="GitHub" />
            </a>
            <a href="https://www.linkedin.com/in/sahil-chawla9799558521/" target="_blank">
                <img src="data:image/png;base64,{linkedin_img}" alt="LinkedIn" />
            </a>
            <a href="mailto:Sahilchawla1094@gmail.com" target="_blank">
                <img src="data:image/png;base64,{email_img}" alt="Email" />
            </a>
        </div>
    </footer>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

# Main App Logic
def main():
    show_profile()
    show_about()
    show_education()
    show_experience()
    show_skills()
    show_projects()
    show_other_platforms()
    show_contact()
    show_footer()
    
    # Add the Download CV button within a dedicated section
    download_cv()

if __name__ == "__main__":
    main()

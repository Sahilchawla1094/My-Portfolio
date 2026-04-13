export const personal = {
  name: "Sahil Chawla",
  role: "Data Scientist",
  tagline: "Building intelligent systems that drive measurable impact.",
  bio: [
    "Data Scientist with 4.5+ years of experience delivering Machine Learning and Generative AI solutions, currently working as a Technology Consultant at Ernst & Young (EY).",
    "Supported global enterprise clients including PepsiCo, American Honda Motors, Carnival Cruise Lines, Ferrero Rocher, and The Schwan's Company — driving improvements in cost efficiency, planning accuracy, and operational performance.",
    "Previously at Great Learning, I designed and delivered DS, DE, and GenAI courses across 15 concurrent batches, created programs for NUS (Singapore) and GLCA, generating INR 50 crore in revenue.",
  ],
  email: "Sahilchawla1094@gmail.com",
  phone: "+919799558521",
  address: "A45 B HKM Nagar, Alwar (Raj)",
  github: "https://github.com/Sahilchawla1094",
  linkedin: "https://www.linkedin.com/in/sahil-chawla9799558521/",
  tableau: "https://public.tableau.com/app/profile/sahil.chawla",
  cv: "/assets/cv/Resume___Sahil_Chawla.pdf",
  domain: "sahilchawla.xyz",
};

export const stats = [
  { value: 4.5, suffix: "+", label: "Years Experience", decimals: 1 },
  { value: 5,   suffix: "+", label: "Enterprise Clients", decimals: 0 },
  { value: 6,   suffix: "",  label: "ML Projects", decimals: 0 },
  { value: 50,  suffix: "Cr", label: "Revenue Generated", prefix: "₹", decimals: 0 },
];

export const experience = [
  {
    title: "Technology Consultant – Data Scientist",
    company: "Ernst & Young (EY)",
    location: "Gurugram",
    duration: "Apr 2024 – Present",
    domain: "Supply Chain",
    tech: ["Python", "PL/SQL", "PySpark", "LangChain", "Power BI", "Azure"],
    bullets: [
      "Data Product Manager for PepsiCo — SPOC/SME for data products, owned GDO and DFS/DRD documentation, led end-to-end delivery across build, UT, FT, SIT, and hypercare.",
      "MLOps engineer for The Schwan's Company — deployed ML pipelines for inventory planning, improving supply chain accuracy by 18%.",
      "PL/SQL developer for Ferrero Rocher — built supply chain optimisation solver for BlueYonder TMS: +90% truck utilisation, −50% transport cost.",
      "MLOps + Power BI for American Honda Motors — identified a $50M data gap across enterprise systems.",
      "Python developer for Carnival Cruise Lines — automated SQL transformation workflows.",
      "Built EY internal AI assets: GenAI synthetic data tool (LangChain + Streamlit) and ERNY 2.0 chatbot (LangChain + React).",
    ],
  },
  {
    title: "Associate Data Scientist – Faculty",
    company: "Great Learning",
    location: "Gurugram",
    duration: "Jan 2022 – Apr 2024",
    domain: "Ed-tech",
    tech: ["Python", "SQL", "Tableau", "Machine Learning", "Generative AI"],
    bullets: [
      "Designed and delivered DS, data engineering, and GenAI courses across 15 concurrent batches.",
      "Created courses for NUS (National University of Singapore) and GLCA — generating INR 50 crore in revenue.",
      "Built an AI code tutor with real-time contextual hints → +40% user satisfaction, +30% platform engagement.",
    ],
  },
  {
    title: "Associate Data Scientist Intern",
    company: "Great Learning",
    location: "Gurugram",
    duration: "Jan 2021 – Dec 2021",
    domain: "Ed-tech",
    tech: ["Python", "SQL", "Microsoft Azure", "IBM Watson"],
    bullets: [
      "Designed and delivered AI and ML learning modules using Microsoft Azure ML.",
      "Built IBM Watson Assistant tutorials for conversational and action-based chatbots.",
      "Implemented Azure Custom Vision projects including helmet and obstacle detection.",
    ],
  },
];

export const education = [
  {
    degree: "Executive PGP in Management (Data Science & Analytics)",
    institution: "Great Lakes Institute of Management, Gurugram",
    duration: "Feb 2022 – Feb 2023",
  },
  {
    degree: "Post Graduate Program in Data Science & Engineering",
    institution: "Great Lakes Institute of Management, Gurugram",
    duration: "Oct 2020 – Aug 2021",
  },
  {
    degree: "B.Tech in Civil Engineering",
    institution: "Anand International College of Engineering",
    duration: "2013 – 2017",
    grade: "65%",
  },
  {
    degree: "12th – PCMB",
    institution: "National Institute of Open Schooling",
    duration: "2011 – 2012",
    grade: "65%",
  },
  {
    degree: "10th Grade",
    institution: "St. Anselms Sr. Sec. School",
    duration: "2009 – 2010",
    grade: "8.6 CGPA",
  },
];

export const skills = [
  { name: "Python",           pct: 90 },
  { name: "Data Analysis",    pct: 90 },
  { name: "Excel",            pct: 90 },
  { name: "SQL",              pct: 85 },
  { name: "Machine Learning", pct: 85 },
  { name: "Data Engineering", pct: 80 },
  { name: "Statistics",       pct: 80 },
  { name: "Streamlit",        pct: 80 },
  { name: "PySpark",          pct: 75 },
  { name: "Deep Learning",    pct: 75 },
  { name: "Power BI",         pct: 75 },
  { name: "Generative AI",    pct: 75 },
  { name: "LLMs & LangChain", pct: 70 },
  { name: "NLP",              pct: 70 },
  { name: "Tableau",          pct: 70 },
  { name: "Microsoft Azure",  pct: 70 },
  { name: "PL/SQL",           pct: 65 },
  { name: "Databricks",       pct: 65 },
  { name: "Snowflake",        pct: 65 },
];

export const projects = [
  {
    title: "Annual Turnover Prediction",
    subtitle: "Restaurant Revenue Forecasting",
    description: "Predict the annual turnover of a restaurant using LGBM Regressor, CatBoost Regressor, and Random Forest. Optimised for RMSE.",
    image: "/assets/projects/project1.jpg",
    tags: ["LGBM", "CatBoost", "Regression"],
    link: "https://github.com/Sahilchawla1094/Annual-Turnover-of-a-restaurant",
  },
  {
    title: "Home Credit Default Risk",
    subtitle: "Loan Default Classification",
    description: "Identify client loan default risk using Logistic Regression, Random Forest, and LightGBM. Optimised for AUC score.",
    image: "/assets/projects/project2.jpg",
    tags: ["LightGBM", "Classification", "AUC"],
    link: "https://github.com/Sahilchawla1094/Home-Credit-Default-Risk",
  },
  {
    title: "Business Loan Default",
    subtitle: "SME Credit Risk Prediction",
    description: "Predict whether a business loan application will default using Logistic Regression, Decision Tree, and Random Forest.",
    image: "/assets/projects/project3.jpg",
    tags: ["Random Forest", "F1 Score", "Finance"],
    link: "https://github.com/Sahilchawla1094/Predicting-whether-a-business-loan-applicant-will-default-or-not",
  },
  {
    title: "Thera Bank Liability",
    subtitle: "Personal Loan Propensity",
    description: "Predict the likelihood of a liability customer buying personal loans using Artificial Neural Networks. Optimised for F1.",
    image: "/assets/projects/project4.jpg",
    tags: ["ANN", "Deep Learning", "Banking"],
    link: "https://github.com/Sahilchawla1094/Thera-Bank",
  },
  {
    title: "Water Potability",
    subtitle: "Drinking Water Safety Analysis",
    description: "Classify whether water is safe for drinking using ANN. Optimised for accuracy across multiple water quality parameters.",
    image: "/assets/projects/project5.jpg",
    tags: ["ANN", "Binary Classification"],
    link: "https://github.com/Sahilchawla1094/Water-Potability",
  },
  {
    title: "CS:GO Round Winner",
    subtitle: "Esports Match Prediction",
    description: "Predict round winners using game-state variables with Logistic Regression, Decision Tree, Random Forest, and XGBoost.",
    image: "/assets/projects/project6.jpg",
    tags: ["XGBoost", "Multi-model", "Sports Analytics"],
    link: "https://github.com/Sahilchawla1094/Counter-Strike--GO-Round-winner",
  },
];

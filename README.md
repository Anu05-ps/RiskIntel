# 🛡️ RiskIntel

## Cyber Crime Intelligence & Fraud Detection Platform

RiskIntel is an end-to-end Data Science and Analytics platform that combines Cyber Crime Intelligence, Women & Children Safety Analytics, PostgreSQL-powered analytics, and Machine Learning-based Fraud Detection.

The platform transforms raw cybercrime and financial transaction data into actionable intelligence through Exploratory Data Analysis (EDA), SQL Analytics, Machine Learning, and Interactive Dashboards.

---

# 🚀 Problem Statement

Cybercrime and digital fraud continue to increase across India, impacting individuals, organizations, women, and children.

While large volumes of cybercrime and financial transaction data exist, extracting meaningful insights for decision-making remains a challenge.

This project aims to:

- Identify cybercrime hotspots across India
- Analyze cybercrime impact on women and children
- Detect fraudulent financial transactions
- Build a data-driven intelligence platform for risk assessment
- Support decision-making using analytics and machine learning

---

# 📊 Project Overview

RiskIntel combines:

✅ Exploratory Data Analysis (EDA)

✅ PostgreSQL Database Integration

✅ SQL Analytics

✅ Machine Learning

✅ Fraud Detection

✅ Streamlit Dashboard

into a unified intelligence platform.

---

# 🛠️ Technology Stack

| Category | Tools |
|-----------|---------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Database | PostgreSQL |
| SQL Integration | SQLAlchemy |
| Machine Learning | Scikit-Learn |
| Dashboard | Streamlit |
| Version Control | Git, GitHub |

---

# 📂 Datasets Used

### Cyber Crime in India
- State-wise cybercrime statistics
- Crime rates
- Chargesheet rates
- Population data

### Cyber Crime Against Women
- State-wise cybercrime incidents
- Women safety analytics

### Cyber Crime Against Children
- Child cybercrime incidents
- Risk assessment

### Credit Card Fraud Dataset
- 284,807 transactions
- Highly imbalanced fraud detection dataset

---

# 🖥️ Dashboard Overview

## Home Dashboard

![Home Dashboard](screenshots/home.png)

The Home Dashboard provides an executive-level summary of the entire platform.

### Dashboard Summary

| Metric | Value |
|----------|----------|
| Total Cyber Crimes | 50,035 |
| Average Crime Rate | 2.78 |
| Highest Risk State | Uttar Pradesh |
| Highest Cases Recorded | 11,097 |
| Women Cybercrime Cases | 10,405 |
| Children Cybercrime Cases | 1,102 |

### Key Insights

- More than **50,000 cybercrime cases** were analyzed.
- Uttar Pradesh emerged as the highest-risk state with **11,097 cases**.
- Women-related cybercrime incidents were nearly **9.4 times higher** than child-related incidents.
- The dashboard serves as a centralized intelligence hub for cybercrime analytics and fraud detection.

---

# 🌐 Cyber Crime Intelligence

## Top States by Cyber Crime Cases

![Top States](screenshots/top_10_cyber_crime_by_state.png)

### Key Findings

- Uttar Pradesh reported approximately **11,097 cybercrime cases**, the highest among all states.
- Karnataka followed closely with more than **10,700 cases**.
- Maharashtra and Telangana also emerged as major cybercrime hotspots.
- The Top 4 states contributed a substantial share of all reported cybercrime incidents.

---

## Cyber Crime Growth Analysis (2018–2020)

![Growth Analysis](screenshots/cyber_crime_growth_2018_2020.png)

### Key Findings

- Karnataka experienced the highest increase in cybercrime, adding nearly **5,000 new cases** between 2018 and 2020.
- Uttar Pradesh showed a similar growth trend.
- Telangana emerged as a rapidly growing cybercrime hotspot.

---

## Cyber Crime Correlation Analysis

![Correlation Matrix](screenshots/cyber_correlation_matrix.png)

### Key Findings

- Cybercrime volumes from 2018–2020 showed extremely strong correlations (**0.98–0.99**).
- Cybercrime growth strongly correlated with crime rate (**0.80 correlation**).
- Chargesheeting rate showed very weak correlation with crime volume.

---

## Cyber Crime Motives

![Cyber Crime Motives](screenshots/cyber_crime_motives.png)

### Key Findings

- Fraud was the dominant cybercrime motive with approximately **30,000+ reported cases**.
- Fraud-related crimes accounted for nearly **60% of all cybercrime motives analyzed**.
- Sexual exploitation and extortion were among the next most significant categories.

---

## Fraud Hotspots by State

![Fraud Motive States](screenshots/fraud_motive_by_state.png)

### Key Findings

- Karnataka recorded nearly **9,700 fraud-related incidents**, the highest among all states.
- Uttar Pradesh and Telangana followed closely behind.
- Fraud-related cybercrime was concentrated in a small number of high-risk states.

---

# 👩 Women Cybercrime Analysis

## Top States by Cyber Crimes Against Women

![Women Crime States](screenshots/cybercrime_against_women.png)

### Key Findings

- Karnataka recorded approximately **2,900 cybercrime incidents against women**.
- Maharashtra ranked second with around **1,600 incidents**.
- Assam, Uttar Pradesh, and Telangana also emerged as high-risk states.

---

## Types of Cyber Crimes Against Women

![Women Crime Types](screenshots/type_of_cyber_crime_against_women.png)

### Key Findings

- Cyber pornography and obscene content publication represented the largest category after total incidents.
- Cyber bullying and harassment remain major threats to women online.
- Fake profile creation and defamation continue to contribute significantly to cyber abuse.

---

## Women Cybercrime Correlation Analysis

![Women Correlation](screenshots/women_correlation_matrix.png)

### Key Findings

- Cyber blackmailing and cyber bullying exhibited a strong positive relationship (**0.61 correlation**).
- Cyber pornography and fake profile creation showed moderate association (**0.43 correlation**).
- Total crimes against women strongly correlated with other cybercrime categories (**0.97 correlation**).

---

# 👶 Children Cybercrime Analysis

## Top States by Cyber Crimes Against Children

![Children Crime States](screenshots/child_crime_by_state.png)

### Key Findings

- Maharashtra recorded over **200 incidents**, the highest among all states.
- Uttar Pradesh followed closely with nearly **200 incidents**.
- Karnataka and Kerala also emerged as significant hotspots.

---

## Types of Cyber Crimes Against Children

![Children Crime Types](screenshots/crime_category_against_children.png)

### Key Findings

- Cyber pornography involving children accounted for approximately **740 incidents**, making it the most significant category.
- Cyber stalking and bullying contributed nearly **140 incidents**.
- Child exploitation-related crimes dominate cybercrime trends against children.

---

## Children Cybercrime Correlation Analysis

![Children Correlation](screenshots/correlation_matrix_children.png)

### Key Findings

- Total child cybercrime incidents showed an extremely high correlation (**0.97**) with child pornography-related crimes.
- Cyber stalking and bullying strongly correlated (**0.73**) with harassment cases.
- Exploitation-related offenses are major contributors to overall child cybercrime volumes.

---

# 🛡️ Vulnerable Population Analytics

## Vulnerable Population Index

![Vulnerability Index](screenshots/vulnerability_population_index.png)

### Key Findings

- Karnataka achieved the highest Vulnerable Population Index score (**~3000**).
- Maharashtra ranked second (**~1800**).
- Assam and Uttar Pradesh followed as high-risk states.
- The Top 4 states represented the majority of vulnerability exposure.

### Impact

The Vulnerable Population Index helps identify regions requiring:

- Targeted cyber awareness campaigns
- Digital safety initiatives
- Focused law enforcement intervention
- Enhanced victim support systems

---

# 📍 State Clustering Analysis

![State Clusters](screenshots/crime_state_cluster.png)

### Key Findings

- States naturally formed four distinct cybercrime clusters.
- A small number of states exhibited significantly higher cybercrime activity than the national average.
- Clustering enabled better identification of high-risk regions.

---

# 🤖 Machine Learning: Fraud Detection

## Fraud Detection Feature Analysis

![Feature Importance](screenshots/fraud_detection_features.png)

### Top Fraud Indicators

| Feature | Importance |
|----------|----------|
| V17 | 22.8% |
| V14 | 20.0% |
| V12 | 10.5% |
| V10 | 7.5% |
| V16 | 7.3% |

### Key Findings

- V17 emerged as the strongest fraud indicator.
- V17, V14, and V12 together contributed over **53% of total model importance**.
- Fraudulent transactions exhibited highly distinguishable patterns.

---

## Confusion Matrix

![Confusion Matrix](screenshots/fraud_label.png)

### Key Findings

- Correctly identified **56,852 legitimate transactions**.
- Correctly detected **68 fraudulent transactions**.
- Generated only **12 false positives**.
- Maintained high precision despite severe class imbalance.

---

# 🎯 Model Performance

![Model Performance](screenshots/model_performance.png)

### Random Forest Classifier

| Metric | Score |
|----------|----------|
| Precision | 93% |
| Recall | 81% |
| ROC-AUC | 0.903 |

### Performance Highlights

- Achieved **93% precision** on highly imbalanced financial transaction data.
- Achieved **81% recall**, successfully identifying fraudulent activities.
- ROC-AUC score of **0.903** demonstrates strong predictive capability.
- Suitable for real-world fraud risk assessment scenarios.

---

# 🗄️ PostgreSQL Integration

PostgreSQL was integrated to support:

- Structured data storage
- SQL-based analytics
- Dashboard connectivity
- Efficient querying and reporting

### Example Query

```sql
SELECT state,
crime_2020
FROM cybercrime_india
ORDER BY crime_2020 DESC;
```

### Benefits

- Faster analytical workflows
- Centralized data management
- Improved scalability
- Efficient integration with Streamlit

---

# 🎯 Project Outcomes

✔ Analyzed **284,807 financial transactions**

✔ Analyzed cybercrime data across **36 Indian States and UTs**

✔ Built a custom **Vulnerable Population Index**

✔ Integrated **PostgreSQL and SQL Analytics**

✔ Developed a **Random Forest Fraud Detection Model**

✔ Achieved **93% Precision** and **0.903 ROC-AUC**

✔ Built a complete **end-to-end Data Science project**

✔ Combined **EDA → SQL → PostgreSQL → Machine Learning → Dashboard Development**

---

# 📁 Project Structure

```text
RiskIntel/
│
├── app/
├── data/
├── models/
├── notebook/
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 👨‍💻 Author

**Anu PS**

Data Analytics | Data Science | Machine Learning

GitHub: https://github.com/Anu05-ps/RiskIntel


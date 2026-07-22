# 📊 Placement Analytics Dashboard

> An end-to-end Data Analytics project that simulates a university placement ecosystem using **Python, PostgreSQL, SQL, and Power BI**.

The placement process generates thousands of records every recruitment season—from student registrations and company drives to interviews and final offers. However, answering questions such as **Which companies hire the most?**, **Where do students drop off in the hiring funnel?**, or **What is the overall placement rate?** often requires combining data spread across multiple systems.

To solve this, I built a complete analytics pipeline that models a realistic university placement workflow, stores it in a normalized PostgreSQL database, analyzes it using SQL, and visualizes executive KPIs in an interactive Power BI dashboard.

---

# Dashboard Preview

> Interactive Executive Dashboard
> <img width="1761" height="994" alt="image" src="https://github.com/user-attachments/assets/7cd9e6d2-55f1-45da-b3ce-cdfd761a46f4" />

With respect to EE branch (interactive dashboard)
<img width="1806" height="1053" alt="image" src="https://github.com/user-attachments/assets/97f85f09-8067-4946-946e-29824bb6a8eb" />




---

# Database Model

> Relational Database Schema

<img width="2443" height="1023" alt="image" src="https://github.com/user-attachments/assets/fb10183f-93f3-4e34-8b7f-3c84057ad3eb" />



---

# Project Highlights

✔ Designed a normalized PostgreSQL database with **7 interconnected tables**

✔ Generated realistic synthetic datasets using **Python**

✔ Simulated the complete recruitment lifecycle

✔ Built analytical SQL queries to derive business insights

✔ Developed an interactive Power BI dashboard with executive KPIs

✔ Automated the complete data generation pipeline

---

# Project Architecture

```
                Python Scripts
                       │
                       ▼
          Synthetic CSV Dataset Generation
                       │
                       ▼
              PostgreSQL Database
                       │
                       ▼
              SQL Analytics Layer
                       │
                       ▼
          Interactive Power BI Dashboard
```

---

# Recruitment Workflow

The project models a realistic university placement process.

```
Student Registration
          │
          ▼
Eligibility Check
          │
          ▼
Company Applications
          │
          ▼
Online Assessment
          │
          ▼
Interview Rounds
          │
          ▼
Offer Generation
          │
          ▼
Final Placement
```

---

# Dataset Scale

| Dataset | Records |
|---------|---------:|
| Students | 5,000 |
| Companies | 150 |
| Placement Drives | 250 |
| Applications | 36,297 |
| Interview Rounds | 34,257 |
| Offers | 11,419 |

The dataset was intentionally generated at a realistic scale to simulate the analytical challenges encountered during university placement seasons.

---

# Database Design

The database follows a relational design consisting of seven tables.

```
Branches
     │
     ▼
Students
     │
     ▼
Applications
     │
     ▼
Interview Rounds
     │
     ▼
Offers

Companies
     │
     ▼
Placement Drives
     │
     └──────────────► Applications
```

Relationships are enforced using primary and foreign keys to maintain referential integrity across all placement stages.

---

# Dashboard KPIs

The dashboard provides executive-level metrics including:

- 👨‍🎓 Total Students
- 🏢 Total Companies
- 📅 Total Placement Drives
- 📝 Total Applications
- 💼 Total Offers
- 🎯 Placement Rate
- 💰 Highest CTC
- 📈 Average CTC
- 🎤 Total Interview Rounds

---

# Business Insights

The dashboard enables placement coordinators to answer questions such as:

- Which branches receive the highest number of offers?
- Which companies hire the most students?
- What percentage of students successfully receive offers?
- Which placement drives attract the maximum applications?
- What is the average compensation offered?
- Where do candidates drop off during the hiring funnel?
- How is hiring distributed across different recruiters?

---

# Dashboard Visualizations

The dashboard contains:

- Executive KPI Cards
- Placement Funnel
- Branch-wise Placement Distribution
- Company-wise Hiring Analysis
- Offer Distribution
- Average & Highest Package Analysis
- Hiring Trends
- Placement Summary

---

# SQL Analytics

Some of the analytical queries implemented include:

### Total Students

```sql
SELECT COUNT(*)
FROM students;
```

---

### Branch-wise Offers

```sql
SELECT
    b.branch_name,
    COUNT(o.offer_id) AS total_offers
FROM branches b
JOIN students s
ON b.branch_id = s.branch_id
JOIN applications a
ON s.student_id = a.student_id
JOIN offers o
ON a.application_id = o.application_id
GROUP BY b.branch_name
ORDER BY total_offers DESC;
```

---

### Company Hiring Rank (Window Function)

```sql
SELECT
    c.company_name,
    COUNT(o.offer_id) AS offers,
    RANK() OVER(
        ORDER BY COUNT(o.offer_id) DESC
    ) AS hiring_rank
FROM companies c
JOIN placement_drives d
ON c.company_id = d.company_id
JOIN applications a
ON d.drive_id = a.drive_id
JOIN offers o
ON a.application_id = o.application_id
GROUP BY c.company_name;
```

---

### Placement Rate

```sql
SELECT
ROUND(
COUNT(DISTINCT o.application_id)*100.0 /
COUNT(DISTINCT a.application_id),
2
) AS placement_rate
FROM applications a
LEFT JOIN offers o
ON a.application_id = o.application_id;
```

More analytical queries are available in:

```
sql/analytics_queries.sql
```

---

# Engineering Challenges

Some interesting engineering challenges solved during development:

- Designing a normalized relational database for a realistic placement workflow.

- Maintaining referential integrity while generating over **80,000+ interconnected records**.

- Simulating believable recruitment behaviour using probabilistic data generation.

- Building reusable Python scripts to automate dataset creation.

- Creating SQL queries capable of generating executive KPIs directly from the database.

- Connecting PostgreSQL with Power BI through a relational model.

---

# Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Synthetic Data Generation |
| PostgreSQL | Relational Database |
| SQL | Data Analysis |
| Power BI | Dashboard & Visualization |
| Git | Version Control |
| GitHub | Project Hosting |

---

# Project Structure

```
Placement-Analytics
│
├── dashboard/
│   └── Placement Analytics Dashboard.pbix
│
├── data/
│
├── docs/
│
├── python/
│
├── sql/
│
└── README.md
```

---

# How to Run

### Clone Repository

```bash
git clone https://github.com/<your-username>/placement-analytics-dashboard.git
```

### Create Database

```sql
CREATE DATABASE placement_analytics;
```

### Import CSV Files

Import all generated CSV datasets into PostgreSQL.

### Execute Analytics Queries

Run

```
sql/analytics_queries.sql
```

### Open Dashboard

Open

```
dashboard/Placement Analytics Dashboard.pbix
```

and refresh the PostgreSQL data source.

---

# Future Enhancements

- Recruiter Performance Dashboard
- Branch-wise Placement Benchmarking
- Drill-through Reports
- Historical Placement Trend Analysis
- Incremental Data Refresh
- Student Placement Cohort Analysis

---

# Author

**Nehal Chaudhary**

B.Tech Electronics & Communication Engineering (AI/ML)

Netaji Subhas University of Technology (NSUT)

---

## ⭐ If you found this project useful, consider giving it a star!

# 📊 Placement Analytics Dashboard

An end-to-end data analytics project that simulates a university placement process using synthetic data, PostgreSQL, SQL analytics, Python automation, and an interactive Power BI dashboard.

The project demonstrates the complete analytics pipeline—from designing a relational database and generating realistic datasets to querying insights with SQL and visualizing KPIs for decision-making.

---

# Dashboard Preview

> Add your dashboard screenshot here

![Dashboard](docs/dashboard.png)

---

# Database Schema

> Add your ERD / Model View screenshot here

![Database Model](docs/database_model.png)

---

# Project Overview

This project simulates the placement process of a university with **5,000+ students**, **150 companies**, and **250 placement drives**.

The complete recruitment lifecycle is modeled:

Student Registration
→ Company Eligibility
→ Applications
→ Online Assessment
→ Interview Rounds
→ Offers
→ Final Selection

The generated data is stored in PostgreSQL and analyzed using SQL and Power BI.

---

# Features

- Relational PostgreSQL database design
- Synthetic dataset generation using Python
- Automated placement simulation
- SQL analytical queries
- Interactive Power BI dashboard
- Placement KPI tracking
- Hiring trend analysis
- Offer conversion analysis
- Branch-wise placement insights

---

# Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Synthetic data generation |
| PostgreSQL | Relational database |
| SQL | Analytics queries |
| Power BI | Dashboard & Visualization |
| Git | Version Control |
| GitHub | Project Hosting |

---

# Database Design

The project contains the following tables:

```
branches
companies
students
placement_drives
applications
interview_rounds
offers
```

Relationships:

```
Companies
      │
      ▼
Placement Drives
      │
      ▼
Applications
      │
      ▼
Interview Rounds
      │
      ▼
Offers

Students ───────────────┘
Branches ───────────────► Students
```

---

# Dataset Statistics

| Dataset | Records |
|---------|---------:|
| Students | 5,000 |
| Companies | 150 |
| Placement Drives | 250 |
| Applications | 36,297 |
| Interview Rounds | 34,257 |
| Offers | 11,419 |

---

# Dashboard KPIs

The dashboard includes:

- Total Students
- Total Companies
- Total Placement Drives
- Total Applications
- Total Interview Rounds
- Total Offers
- Placement Rate
- Highest Package
- Average Package

Additional Visualizations:

- Application Funnel
- Branch-wise Applications
- Hiring Trend
- Company-wise Hiring
- Offer Distribution
- Placement Analysis

---

# Folder Structure

```
Placement-Analytics/
│
├── dashboard/
│   └── Placement Analytics Dashboard.pbix
│
├── data/
│   ├── students.csv
│   ├── companies.csv
│   ├── placement_drives.csv
│   ├── applications.csv
│   ├── interview_rounds.csv
│   └── offers.csv
│
├── python/
│   ├── generate_students.py
│   ├── generate_companies.py
│   ├── generate_drives.py
│   ├── generate_applications.py
│   ├── generate_interviews.py
│   └── generate_offers.py
│
├── sql/
│   └── analytics_queries.sql
│
├── docs/
│   ├── dashboard.png
│   └── database_model.png
│
└── README.md
```

---

# SQL Analytics

Example insights generated using SQL:

- Placement Rate
- Average CTC
- Highest CTC
- Applications by Branch
- Offers by Company
- Interview Success Rate
- Hiring Trend
- Company-wise Hiring
- Top Recruiters

---

# Dashboard Insights

The dashboard enables recruiters and placement coordinators to answer questions such as:

- Which branches receive the highest number of offers?
- Which companies recruit the most students?
- What is the overall placement rate?
- What is the average offered package?
- Which placement drives attract the most applications?
- How does hiring vary across companies?

---

# Future Improvements

- Recruiter Performance Dashboard
- Student Skill Analytics
- Resume Score Prediction
- Interview Success Prediction using Machine Learning
- Placement Forecasting
- Interactive Filters & Drill-through Reports

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/yourusername/placement-analytics-dashboard.git
```

## Create PostgreSQL Database

```sql
CREATE DATABASE placement_analytics;
```

## Import CSV Files

Import all generated CSV files into PostgreSQL.

## Execute SQL Queries

Run:

```
sql/analytics_queries.sql
```

## Open Dashboard

Open:

```
dashboard/Placement Analytics Dashboard.pbix
```

Refresh the data source if required.

---

# Key Learnings

- Relational Database Design
- Data Modeling
- SQL Analytics
- Synthetic Data Generation
- Dashboard Development
- Power BI Relationships
- Data Visualization
- KPI Design

---

# Author

**Nehal Chaudhary**

B.Tech Electronics & Communication Engineering (AI/ML)

Netaji Subhas University of Technology (NSUT)

---

⭐ If you found this project interesting, consider giving it a star!

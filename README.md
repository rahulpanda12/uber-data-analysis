# 🚖 Uber Data Analysis

An end-to-end Data Analytics project that transforms messy Uber trip data into meaningful business insights using **Python, Pandas, NumPy, Matplotlib, MySQL, and SQL**.

---

## 📌 Project Overview

Real-world datasets are rarely clean. This project focuses on:

- Cleaning and validating raw data
- Handling missing values and duplicates
- Feature engineering
- Exploratory Data Analysis (EDA)
- Data visualization
- SQL-based analysis using MySQL
- Extracting business insights

### Workflow

```text
Raw CSV
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Visualizations
   ↓
MySQL Database
   ↓
SQL Analysis
   ↓
Business Insights
```

---

## 📂 Dataset Information

The dataset contains Uber trip records with:

- Start & End Date/Time
- Trip Category
- Start & Stop Locations
- Distance (Miles)
- Trip Purpose

### Dataset Summary

| Metric | Value |
|----------|---------|
| Original Records | 1,156 |
| Clean Records | 1,154 |
| Original Columns | 7 |
| Final Columns | 11 |

---

## 🧹 Data Cleaning

The raw dataset contained:

- Missing values
- Duplicate records
- Inconsistent location names
- Mixed date formats
- Non-trip summary rows

Cleaning steps:

- Removed duplicate records
- Removed non-trip rows
- Handled missing values
- Standardized locations
- Parsed datetime columns
- Filled missing purposes as `Unknown`

---

## ⚙️ Feature Engineering

Additional features created:

| Feature | Description |
|----------|-------------|
| MONTH | Trip month |
| DAY_OF_WEEK | Day name |
| HOUR | Trip hour |
| DISTANCE_TYPE | Short / Medium / Long |

### Distance Categories

| Type | Miles |
|--------|--------|
| Short | ≤ 5 |
| Medium | 5–15 |
| Long | > 15 |

---

## 📊 Exploratory Data Analysis

The project analyzes:

- Business vs Personal Trips
- Trip Purposes
- Start & Stop Locations
- Common Routes
- Distance Patterns
- Outliers
- Hourly Trends
- Weekly Trends
- Monthly Trends

---

## 🔍 Key Insights

### Trip Categories

| Category | Trips | Percentage |
|-----------|--------|-------------|
| Business | 1077 | 93.33% |
| Personal | 77 | 6.67% |

---

### Trip Purpose

Top recorded purposes:

- Meeting → 186
- Meal/Entertain → 160
- Errand/Supplies → 128
- Customer Visit → 101

⚠️ 43.5% of trips had unknown purposes.

---

### Location Insights

Most active locations:

| Location | Total Activity |
|------------|----------------|
| Cary | 403 |
| Unknown Location | 297 |
| Morrisville | 169 |
| Whitebridge | 133 |

Most common route:

```text
Morrisville → Cary (75 trips)
Cary → Morrisville (67 trips)
```

---

### Distance Insights

| Metric | Value |
|----------|---------|
| Average Distance | 10.57 miles |
| Median Distance | 6 miles |
| Maximum Distance | 310.3 miles |

Most trips were Short or Medium distance.

---

### Time Insights

- Peak Hour: **3 PM (98 trips)**
- Busiest Day: **Friday (206 trips)**
- Peak Month: **December (146 trips)**

---

## 🗄 SQL Analysis

The cleaned dataset was imported into MySQL.

SQL analysis included:

- GROUP BY
- Aggregations
- Filtering
- Subqueries
- UNION ALL
- Route Analysis

SQL Scripts:

```text
sql/
├── schema.sql
├── business_analysis.sql
├── purpose_analysis.sql
├── location_analysis.sql
├── distance_analysis.sql
└── time_analysis.sql
```

---

## 📈 Visualizations

Generated charts:

- Trips by Hour
- Trips by Day
- Trips by Month
- Distance Distribution
- Average Distance by Hour

Stored inside:

```text
reports/
```

---

## 🛠 Tech Stack

### Programming

- Python
- SQL

### Libraries

- Pandas
- NumPy
- Matplotlib

### Database

- MySQL

### Tools

- VS Code
- MySQL Workbench
- Git
- GitHub

---

## 📁 Project Structure

```text
uber-data-analysis/
│
├── data/
├── reports/
├── src/
├── sql/
├── README.md
└── .gitignore
```

---

## 🎯 Skills Demonstrated

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- SQL Query Writing
- Data Visualization
- Database Management
- Business Insight Generation
- Git & GitHub Workflow

---

## ⚠️ Limitations

- 43.5% trip purposes are unknown.
- Dataset does not represent all Uber demand.
- Some locations are ambiguous.
- Long trips affect average-distance calculations.

---

## 👨‍💻 Author

**Rahul Panda**

B.Tech CSE | Data Analytics & Data Science Enthusiast

GitHub: https://github.com/rahulpanda12

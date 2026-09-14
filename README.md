\# Uber Data Analysis



An end-to-end data analysis project using Python, Pandas, NumPy, Matplotlib, MySQL, and SQL to clean, explore, and extract insights from Uber trip data.



\## Project Objective



The goal of this project is to transform messy raw Uber trip data into clean, structured data and use Python and SQL to identify meaningful patterns in trip behavior.



The project covers the complete data analysis workflow:



Raw Data → Data Cleaning → Feature Engineering → EDA → MySQL → SQL Analysis → Insights



\## Dataset



The dataset contains Uber trip records with information such as:



\- Start and end date/time

\- Trip category

\- Start and stop locations

\- Distance in miles

\- Trip purpose



The original dataset contained 1,156 rows and 7 columns.



After cleaning, the dataset contains 1,154 valid records and 11 columns.



\## Data Cleaning



The raw dataset contained missing values, duplicate records, inconsistent location names, mixed date formats, and a non-trip `Totals` row.



The cleaning process included:



\- Removing the non-trip `Totals` row

\- Removing duplicate records

\- Handling missing values

\- Standardizing inconsistent location names

\- Parsing mixed date formats

\- Filling missing trip purposes as `Unknown`

\- Removing records missing essential fields

\- Creating additional analytical features



\### Feature Engineering



The following features were created:



\- `MONTH`

\- `DAY\_OF\_WEEK`

\- `HOUR`

\- `DISTANCE\_TYPE`



Distance was categorized as:



\- Short: ≤ 5 miles

\- Medium: 5–15 miles

\- Long: > 15 miles



\## Exploratory Data Analysis



The project analyzes:



\- Business vs Personal trips

\- Trip purposes

\- Start and stop locations

\- Common routes

\- Distance distribution

\- Distance outliers

\- Trips by hour

\- Trips by day of week

\- Trips by month

\- Average distance by hour



\## Key Findings



\### Trip Category



\- Business trips: 1,077 (93.33%)

\- Personal trips: 77 (6.67%)



The dataset is heavily dominated by business-related trips.



\### Trip Purpose



The most common recorded purpose was:



\- Meeting: 186 trips

\- Meal/Entertain: 160 trips

\- Errand/Supplies: 128 trips

\- Customer Visit: 101 trips



However, 502 trips (43.50%) have an unknown purpose, which is an important data-quality limitation.



\### Locations



Cary had the highest overall start/stop activity with 403 recorded activities.



The most common known route was:



\- Morrisville → Cary: 75 trips

\- Cary → Morrisville: 67 trips



\### Distance



\- Average trip distance: 10.57 miles

\- Median trip distance: 6 miles

\- Maximum trip distance: 310.3 miles



Most trips were Short or Medium distance, while a relatively small number of long trips contributed substantially to total mileage.



\### Time



The busiest recorded hour was 3 PM with 98 trips.



Friday had the highest number of recorded trips with 206.



December had the highest monthly trip count with 146.



These results describe the trips contained in this dataset and should not be interpreted as overall Uber demand.



\## SQL Analysis



The cleaned dataset was imported into MySQL and analyzed using SQL.



SQL scripts are organized into:



\- `schema.sql`

\- `business\_analysis.sql`

\- `purpose\_analysis.sql`

\- `location\_analysis.sql`

\- `distance\_analysis.sql`

\- `time\_analysis.sql`



The SQL analysis uses operations such as:



\- `GROUP BY`

\- `COUNT`

\- `SUM`

\- `AVG`

\- `ROUND`

\- `ORDER BY`

\- `WHERE`

\- Subqueries

\- `UNION ALL`



\## Visualizations



The project generates visualizations for:



\- Trips by day

\- Trips by hour

\- Trips by month

\- Trip distance distribution

\- Average trip distance by hour



All generated charts are stored in the `reports/` directory.



\## Project Structure



```text

uber-data-analysis/

│

├── data/

│   ├── raw/

│   └── processed/

│       └── uber\_cleaned.csv

│

├── reports/

│   ├── trips\_by\_day.png

│   ├── trips\_by\_hour.png

│   ├── trips\_by\_month.png

│   ├── distance\_boxplot.png

│   └── avg\_distance\_by\_hour.png

│

├── src/

│   ├── data\_cleaning.py

│   ├── eda.py

│   ├── business\_analysis.py

│   ├── purpose\_analysis.py

│   ├── location\_analysis.py

│   ├── distance\_analysis.py

│   └── time\_analysis.py

│

├── sql/

│   ├── schema.sql

│   ├── business\_analysis.sql

│   ├── purpose\_analysis.sql

│   ├── location\_analysis.sql

│   ├── distance\_analysis.sql

│   └── time\_analysis.sql

│

├── download\_data.py

├── data\_inspection.py

├── .gitignore

└── README.md


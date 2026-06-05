# API Data Pipeline Project (End-to-End Data Engineering Project)

## 🚀 Project Overview
This project demonstrates a complete data engineering pipeline using Python, Pandas, Apache Spark, and SQL.

The pipeline extracts data from a public API, transforms it, processes it using Spark, and performs SQL-based analysis for insights.

---

## 🏗️ Architecture

API → Python Extraction → Pandas Transformation → Spark Processing → SQL Analysis → Insights

---

## 🔧 Tech Stack
- Python
- Pandas
- Apache Spark (PySpark)
- SQL
- Git & GitHub
- JSONPlaceholder API

---

## 📥 Data Extraction
- Data is fetched from a public API using Python `requests`
- Raw JSON is converted into structured format

📄 File: `extract_api_data.py`

---

## 🔄 Data Transformation
- Cleaned and formatted using Pandas
- Handled missing values
- Prepared dataset for Spark processing

📄 File: `transform_users_data.py`

---

## ⚡ Spark Processing
- Loaded data into Apache Spark
- Created temporary views for analysis
- Performed distributed processing

📄 File: `spark_user_processing.py`

---

## 📊 SQL Analysis
- Executed SQL queries on dataset
- Used aggregations and filtering
- Extracted insights from user data

📄 File: `user_data_sql_analysis.py`

---

## 📌 Key Skills Demonstrated
- API data extraction
- Data cleaning and transformation
- Big data processing with Spark
- SQL analytics
- End-to-end pipeline design
- GitHub project management

---

## 📷 Screenshots

### 📥 API Extraction

![API Output](screenshots/api_output.png)

---

### 🔄 Pandas Transformation

![Pandas Summary](screenshots/pandas_summary.png)

![Pandas Table](screenshots/pandas_table.png)

---

### ⚡ Spark Processing

![Spark Output 1](screenshots/spark_output_1.png)

![Spark Output 2](screenshots/spark_output_2.png)

![Spark Output 3](screenshots/spark_output_3.png)

![Spark Output 4](screenshots/spark_output_4.png)

---

### 📊 SQL Analysis

![SQL Output 1](screenshots/sql_output_1.png)

![SQL Output 2](screenshots/sql_output_2.png)

![SQL Output 3](screenshots/sql_output_3.png)

![SQL Output 4](screenshots/sql_output_4.png)

![SQL Output 5](screenshots/sql_output_5.png)


---

## 🚀 Future Improvements
- Automate pipeline using Apache Airflow
- Deploy on AWS (S3 + Glue + Redshift)
- Add logging & monitoring
- Build dashboard using Power BI / Tableau

---

## 👩‍💻 Author
Vrushali Waghmode
Aspiring Data Engineer

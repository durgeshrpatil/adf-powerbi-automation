# Automated Sales ETL & Reporting – Azure ADF + Power BI + Databricks

This project demonstrates a basic ETL pipeline that loads sales data from a CSV file into Azure Data Lake, transforms it using Databricks (PySpark), and visualizes it in a Power BI dashboard. Designed to simulate real-world automation with parameterized ADF pipelines and PBIX-based dashboard refresh.

---

## 🔧 Tools Used
- Azure Data Factory (ADF)
- Azure Databricks (PySpark)
- Azure Data Lake Storage (ADLS Gen2)
- Power BI (PBIX + Gateway)
- PostgreSQL (optional for source simulation)

---

## 📊 Workflow Overview
1. ADF extracts data from Blob/CSV
2. Loads to Azure Data Lake
3. Databricks notebook transforms the data (cleaning, aggregation)
4. Final data pushed to Power BI via .pbix file
5. PBIX file is refreshed via UI or service gateway

---

## 📁 Files
- `datasets/sales_data.csv`: Sample dataset
- `databricks-script/transform_sales_data.py`: PySpark transformation logic
- `powerbi-dashboard.pbix`: Pre-built Power BI dashboard with DAX measures
- `adf-pipeline-screenshot.png`: Visual of ADF pipeline
- `pipeline-design.md`: Project flow explanation

---

## 🚀 Key Concepts
- ADF Pipeline & Trigger
- Databricks Delta Table usage
- Power BI automation using PBIX
- Data cleansing and aggregation logic

---

## 👨‍💻 Author
**Durgesh Patil**  
[LinkedIn](https://www.linkedin.com/in/durgesh-patil-0784b7326/) | [Email](mailto:durgeshrpatil@gmail.com)


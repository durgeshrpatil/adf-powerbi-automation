# Project Design: Azure ADF + Databricks + Power BI

This project demonstrates an end-to-end data pipeline using Azure services and Power BI.

## 🔄 Data Flow

1. **Data Source (sales_data.csv):**
   - Simulated flat file containing sales data.
   - Uploaded to Azure Blob Storage.

2. **Azure Data Factory (ADF):**
   - Ingests the CSV file from Blob Storage.
   - Triggers transformation job in Azure Databricks.

3. **Azure Databricks (PySpark):**
   - Reads raw data.
   - Performs cleaning and aggregation.
   - Writes output to Azure Data Lake (Parquet or Delta format).

4. **Azure Synapse / Power BI:**
   - Transformed data can be consumed directly by Power BI via ADLS or Synapse SQL Pools.
   - Power BI .pbix file visualizes total sales per product.

## 🧰 Tools Used
- Azure Data Factory (for orchestration)
- Azure Databricks (for transformation)
- Power BI (for visualization)
- Azure Blob Storage / ADLS Gen2 (for data storage)

## 🚀 Goal
Automate sales data reporting using scalable cloud services and produce insightful dashboards with minimal manual effort.

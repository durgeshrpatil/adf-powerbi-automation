from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Initialize Spark session
spark = SparkSession.builder.appName("SalesDataTransformation").getOrCreate()

# Load data from CSV (replace with actual path in production)
df = spark.read.option("header", True).csv("sales_data.csv", inferSchema=True)

# Data cleaning: remove rows with nulls (if any)
df_clean = df.dropna()

# Convert data types if needed
df_clean = df_clean.withColumn("Quantity", col("Quantity").cast("int"))                    .withColumn("Price", col("Price").cast("double"))

# Aggregation: Total sales per product
df_summary = df_clean.groupBy("Product").agg(
    _sum(col("Quantity") * col("Price")).alias("Total_Sales")
)

# Show the result
df_summary.show()

# Save transformed data to Delta or Parquet (example)
df_summary.write.mode("overwrite").parquet("output/sales_summary")

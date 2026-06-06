# Databricks notebook source
# ================================
# IMPORT LIBRARIES
# ================================

import requests
import pandas as pd

from pyspark.sql.functions import upper, count

# ================================
# STEP 1 — EXTRACT API DATA
# ================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print("API Extraction Successful!")

# ================================
# STEP 2 — TRANSFORM DATA
# ================================

df_flat = pd.json_normalize(data)

df_clean = df_flat[[
    'id',
    'name',
    'username',
    'email',
    'address.city',
    'phone',
    'company.name'
]]

df_clean = df_clean.rename(columns={
    'address.city': 'city',
    'company.name': 'company_name'
})

# Data Quality Checks
print("\nMissing Values")
print(df_clean.isnull().sum())

print("\nDuplicate Records")
print(df_clean.duplicated().sum())

# Cleaning
df_clean = df_clean.dropna()
df_clean = df_clean.drop_duplicates()

# Data Type Conversion
df_clean['id'] = df_clean['id'].astype(int)

print("\nRecords After Cleaning:", len(df_clean))

# ================================
# STEP 3 — CREATE SPARK DATAFRAME
# ================================

spark_df = spark.createDataFrame(df_clean)

print("\nSpark DataFrame Created Successfully!")

print("Total Records:", spark_df.count())

# ================================
# STEP 4 — SAVE AS TABLE
# ================================

spark_df.write.mode("overwrite").saveAsTable("users_table")

print("users_table Created Successfully!")

# ================================
# STEP 5 — SHOW DATA
# ================================

spark_df.show()

# ================================
# STEP 6 — PRINT SCHEMA
# ================================

spark_df.printSchema()

# ================================
# STEP 7 — SELECT COLUMNS
# ================================

print("\nSelected Columns")

spark_df.select(
    "name",
    "city"
).show()

# ================================
# STEP 8 — FILTER DATA
# ================================

print("\nUsers From Gwenborough")

spark_df.filter(
    spark_df.city == "Gwenborough"
).show()

# ================================
# STEP 9 — ADD NEW COLUMN
# ================================

spark_df = spark_df.withColumn(
    "name_upper",
    upper("name")
)

print("\nNew Column Added")

spark_df.show()

# ================================
# STEP 10 — DISTINCT VALUES
# ================================

print("\nDistinct Cities")

spark_df.select("city").distinct().show()

# ================================
# STEP 11 — SORT DATA
# ================================

print("\nSorted By Name")

spark_df.orderBy("name").show()

# ================================
# STEP 12 — GROUP BY
# ================================

print("\nUsers Per City")

spark_df.groupBy(
    "city"
).count().show()

# ================================
# STEP 13 — AGGREGATION
# ================================

print("\nCity Wise User Count")

spark_df.groupBy(
    "city"
).agg(
    count("*").alias("total_users")
).show()

# ================================
# STEP 14 — CREATE SQL VIEW
# ================================

spark_df.createOrReplaceTempView("users")

print("SQL View Created Successfully!")

# ================================
# COMPLETED
# ================================

print("Spark Processing Completed Successfully!")
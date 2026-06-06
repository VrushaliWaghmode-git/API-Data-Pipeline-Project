# Databricks notebook source
import requests
import pandas as pd

# API Extraction
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

# Flatten JSON
df_flat = pd.json_normalize(data)

# Clean Data
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

# Convert to Spark DataFrame
spark_df = spark.createDataFrame(df_clean)

# Create SQL Temporary View
spark_df.createOrReplaceTempView("users")

print("SQL View Created Successfully!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM userss_table;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🔥 STEP 3 — Run SQL Queries

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 1 — Show All Users
# MAGIC
# MAGIC SELECT * FROM users ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 2 — Show Only Name And City
# MAGIC
# MAGIC  SELECT name,
# MAGIC        city
# MAGIC FROM users;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 3 — Count Total Users
# MAGIC -- ❓ Problem :: Find total number of users.
# MAGIC
# MAGIC SELECT COUNT (*) AS total_users
# MAGIC FROM users ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 4 — Distinct Cities
# MAGIC -- ❓ Problem :: Show unique cities.
# MAGIC SELECT DISTINCT city
# MAGIC FROM users ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 5 — Filter Specific City
# MAGIC -- ❓ Problem  :::: Show users from Gwenborough.
# MAGIC
# MAGIC SELECT * 
# MAGIC FROM  users 
# MAGIC WHERE city = "Gwenborough"

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 6 — Sort Names Alphabetically
# MAGIC -- ❓ Problem :: Sort users by name.
# MAGIC
# MAGIC SELECT  *
# MAGIC FROM users 
# MAGIC ORDER BY name  ;

# COMMAND ----------

# MAGIC %sql
# MAGIC --✅ Query 7 — Sort Descending
# MAGIC --❓ Problem :: Sort names in descending order.
# MAGIC
# MAGIC SELECT *
# MAGIC FROM users
# MAGIC ORDER BY name DESC;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 8 — Count Users Per City
# MAGIC -- ❓ Problem :: Find total users in each city.
# MAGIC
# MAGIC  SELECT city , COUNT (*)AS total_users
# MAGIC  FROM users 
# MAGIC  GROUP BY  city ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 9 — Company Wise User Count
# MAGIC -- ❓ Problem :: Find number of users in each company.
# MAGIC
# MAGIC SELECT company_name, COUNT(*) AS total_users
# MAGIC FROM users 
# MAGIC GROUP BY company_name
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 10 — HAVING Clause
# MAGIC -- ❓ Problem :: Show cities having more than 1 user.
# MAGIC
# MAGIC SELECT city , COUNT (*) AS total_users 
# MAGIC FROM users
# MAGIC GROUP BY city 
# MAGIC HAVING COUNT (*) > 1 ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 11 — Uppercase Names & lowercase Names
# MAGIC -- ❓ Problem :: Convert names to uppercase. and Lowercase 
# MAGIC
# MAGIC SELECT UPPER (name) AS upper_name
# MAGIC FROM users ;
# MAGIC
# MAGIC
# MAGIC SELECT LOWER AS lower_name
# MAGIC FROM users ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 12 — Name Length
# MAGIC -- ❓ Problem :: Find length of each user name.
# MAGIC
# MAGIC SELECT name, LENGTH(name) AS name_length
# MAGIC FROM users ;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 13 — Add Static Column
# MAGIC -- ❓ Problem :: Add country column with value 'India'. (2️⃣ 'India' AS country  . This is the key part.
# MAGIC
# MAGIC -- It means:
# MAGIC --👉 Create a NEW column
# MAGIC
# MAGIC --👉 Name it country
# MAGIC
# MAGIC --👉 Fill SAME value "India" for every row
# MAGIC
# MAGIC --So it is a static / constant column.)
# MAGIC
# MAGIC SELECT *,
# MAGIC        'India' AS country
# MAGIC FROM users;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 14 — CASE WHEN
# MAGIC -- ❓ Problem :: Categorize cities.
# MAGIC
# MAGIC -- ✅ Solution
# MAGIC
# MAGIC SELECT name, city,
# MAGIC     CASE
# MAGIC         WHEN city = 'Gwenborough'
# MAGIC         THEN 'Tier 1'
# MAGIC
# MAGIC         ELSE 'Other'
# MAGIC     END AS city_category
# MAGIC
# MAGIC FROM users;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 15 — ROW_NUMBER Window Function
# MAGIC -- ❓ Problem :: Assign row numbers within each city.
# MAGIC
# MAGIC SELECT name,city,
# MAGIC     ROW_NUMBER() OVER(
# MAGIC         PARTITION BY city
# MAGIC         ORDER BY name
# MAGIC     ) AS row_num
# MAGIC
# MAGIC FROM users;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 16 — RANK Function
# MAGIC -- ❓ Problem :: Rank users inside each city.
# MAGIC
# MAGIC -- ✅ Solution
# MAGIC
# MAGIC SELECT name,city,
# MAGIC
# MAGIC     RANK() OVER(
# MAGIC         PARTITION BY city
# MAGIC         ORDER BY name
# MAGIC     ) AS rank_num
# MAGIC
# MAGIC FROM users;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 17 — DENSE_RANK Function
# MAGIC -- ❓ Problem :: Dense rank users inside each city.
# MAGIC
# MAGIC --✅ Solution
# MAGIC
# MAGIC SELECT
# MAGIC     name,
# MAGIC     city,
# MAGIC
# MAGIC     DENSE_RANK() OVER(
# MAGIC         PARTITION BY city
# MAGIC         ORDER BY name
# MAGIC     ) AS dense_rank_num
# MAGIC
# MAGIC FROM users;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ✅ Query 18 — First User Per City
# MAGIC -- ❓ Problem :: Find alphabetically first user from each city.  
# MAGIC
# MAGIC SELECT *
# MAGIC FROM (
# MAGIC
# MAGIC     SELECT name,city,
# MAGIC
# MAGIC         ROW_NUMBER() OVER(
# MAGIC             PARTITION BY city
# MAGIC             ORDER BY name
# MAGIC         ) AS rn
# MAGIC     FROM users
# MAGIC ) t
# MAGIC
# MAGIC WHERE rn = 1;
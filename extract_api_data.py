# Databricks notebook source
import requests
import pandas as pd

# Step 1 — API Extraction

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    # Check API status
    response.raise_for_status()

    data = response.json()

    print("API Extraction Successful")

except Exception as e:
    print("API Extraction Failed")
    print(e)

# Step 2 — Convert JSON to DataFrame

df = pd.DataFrame(data)

print("Total Records:", len(df))

df.head()


# COMMAND ----------


# Databricks notebook source
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

# -------------------------------
# TRANSFORM DATA NOTEBOOK
# -------------------------------

# Step 1 — Flatten Nested JSON

df_flat = pd.json_normalize(data)

print("Flattened Data")
display(df_flat.head())

# Step 2 — Select Required Columns

df_clean = df_flat[[
    'id',
    'name',
    'username',
    'email',
    'address.city',
    'phone',
    'company.name'
]]

# Step 3 — Rename Columns

df_clean = df_clean.rename(columns={
    'address.city': 'city',
    'company.name': 'company_name'
})

# Step 4 — Data Quality Checks

print("\nMissing Values")
print(df_clean.isnull().sum())

print("\nDuplicate Records")
print(df_clean.duplicated().sum())

print("\nRecords Before Cleaning")
print(len(df_clean))

# Step 5 — Drop Null Values

df_clean = df_clean.dropna()

# Step 6 — Remove Duplicate Rows

df_clean = df_clean.drop_duplicates()

# Step 7 — Change Data Types

df_clean['id'] = df_clean['id'].astype(int)

# Step 8 — Validation

print("\nRecords After Cleaning")
print(len(df_clean))

print("\nTotal Columns")
print(len(df_clean.columns))

# Step 9 — Final Clean Data

print("\nFinal Cleaned Data")
display(df_clean.head())

# Step 10 — Save Clean Data

try:
    df_clean.to_csv("clean_users.csv", index=False)
    print("\nClean CSV File Created Successfully!")
except Exception as e:
    print("\nCSV Save Skipped:", e)
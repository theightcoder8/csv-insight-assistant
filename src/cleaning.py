#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

def clean_data(df):
    # 1. Standardizing column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("%", "percent")

    # 2. Dropping duplicate rows
    df = df.drop_duplicates()

    # 3. Dropping completely empty rows/columns
    df = df.dropna(how='all')         # drop rows where ALL values are NaN
    df = df.dropna(axis=1, how='all') # drop columns where ALL values are NaN

    # 4. Converting obvious numeric columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')  # will leave text untouched

    return df


# In[ ]:





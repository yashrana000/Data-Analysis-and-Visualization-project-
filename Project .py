import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

data = pd.read_csv("Project Data.csv")
df= pd.DataFrame(data)
print(df)

df=df.drop(columns=['Timestamp'])
df=df.drop(columns=['Is there is any gum and teeth related diseases have been there in your family trade  '])

columns_with_missing_values = df.columns[df.isnull().any()].tolist()

for column in columns_with_missing_values:
    if df[column].dtype == 'float64': 
        df[column].fillna(df[column].mean(), inplace=True)
        
for column in columns_with_missing_values:
    if df[column].dtype == 'object':  
        df[column].fillna(df[column].mode().iloc[0], inplace=True)
        
for column in df.columns:
    if df[column].dtype == 'object':  # Check if the column contains object/string data
        df[column] = df[column].str.upper()

for column in df.columns:
    if df[column].dtype == 'object':  # Check if the column contains object/string data
        df[column] = df[column].str.strip()
    
df.to_csv('Project Data2.csv', index=False)

##########################################################################################





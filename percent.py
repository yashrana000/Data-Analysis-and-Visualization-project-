import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('Project Data2.csv')

columns_of_interest = [
 'Which brand of toothpaste do you commonly use ?',
 'Which factor influence your choice of toothpaste ?',
 'Are you satisfied with the toothpaste you use ?',
 'Have you switched toothpaste brands in the past year? if yes then why?',
 'For how long you brush your teeth ?',
 'Which type of brush are you using ?',
 'How often do you brush your teeth in a typical day ?',
 'Do you use any additional oral care product such as mouthwash or dental floss ?',
 'Do you follow any specific brushing techniques recommended by your dentist ?',
 'Do you drink hot or cold beverages regularly ?',
 'Do you consume Tea or Coffee regularly ? ',
 'Have you experienced any dental issues even after doing regular brushing ? ',
 'Have you faced any issue after using a certain toothpaste? if yes then name the toothpaste ',
 'How much sugar do you consume daily ?',
 'Have you ever diagnose with any problem related to teeth ?',
 'Do you consume any of these Tobacco, alcohol and smoking ?']  


for column_name in columns_of_interest:
    unique_values = df[column_name].unique()
    print(f"Column: {column_name}")
    for value in unique_values:
        value_count = (df[column_name] == value).sum()
        total_values = len(df[column_name])
        percentage = (value_count / total_values) * 100
        print(f"Percentage of '{value}' occurrences: {percentage:.2f}%")
    print()     
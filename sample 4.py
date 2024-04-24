import pandas as pd
import numpy as np


df = pd.read_csv('Project Data2.csv')


toothpaste_brand = df['Which brand of toothpaste do you commonly use ?']
brushing_frequency = df['How often do you brush your teeth in a typical day ?']
brushing_duration = df['For how long you brush your teeth ?']
hot_cold_beverage = df['Do you drink hot or cold beverages regularly ?']
tea_coffee_consumption = df['Do you consume Tea or Coffee regularly ? ']
sugar_consumption = df['How much sugar do you consume daily ?']
dental_issues = df['Have you experienced any dental issues even after doing regular brushing ? ']


hot_cold_beverage = np.where(hot_cold_beverage == 'Yes', 1, 0)
tea_coffee_consumption = np.where(tea_coffee_consumption == 'Yes', 1, 0)


toothpaste_dental_issues = pd.crosstab(toothpaste_brand, dental_issues, normalize='index') * 100

brushing_dental_issues = pd.crosstab(brushing_frequency, dental_issues, normalize='index') * 100


duration_dental_issues = pd.crosstab(brushing_duration, dental_issues, normalize='index') * 100


print("\nToothpaste vs. Dental Issues:")
print(toothpaste_dental_issues)

print("\nBrushing Frequency vs. Dental Issues:")
print(brushing_dental_issues)

print("\nBrushing Duration vs. Dental Issues:")
print(duration_dental_issues)
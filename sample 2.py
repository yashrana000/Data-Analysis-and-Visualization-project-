import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


toothpaste_dental_issues = pd.crosstab(toothpaste_brand, dental_issues)


brushing_dental_issues = pd.crosstab(brushing_frequency, dental_issues)

duration_dental_issues = pd.crosstab(brushing_duration, dental_issues)


plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 2)
brushing_dental_issues.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Brushing Frequency vs. Dental Issues')
plt.xlabel('Number of Times Brushed per Day')
plt.ylabel('Number of Participants')
plt.legend(title='Dental Issues', bbox_to_anchor=(1, 1))


plt.tight_layout()
plt.show()
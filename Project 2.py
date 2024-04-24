import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


['Name', 'Email Id or Phone Number ',
 'Age ', 'Gender ', 'Which state are you in ?',
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


df = pd.read_csv('Project Data2.csv')
##column_name = 'Age'
##
### Check if the specified column exists in the DataFrame
##if column_name not in df.columns:
##    print(f"Error: Column '{column_name}' not found in the DataFrame. Available columns are: {df.columns.tolist()}")
##else:
##    # Count the occurrences of each unique value in the specified column
##    value_counts = df[column_name].value_counts()


###################'Age'########################

value_counts = df['Which state are you in ?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Which state are you in ?')
plt.xlabel('State')
plt.ylabel('Count')
plt.show()

value_counts = df['Age '].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Bar Chart of Age')
plt.xlabel('Age')
plt.ylabel(' ')
plt.show()

age_mean=df['Age '].mean()
print("Average age is:")
print(age_mean)

###################'Gender'########################

value_counts = df['Gender '].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Gender')
plt.show()


mode_value = df['Gender '].mode()[0]  # Get the first mode (in case of multiple modes)
mode_count = df['Gender '].value_counts()[mode_value]

total_values = len(df['Gender '])
mode_percentage = (mode_count / total_values) * 100

print(mode_value,"  ",mode_count,mode_percentage)

###################'Which brand of toothpaste do you commonly use ?'########################

value_counts = df['Which brand of toothpaste do you commonly use ?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Which brand of toothpaste do you commonly use ?')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.show()

mode_value1= df['Which brand of toothpaste do you commonly use ?'].mode()[0]  # Get the first mode (in case of multiple modes)
mode_count1= df['Which brand of toothpaste do you commonly use ?'].value_counts()[mode_value1]

total_values1 = len(df['Which brand of toothpaste do you commonly use ?'])
mode_percentage1 = (mode_count1 / total_values1) * 100

print(mode_value1,"  ",mode_count1,mode_percentage1)


###################'Do you drink hot or cold beverages regularly ?'########################


value_counts = df['Do you drink hot or cold beverages regularly ?'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Do you drink hot or cold beverages regularly ?')
plt.show()

###################'Are you satisfied with the toothpaste you use ?'########################

value_counts = df['Are you satisfied with the toothpaste you use ?'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Are you satisfied with the toothpaste you use ?')
plt.show()


###################'Have you switched toothpaste brands in the past year? if yes then why?'########################

value_counts = df['Have you switched toothpaste brands in the past year? if yes then why?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Have you switched toothpaste brands in the past year? if yes then why?')
plt.xlabel('')
plt.ylabel('Count')
plt.show()



###################''For how long you brush your teeth ?''########################

value_counts = df['For how long you brush your teeth ?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'For how long you brush your teeth ?')
plt.xlabel('')
plt.ylabel('Count')
plt.show()


###################'Which type of brush are you using ?'########################

value_counts = df['Which type of brush are you using ?'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Brush Using')
plt.show()

###################'How often do you brush your teeth in a typical day ?'########################

value_counts = df['How often do you brush your teeth in a typical day ?'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Pie Chart of Brushing Teeth in a day')
plt.show()

###################'Do you use any additional oral care product such as mouthwash or dental floss ?'########################

value_counts = df['Do you use any additional oral care product such as mouthwash or dental floss ?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Oral Prodct')
plt.xlabel('')
plt.ylabel('Count')
plt.show()

###################'Do you follow any specific brushing techniques recommended by your dentist ?'########################

value_counts = df['Do you follow any specific brushing techniques recommended by your dentist ?'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Do you follow any specific brushing techniques recommended by your dentist ?')
plt.show()

###################'Do you drink hot or cold beverages regularly ?'########################

value_counts = df['Do you drink hot or cold beverages regularly ?'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Do you drink hot or cold beverages regularly ?')
plt.show()

###################'Do you consume Tea or Coffee regularly ? '########################

value_counts = df['Do you consume Tea or Coffee regularly ? '].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Do you consume Tea or Coffee regularly ?')
plt.show()

###################'Have you experienced any dental issues even after doing regular brushing ? '########################


value_counts = df['Have you experienced any dental issues even after doing regular brushing ? '].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Have you experienced any dental issues even after doing regular brushing ? ')
plt.xlabel('')
plt.ylabel('Count')
plt.show()
###################'Have you faced any issue after using a certain toothpaste? if yes then name the toothpaste '########################


value_counts = df['Have you faced any issue after using a certain toothpaste? if yes then name the toothpaste '].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Issue after using certain toothpaste')
plt.xlabel(' ')
plt.ylabel('Count')
plt.show()

###################'How much sugar do you consume daily ?'########################


value_counts = df['How much sugar do you consume daily ?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'How much sugar do you consume daily ?')
plt.xlabel('')
plt.ylabel('Count')
plt.show()

###################'Have you ever diagnose with any problem related to teeth ?'########################

value_counts = df['Have you ever diagnose with any problem related to teeth ?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Have you ever diagnose with any problem related to teeth ?')
plt.xlabel(' ')
plt.ylabel('Count')
plt.show()

###################'Do you consume any of these Tobacco, alcohol and smoking ?'########################

value_counts = df['Do you consume any of these Tobacco, alcohol and smoking ?'].value_counts()
plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Do you consume any of these Tobacco, alcohol and smoking ?')
plt.xlabel(' ')
plt.ylabel('Count')
plt.show()


##df = df.dtypes
##print(df )







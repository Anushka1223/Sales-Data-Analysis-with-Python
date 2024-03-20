# -*- coding: utf-8 -*-
"""Sales Data Analysis with Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dt7H3viJjaiJQBdE2SqhTlUwVGj2n_JK
"""

import matplotlib.pyplot as plt

# Line Graph
x=[1,2,3,4,5]
y=[2,4,6,8,10]

# Creating the Plot
plt.plot(x,y)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Line Graph for y=2x')

# Scatter Plot
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.scatter(x,y)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('scatter plot')
plt.show()

# Pie Chart
categories=['A','B','C','D']
values=[10,40,80,35]
plt.pie(values,labels=categories,autopct='%1.1f%%')
plt.title('Abstract Pie Chart')
plt.show()

# Bar Graph
categories=['A','B','C','D','E']
values=[10,12,5,10,20]
plt.bar(categories,values)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar Graph')
plt.show()

#Histogram
marks=[5,6,7,10,12,22,25,26,27,41]
plt.hist(marks,bins=5)
plt.xlabel('Range of marks')
plt.ylabel('No of students')
plt.title('Histogram of Distribution of Marks')
plt.show()

"""**ANOTHER PYTHON** **LIBRARY** **
**
"""

import requests
from bs4 import BeautifulSoup

# Choosing a website to scrap
url='https://news.yahoo.com/'

# Send a get request to the url
response= requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
headlines=soup.find_all('h3')
for headline in headlines:
  print(headline.text)

"""**Draw Some INSIGHTS out of SALES DATA"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('Sales Data.csv', encoding='unicode_escape')

df.shape

df.info()

df.head()

df.tail()

# cleaning the data
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

#checking for null values

pd.isnull(df).sum()

df.dropna(inplace=True)

df

df[['Age','Orders','Amount']].describe()

df['Marital_Status'].sum()

#Gender Split Analysis of Customers

#Just a variation of the Bar Plot in Seaborn

cp = sns.countplot(x = 'Gender', data=df)

for bars in cp.containers:
  cp.bar_label(bars)

cp2 = sns.countplot(x = 'Age Group', data=df, hue = 'Gender')

for bars in cp2.containers:
  cp2.bar_label(bars)

cp3 = sns.countplot(x = 'Zone', data=df, hue = 'Gender')
for bars in cp3.containers:
  cp3.bar_label(bars)

#Best performing product categories

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize': (20, 5)})

sns.barplot(data= sales_state, x='Product_Category', y='Amount' )

"""**CONCLUSION**

THE TOP 3 AGE GROUPS ARE?
26-35
18-25
36-45

TOP 5 PRODUCT CATEGORIES?    
FOOD, Clothing and apparel, electronics and gadgets, footwear and shoes, furniture

TOP 2 ZONES?
CENTRAL AND SOUTHERN ZONE
"""
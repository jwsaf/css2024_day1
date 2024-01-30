# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:06:27 2024

@author: u92166262
"""


#### WATCH THE ZOOM RECORDING ALSO FOR COMMANDS HE USED


age = 100
height = 100
fruit = "banana
mortality = "cvd"
hosp = "rd"
city = "Cape Town"
import pandas
file = pandas.read_csv("country_data.csv")
file = pandas.read_csv("D:\SHSPH 2024\Coding Summer School\Day 1\data_01\country_data.csv")
head(country_data)
print(country_data)
print(file)
print(file.info())
print(file.describe())

file = pandas.read_csv("D:\SHSPH 2024\Coding Summer School\Day 1\data_01\diab_data.csv")
print(file.info())
print(file.describe())
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('D:\SHSPH 2024\Coding Summer School\Day 1\data_01\diab_data.csv')
df.plot()
df.plot(kind = 'scatter', x = 'BMI' , y = 'insulin')
df["preg_count"].plot(kind = 'hist')
df["age"].plot(kind = 'hist')
df.corr()


file = pandas.read_csv("D:\SHSPH 2024\Coding Summer School\Day 1\data_01\insurance_data.csv")
file = pandas.read_csv("D:\SHSPH 2024\Coding Summer School\Day 1\data_01\insurance_data.csv", skiprows=5)
print(file.info())
print(file.describe())



file.describe(include=['category'])

#no variable names in this dataset
file = pandas.read_csv("D:\SHSPH 2024\Coding Summer School\Day 1\data_01\housing_data.csv")
print(file.info())
column_names = []    #### but must still write names!

file = pandas.read_csv("D:\SHSPH 2024\Coding Summer School\Day 1\data_01\housing_data.csv, names = column_names")
file.means()
file.heatmap('insulin', 'BMI')
print(max("age"))




import pandas as pd
df = pd.read_csv("D:\SHSPH 2024\Coding Summer School\Day 2\data_02\country_data_index.csv")
print(df.info())
print(df.describe())
import matplotlib.pyplot as plt
df.plot(kind = 'scatter', x = 'Age' , y = 'Unnamed')
df["Age"].plot(kind = 'hist')
df["age"].plot(kind = 'hist')
df.corr()



df = pd.read_csv("D:\SHSPH 2024\Coding Summer School\Day 2\data_02\iris.csv")
print(df.info())
print(df.describe())
df.plot(kind = 'scatter', x = 'petal_length' , y = 'sepal_length')
df["petal_length"].plot(kind = 'hist')
axes = df.hist(['petal_length','sepal_length'], by='class')
df.corr()
df.head()
df.sample(20)
df.shape




### day 2 quiz
print("x")


x = [1,2,3]
y = x
y[0] = 4
print(x)


x = "5"
y = 5
print(y + x)




$fi=3
if=2
_public=4
bob's=6
emp_id=7
emp id=8


x=23
y=10
print(z)


val = 2+3*(36/9+1)**2-1
val

"""
-----------------------------

Welcome to my project regarding employee churn data.

-----------------------------
"""

import matplotlib.pyplot as plot
import pandas as pd
import seaborn as sb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics



# Let's import the dataset we will be using!
data = pd.read_csv('HR_Employee_Measurement.csv')

# This will give us a nice overview of the data.
data.head()

# In order to further our understanding of the dataset
# attributes and the datatypes we can use info()
data.info()

# We want to look into the data of the employees who left the 
# company. Thus, we can  group them by  who left he company.
ex_employees = data.groupby('left')
ex_employees.mean()

left_count=data.groupby('left').count()
plot.bar(left_count.index.values, left_count['satisfaction_level'])
plot.xlabel('# of Employees Who Left The Company')
plot.ylabel('Total # Number of Employees')
plot.show()

print(data.left.value_counts())


# This chart measures the relationship between time spent at the company
# and number of employees.
time_spent=data.groupby('time_spend_company').count()
plot.bar(time_spent.index.values, time_spent['satisfaction_level'])
plot.xlabel('Number of Years Spend in Company')
plot.ylabel('Number of Employees')
plot.show()


"""
-----------------------------

Welcome to my project regarding employee churn data.

-----------------------------
"""

import matplotlib.pyplot as plot
import pandas
import seaborn as sb

# Let's import the dataset we will be using!
data = pandas.read_csv('HR_Employee_Measurement.csv')

# In order to further our understanding of the dataset
# attributes and the datatypes we can use info()
data.info()

# We want to look into the data of the employees who left the 
# company. Thus, we can  group them by 
ex_employees = data.groupby('left')
ex_employees.mean()

left_count=data.groupby('left').count()
plot.bar(left_count.index.values, left_count['satisfaction_level'])
plot.xlabel('# of Employees Who Left The Company')
plot.ylabel('Total # Number of Employees')
plot.show()

print(data.left.value_counts())



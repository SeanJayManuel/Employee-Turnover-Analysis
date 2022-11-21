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
from sklearn import preprocessing
from sklearn.cluster import KMeans



# Let's import the dataset we will be using!
data = pd.read_csv('HR_Employee_Measurement.csv')

# This will give us a nice overview of the data.
data.head()

# In order to further our understanding of the dataset
# attributes and the datatypes we can use info()
data.info()

# We want to look into the data of the employees who left the 
# company. Thus, we can  group them by  who left he company.
ex_employees = data.groupby('Left')
ex_employees.mean()

Left=data.groupby('Left').count()
plot.bar(Left.index.values, Left['Satisfaction'])
plot.xlabel('# of Employees Who Left The Company')
plot.ylabel('Total # Number of Employees')
plot.show()

print(data.Left.value_counts())


# This chart measures the relationship between time spent at the company
# and number of employees.
Tenure=data.groupby('Tenure').count()
plot.bar(Tenure.index.values, Tenure['Satisfaction'])
plot.xlabel('Number of Years Spend in Company')
plot.ylabel('Number of Employees')
plot.show()


# We this displays the the realtionship between hours worked and the number of employees.
Monthly_Hours=data.groupby('Monthly_Hours').count()
plot.title("Hours Worker per Month vs. # of Employees ")
plot.bar(Monthly_Hours.index.values, Monthly_Hours['Satisfaction'])
plot.xlabel('Average Monthly Hours Worked')
plot.ylabel('Number of Employees')
plot.show()

graph = sb.pairplot(data, hue='Left')
graph.fig.suptitle("Scatterplot and histogram of pairs of variables color coded by who left the company", 
               fontsize = 14, # defining the size of the title
               y=1.05); # y = definig title y position (height)
plot.show()


### This is the Machine Learning Portion

x = data.iloc[:, 0:4].values
y = data.iloc[:, 4].values


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

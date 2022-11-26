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

# This chart shows us who left the company
Left=data.groupby('Left').count()
plot.title("Employees Who Left vs. Total # of Employees ")
plot.bar(Left.index.values, Left['Satisfaction'])
plot.xlabel('# of Employees Who Left Their Company')
plot.ylabel('Total # Number of Employees')
plot.show()

print(data.Left.value_counts())

# This chart measures the relationship between time spent at the company
# and number of employees.
Tenure=data.groupby('Tenure').count()
plot.title("Years Spent in Company vs. # of Employees")
plot.bar(Tenure.index.values, Tenure['Satisfaction'])
plot.xlabel('Number of Years Spent in Company')
plot.ylabel('Number of Employees')
plot.show()


# This displays the the relationship between hours worked and the number of employees.
Monthly_Hours=data.groupby('Monthly_Hours').count()
plot.title("Hours Worked per Month vs. # of Employees ")
plot.bar(Monthly_Hours.index.values, Monthly_Hours['Satisfaction'])
plot.xlabel('Average Monthly Hours Worked')
plot.ylabel('Number of Employees')
plot.show()

# Cluster graph 
left_emp =  data[['Satisfaction', 'Evaluation']][data.Left == 1]
kmeans = KMeans(n_clusters = 3, random_state = 0).fit(left_emp)
left_emp['label'] = kmeans.labels_

# Creates a scatter plot of three groups of employees
plot.scatter(left_emp['Satisfaction'], left_emp['Evaluation'], c=left_emp['label'],cmap='Accent')
plot.xlabel('Satisfaction Level')
plot.ylabel('Last Evaluation')
plot.title('3 Clusters of Employees Who Left')
plot.show()


# Using Seaborn creates a sub plot
features=['Project_Count','Tenure','Work_Accident','Left', 'Promotion','Departments','Salary']
fig=plot.subplots(figsize=(10,15))
plot.title('Comparing Attributes of Past and Current Employees')
for i, j in enumerate(features):
    plot.subplot(4, 2, i+1)
    plot.subplots_adjust(hspace = 1.0)
    sb.countplot(x=j,data = data, hue='Left')
    plot.xticks(rotation=90)
    plot.title("# Of Employees")

# This creates are histogram to cross examine the categories against eachother
graph = sb.pairplot(data, hue='Left')
graph.fig.suptitle("Scatterplot and Histogram of pairs of variables color coded by who left the company", 
               fontsize = 12, # defining the size of the title
               y=1.05); # y = definig title y position (height)
plot.show()



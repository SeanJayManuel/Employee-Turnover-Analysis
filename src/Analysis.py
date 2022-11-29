"""
-----------------------------

Welcome to my project regarding employee churn data.

-----------------------------
"""

import matplotlib.pyplot as plot
import pandas as pd
import seaborn as sb
import numpy as np
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

print(data.Left.value_counts())

def left_chart(dataset):
# This chart shows us who left the company
    
    left = dataset.groupby('Left').count()
   
    plot.title("Employees Who Left vs. Total # of Employees ")
    plot.bar(left.index.values, left['Satisfaction'])

    plot.xlabel('# of Employees Who Left Their Company')
    plot.ylabel('Total # Number of Employees')

    return plot.show()


def tenure_chart(dataset):
    # This chart measures the relationship between time spent at the company
    # and number of employees.
    
    tenure = dataset.groupby('Tenure').count()
    
    plot.title("Years Spent in Company vs. # of Employees")
    plot.bar(tenure.index.values, tenure['Satisfaction'])

    plot.xlabel('Number of Years Spent in Company')
    plot.ylabel('Number of Employees')
   
    return plot.show()

def hours_chart(dataset):
    # This displays the the relationship between hours worked and the number of employees.
    
    monthly_hours = dataset.groupby('Monthly_Hours').count()
   
    plot.title("Hours Worked per Month vs. # of Employees ")
    plot.bar(monthly_hours.index.values, monthly_hours['Satisfaction'])

    plot.xlabel('Average Monthly Hours Worked')
    plot.ylabel('Number of Employees')
    
    return plot.show()


def cluster_graph(dataset):

     # Cluster graph 
    left_emp =  dataset[['Satisfaction', 'Evaluation']][dataset.Left == 1]
    kmeans = KMeans(n_clusters = 3, random_state = 0).fit(left_emp)
    left_emp['label'] = kmeans.labels_

    # Creates a scatter plot of three groups of employees
    plot.title('3 Clusters of Employees Who Left')
    plot.scatter(left_emp['Satisfaction'], left_emp['Evaluation'], c = left_emp['label'], cmap = 'Accent')

    plot.xlabel('Satisfaction Level')
    plot.ylabel('Last Evaluation')
    
    return plot.show()

def subplot_graphs(dataset):
    """ Takes read csv dataset and subplot
    """
    attributes = ['Project_Count','Tenure','Work_Accident','Left', 'Promotion','Department','Salary']

    plot.title('Comparing Attributes of Past and Current Employees')
    
    for i, j in enumerate(attributes):
        plot.subplot(4, 2, i+1)
        plot.subplots_adjust(hspace = 1.0)
        sb.countplot(x=j, data = dataset, hue='Left')
        plot.xticks(rotation=90)
        plot.title("# Of Employees")
    
    return plot.show()

def histogram(dataset):
    """Takes read csv dataset and
    creates scatterplot and histogram cross examining each attribute to eachother"""

    graph = sb.pairplot(dataset, hue = 'Left')
    graph.fig.suptitle("Scatterplot and Histogram of pairs of variables color coded by who left the company", 
                fontsize = 12, # defining the size of the title
                y = 1.05); # y = definig title y position (height)
    plot.show()



def main():
    left_chart(data)
    subplot_graphs(data)
    print("File Executed")

if __name__ == "__main__":
    main()
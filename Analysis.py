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


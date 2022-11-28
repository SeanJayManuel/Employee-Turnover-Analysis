"""
-----------------------------

Welcome to the K Nearest Neighbor Regressor

------------

"""

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sb


data = pd.read_csv('HR_Employee_Measurement.csv')

# Replace all string values with ints as to pass through training set and regressor
data['Salary'] = data['Salary'].replace('low', 0).replace('medium', 1).replace('high', 2)
data['Department'] = data['Department'].replace('sales', 0).replace('accounting', 1).replace('hr',2).replace('technical',3).replace('support',4).replace('management',5).replace('IT',6).replace('product_mng',7).replace('marketing',8).replace('RandD', 9)


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

y = data['Left']
X = data.drop(['Left'], axis = 1)

correlation_matrix = data.corr()
print(correlation_matrix["Left"])


new_data_point = np.array([
    -0.388375,
    0.006567,
    0.023787,
    0.071287,
    0.144822,
    -0.154622,
    -0.061788,
    -0.043814,
    -0.157898])

distances = np.linalg.norm(X - new_data_point, axis=1)

k = 3
nearest_neighbor_ids = distances.argsort()[:k]
print(nearest_neighbor_ids)
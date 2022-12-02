"""
-----------------------------

Welcome to the K Nearest Neighbor Regressor

------------

"""

import pandas as pd
import matplotlib.pyplot as plot

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import mean_squared_error
import seaborn as sb
import scipy.stats
from math import sqrt


data = pd.read_csv('HR_Employee_Measurement.csv')

# Replace all string values with ints as to pass through training set and regressor
data['Salary'] = data['Salary'].replace('low', 0).replace('medium', 1).replace('high', 2)
data['Department'] = data['Department'].replace('sales', 0).replace('accounting', 1).replace('hr',2).replace('technical',3).replace('support',4).replace('management',5).replace('IT',6).replace('product_mng',7).replace('marketing',8).replace('RandD', 9)

SEED = 12345

y = data['Left']
x = data.drop(['Left'], axis = 1)

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

distances = np.linalg.norm(x - new_data_point, axis=1)

k = 3
nearest_neighbor_ids = distances.argsort()[:k]
print(nearest_neighbor_ids)

print("-------")
nearest_neighbor_left = y[nearest_neighbor_ids]

print(nearest_neighbor_left)
prediction = nearest_neighbor_left.mean()


x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                        test_size = 0.25, # 25% of the dataset is used for testing, 75% for training
                                                        random_state = SEED)

knn_model = KNeighborsRegressor(n_neighbors = 3)
knn_model.fit(x_train, y_train)
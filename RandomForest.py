"""
-----------------------------

Welcome to the random forest classifier.

------------

"""
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split


data = pd.read_csv('HR_Employee_Measurement.csv')

print(data['Left'].unique())

y = datat['Left']
X = data.drop(['Left'], axis=1)


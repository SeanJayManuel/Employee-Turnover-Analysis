"""
-----------------------------

Welcome to the K Nearest Neighbor Regressor

------------

"""

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from sklearn.model_selection import train_test_split


data = pd.read_csv('HR_Employee_Measurement.csv')
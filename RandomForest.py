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
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree


data = pd.read_csv('HR_Employee_Measurement.csv')

print(data['Left'].unique())

y = datat['Left']
x = data.drop(['Left'], axis=1)

SEED = 65

x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.25, 
                                                    random_state=SEED)


randomfc = RandomForestClassifier(n_estimators=3, 
                             max_depth=2,
                             random_state=SEED)


randomfc.fit(x_train, y_train)

y_pred = randomfc.predict(x_test)

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
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, mean_squared_error




data = pd.read_csv('HR_Employee_Measurement.csv')

print(data['Left'].unique())

y = data['Left']
x = data.drop(['Left'], axis=1)


# Random Forest Regresor
SEED = 45
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.25, 
                                                    random_state=SEED)


randomfr = RandomForestRegressor(n_estimators=35, # 35 trees
                             max_depth=4, # levels
                             random_state=SEED)


randomfr.fit(x_train, y_train)
y_pred = randomfr.predict(x_test)

attributes = x.columns
tree1 = randomfr.estimators_[0]

plot.figure(figsize=(15,6))
tree.plot_tree(tree1,
               feature_names=attributes,
               fontsize=8, 
               filled=True, 
               rounded=True);
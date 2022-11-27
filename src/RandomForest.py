"""
-----------------------------

Welcome to the random forest classifier.

------------

"""
from lib2to3.pgen2.pgen import DFAState
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plot

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, mean_squared_error




data = pd.read_csv('HR_Employee_Measurement.csv')

print(data['Left'].unique())


print(data['Departments'].unique())
# Random Forest Regresor
SEED = 45

data['Salary'] = data['Salary'].replace('low', 0).replace('medium', 1).replace('high', 2)
data['Departments'] = data['Departments'].replace('sales', 0).replace('accounting', 1).replace('hr',2).replace('technical',3).replace('support',4).replace('management',5).replace('IT',6).replace('product_mng',7).replace('marketing',8).replace('RandD', 9)

y = data['Left']
x = data.drop(['Left'], axis=1)

print(data)
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

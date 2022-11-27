"""
-----------------------------

Welcome to the random forest classifier.

------------

"""
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plot

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, mean_squared_error



# Import and read our data set
data = pd.read_csv('HR_Employee_Measurement.csv')

print(data['Left'].unique())

# Replace all string values with ints as to pass through training set and regressor
data['Salary'] = data['Salary'].replace('low', 0).replace('medium', 1).replace('high', 2)
data['Department'] = data['Department'].replace('sales', 0).replace('accounting', 1).replace('hr',2).replace('technical',3).replace('support',4).replace('management',5).replace('IT',6).replace('product_mng',7).replace('marketing',8).replace('RandD', 9)

# Sets y to our desired value and drops siad value for x
y = data['Left']
x = data.drop(['Left'], axis=1)

# Random Forest Classifier
SEED1 = 45
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED1)

randomfc = RandomForestClassifier(n_estimators=3, 
                             max_depth=2,
                             random_state=SEED1)


randomfc.fit(x_train, y_train)
y_pred = randomfc.predict(x_test)

attributes = x.columns.values
classes = ['0', '1']

for estimator in randomfc.estimators_:
    print(estimator)
    plot.figure(figsize=(12,6))
    tree.plot_tree(estimator,
                   feature_names=attributes,
                   class_names=classes,
                   fontsize=8, 
                   filled=True, 
                   rounded=True)
    plot.show()

# M
cm = confusion_matrix(y_test, y_pred)
sb.heatmap(cm, annot=True, fmt='d').set_title('Maternal risks confusion matrix (0 = Stayed, 1 = Left)')

print(classification_report(y_test,y_pred))


# Random Forest Regresor
SEED2 = 45

# prints our changes to our data to ensure they were in place
print(data)


# Splits our data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.25, 
                                                    random_state=SEED2)


randomfr = RandomForestRegressor(n_estimators=35, # 35 trees
                             max_depth=4, #  4 levels
                             random_state=SEED2)


randomfr.fit(x_train, y_train)

y_pred = randomfr.predict(x_test)

attributes = x.columns
tree1 = randomfr.estimators_[0]


plot.figure(figsize=(20,6))
tree.plot_tree(tree1,
               feature_names=attributes,
               fontsize=8, 
               filled=True, 
               rounded=True);
plot.show()


# Prints potential error metrics to see how accurate the regressor is.
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, y_pred)))
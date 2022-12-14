"""
-----------------------------

Welcome to the random forest classifier and regressor.

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



# Import and read our data set
data = pd.read_csv('HR_Employee_Measurement.csv')


# Replace all string values with ints as to pass through training set and regressor
data['Salary'] = data['Salary'].replace('low', 0).replace('medium', 1).replace('high', 2)
data['Department'] = data['Department'].replace('sales', 0).replace('accounting', 1).replace('hr',2).replace('technical',3).replace('support',4).replace('management',5).replace('IT',6).replace('product_mng',7).replace('marketing',8).replace('RandD', 9)

# prints our changes to our data to ensure they were in place
print(data)

# Sets y to our desired attribute and drops said value for x
y = data['Left']
x = data.drop(['Left'], axis = 1)

# Set our random seed value to a constant value
SEED1 = 45
SEED2 = 45


# Random Forest Classifier function
def random_forest_classifier(x, y):
    """ Takes x and y values that we determined above and passes them through our classifier.
    Then plots our classifier trees which are evelauted by printing confusion matrix"""


    # Splits data into training and testing
    x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                        test_size = 0.25, # 25% of the dataset is used for testing, 75% for training
                                                        random_state = SEED1)

    # Random forest classifier sets number of trees, and depth
    randomfc = RandomForestClassifier(n_estimators = 30, # 30 trees
                                max_depth = 4, # 4 levels
                                random_state = SEED1)

    # Builds a forest of trees from the training data and predicts based off of test data
    randomfc.fit(x_train, y_train)
    y_pred = randomfc.predict(x_test)

    # 
    attributes = x.columns.values
    classes = ['0', '1']

    # Plots and prints each tree from classifier *COMMENT OUT FOR LARGE # OF TREES/FORESTS*
    for estimator in randomfc.estimators_:
        print(estimator)
        plot.figure(figsize = (20,6))
        tree.plot_tree(estimator,
                    feature_names = attributes,
                    class_names = classes,
                    fontsize = 8, 
                    filled = True, 
                    rounded = True)
        plot.show()

    # Plots matrix depicting accuracy 
    matrix_1 = confusion_matrix(y_test, y_pred)
    sb.heatmap(matrix_1, annot = True, fmt = 'd').set_title('Maternal risks confusion matrix (0 = Stayed, 1 = Left)')

    # Prints classification report with precsion, recall, f1-score, and support
    print(classification_report(y_test, y_pred))


def random_forest_regressor(x, y):
    """ Takes the x and y value and passes through our regression model, then ploting our regression trees. 
    Prints our potential error values"""

    # Splits our data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                        test_size = 0.25, # 25% of the dataset is used for testing, 75% for training
                                                        random_state = SEED2)


    # Random forest regressor sets number of trees, and depth
    randomfr = RandomForestRegressor(n_estimators = 35, # 35 trees
                                max_depth = 4, #  4 levels
                                random_state = SEED2)


    # Builds forest withing training data
    randomfr.fit(x_train, y_train)

    y_pred = randomfr.predict(x_test)

    attributes = x.columns
    tree1 = randomfr.estimators_[0]

    # Plots regressor tree and prints
    plot.figure(figsize=(20, 6))
    tree.plot_tree(tree1,
                feature_names = attributes,
                fontsize = 8, 
                filled = True, 
                rounded = True)
    plot.show()


    # Prints potential error metrics to see how accurate the regressor is.
    print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, y_pred)))


def main():
    random_forest_classifier(x,y)
    random_forest_regressor(x,y)
    print("File Executed")

if __name__ == "__main__":
    main()
    
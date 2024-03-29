# Employee Turnover Analysis

## Table of Contents
- [About](#about)

- [Attributes](#attributes)

- [A Dive Into Data Visualization](#a-dive-into-data-visualization)

- [Random Forest Model](#random-forest-model)

    - [Prepping Our Random Forest Model](#prepping-our-random-forest-model)
    
    - [Random Forest Classifier](#random-forest-classifier)

    - [Random Forest Regressor](#random-forest-regressor)




## About
This project will analyze employee data and metrics in order to predict the companies employee retention. We will look into which trends are most prominent in employees who left the company. To further examine the trends we find, this analysis will conclude with the results we find after building a **random forest regression** model as well as a **K Nearest Neighbor regression** model.

We will see which model is better suited for our dataset and our desired use cases.

We will use this README.md as a report in which we discuss some of the findings we discover by analyzing the data as well how we reached these findings.


## Attributes

To begin our analysis, we need to understand the datasets attributes and what they mean. These are the 10 we can discuss:

* **Satisfaction**: Measures an employees satisfaction within theirr company; ranges from 0-1.
* **Evaluation**: An employees most recent evaluation from their employer; ranges from 0-1.
* **Project_Count**: The number of projects an employee has been assigned.
* **Monthly_Hours**: The average amount of hours spent working by an employee during a month.
* **Tenure**: The number of years spent by an employee in the company.
* **Work_Accident**: Whether an employee has had a work accident or not.
* **Promotion**: Whether an employee has received a promotion within the last 5 years or not.
* **Departments**: Employee's working department/division.
* **Salary**: Salary level of the employee; ranges from low, medium and high.
* **Left**: Whether the employee has left the company or not.

## A Dive Into Data Visualization

Our data serves little use in it's current form, so let's try a creating a few different graphs to help grasp the different relationships in our dataset.

To begin, lets first look into how many employees left the company in comparison to how many stayed. See Figure. 1

![](Graphs/Figure_1.png)<br>
Figure. 1

By running the following code: 

    print(data.Left.value_counts())
<br>
We get the output;

    0    11428
    1     3571

Thus, we can see that out of nearly 15,000 employees, over 3,500 left their job.

Secondly, we can create a graph for the relationship between employee tenure and how many employee's there are. See *Figure. 2* below.

![](Graphs/Figure_2.png)<br>
Figure. 2

Figure. 2 dispalys the seniority of employees. We see that the majority of employees are relatively new, with the bulk of the workforce haveing spent 3 years at the company.

***

Below we can see the average hours worked in comparison to the number of employees. See Figure. 3

![](Graphs/Figure_3.png)<br>
Figure. 3

We can see an acceptional spike around the 150 hour mark per month. This gives us a better insight into the typical employee workload that our dataset would experience.

Finally, we are begining to understand that there seems to be patterns in terms of the type of employees who left. A heavy attribute that we should examine is Satisfaction. We can cross examine this with our Last Evaluation attritbute using a cluster graph. See Figure. 4

![](Graphs/Figure_4.png)<br>
Figure. 4

There seems to be 3 main clusters of employees who left.

1. High Satisfaction and High Evaluation.
2. Low Satisfaction and High Evaluation.
3. Average Satisfaction and Average Evaluation.



## Random Forest Algorithm
### Prepping Our Random Forest Algorithm

Before we can create our random forest classifier we need to understand more about the data so we know the appropriate properties to assign. One of the ideal properties to decide on in a random forest algorithm is the number of trees needed to accurately classify the individual points.

By creating a histogram and scatterplot, we can gain valuable information that will help us make an informed decision. See 
Figure. 5

![](Graphs/Figure_5.png)<br>
Figure. 5

When looking at our plotted graphs, the preferable situation would be a clear seperation between the the curves and data points of our two classes. Looking above we can see that our two different classes are overlapping quite a bit. Since trees internally create lines when establishing the space between points, we can draw to a conclusion that more trees are needed in our forest to better classify our data points. 

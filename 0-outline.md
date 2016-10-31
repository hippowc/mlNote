1 some terminology
expert system: creating a computer system to recognize birds. Then we replaced an ornithologist with an computer

feature: the values we measured for a subject, also called attributes

training set: To train the algorithm we feed it with quality data. And that is it.

target variable: target variable is what we are trying to predict with our algorithm. In classification the target variable takes on a nominal value. In the task of regression its value could be continuous.

test set: have not target varialbe, algorithm will decide which class each example should belong to. Through this progress we can get a sense for how accurate the algorithm is.

knowledge representation: if a program has been tested, and it meets our desired level of accuracy, that the machine has learned is called knowlege representation.

supervised learning: this set of problems is known as supervised because we told the algorithm what to predict. Like classification and regression.

unsupervised learning: there is no label or target value given for the data. Like clusting--that we group similar items together. In this progress, we also want to find out some statistical value that describe the data, and we call it density estimation.

2 key tasks of ML
tasks for supervised learning:
--classification: predict what class an instance should fall into.
--regression: it's the prediction of a numeric value. an eg. is drawing an best-fit line througn soem data points to generalize the data points.

tasks for unsupervised learning:
--clusting: group simailar items together.
--reducing the data from many featrues to a small number so that we can visualize it in two or three dimensions.

some tasks and its corresponding algorithm:
supervised learning:
--k-Nearest Neighbors --Linear --Naive Bayes --Locally weighted linear --Support vector machines --Ridge --Decision trees --lasso
unsupervised learning:
--k-Means --Expectation maximization --DBUSCAN --Parzen window

how to choose the right algorithm:
1 if you are prediction a target value? if true, then supervised leanring. Otherwise, unsupervised leanring.
2 In supervised learning. what is your target value? If discrete value, then look into classification. Or it's a number of values,  like from 0 to 100, look into regression.
3 In unsupervised learning. If tring to fit your data into some discrete group, look into clusting. If you have some numeric estimate of how strong the fit is into each group, then look into density estimation algorithm.
4 know your data. Are the features nominal or continuous? Are there missing values in the features? Are there outliers in the data?

steps in developing a machine learning application
--collect data: from web, rss feed, sensors...
--prepare the input data: make data into useable format. Some algorithm need features in a special format.
--analyze the input data
--eliminate garbage data
--train the algorithm
--test the algorithm
--user it

Note:
1 when the algorithm is fed with the train set, it itself will find out the relationship between the features and the target valus. That's how it works.
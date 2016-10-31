Classifying with k-Nearest Neighbors
1 classifying with distance measurement

About the k-nearest Neighbors(kNN)
pros: High accuracy, insensitive to outliers, no assumption about data
cons: Computationally expensive, requires a lot of memory
work with: Numeric values, nominal values

Through eg of the movie classification, we find some steps for knn:
1 we use how many times of kiss or kicked in a movie as the data-set, and use a numeric value as the classification.
2 Given a movie with kiss times and kicked times, then use knn to classify it correctly
3 we calculate the distance between the given one and each point in the data-set. Pick up the top k point, vote for its label, and we take the majority label

normallizing numeric values
When dealing with values that lie in different ranges, we need to normallize them, or some feature with large range will have more effect.

how to normallize value
Common ranges are 0-1 or -1-1
newValue = (oldValue-min) / (max-min) use this formula we can scale every number from 0 to 1
min and max are the smallest and largest values in the dataset

test the classifier as a whole program
One common task in machine learning is evaluating an algorithm's accuracy. 
Take 90% of the existing data to train the classifier, the remaining 10% to test the classifier.
Error rate is the  number of misclassified pieces of data divided by the total number of data

Notes:
1 array is a dataType comes from numpy package which in python there is no this kind of dataType.
2 matplotlib: used to plotting data, we can setup the pack with pip
--python -m pip install -U pip setuptools
--python -m pip install matplotlib
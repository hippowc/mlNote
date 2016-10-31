Decision Tree
It is most commonly used classification techniques, which just looks like a tree.

It has decision blocks and terminating block. The best thing about decision tree is that human can easily understand the data.
The algorithm we will build can take a set of data, build a decision tree. The decision tree does a great job of distilling data into knowledge. It is often used in expert system.

pros:computationally cheap to use, easy for human to understatnd learned result, missing values ok, can deal with irrelevant features
cons: prone to overfitting
works with: numeric values, nominal values

How to build a decision tree
1 first decide which feature is used to split the data into subsets
2 the subsets traverse down the branches of the first decision node
3 if the data on the branches is the same class, that means you've properly classified it and don't need to continue, if not, you need to repeat splitting process on this subset
by the way: how to dictate which feature is used to split the data? you need to try every feature and measure which split give you the best result

split on one and only one feature at a time, and then, 
How to decide which feature we use to split the data?

some terminology.
information theory: It is a branch fo science that's concerned with quantifying information. or we say, how to measure the information
information gain: The change in information before and after the split.
entropy: the expected value of the information

Then, how to decide which feature is used to split the data?
We calculate information gain to see which split gives you the highest information gain.

How to calculate the information gain? the measure of information of a set is known as the Shannon entropy,  or just entropy for short. And I have collect some information on wh
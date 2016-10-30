assuming we have already know how to calculate the entropy of the dataset
then we will split the dataset in a way that will give us the largest information gain or entropy

how to find the largest entropy? we measure every feature and compare them. By the way, another measure of disorder is the Gini impurity

之前理解有点问题关于根据哪个feature来split这个dataset，实际操作是这样：
假定数据集是多个list的列表形式，每个list的长度相同，最后一列为类目的label
先计算baseEntropy,即这个根据label计算这个数据集的entropy
然后遍历feature，从第一个feature开始，根据每个value，split这个dataset，求subSet的entropy，然后乘以这个value的概率，称为newEntropy，然后求所有newEntropy的和，得出这样分割的总的newEntropy,然后计算每个feature的newEntropy，取最大的那个

决策树的目的是为了将数据集分类：通过分类，是数据更好的组织，直观看上去，比较平均

决策树递归算法：
寻找最大information gain的feature，分为多个subSet，然后对其他的subSet继续执行该方法，直到：这个子集的类目都相同，或者已经没有feature可以再进行split。

我们获得决策树是为了使用决策树进行分类，获得决策树之后可以将这个数据结构保存下来，以便后续使用该树进行分类。

本章使用的分割数据生成决策树的算法叫做ID3，它只能对离散的值进行分类，在分类时使用了递归的方式，最后决策树保存在了dict数据结构中，并没有使用其他更复杂的数据结构

另外还有其他生成决策树的算法：C4.5或者CART

Note:
1 why we have to split a dataset in a way that bring us a largest information gain? what's the benifit?
2 经过决策树分类后，会得到一个怎样的树？这个树有什么好处？

Classifying with probability theory:Naive Bayes--朴素贝叶斯，之所以成为朴素，是因为这个公式做了一些单纯的猜想。
In first two chapters, we use classifiers to make hard decisions, ie. asked for a definite answer.
Probability theory, 概率论组成了很多机器算法的基础。

Classifying with Bayesian decision theory:
好处：需要少量的数据，处理多种类型
坏处：对输入数据敏感
数据：nominal values

Naive Bayes is a subset of Bayesian decision theory. 先看下贝叶斯决策理论
假设数据有两个feature，对于某个feature (x,y)，它属于class1的概率用方程式p1(x,y)表示，它属于class2的概率用方程式p2(x,y)表示。如果对一个新的测量值(x,y)分类，使用如下规则：
if p1(x,y) > p2(x,y), then the class is 1
if p1(x,y) < p2(x,y), then the class is 2
we choose the class with high probability.简而言之，贝叶斯决策理论：choosing the decision with the highest probability.
For now, we already know two types of classifier: knn, decision tree，但是反正各种问题，要不怎么引入下面这个算法呢。。

conditional probability:
P(gray|bucket B) = P(gray and bucket B) / P(bucketB)。关于条件概率的解释在另外一个文档中写明

实际比较的概率是p(c1 | x,y), p(c2 | x,y) 意思是，给了一个指定的点(x,y)，来自c1的概率和来自c2的概率。

那么来看个应用：机器学习一个重要的应用是，文档自动分类。
实例：一篇文档，譬如一份邮件。
features：是文档的各种内容。然后我们通过查看每一个words是否存在，来对其分类。
估计英语的单词数量要超过500000，假定我们的词汇量是1000，为了能生成好的概率分布，我们需要足够的数据样本。统计表明，如果一个feature需要n个sample，那么10个feature需要n的10次方个。那么我们假定有1000个words，则需要n的1000次方个samples。不过我们可以假定每个word都是独立的，这样可以将samples减少到1000*n个(i dont know why)。
朴素贝叶斯算法之所以称为朴素在于：
1、假设每个word都是独立的，即每个单词和另外单词一块出现的概率相同。
2、每个word的重要性是一样的。

接下来用python实现一个Bayes classifier，应用场景如下：
已给出一组words，譬如：good,like,yes，这种关键字之类的，给出一篇Document，判断这个Document是属于什么类别？
我们把这组words记做 w，类别记做ci（有i中类别）实际上是在求：
p(ci | w)即出现了w这些数组，各种类别的概率是多大？概率最大的类别就认为是该Document的类别。
根据贝叶斯公式就是求：(p(w|ci)p(ci) / p(w))，即分别要求ci类中出现w的概率，ci类出现的概率，所有Document出现w的概率，都是可求的。由于朴素贝叶斯的假定，每个单词都是独立的可能，那么p(w) = p(w0)p(w1)...
p(w|ci)的求法：
先列出所有文章的单词，去重后放入一个list
然后构造一个所有文章的矩阵：以所有的单词为一行，每一行为一篇文章，行中的元素表示这篇文章中是否存在这个单词（并不是出现单词的个数，而是是否出现这个单词，只有0 1 两种数值）。
然后计算每一种类别的文章中每个单词出现的概率，计算方式为：该单词的总数 / 总的单词数，就可以得到每个单词的条件概率：p(wj | ci)，但实际计算后发现有很多单词的概率为0，但是我们需要计算总概率就要将所有的概率相乘，如果以任何一项为零那么总概率就为零，这显然是一个缺陷，于是我们把出现次数初始值设置为1，分母初始值设置为2。
另外还有一个问题是每个概率值比较小，都乘在一块会变得更小，python计算时会四舍五入使结果趋近0.于是可以将结果取自然对数。取自然对数后函数的最大值不会有变化。所以取最大值时可考虑取自然对数来代替。
这个概率是训练样本的概率，后面要根据这个概率为文章分类。
接下来给出一个Document，将它转化成一个list，list表示每个单词的存在情况。用这个list和之前计算的p(w|ci)相乘，在加上p(ci)的对数，比较那个类的情况大就算作哪一类，实际上就是求的p(ci|w)的概率，其中p(w|ci)就是之前由矩阵求出来的概率

刚才那个模型叫做 set-of-words model ，我们将这个单词是否在一个文档中作为一个feature。但实际一个单词出现的数量也能传达某些信息，但是之前我们没有使用。接下来用一个模型叫 bag-of-words，它会记录一个单词出现的次数。
例子：在代码中增加一个方法 bagOfWords2VecMN(),它与setOfwords方法的不同是，会增加单词的数量

贝叶斯方法的经典应用--垃圾邮件过滤 email spam filter
思路：
1 通过训练数据，构造垃圾邮件单词数组-token vector
2 通过训练数据，求出垃圾邮件中的单词概率
3 提供一个已知分类的测试数据，测试分类器看错误率--分类出错的文章数 / 总文章数， 错误率可以多测几次取平均值
思路和方法与之前一模一样，不在重复了。

如何解释从贝叶斯分类器学到的知识
上面举了两个应用例子，过滤恶意留言和过滤垃圾邮件，还有很多其他应用。最后一个栗子：是否不同的城市人使用不同的words？
我们统计每个city的words probability，最后不使用这个概率去做什么，只是看是否能从这个probability数值中得到些什么。
#由于现在进度比较慢，一些扩展的我就跳过了，先把主干的知识学一下#

使用概率分类会比轻盈的规则更有效，通过移除 stop words(禁用词，非常常见的单词或短语)可以优化分类器。


Note:
1 Bayesian probability can be applied to prior knowledge, frequency probability only draws conclusions from data adn doesnot allow for logic and prior knowledge.

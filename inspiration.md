1 knn算法的运用
原理：k-nearest neighbor是一种分类算法，它解决这样的问题：根据一堆已知类目的数据--training data，找出给定数据的类目。
做法：假定training data中的每个数据以及给定的数据都是由数字组成，可将每个数据看做一个元组，由多个feature数据组成的元组，求出给定数据到每个training data的欧几里得距离，根据距离最近选取前k个data，观察其对应类目，选择类目数据最多的作为给定数据的类目。
eg 1. improving dating matching
training data包含三个numeric featrue. class label是喜欢程度，由此计算距离并得出
eg 2. handwriting recognition
training data是32*32的像素矩阵，class label是对应数值。首先将32*32数据处理为1*1024的vector，之后可根据之前方法继续。

优缺点：
knn是一个基于实例的算法，在分类时很有效，但是要有data-set，要有存储空间，要计算和每一个数据的距离。另外knn会让你看不懂底层的数据结构，不知道distance到底是什么样
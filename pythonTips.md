1 python 列表解析，基本形式：[fun(x) for x in liter(x)] 
通过对可迭代对象liter(x)的迭代，返回一个fun(x)的列表

2 set(),set操作，去掉列表中的重复对象。类似的方法：str(), int(),float()等

3 关于递归的写法：
a 首先写明终止条件，如果符合，则返回
b 调用本方法，进行递归求值

4 list.count(obj),返回该元素在list中出现的次数

5 del 用于删除列表中的某个值，或删除整个变量的引用

6 type(x) 用来查看x的类型，type(x).__name__可以将类型用str表示

7 pickle模块。实现了一个算法，将python对象序列化和反序列化
# coding:utf-8

from math import log
import operator

def calShannonEnt(dataSet):
	numeEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numeEntries
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt

def createDataSet():
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing', 'flippers']
	return dataSet, labels

# dataSet is the given dataSet to be split
# axis is the index of the feature to be split on
# value is the feature's value
# return: the left dataset split by feature == value
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis + 1 :])
			retDataSet.append(reducedFeatVec)
	return retDataSet

# 默认dataSet的格式为：前几列为feature，最后一列为label或者叫类目
# 根据label计算一个dataSet的entropy，称为baseEntropy
# 每一个feature的entropy是这样计算的：
# 计算该feature中某个值的概率，乘以在该值下获得的subSet的baseEntropy,得到newEntropy，然后该feature下所有值的newEntropy求和
# infoGain = baseEntropy - newEntropy
# 取最大的infoGain的feature
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1 # 减一是因为去掉最后一列label
	baseEntropy = calShannonEnt(dataSet) # 从label的角度计算该dataSet的entropy
	bestInfoGain = 0.0
	bestfeature = -1
	for i in xrange(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEntropy += prob * calShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if infoGain > bestInfoGain:
		 	bestInfoGain = infoGain
		 	bestfeature = i
	return bestfeature

def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classList.keys() :
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverser = True)
	return sortedClassCount[0][0]

# dataSet指的是数据集，这里的label指的是feature的名称，不是类目的label
def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet] # 返回label列表
	# 如果数据集中所有类目都相同，则返回该label
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	# 如果feature都用完了，则返回出现最多的label
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat] # 获取bestFeat的名称
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat]) # 删除当前label，以便后续的遍历操作
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	# 根据bestFeat的值进行遍历，获取每个value下的subSet，并继续创建树并返回
	# 每个feature的每个value都是一个子节点，下面仍有子集的树
	for value in uniqueVals:
		subLables = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat, value), subLables)
	return myTree

# 每一个feature是一个节点，该节点下分支的内容是feature的所有取值
# 某个取值下又是一个feature节点，依次往下
# 本方法生成的决策树的第一个节点是feature的名称(label)，所以要先去的这个feature的index进行比较
def classify(inputTree, featLabels, testVec):
	firstStr = inputTree.keys()[0]
	print firstStr
	secondDic = inputTree[firstStr]
	featIndex = featLabels.index(firstStr)
	for key in secondDic.keys():
		if testVec[featIndex] == key:
			if type(secondDic[key]).__name__ == 'dict':
				classLabel = classify(secondDic[key], featLabels, testVec)
			else:
				classLabel = secondDic[key]
	return classLabel

def storeTree(inputTree, filename):
	import pickle
	fw = open(filename, 'w')
	pickle.dump(inputTree, fw)
	fw.close

def grabTree(filename):
	import pickle
	fr = open(filename)
	return pickle.load(fr)

def main():
	dataSet, labels = createDataSet()
	#shannonEnt = calShannonEnt(dataSet)
	myTree = createTree(dataSet, labels)
	storeTree(myTree, 'classifierStorage.txt')
	pTree = grabTree('classifierStorage.txt')
	print pTree

if __name__ == '__main__':
	main()
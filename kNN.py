# coding:utf-8

from numpy import *
import operator
import parse2Matrix as pm
import autoNorm
import digit2Matrix as dm

def createDateSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

def classify0(inX, dataSet, labels, k):
	# shape: get the dimension of the matrix
	dataSetSize = dataSet.shape[0] 
	# tile: copy inX to a new array, the tuple means (dimensions, times)
	# array minus, corresponding element minus
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	# calculate each element's square
	sqDiffMat = diffMat ** 2
	# calulate each line's sum
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	# return the index array of elements asc
	sortedDisIndicies = distances.argsort()
	classCount = {}
	for i in xrange(k):
		voteIlabel = labels[sortedDisIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def analyseDating():
	group, labels = pm.file2matrix("datingTestSet.txt")
	norMSet, ranges, minVals = autoNorm.autoNorm(group)
	ptGame = float(raw_input("input ptGame?"))
	ffMiles = float(raw_input("input ffMiles?"))
	iceC = float(raw_input("input iceC?"))
	inputA = array([ffMiles,ptGame,iceC])
	result = classify0((inputA - minVals) / ranges,norMSet, labels, 3)
	print result

def analyseDigit():
	group, labels = dm.file2Matrix()
	targetDig = dm.file2Vector(".\\digits\\testDigits\\9_0.txt")
	result = classify0(targetDig,group,labels,1)
	print result

def main():
	analyseDigit()

if __name__ == '__main__':
	main()
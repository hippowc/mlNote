# coding:utf-8

from math import log

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
	dataSet = [[1,1,'maybe'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing', 'filppers']
	return dataSet, labels

def main():
	dataSet, labels = createDataSet()
	shannonEnt = calShannonEnt(dataSet)
	print shannonEnt

if __name__ == '__main__':
	main()
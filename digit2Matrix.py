# coding:utf-8
from numpy import *

def file2Vector(fileName):
	returnVect = zeros((1,1024))
	with open(fileName) as digitF:
		for i in xrange(32):
			lineStr = digitF.readline()
			for j in xrange(32):
				returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect

def file2Matrix():
	returnMa = zeros((10,1024))
	for i in xrange(10):
		fileName = ".\\digits\\trainingDigits\\" + str(i) + "_0.txt"
		returnVect = file2Vector(fileName)
		returnMa[i] = returnVect
	return returnMa,[0,1,2,3,4,5,6,7,8,9]
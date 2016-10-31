# coding:utf-8
from numpy import *

def file2matrix(filename):
	fr = open(filename);
	numberOfLines = len(fr.readlines())
	# assuming that there are 3 kinds of features in the data-set
	returnMat = zeros((numberOfLines, 3))
	classLabelVector = []
	# once read, the file pointer will to the end of the file
	fr = open(filename)
	index = 0
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector

def main():
	print 'main'

if __name__ == '__main__':
	main()
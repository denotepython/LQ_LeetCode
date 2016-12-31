# -*- coding:utf-8 -*-

class Solution(object):
	def rotate(self, matrix):
		length = len(matrix)
		#temp = matrix #问题出在这里，这里temp和matrix指向了同一内存
		temp =  [[0 for col in range(length)] for row in range(length)]
		for i in xrange(length):
			for j in xrange(length):
				temp[j][length-i-1] = matrix[i][j]
		for i in xrange(length):
			for j in xrange(length):
				matrix[i][j] = temp[i][j]
		return matrix
		#也不能用matrix = temp，这样matrix映射到新的id，原来的id值没变

'''
import numpy as np
class Solution(object):
	def rotate(self, matrix):
		matrix = np.matrix(matrix)
		length = len(tmp)
		i, j = 0, length-1
		while i < j:
			tmp[[i,j]] = tmp[[j,i]]
			i += 1
			j -= 1
		return tmp.transpose()
'''

if __name__ == "__main__":
	result = Solution().rotate([[1,2,3],[4,5,6], [7,8,9]])
	print result




# class Solution(object):
# 	def generateMatrix(self, n):
# 		cols, rows = n, n
# 		matrix = [[0 for col in range(cols)] for row in range(rows)]
# 		level = n
# 		k, down, right, up, left = level, level, level, 0, 0
# 		count = 1
# 		while k > 1 and left <= right and up <= down:
# 			for i in xrange(left,right):
# 				matrix[up][i] = count
# 				count += 1
# 			for i in xrange(up+1,down-1):
# 				matrix[i][right-1] = count
# 				count += 1
# 			for i in xrange(left,right):
# 				matrix[down-1][level-i-1] = count
# 				count += 1
# 			for i in xrange(up+1,down-1):
# 				matrix[level-i-1][left] = count
# 				count += 1
# 			up += 1
# 			down -= 1
# 			left += 1
# 			right -= 1
# 			k -= 2
# 		if k == 1:
# 			matrix[level/2][level/2] = count
# 		return matrix

import numpy as np  #可以导入想用的包
#主要是证明了这个方法的可行性
class Solution(object):
	def generateMatrix(self, n):
		temp = np.zeros((n,n), dtype=np.int)
		level = n
		k, down, right, up, left = level, level, level, 0, 0
		count = 1
		while k > 1 and left <= right and up <= down:
			for i in xrange(left,right):
				temp[up][i] = count
				count += 1
			for i in xrange(up+1,down-1):
				temp[i][right-1] = count
				count += 1
			for i in xrange(left,right):
				temp[down-1][level-i-1] = count
				count += 1
			for i in xrange(up+1,down-1):
				temp[level-i-1][left] = count
				count += 1
			up += 1
			down -= 1
			left += 1
			right -= 1
			k -= 2
		if k == 1:
			temp[level/2][level/2] = count
		matrix = temp.tolist() #这样有时候一些二维数组的创建更加方便
		return matrix

if __name__ == "__main__":
	result = Solution().generateMatrix(3)
	print result



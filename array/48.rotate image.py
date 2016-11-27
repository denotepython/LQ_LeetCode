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
		#也不能用matrix = temp，这样matrix映射到新的id，原来的id值没变

if __name__ == "__main__":
	result = Solution().rotate([[1,2],[3,4]])
	print result



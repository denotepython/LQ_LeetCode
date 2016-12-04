class Solution(object):
	def spiralOrder(self, matrix):
		level = len(matrix)
		n, down, right, up, left = level, level, level, 0, 0
		ans = []
		while n > 1 and left <= right and up <= down:
			for i in xrange(left,right):
				ans.append(matrix[up][i])
			for i in xrange(up+1,down-1):
				ans.append(matrix[i][right-1])
			for i in xrange(left,right):
				ans.append(matrix[down-1][level-i-1])
			for i in xrange(up+1,down-1):
				ans.append(matrix[level-i-1][left])
			up += 1
			down -= 1
			left += 1
			right -= 1
			n -= 2
		if n == 1:
			ans.append(matrix[level/2][level/2])
		return ans

if __name__ == "__main__":
	matrix = [
				[ 1, 2, 3 ],
				[ 4, 5, 6 ],
				[ 7, 8, 9 ]
			 ]
	matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	result = Solution().spiralOrder(matrix1)
	print result



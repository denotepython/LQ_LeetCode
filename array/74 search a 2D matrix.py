class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False       
        n = len(matrix[0])
        if n == 0:
            return False
        for i in xrange(0,m):
            for j in xrange(0, n):
                if target == matrix[i][j]:
                    return True
                elif target < matrix[i][j]:
                    return False
                elif i == m-1 and j == n - 1:
                    return False

matrix1 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
        ]
matrix = [[1]]
if __name__ == "__main__":
    result = Solution().searchMatrix(matrix, 2)
    print result
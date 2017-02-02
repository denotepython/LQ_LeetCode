class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        mark = []
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    mark.append([i,j])
        for i in range(len(mark)):
            row, col = mark[i][0], mark[i][1]
            for k in range(0,m):
                matrix[k][col] = 0
            for k in range(0,n):
                matrix[row][k] = 0
        #return matrix
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
matrix = [[1,2,4],[0,4,6],[5,6,8]]
result = Solution().setZeroes(matrix)
print result

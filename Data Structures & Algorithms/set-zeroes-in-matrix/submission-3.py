class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))


        for row, col in zeros:

            for i in range(n):
                matrix[row][i] = 0
            
            for j in range(m):
                matrix[j][col] = 0       
        
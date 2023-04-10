class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        for i in range(m-1):
            ro = 0
            col = i
            val = matrix[ro][col]
            while col < m and ro < n:
                if val != matrix[ro][col]:
                    return False
                col += 1
                ro += 1
        for i in range(n-1):
            ro = i
            col = 0
            val = matrix[ro][col]
            while col < m and ro < n:
                if val != matrix[ro][col]:
                    return False
                col += 1
                ro += 1
        return True
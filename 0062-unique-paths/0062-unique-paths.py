class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                right_val = 0
                down_val = 0
                if j + 1 == n and i + 1 == m:
                    right_val = 1
                if j+1 < n:
                    right_val = matrix[i][j+1]
                if i+1 < m:
                    down_val = matrix[i + 1][j]
                matrix[i][j] = down_val + right_val
        return matrix[0][0]
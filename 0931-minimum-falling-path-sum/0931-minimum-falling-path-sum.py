class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix)
        direction = [(1, 0), (1, 1), (1, -1)]
        dp = {}
        
        def valid_cord(row, col):
            nonlocal n, m
            return 0 <= row < n and 0 <= col < m
        def backT(row, col):
            nonlocal n
            if row == n - 1:
                return matrix[row][col]
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            childSum = float("inf")
            for dirc in direction:
                newRow = row + dirc[0]
                newCol = col + dirc[1]
                if valid_cord(newRow, newCol):
                    childSum = min(backT(newRow, newCol), childSum)
            dp[(row,col)] = matrix[row][col] + childSum
            return dp[(row, col)]
        
        ans = float("inf")
        for i in range(m):
            ans = min(ans, backT(0, i))
        return ans
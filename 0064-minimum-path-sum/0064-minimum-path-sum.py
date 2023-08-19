class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        direction = [(1,0), (0,1)]
        dp = {}
        def valid_cord(row, col):
            nonlocal n, m
            return row < n and col < m
        def backT(row, col):
            nonlocal n, m
            if row == n-1 and col == m-1:
                return grid[row][col]
            if (row, col) in dp:
                return dp[(row, col)]
            pathSum = float("inf")
            for dirc in direction:
                newRow, newCol = dirc[0] + row, dirc[1] + col
                if valid_cord(newRow, newCol):
                    pathSum = min(backT(newRow, newCol), pathSum)
            dp[(row, col)] = grid[row][col] + pathSum
            return dp[(row, col)]
        return backT(0, 0)
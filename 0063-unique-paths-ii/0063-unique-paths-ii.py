class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        direction = [(1,0), (0,1)]
        dp = {}
        
        if grid[0][0]:
            return 0
        
        def valid_cord(row, col):
            nonlocal n, m
            return row < n and col < m
        
        def backT(row, col):
            nonlocal n, m
            if row == n-1 and col == m-1:
                return 1
            if (row, col) in dp:
                return dp[(row, col)]
            pathSum = 0
            for dirc in direction:
                newRow, newCol = dirc[0] + row, dirc[1] + col
                if valid_cord(newRow, newCol) and not grid[newRow][newCol]:
                    pathSum += backT(newRow, newCol)
            dp[(row, col)] =  pathSum
            return dp[(row, col)]
        return backT(0, 0)
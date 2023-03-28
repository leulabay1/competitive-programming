class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            RightCol = 0
            while RightCol + 2 < n:
                res = max(grid[row][RightCol] + grid[row][RightCol + 1]+grid[row][RightCol + 2] + grid[row + 1][RightCol + 1] + grid[row + 2][RightCol] + grid[row + 2][RightCol + 1] + grid[row + 2][RightCol + 2], res)
                RightCol += 1
        return res
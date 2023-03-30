class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[] for _ in range(m-2)]
        row = 0
        while row + 2 < m:
            i = 0
            while i+2 < n:
                ans[row].append(max(max(grid[row][i:i+3]), max(grid[row+1][i:i+3]),max(grid[row+2][i:i+3])))
                i += 1
            row += 1
        return ans
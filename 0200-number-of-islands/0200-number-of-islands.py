class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(m)] for j in range(n)]
        def inbound(row, col):
            return (0 <= row < n and 0 <= col < m)
        def dfs(grid, visited, row, col):
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid[new_row][new_col] == "1" and not visited[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col)
        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and not visited[row][col]:
                    ans += 1
                    dfs(grid, visited, row, col)
        return ans
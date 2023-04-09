class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(m)] for j in range(n)]
        def inbound(row, col):
            return (0 <= row < n and 0 <= col < m)
        def dfs(grid, visited, row, col, no_vis):
            visited[row][col] = True
            no_vis.append(1)
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid[new_row][new_col] and not visited[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col, no_vis)
            return len(no_vis)
        for row in range(n):
            for col in range(m):
                if grid[row][col] and not visited[row][col]:
                    max_area = max(max_area, dfs(grid, visited, row, col, []))
        return max_area
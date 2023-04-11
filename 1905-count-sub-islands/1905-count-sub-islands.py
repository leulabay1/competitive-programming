class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
        max_cou = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(m)] for j in range(n)]
        def inbound(row, col):
            return (0 <= row < n and 0 <= col < m)
        flag = True
        def dfs(grid, visited, row, col):
            nonlocal flag
            visited[row][col] = True
            if not grid1[row][col]:
                flag = False
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid[new_row][new_col] and not visited[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col)
                    
        for row in range(n):
            for col in range(m):
                if grid2[row][col] and not visited[row][col]:
                    dfs(grid2, visited, row, col)
                    if flag:
                        max_cou += 1
                    else:
                        flag = True
        return max_cou
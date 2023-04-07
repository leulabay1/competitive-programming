class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        ans = 0
        
        def dfs(grid, visited, row, col):
         # base case
            nonlocal ans
            visited[row][col] = True
            sqPar = 4
            for dic in directions:
                if inbound(row + dic[0], col + dic[1]) and grid[row + dic[0]][col + dic[1]]:
                    sqPar -= 1
            ans += sqPar
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col)
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    dfs(grid, visited,row,col)
                    return ans
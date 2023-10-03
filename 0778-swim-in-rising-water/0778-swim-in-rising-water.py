class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = [[float("inf")]*m for _ in range(n)]
        
        
        def is_inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        visited = set()
        que = [(grid[0][0], 0, 0)]
        parents = {}
        parents[(0, 0)] = None
        
        while que:
            weight, row, col = heappop(que)
            visited.add((row, col))
            
            if row == n-1 and col == m - 1:
                ans = 0
                node = (row, col)
                while node:
                    ans = max(ans, grid[node[0]][node[1]])
                    node = parents[node]
                return ans
            
            for dirc in directions:
                new_row = row + dirc[0]
                new_col = col + dirc[1]
                if is_inbound(new_row, new_col):
                    new_weigh = grid[new_row][new_col]
                
                if is_inbound(new_row, new_col) and (new_row, new_col) not in visited and dist[new_row][new_col] > new_weigh:
                    
                    parents[(new_row, new_col)] = (row, col)
                    
                    dist[new_row][new_col] = new_weigh
                    heappush(que, (new_weigh, new_row, new_col))
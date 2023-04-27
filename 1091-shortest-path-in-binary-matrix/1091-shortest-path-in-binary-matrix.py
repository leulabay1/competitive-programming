class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bound(row, col):
            if 0 <= row < n and 0 <= col < m:
                return True
            else:
                return False
        n, m = len(grid), len(grid[0])
        direction = [(1,1),(0,1),(1,0),(1,-1),(-1,1),(-1,0),(0,-1),(-1,-1)]
        
        if grid[0][0]:
            return -1
        
        visited = set([(0,0)])
        que = deque([(0,0)])
        parent = {(0,0): None}
        
        while que:
            ro, co = que.popleft()
            
            
            if (ro, co) == (n-1, m-1):
                path = []
                node = (ro, co)
                while node:
                    path.append(node)
                    node = parent[node]
                return len(path)
            
            for row, col in direction:
                newrow = row + ro
                newcol = col + co
                if bound(newrow, newcol) and not grid[newrow][newcol] and (newrow,newcol) not in visited and (newrow,newcol) not in que:
                    visited.add((newrow, newcol))
                    parent[(newrow, newcol)] = (ro, co)
                    que.append((newrow, newcol))
        return -1
            
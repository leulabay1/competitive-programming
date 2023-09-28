class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        dist = -1
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
        if len(q) == n * n:
            return dist

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
                    dr, dc = r + i, c + j
                    if n in (dr, dc) or -1 in (dr, dc) or grid[dr][dc] == 1:
                        continue
                    q.append((dr, dc))
                    grid[dr][dc] = 1
            dist += 1
        return dist
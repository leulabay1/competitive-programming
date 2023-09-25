class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        global n, m
        n = len(dungeon)
        m = len(dungeon[-1])
        
        dp = defaultdict(int)
        def dfs(i, j):
            if i == n - 1 and j == m - 1:
                return max(-dungeon[i][j] + 1, 1)
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            val1 = val2 = float("inf")
            if i + 1 < n:
                val2 = dfs(i + 1, j)
            
            if j + 1 < m:
                val1 = dfs(i, j + 1)
                
            dp[(i, j)] = max(min(val1 - dungeon[i][j], val2 - dungeon[i][j]), 1)
            
            return dp[(i, j)]

        return dfs(0, 0)
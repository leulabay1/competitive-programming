class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            seen[node] = 1
            
            for i in range(n):
                if seen[i] == 0 and isConnected[node][i] == 1:
                    dfs(i)
        res = 0
        n = len(isConnected)
        seen = [0 for _ in range(n)]
        for i in range(n):
            if seen[i] == 0:
                res += 1
                dfs(i)
        return res
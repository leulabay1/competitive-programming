class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for a, b, w, in roads:
            graph[a].append((b,w))
            graph[b].append((a,w))
        
        score = float("inf")
        def dfs(node, visited):
            nonlocal score
            visited.add(node)
            for nei, w in graph[node]:
                score = min(w, score)
                if nei not in visited:
                    
                    dfs(nei, visited)
            return
        dfs(1, set())
        return score
            
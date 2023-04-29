class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        ans = 0
        graph = defaultdict(list)
        visitedTotal = set()
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        def dfs(node, visited, visited0):
            visited0.add(node)
            nonlocal ans
            nonlocal visitedTotal
            if hasApple[node]:
                ans += len(visited - visitedTotal)
                visitedTotal = visited.copy()
            for nei in graph[node]:
                if nei not in visited0:
                    visited.add(nei)
                    dfs(nei, visited, visited0)
                    visited.remove(nei)
        dfs(0, set([0]), set())
        return 2 * (ans - 1) if ans != 0 else ans
                    
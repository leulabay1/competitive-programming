class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        for i, bomb in enumerate(bombs):
            x, y, radius = bomb
            for j, bomb in enumerate(bombs):
                if j == i:
                    continue
                x2, y2, r2 = bomb
                centDif = math.sqrt((x-x2)**2 + (y-y2)**2)
                if centDif <= radius:
                    graph[i].append(j)
        ans = 0
        def dfs(node, visited):
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj, visited)
            return len(visited)
        if len(graph) == 0:
            return 1
        for i in range(len(bombs)):
            if i in graph:
                ans = max(ans, dfs(i, set()))
        return ans
        
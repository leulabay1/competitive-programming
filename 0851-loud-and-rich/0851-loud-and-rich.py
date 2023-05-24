class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {i:[] for i in range(n)}
        depend = [0]*n
        ans = [i for i in range(n)]
        
        for edge in richer:
            graph[edge[0]].append(edge[1])
            depend[edge[1]] += 1
        que = deque()
        for node in graph:
            if depend[node] == 0:
                que.append(node)
                
        while que:
            node = que.popleft()
            
            for nei in graph[node]:
                if quiet[ans[nei]] > quiet[ans[node]]:
                    ans[nei] = ans[node]
                depend[nei] -= 1
                if depend[nei] == 0:
                    que.append(nei)
        return ans
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graphRep = {i:[] for i in range(len(graph))}
        depend = {i : len(graph[i]) for i in range(len(graph))}
        
        for i in range(len(graph)):
            for node in graph[i]:
                graphRep[node].append(i)
        que = deque()    
        for node in graphRep:
            if depend[node] == 0:
                que.append(node)
        ans = list()
        while que:
            node = que.popleft()
            ans.append(node)
            for nei in graphRep[node]:
                depend[nei] -= 1
                if not depend[nei]:
                    que.append(nei)
        return sorted(ans)
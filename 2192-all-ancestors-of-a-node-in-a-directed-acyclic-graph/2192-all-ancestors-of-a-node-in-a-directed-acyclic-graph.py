class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i:[] for i in range(n)}
        depend = [0]*n
        ans = {i: set() for i in range(n)}
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            depend[edge[1]] += 1
        que = deque()
        for node in graph:
            if depend[node] == 0:
                que.append(node)
                
        while que:
            node = que.popleft()
            
            for nei in graph[node]:
                ans[nei].add(node)
                ans[nei] |= ans[node]
                depend[nei] -= 1
                if not depend[nei]:
                    que.append(nei)
        for i in range(len(ans)):
            ans[i] = sorted(list(ans[i]))
        return list(ans.values())
            
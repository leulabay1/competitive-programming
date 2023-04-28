class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[1]].append(edge[0])
            graph[edge[0]].append(edge[1])
        
        ans = [0]*n
        def tracker(node, visited):
            visited.add(node)
            dec2 = Counter(labels[node])
            
            for adj in graph[node]:
                if adj not in visited:
                    dec2 += tracker(adj, visited)
            ans[node] = dec2[labels[node]]
            return dec2
        tracker(0, set())
        return ans
        
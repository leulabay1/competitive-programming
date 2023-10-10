class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        dist = [0]*n
        
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[1], succProb[i]))
            graph[edge[1]].append((edge[0], succProb[i]))
        
        visited = set()
        que = [(-1, start_node)]
        
        while que:
            prob, node = heappop(que)
            visited.add(node)
            
            if node == end_node:
                return -1*prob
            
            for child, child_prob in graph[node]:
                if child not in visited and -1*prob*child_prob > dist[child]:
                    dist[child] = -1*prob*child_prob
                    heappush(que, (prob*child_prob, child))
        return 0
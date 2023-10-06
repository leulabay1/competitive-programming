class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for src, dist, time in times:
            graph[src].append((dist, time))
        
        dist = [float("inf") for _ in range(n)]
        
        visited = set()
        que = [(0, k)]
        
        while que:
            time, node = heappop(que)
            visited.add(node)
            if len(visited) == n:
                return time
                
            for child, child_time in graph[node]:
                
                if child not in visited and dist[child - 1] > time + child_time:
                    dist[child - 1] = time + child_time
                    heappush(que, (time + child_time, child))
        return -1
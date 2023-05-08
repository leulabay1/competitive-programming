class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        degree = defaultdict(int)
        for i in range(numCourses):
            degree[i]=0
        for pre, cor in prerequisites:
            graph[cor].add(pre)
            degree[pre] += 1
        
        que = deque()
        for nod in degree:
            if not degree[nod]:
                que.append(nod)
                
        path = []
        while que:
            node = que.popleft()
            path.append(node)
            for nei in graph[node]:
                if nei not in que:
                    degree[nei] -= 1
                    if not degree[nei]:
                        que.append(nei)
        
        return True if len(path) == numCourses else False
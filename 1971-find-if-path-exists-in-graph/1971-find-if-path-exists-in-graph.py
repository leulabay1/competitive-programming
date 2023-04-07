class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            

        def DFS(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    if DFS(adj, visited):
                        return True
        return DFS(source, set())
#         def DFS(start, end):
#             stack = [start]
#             visited = set()
            
#             while stack:
                
#                 node = stack.pop()
#                 if node == end:
#                     return True
                
#                 if node not in visited:
#                     visited.add(node)
#                     for adj in graph[node]:
#                         if adj not in visited:
#                             stack.append(adj)
#             return False
            
        
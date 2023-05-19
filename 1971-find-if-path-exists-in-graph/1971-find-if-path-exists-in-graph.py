class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(node):
            hold = parent[node]
            while parent[node] != node:
                node = parent[node]
            res = hold
            while res != node:
                temp = res
                parent[res] = node
                res = parent[temp]
            return node
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 == parent2:
                return
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                
                rank[parent2] += rank[parent1]
        for a, b in edges:
            union(a, b)
        return find(source) == find(destination)
        
        
        
#         graph = defaultdict(list)
#         for edge in edges:
#             graph[edge[0]].append(edge[1])
#             graph[edge[1]].append(edge[0])
            

#         def DFS(node, visited):
#             if node == destination:
#                 return True
#             visited.add(node)
#             for adj in graph[node]:
#                 if adj not in visited:
#                     if DFS(adj, visited):
#                         return True
#         return DFS(source, set())
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
            
        
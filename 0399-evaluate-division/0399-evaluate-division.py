class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for i, equation, value in zip(range(len(values)), equations, values):
            graph[equation[0]].append((equation[1], value))
            graph[equation[1]].append((equation[0], 1/value))
            
        ans = []
        
        for query in queries:
            
            if query[0] not in graph or query[1] not in graph:
                ans.append(-1)
                continue
            
            que = []
            visited = set()
            que.append((query[0], 1))
            
            flag = False
            while que:
                
                node, val = que.pop()
                visited.add(node)
                
                if node == query[1]:
                    ans.append(val)
                    flag = True
                    break
                
                for child, child_val in graph[node]:
                    if child not in visited and child:
                        que.append((child, child_val * val))
            if not flag:
                ans.append(-1)
        return ans
                    
                    
                    
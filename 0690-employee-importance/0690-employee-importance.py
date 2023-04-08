"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        empMap = {e.id: e for e in employees}
        def dfs(Id):
            stack = [Id]
            visited = set()
            imp = 0
            while stack:
                node = stack.pop()
                if node not in visited:
                    imp += empMap[node].importance
                    visited.add(node)
                    for adj in empMap[node].subordinates:
                        if adj not in visited:
                            stack.append(adj)
            return imp
        return dfs(id)
            
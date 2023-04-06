class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()
        ans = []
        for i in edges:
            incoming.add(i[1])
        for j in range(n):
            if j not in incoming:
                ans.append(j)
        return ans
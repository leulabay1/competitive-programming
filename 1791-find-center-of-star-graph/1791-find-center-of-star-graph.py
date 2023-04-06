class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in edges[0]:
            if i == edges[1][0]:
                return i
            if i == edges[1][1]:
                return i
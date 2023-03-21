class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(len(matrix[0]))]
        for row in matrix:
            for i in range(len(row)):
                ans[i].append(row[i])
        return ans
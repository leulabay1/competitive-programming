class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        n = len(triangle)
        m = [i for i in range(1, n)]
        def backT(row, col):
            nonlocal n, m
            if row == n-1:
                return triangle[row][col]
            if col >= m[row]:
                return float("inf")
            if (row, col) in dp:
                return dp[(row, col)]
            dp[(row, col)] = triangle[row][col] + min(backT(row+1, col), backT(row+1, col+1))
            return dp[(row, col)]
        return backT(0, 0)
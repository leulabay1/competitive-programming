class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        n = len(s)
        def backT(param):
            nonlocal n
            i, j = param
            if s[i] == "0" or not 0 < int(s[i:j+1]) <= 26 or j >= n:
                return 0
            if j == n - 1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = backT((j + 1, j + 1)) + backT((j + 1, j + 2))
            return dp[(i, j)]
        return backT((0, 0)) + backT((0, 1))
    
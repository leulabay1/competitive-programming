class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def backT(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in dp:
                return dp[n]
            dp[n] = backT(n - 1) + backT(n - 2) + backT(n - 3)
            return dp[n]
        return backT(n)
class Solution:
    def numTrees(self, n: int) -> int:
        def help(n,dp):
            if n == 0 or n == 1: return 1
            if n == 2: return 2
            if dp[n] != 0: return dp[n]
            for i in range(1,n+1):
                dp[n] += help(i-1,dp)*help(n-i,dp)
            return dp[n]
        dp = [0 for i in range(n+1)]
        return help(n,dp)
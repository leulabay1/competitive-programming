class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = {}
        
        for i in range(n+1):
            if i in [0, 1]:
                dp[i] = i
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2 + 1]
                
        return max(dp.values())
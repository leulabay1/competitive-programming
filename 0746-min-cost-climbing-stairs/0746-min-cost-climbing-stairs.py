class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0],cost[1]]
        n = len(cost)
        for i in range(2, n):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        return min(dp[-1], dp[-2])
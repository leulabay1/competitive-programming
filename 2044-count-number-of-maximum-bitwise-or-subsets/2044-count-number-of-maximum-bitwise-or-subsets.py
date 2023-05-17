class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = collections.Counter([0])
        for a in nums:
            items = list(dp.items()).copy()
            for k, v in items:
                dp[k | a] += v
        return dp[max(dp)]
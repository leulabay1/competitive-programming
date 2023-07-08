class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            for val in dp[:]:
                dp[(val+num)%3] = max(dp[(val+num)%3],val + num)
        return dp[0]
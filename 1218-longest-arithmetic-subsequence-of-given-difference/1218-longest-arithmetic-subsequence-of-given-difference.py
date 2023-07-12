class Solution:
    def longestSubsequence(self, nums: List[int], dif: int) -> int:
        dp = {}
        ans = 1
        for num in nums:
            before_num = dp.get(num - dif, 0)
            dp[num] = before_num + 1
            ans = max(dp[num], ans)
        print(dp)
        return ans
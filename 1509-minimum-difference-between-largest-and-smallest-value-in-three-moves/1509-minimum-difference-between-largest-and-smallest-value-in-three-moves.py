class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        n = len(nums)
        ans = float("inf")
        for i in range(4):
            for j in range(4-i):
                ans = min(ans, abs(nums[i] - nums[n-j-1]))
        return ans
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = float("-inf")
        temp = 0
        for i in range(n):
            temp += nums[i]
            _sum = max(_sum, temp)
            if temp < 0:
                temp = 0
        return _sum
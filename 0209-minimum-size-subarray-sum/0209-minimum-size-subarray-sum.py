class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = nums[0]
        i = 0
        j = 0
        res = len(nums)+1
        while j < len(nums) and i < len(nums):
            if curSum < target:
                j+=1
                if j == len(nums):
                    break
                curSum += nums[j]
            else:
                if j-i+1 < res:
                    res = j-i+1
                curSum -= nums[i]
                i+=1
        if res == len(nums)+1:
            return 0
        return res
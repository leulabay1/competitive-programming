class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for i, num in enumerate(nums):
            
            while 0 < num <= n:
                idx = nums[num - 1]
                nums[num - 1] = float("inf")
                num = idx
        
        for i in range(n):
            if nums[i] != float("inf"):
                return i + 1
            
        return n + 1
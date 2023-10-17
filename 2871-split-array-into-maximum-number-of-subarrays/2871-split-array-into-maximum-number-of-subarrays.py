class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        ans = 0
        temp = -1
        for i in range(len(nums)):
            temp &= nums[i]
            
            if not temp:
                ans += 1
                temp = -1
        
        return max(ans, 1)
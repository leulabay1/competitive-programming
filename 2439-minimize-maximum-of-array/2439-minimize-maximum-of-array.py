class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += nums[i]
            ans = max(ans, ceil(prefix_sum/(i+1)))
            
        return ans
    
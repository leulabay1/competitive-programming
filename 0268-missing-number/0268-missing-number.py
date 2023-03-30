class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mising = nums[0]
        notMising = 0
        for i in range(1, len(nums)):
            mising ^= nums[i]
            notMising ^= i
            
        notMising ^= len(nums)
        
        return notMising ^ mising
            
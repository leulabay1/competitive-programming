class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longestOnes = 0
        k = 1
        rp = lp = 0
        while rp < len(nums):
            if nums[rp] == 0:
                k -= 1
            while k < 0:
                if nums[lp]==0:
                    k+= 1
                lp += 1
            
            longestOnes = max(longestOnes, rp-lp)
            rp += 1
        return longestOnes
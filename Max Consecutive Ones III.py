class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        fast = 0
        slow = 0
        res = 0
        while fast <len(nums):
            
            if nums[fast] == 0:
                k -= 1
                
            while k < 0:
                if nums[slow] == 0:
                    k+=1
                slow+=1
            res = max(res, fast-slow+1)
            fast += 1
        return res

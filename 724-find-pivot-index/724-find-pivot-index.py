class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        p = []
        s = 0
        for i in nums:
            p.append(s)
            s+=i
        for i in range(len(nums)):
            if p[i] == s - p[i] - nums[i]:
                return i
        else:
            return -1
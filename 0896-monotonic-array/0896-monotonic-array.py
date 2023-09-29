class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        flag1 = False
        flag2 = False
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                break
        else:
            flag1 = True
                
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                break
        else:
            flag2 = True
            
        return flag1 or flag2
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numsDict = {}
        
        for i in nums:
            numsDict[i] = numsDict.get(i,0)+1
        
        ctr = 0
        for i in range(3):
            if i in numsDict:
                for j in range(numsDict[i]):
                    nums[ctr] = i
                    ctr+=1
        
        return nums
    
            
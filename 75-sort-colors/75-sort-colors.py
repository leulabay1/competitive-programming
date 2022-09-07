class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n >1:
            mid =  n// 2
            leftList = nums[:mid]
            rightList = nums[mid:]
      
            self.sortColors(leftList)
            self.sortColors(rightList)

            
            m = 0
            x = 0
            
            z = 0

            while m < len(leftList) and x < len(rightList):
                if leftList[m] <= rightList[x]:
                    
                    nums[z] = leftList[m]
                     
                    m += 1
                else:
                    nums[z] = rightList[x]
                    x += 1
                z += 1

           
            while m < len(leftList):
                nums[z] = leftList[m]
                m += 1
                z += 1

            while x < len(rightList):
                nums[z]=rightList[x]
                x += 1
                z += 1
class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        
        for i in range(len(l)):
            temp = nums
            nums1 = temp[l[i]: r[i]+1]
            nums1.sort()
            
            Difference = nums1[1]-nums1[0]
            flag = True
            for i in range(len(nums1)-1):
                if nums1[i+1]-nums1[i] != Difference:
                    flag = False
                    break
            result.append(flag)
        return result
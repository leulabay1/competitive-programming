class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for i in nums1:
            j = nums2.index(i)
            for k in range(j,len(nums2)-1):
                if nums2[j]<nums2[k+1]:
                    result.append(nums2[k+1])
                    break
            else:
                result.append(-1)
        return result
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchIndex(nums1, target):
            lo = 0
            high = len(nums1)-1
            while high-lo > 1:
                mid = (high+lo)//2
                if nums1[mid] < target:
                    lo = mid+1
                else:
                    high = mid
            if len(nums1)==0:
                return -1
            if nums1[lo] == target:
                return lo
            elif nums1[high] == target:
                return high
            else:
                return -1
        value = searchIndex(nums, target)
        
        if value != -1:
            start = value
            while start >= 0 and nums[start] == target:
                start-=1
            end = value
            while end < len(nums) and nums[end] == target:
                end+=1
            return [start+1, end-1]
        else:
            return [-1,-1]

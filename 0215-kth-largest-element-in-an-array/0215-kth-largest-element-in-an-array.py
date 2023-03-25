class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            i = left - 1
            pivot = nums[right]
            for j in range(left, right):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            
            nums[right], nums[i + 1] = nums[i + 1], nums[right]
            return i + 1

        def quick(left, right):
            pivot = partition(left, right)
            if pivot == len(nums) - k:
                return nums[pivot]
            elif pivot > len(nums) - k:
                return quick(left, pivot - 1)
            else:
                return quick(pivot + 1, right)
        return quick(0, len(nums)-1)
        
            
            
                    
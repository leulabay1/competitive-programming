class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0 
        b = 0
        while b < len(nums):
            if nums[a] == 0 and nums[b] == 0:
                b += 1
            elif nums[a] == 0 and nums[b] != 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1
            else:
                a += 1
                b += 1
        return nums
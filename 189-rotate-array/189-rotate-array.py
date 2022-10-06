class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) 
        a = 0
        b = len(nums)-1
        while a <= b:
            nums[a],nums[b] = nums[b],nums[a]
            a += 1
            b -= 1
        
        a = 0
        b = k-1
        while a <= b:
            nums[a],nums[b] = nums[b],nums[a]
            a += 1
            b -= 1
        a = k
        b = len(nums)-1
        while a <= b:
            nums[a],nums[b] = nums[b],nums[a]
            a += 1
            b -= 1
        
        return nums
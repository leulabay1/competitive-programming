class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i+1]:
                del nums[i+1]
                continue
            i += 1
        return len(nums)
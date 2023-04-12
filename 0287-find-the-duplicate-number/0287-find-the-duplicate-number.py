class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] != i + 1:
                num1 = nums[i]
                if nums[num1-1] == num1:
                    return num1
                nums[i] = nums[num1-1]
                nums[num1-1] = num1
                continue
            i+=1
        return nums[i]
        
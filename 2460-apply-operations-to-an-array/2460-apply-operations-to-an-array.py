class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = []
        ans = []
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                zeros.append(0)
                i += 1
                continue
            if nums[i] == nums[i+1]:
                ans.append(nums[i]*2)
                zeros.append(0)
                i += 2
            else:
                ans.append(nums[i])
                i += 1
        if len(ans) + len(zeros) == len(nums):
            return ans + zeros
        else:
            if nums[len(nums)-1] == 0:
                zeros.append(0)
            else:
                ans.append(nums[len(nums)-1])
            return ans + zeros
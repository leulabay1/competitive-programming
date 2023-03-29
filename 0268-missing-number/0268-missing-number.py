class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tempDic = set(nums)
        minVal = min(nums)
        maxVal = max(nums)
        if minVal != 0:
            return 0
        for i in range(minVal, maxVal+1):
            if i not in tempDic:
                return i
        else:
            return maxVal + 1
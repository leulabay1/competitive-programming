class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result = []
        ctr = 0
        for i in nums:
            if i == target:
                result.append(ctr)
            ctr += 1
        return result
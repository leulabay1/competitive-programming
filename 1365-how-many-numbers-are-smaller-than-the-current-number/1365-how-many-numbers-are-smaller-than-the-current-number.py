class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            ctr = 0
            for j in nums:
                if i > j:
                    ctr += 1
            result.append(ctr)
        return result
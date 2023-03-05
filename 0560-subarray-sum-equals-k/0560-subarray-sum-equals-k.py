class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0:1}
        curSum = 0
        res = 0
        for i in nums:
            curSum += i
            diff = curSum - k
            
            res += prefixsum.get(diff,0)
            prefixsum[curSum] = 1 + prefixsum.get(curSum,0)
            
        return res
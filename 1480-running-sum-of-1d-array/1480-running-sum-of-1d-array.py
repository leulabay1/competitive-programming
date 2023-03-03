class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        ans = []
        
        for i in nums:
            s += i
            ans.append(s)
        
        return ans
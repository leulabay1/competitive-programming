class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)
        ans = 0
        def backT(i, sum_):
            if i == n:
                return 1 if sum_ == target else 0
            if (i, sum_) in dp:
                return dp[(i, sum_)]
            
            
            dp[(i, sum_)] = backT(i + 1, sum_ + nums[i]) + backT(i + 1, sum_ - nums[i])
            return dp[(i, sum_)]
        return backT(0, 0)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        def backT(i, sum_):
            nonlocal n
            if sum_ > target:
                return 0
            if sum_ == target:
                return 1
            if sum_ in dp:
                return dp[sum_]
            for j in range(0, n):
                dp[sum_] += backT(j, sum_+ nums[j])
            return dp[sum_]
        return backT(0, 0)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                dif = nums[i] - nums[j]
                j_cnt = dp[j].get(dif, 0)
                i_cnt = dp[i].get(dif, 0)
                dp[i][dif] = i_cnt + j_cnt + 1
                ans += j_cnt
                    
        return ans
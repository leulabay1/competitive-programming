class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i,k,holding):
            if i >= n or k == 0:
                return 0

            max_val = dfs(i+1,k,holding)

            if holding:
                max_val = max(max_val,prices[i] + dfs(i+1,k-1,not holding))
            else:
                max_val = max(max_val,-prices[i] + dfs(i+1,k,not holding))

            return max_val

        return dfs(0,2,False)
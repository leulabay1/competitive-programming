class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(rem, leng):
            if rem < 0:
                return math.inf
            if rem == 0:
                return 0
            if rem in dp:
                return dp[rem]
            dp[rem] = math.inf
            for coin in coins:
                dp[rem] = min(dp[rem], dfs(rem - coin, leng + 1) + 1)
            return dp[rem]
        val = dfs(amount, 0)
        print(dp)
        return -1 if val == math.inf else val
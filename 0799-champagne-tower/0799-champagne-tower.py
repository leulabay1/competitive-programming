class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*i for i in range(1, 101)]
        dp[0][0] = poured
        
        for row in range(query_row):
            for col in range(row + 1):
                fill = (dp[row][col] - 1)/2
                if fill > 0:
                    dp[row + 1][col] += fill
                    dp[row + 1][col + 1] += fill
        return min(1, dp[query_row][query_glass])
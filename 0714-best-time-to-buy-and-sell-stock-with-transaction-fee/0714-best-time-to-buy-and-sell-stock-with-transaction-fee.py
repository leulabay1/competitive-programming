class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float('-inf')
        sell = 0  

        for price in prices:
            prev_buy = buy
            buy = max(buy, sell - price)
            sell = max(sell, prev_buy + price - fee)

        return sell
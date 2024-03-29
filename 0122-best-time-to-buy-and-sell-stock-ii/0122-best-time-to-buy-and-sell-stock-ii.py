class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right in range(len(prices)):
            if prices[right] > prices[left]:
                profit += prices[right] - prices[left]
            left = right
        return profit
                
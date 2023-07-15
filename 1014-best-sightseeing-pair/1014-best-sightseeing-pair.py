class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        maxScoreIndex = 0
        ans = 0
        for i in range(1, n):
            
            ans = max(ans, values[i] + values[maxScoreIndex] + maxScoreIndex - i)
            if values[i] - (n - i) > values[maxScoreIndex] - (n - maxScoreIndex):
                maxScoreIndex = i
        return ans
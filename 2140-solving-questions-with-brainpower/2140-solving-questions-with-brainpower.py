class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def backT(idx):
            if idx in dp:
                return dp[idx]
            if idx >= len(questions):
                return 0
            dp[idx] = max(backT(idx + 1), backT(idx + questions[idx][1] + 1) + questions[idx][0])
            return dp[idx]
        return backT(0)
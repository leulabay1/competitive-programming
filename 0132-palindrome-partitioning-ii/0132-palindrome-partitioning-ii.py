class Solution:
    def minCut(self, s: str) -> int:
        is_palindrom = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            c = 0
            while i - c > -1 and i + c < len(s) and s[i - c] == s[i + c]:
                is_palindrom[i - c][i + c] = True
                c += 1
        
        for i in range(1, len(s)):
            c = 0
            while i - c - 1 > -1 and i + c < len(s) and s[i - c - 1] == s[i + c]:
                is_palindrom[i - c - 1][i + c] = True
                c += 1
        dp = [inf for _ in range(len(s) + 1)]
        dp[0] = -1
        for i in range(1, len(s) + 1):
            for j in range(i):
                if is_palindrom[j][i - 1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
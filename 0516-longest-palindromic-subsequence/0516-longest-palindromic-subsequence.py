class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = defaultdict(int)
        
        def solver(i, j):
            if dp[(i,j)]:
                return dp[(i, j)]
            if i > j:
                return 0
            if i == j and s[i] == s[j]:
                return 1
            if s[i] == s[j]:
                val = 2 + solver(i + 1, j - 1)
            else:
                val = max(solver(i + 1, j), solver(i, j - 1))
            
            dp[(i, j)] = max(val, dp[(i, j)])
            
            return dp[(i, j)]
        
        return solver(0, len(s) - 1)
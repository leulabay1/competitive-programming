class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def p(sub):
            for i in range(len(sub)//2):
                if sub[i] != sub[len(sub) - i - 1]:
                    return False
            return True
        n = len(s)
        dp = [[] for i in range(n + 1)]
        dp[0] = [[""]]
        
        for i in range(1, n + 1):
            for j in range(i):
                if p(s[j:i]):
                    if j == 0:
                        dp[i].append([s[j:i]])
                    elif dp[j]:
                        for value in dp[j]:
                            dp[i].append(value + [s[j:i]])
            
        
        return dp[-1]
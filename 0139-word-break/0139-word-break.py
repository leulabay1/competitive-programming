class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        
        @cache
        def dp(i):
            if i == len(s):
                return True
            for j in range(i, len(s)):
                if s[i : j + 1] in wordDict and dp(j + 1):
                    return True
            return False
        
        return dp(0)
        
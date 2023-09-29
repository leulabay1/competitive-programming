class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        
        def dp(i, arr):
            nonlocal ans
            if i >= len(s):
                ans.append(" ".join(arr))
                return
            
            for j in range(i, len(s)):
                if s[i : j + 1] in wordDict:
                    arr.append(s[i: j + 1])
                    dp(j + 1, arr)
                    arr.pop()
                    
        dp(0, [])
        return ans
                    
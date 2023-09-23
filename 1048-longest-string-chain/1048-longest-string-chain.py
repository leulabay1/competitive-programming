class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def compare(word1, word2):
            if len(word1) != len(word2) + 1:
                return False
            for i in range(len(word1)):
                if word1[:i] + word1[i + 1:] == word2:
                    return True
            return False
        
        words.sort(key = lambda word: len(word))
        dp = [1]*len(words)
        
        for i in range(len(words)):
            for j in range(i):
                if compare(words[i], words[j]):
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
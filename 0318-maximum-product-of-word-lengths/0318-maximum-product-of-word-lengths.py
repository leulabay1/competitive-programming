class Solution:
    def maxProduct(self, words: List[str]) -> int:
        look_up = {}
        for word in words:
            btw = 0
            for char in word:
                btw |= 1<<ord(char)%97
            look_up[word] = btw
        
        def validator(word0, word1):
            return not look_up[word0] & look_up[word1]
        
        ans = 0
        for word0 in words:
            for word1 in words:
                if validator(word0, word1):
                    ans = max(ans, len(word1)*len(word0))
                    
        return ans
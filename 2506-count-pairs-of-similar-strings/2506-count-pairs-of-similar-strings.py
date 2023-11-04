class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [set(word) for word in words]
        
        ans = 0
        for i in range(len(words)):
            for j in range(i):
                if words[i] == words[j]:
                    ans += 1
                    
        return ans
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        
        ans = 0
        for word in words:
            if len(set(word).intersection(allowed)) == len(set(word)):
                ans += 1
        
        return ans
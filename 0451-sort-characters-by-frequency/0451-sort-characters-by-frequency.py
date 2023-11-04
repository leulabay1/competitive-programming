class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = dict(sorted(Counter(s).items(), key = lambda x: x[-1], reverse = True))
        
        ans = ""
        for ele in freq.keys():
            ans += ele*freq[ele]
        
        return ans
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def getMinFreqCount(string):
            return string.count(min(string))
        
        def binary_search(query):
            minFreqCount = getMinFreqCount(query)
            l, r = 0, len(words_min_freq_counts)
            while l < r:
                m = l+(r-l)//2
                if words_min_freq_counts[m] <= minFreqCount:
                    r = m
                else:
                    l = m+1
            return l
        
        words_min_freq_counts = sorted([getMinFreqCount(word) for word in words], reverse=True)
                
        return [binary_search(query) for query in queries]
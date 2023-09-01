class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freqWord1 = dict(Counter(word1))
        freqWord2 = dict(Counter(word2))
        
        if freqWord1.keys() != freqWord2.keys():
            return False
        
        count1 = Counter(freqWord1.values())
        count2 = Counter(freqWord2.values())
        
        for key in count1.keys():
            if count1[key] != count2[key]:
                return False
        else:
            return True
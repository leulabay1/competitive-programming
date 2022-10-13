class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_no = 0 
        for i in range(k):
            if s[i] in vowels:
                max_no += 1
                
        i = 0
        j = k-1
        temp = max_no
        while j < len(s)-1:
            if s[i] in vowels:
                temp-=1
            if s[j+1] in vowels:
                temp+=1
            max_no = max(max_no,temp)
            i+=1
            j+=1
        return max_no
            
                
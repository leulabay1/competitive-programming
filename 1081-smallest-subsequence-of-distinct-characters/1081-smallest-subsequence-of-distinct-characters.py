class Solution:
    def smallestSubsequence(self, text: str) -> str:
        s = []
        for i,t in enumerate(text):
            if t not in s:
                while s and ord(t) <= ord(s[-1]) and s[-1] in text[i+1:]:
                    s.pop()
                s.append(t)
        
        return ''.join(s)
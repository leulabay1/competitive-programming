class Solution:
    def isPalindrome(self, S: str) -> bool:
        s = ""
        for i in S:
            if i.isalpha() or i.isdigit():
                s += i.lower()
        
        print(s)
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        else:
            return True
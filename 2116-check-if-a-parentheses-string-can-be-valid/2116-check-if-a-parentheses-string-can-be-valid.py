class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open=0
        closed=0
        if len(s)%2==1:
            return False
        for i in range(len(s)):
            if locked[i]=='1':
                if s[i]==")":
                    closed+=1
                    if closed>(i+1)/2:
                        return False
            #j=len(s)-1-i
            if locked[len(s)-1-i]=='1':
                if s[len(s)-1-i]=="(":
                    open+=1
                    if open>(i+1)/2:
                        return False
                        
        return True
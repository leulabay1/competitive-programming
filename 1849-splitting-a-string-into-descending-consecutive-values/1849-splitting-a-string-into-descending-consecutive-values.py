class Solution:
    def splitString(self, s: str) -> bool:
        
        def backTracker0(num, i):
                
            for j in range(i, len(s)):
                temp = int(s[i:j+1])
                if (num - temp) == 1:
                    if temp == 0:
                        if j+1 == len(s):
                            return True
                        else:
                            continue
                    if j+1 == len(s):
                        return True
                    return backTracker0(int(s[i:j+1]), j+1)
            else:
                return False
        
        for i in range(0, len(s)-1):
            temp0 = int(s[:i+1])
            if backTracker0(temp0, i+1):
                return True
        else:
            return False
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        a = 0
        b = 0
        result = []
        part = ""
        sR = s[-1::-1]
        while b < len(s):
            b = len(s)-1 - sR.find(s[a])
            if b != a:
                while a <= b:
                    k = len(s)-1 - sR.find(s[a])
                    if k > b:
                        b = k
                    part += s[a]
                    a += 1
                    
            else:
                part += s[a]
                a += 1
                
            b += 1
            result.append(len(part))
            part = ""
        return result
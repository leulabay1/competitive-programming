class Solution:
    def compress(self, chars: List[str]) -> int:
        a = 0
        b = 1
        ctr1 = 0
        
        if len(chars) <= 1:
            return len(chars)
        while b < len(chars):
            
            if chars[a] == chars[b]:
                ctr = 1
                while b < len(chars) and chars[b] == chars[a]:
                    b+=1
                    ctr+=1
                s = chars[a]
                s = s + str(ctr)
                for i in s:
                    chars[ctr1] = i
                    ctr1 += 1    
                a = b
                b+=1
                if b == len(chars):
                    chars[ctr1] = chars[a]
                    ctr1 += 1
            else:
                chars[ctr1] = chars[a]
                a += 1
                b += 1
                ctr1 += 1
                if b == len(chars):
                    chars[ctr1] = chars[a]
                    ctr1 += 1
        chars = chars[0:ctr1]
        print(chars)
        return len(chars)
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            res = ""
            for i in range(len(s)):
                if s[i] == "0":
                    res += "1"
                else:
                    res += "0"
            return res
        def finder(n):
            if n == 1:
                return "0"
            s = finder(n-1)
            return s + "1" + invert(s)[::-1]
        res = finder(n)
        return res[k-1]
        
            
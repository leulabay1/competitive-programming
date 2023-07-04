class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        m = len(bin(n))-3
        for i in range(m):
            if ((1 << i) & n)<<1 == ((1 << (i + 1)) & n):
                return False
        else:
            return True
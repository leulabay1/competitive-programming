class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        else:
            size = 2**n-1
            if k < size//2 + 1:
                 return self.findKthBit(n-1,k)
            elif k > size//2 + 1:
                backsize = 2**(n-1) - 1
                gap = k - (size//2 + 1)
                value = int(self.findKthBit(n-1,backsize - gap + 1))
                value = 1 - value
                return str(value)
                
            return str(1)
                
        
            
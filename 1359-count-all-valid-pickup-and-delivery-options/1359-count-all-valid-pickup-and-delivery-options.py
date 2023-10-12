class Solution:
    def countOrders(self, n: int) -> int:
        
        count = 1
        
        for i in range(0, n):
            count = count * ((i + 1) * (2*i + 1))
            count %= (10**9 + 7)
        return count
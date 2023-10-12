class Solution:
    def countOrders(self, n: int) -> int:
        
        temp = 1
        
        for i in range(0, n):
            temp = temp * ((2*i + 2)*(2*i + 1)//2)
            temp %= (10**9 + 7)
        return temp
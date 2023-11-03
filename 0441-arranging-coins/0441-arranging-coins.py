class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left = 0
        right = n
        
        while left <= right:
            mid = (left + right)//2
            
            if ((mid + 1) * mid) // 2 <= n:
                
                left = mid + 1
                
            else:
                right = mid - 1
                
        return left - 1
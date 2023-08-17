class Solution:
    def climbStairs(self, n: int) -> int:
        prev0 = 0
        prev1 = 1
        for i in range(n):
            temp = prev1
            prev1 = prev0 + prev1
            prev0 = temp
        
        return prev1
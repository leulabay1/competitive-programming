class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        self.n = len(satisfaction)
        
        satisfaction.sort()
        
        @cache
        def solve(i,time):
            
            if i>=self.n:
                return 0

            op1 = satisfaction[i]*time+solve(i+1,time+1)

            op2 = solve(i+1,time)
            
            return max(op1,op2)
        
        return solve(0,1)
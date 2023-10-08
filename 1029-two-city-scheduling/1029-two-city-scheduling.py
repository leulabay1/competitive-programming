class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        res = 0
        diff = sorted(costs, key = lambda x: x[0] - x[1])
        
        for i in range(2*n):
            if i < n:
                res += diff[i][0]
            else:
                res += diff[i][1]
        return res 
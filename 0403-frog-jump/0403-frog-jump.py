class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        pos_set = set(stones)
        direction = [1, 0, -1]
        
        if stones[0] + 1 not in pos_set:
            return False
        
        def backT(pos, k):
            if (pos, k) in dp:
                return dp[(pos, k)]
            
            if pos == stones[-1]:
                return True
            if pos > stones[-1]:
                return False
            
            flag = False
            for dirc in direction:
                if k + dirc + pos > pos and k + dirc + pos in pos_set:
                    flag = flag or backT(k + dirc + pos, k + dirc)
            dp[(pos, k)] = flag
            return dp[(pos, k)]
        return backT(stones[0] + 1, 1)
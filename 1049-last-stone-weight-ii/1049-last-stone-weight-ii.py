class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def rec(a,b,index):
            if index<0:
                return abs(a-b)
            
            s = stones[index]
            return min( rec(a+s, b, index-1), 
                        rec(a,  b+s, index-1))
        
        return rec(0,0,len(stones)-1)
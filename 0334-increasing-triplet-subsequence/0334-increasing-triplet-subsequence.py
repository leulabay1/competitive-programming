class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        res = []
        
        for n in nums:
            index = bisect.bisect_left(res, n)
            
            if index == len(res):
                res.append(n)    
            else:
                res[index] = n
            if len(res) == 3:
                return True
            
        return False
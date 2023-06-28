class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x+y > y+x:
                return -1
            elif x+y < y+x:
                return 1
            else:
                return 0
        
        def cmp_to_key(cmp):
            
            class K:
                def __init__(self,obj):
                    self.obj = obj
                def __lt__(self,other):
                    return cmp(self.obj,other.obj) < 0
            return K
            
        
        sorted_nums = sorted(map(str,nums), key = cmp_to_key(compare))
        return "".join(sorted_nums) if sorted_nums[0] != "0" else "0"
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False
        
        
#         from fractions import gcd
#         vals = collections.Counter(deck).values()
#         return reduce(gcd, vals) >= 2
        
        # table = Counter(deck)
        # temp = min(table.values())
        # if len(deck) < 2 or temp <= 1:
        #     return False
        # for i in table.values():
        #     if i%temp != 0:
        #         return False
        # else:
        #     return True
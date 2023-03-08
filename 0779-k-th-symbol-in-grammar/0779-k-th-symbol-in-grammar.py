class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def kth(k, even):
            if k == 1:
                return 0
            else:
                even = True if k%2==0 else False
                num = kth(ceil(k/2), even)
                if even:
                    return 1-num
                else:
                    return num
                
        even = True if k%2==0 else False
        ans = kth(k, even)
        
        return ans
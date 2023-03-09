class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        fair = [0 for _ in range(k)]
        
        def backT(i, child):
            
            if i >= len(cookies):
                return max(child)
            
            noCh = child.count(0)
            rem = len(cookies) - i
            if noCh > rem:
                return float("inf")
            
            temp = float("inf")
            for j in range(k):
                child[j] += cookies[i]
                temp = min(temp, backT(i+1, child))
                child[j] -= cookies[i]
            return temp
                    
        cookies.sort(reverse=True)
        return backT(0, fair)
        
                
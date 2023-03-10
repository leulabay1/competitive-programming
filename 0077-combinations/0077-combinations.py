class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
            ans = []
            def backT(i, space):
                if len(space) == k:
                    minAns = space.copy()
                    ans.append(minAns)
                    return
                
                for j in range(i,n+1):
                    space.append(j)
                    backT(j+1,space)
                    space.pop()
            
            backT(1,[])
            return ans
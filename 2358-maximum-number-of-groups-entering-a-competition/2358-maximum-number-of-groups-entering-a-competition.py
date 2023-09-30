class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n=len(grades)
        t=0
        g=0
        count=2
        while(t<n):
            t+=count
            g+=1
            count+=1
        return g
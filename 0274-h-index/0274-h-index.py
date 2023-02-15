class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        h = 0
        NoOfP = len(citations)
        for i in citations:
            if i >= NoOfP:
                h = max(h, NoOfP)
            NoOfP-=1
            if h > NoOfP:
                break
                
        
        return h
            
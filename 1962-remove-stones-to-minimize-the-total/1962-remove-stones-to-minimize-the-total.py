class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-1*val for val in piles]
        heapq.heapify(piles)
        for i in range(k):
            stones = heapq.heappop(piles)
            heapq.heappush(piles, (1*stones+(-1*stones)//2))
        
        return -1*sum(piles)
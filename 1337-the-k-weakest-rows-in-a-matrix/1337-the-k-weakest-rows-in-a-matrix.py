class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        heapify(heap)
        
        for i, row in enumerate(mat):
            heapq.heappush(heap, (Counter(row)[1], i))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
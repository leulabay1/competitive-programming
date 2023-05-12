class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix = [deque(row) for row in matrix]
        heapq.heapify(matrix)
        for i in range(k-1):
            node = heapq.heappop(matrix)
            node.popleft()
            if node:
                heapq.heappush(matrix, node)
        return heapq.heappop(matrix).popleft()
    
        
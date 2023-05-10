class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = []
        heapq.heapify(temp)
        for stone in stones:
            heapq.heappush(temp, -1*stone)
            
        while len(temp) > 1:
            val1 = -1*heapq.heappop(temp)
            val2 = -1*heapq.heappop(temp)
            if val1 > val2:
                heapq.heappush(temp, val2 - val1)
        return -1*temp[0] if temp else 0
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        heap = []
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)
        use_count = {i: 0 for i in range(n)}

        for start, end in meetings:
            # clear out the rooms that are done being used
            while heap and heap[0][0] <= start:
                prev_end, idx = heapq.heappop(heap)
                heapq.heappush(available_rooms, idx)
            
            # if there is still no room available to use, we wait
            # for the next room to become available
            if not available_rooms:
                prev_end, idx = heapq.heappop(heap)
                new_end = end + (prev_end - start)
                heapq.heappush(heap, (new_end, idx))
                use_count[idx] += 1
            else:
                idx = heapq.heappop(available_rooms)
                heapq.heappush(heap, (end, idx))
                use_count[idx] += 1
        
        res_idx = 0
        res_count = 0

        for key in sorted(use_count.keys()):
            if use_count[key] > res_count:
                res_idx = key
                res_count = use_count[key]
        
        return res_idx
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        m, n = len(nums1), len(nums2)
        heap = [(nums1[0]+nums2[0],0,0)]
        visited = set((0,0))
        res = []
        k = min(k, m*n)
        while k > 0:
            pop = heapq.heappop(heap)
            res.append([nums1[pop[1]],nums2[pop[2]]])
            r, c = pop[1], pop[2]
            if r+1 < m and (r+1,c) not in visited:
                heapq.heappush(heap, (nums1[r+1]+nums2[c], r+1, c))
                visited.add((r+1,c))
            if c+1 < n and (r,c+1) not in visited:
                heapq.heappush(heap, (nums1[r]+nums2[c+1], r, c+1))
                visited.add((r,c+1))
            k -= 1
        return res
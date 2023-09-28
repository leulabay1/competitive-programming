class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0]) if R else 0
        ans = [] 
        if not R or not C:
            return ans
        def rank(row, col, price, dist):
            return (dist, price, row,col) # dist + row + col + price
        seen = set()
        q = deque([(start[0], start[1], 0)])
        while q:
            row, col, dist = q.popleft()
            if row < 0 or row >=R or col < 0 or col >= C or grid[row][col] == 0:
                continue
            if (row, col) in seen:
                continue
                
            seen.add((row, col))
            r = rank(row, col, grid[row][col], dist) 
            if pricing[0] <= grid[row][col] <= pricing[1]:
                
                heapq.heappush(ans, (r, (row, col))) 
            
            for dr, dc in ((0,1),(1,0),(-1,0),(0,-1)):
                q.append((row+dr, col+dc, dist+1))
        
        
        return [(x[0], x[1]) for _, x in heapq.nsmallest(k, ans)]
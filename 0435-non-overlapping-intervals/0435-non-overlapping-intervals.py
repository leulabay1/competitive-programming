class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = list(sorted(intervals, key = lambda interval: interval[1]))
        
        ans = 0
        k = float("-inf")
        for interval in intervals:
            if interval[0] >= k:
                k = interval[1]
            else:
                ans += 1
        return ans
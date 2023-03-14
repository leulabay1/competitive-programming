class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        inf = -1*float('inf')
        heights.append(inf)
        stack = []
        g_max = 0
        print(heights)
        for idx, height in enumerate(heights):
            while stack and stack[-1][-1] > height:
                poped = stack.pop()
                left = stack[-1][0] if stack else -1
                right = idx
                g_max = max(g_max, (right - left - 1)*poped[-1])
            stack.append([idx, height])
            
        return g_max
                
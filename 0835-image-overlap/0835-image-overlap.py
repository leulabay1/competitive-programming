class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        for i in range(-n+1, n):
            for j in range(-n+1, n):
                overlap = 0
                for x in range(max(0, i), min(n, n + i)):
                    for y in range(max(0, j), min(n, n + j)):
                        overlap += img1[x][y] & img2[x - i][y - j]
                max_overlap = max(max_overlap, overlap)

        return max_overlap
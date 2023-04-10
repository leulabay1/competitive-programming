class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat[0])
        n = len(mat)
        if r*c != n*m:
            return mat
        
        ans = [[0]*c for _ in range(r)]
        
        ro = col = 0
        for row in mat:
            for ele in row:
                ans[ro][col] = ele
                col += 1
                if col == c:
                    col = 0
                    ro += 1
        return ans
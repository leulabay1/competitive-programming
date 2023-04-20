class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in range(n // 2):
            for i in range(n - 2 * l - 1):
                rmin, rmax = l, n - l - 1 
                cmin, cmax = l, n - l - 1                
                matrix[rmin][cmin+i], matrix[rmin+i][cmax], matrix[rmax][cmax-i], matrix[rmax-i][cmin] = (
                    matrix[rmax-i][cmin], matrix[rmin][cmin+i], matrix[rmin+i][cmax], matrix[rmax][cmax-i])
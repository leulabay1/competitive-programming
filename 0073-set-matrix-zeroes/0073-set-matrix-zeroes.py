class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        columns = set()
        rows = set()
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    columns.add(col)
                    rows.add(row)
        for row in range(n):
            for col in range(m):
                if row in rows or col in columns:
                    matrix[row][col] = 0
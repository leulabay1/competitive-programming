class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def valid_checker(row, col):
            nonlocal n, m
            return 0 <= row <= n and 0 <= col <= m and board[row][col] == "O"
        
        def outbound_checker(row, col):
            nonlocal n, m
            for dirct in direction:
                if dirct[0] + row < 0 or dirct[0] + row > n or dirct[1] + col < 0 or dirct[1] + col > m:
                    return True
            else:
                return False
            
        def dfs(row, col, ret):
            nonlocal flag
            visited[row][col] = 1
            ret.append((row, col))
            if outbound_checker(row, col):
                flag = False
            for dirct in direction:
                new_row = row + dirct[0]
                new_col = col + dirct[1]
                if valid_checker(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(new_row, new_col, ret)
            return ret
        
        n, m = len(board)-1, len(board[0])-1
        visited = [[0]*(m+1) for _ in range(n+1)]
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        flag = True
        
        for i in range(n+1):
            for j in range(m+1):
                if board[i][j] == "O" and not visited[i][j]:
                    to_be_fliped = dfs(i, j, [])
                    if flag:
                        for x, y in to_be_fliped:
                            board[x][y] = "X"
                    flag = True
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0] * n for _ in range(m)]
        for i, j in walls:
            board[i][j] = 2
        for i, j in guards:
            board[i][j] = 2
        
        for i, j in guards:
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i + di, j + dj
                while 0 <= ni < m and 0 <= nj < n and board[ni][nj] != 2:
                    board[ni][nj] = 1
                    ni += di
                    nj += dj
        
        return sum(row.count(0) for row in board)

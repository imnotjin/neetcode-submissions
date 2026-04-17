class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def bfs(i, j):
            q = deque([(i, j)])
            board[i][j] = '*'

            while q:
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                        board[ni][nj] = '*'
                        q.append((ni, nj))

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    bfs(i, j)
        
        print(board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        


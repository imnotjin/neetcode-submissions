class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ones = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                state = grid[i][j]
                if state == 1:
                    ones += 1
                elif state == 2:
                    q.append((i, j))
        def rottable(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1
        res = 0
        while q and ones > 0:
            len_q = len(q)
            for _ in range(len_q):
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if rottable(ni, nj):
                        q.append((ni, nj))
                        grid[ni][nj] = 2
                        ones -= 1
            res += 1
        return res if ones == 0 else -1
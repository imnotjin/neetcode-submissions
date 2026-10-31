class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 2**31 - 1
        def reachable(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == INF
        q = deque([(i, j) for j in range(n) for i in range(m) if grid[i][j] == 0])
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if reachable(ni, nj):
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni,nj))

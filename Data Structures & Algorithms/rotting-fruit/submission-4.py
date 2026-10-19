class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ones = 0
        twos = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones += 1
                if grid[i][j] == 2:
                    twos += 1
                    q.append((i, j))
        
        time = 0
        while q and ones > 0:
            len_q = len(q)
            for _ in range(len_q):
                i, j = q.popleft()
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        q.append((ni, nj))
                        ones -= 1
                        grid[ni][nj] = 2
            time += 1
        print(ones)
        return time if ones == 0 else -1


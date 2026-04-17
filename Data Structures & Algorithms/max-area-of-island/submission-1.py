class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        area = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = 0
            local = 1

            while q:
                i, j = q.popleft()

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                        q.append((ni, nj))
                        grid[ni][nj] = 0
                        local += 1    
            return local
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = max(area, bfs(i, j))
        
        return area
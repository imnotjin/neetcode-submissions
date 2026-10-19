class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j]:
                return 0
            
            res = 0
            grid[i][j] = 0
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                res += dfs(i + di, j + dj)
            # grid[i][j] = 1

            return 1 + res
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        
        return res
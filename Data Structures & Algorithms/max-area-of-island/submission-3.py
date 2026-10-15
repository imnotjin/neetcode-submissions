class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j]:
                return 0
            grid[i][j] = 0
            return 1 + (
                dfs(i + 1, j) +
                dfs(i - 1, j) +
                dfs(i, j + 1) +
                dfs(i, j - 1)
            )

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res
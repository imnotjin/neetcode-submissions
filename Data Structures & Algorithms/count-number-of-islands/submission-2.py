class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "1":
                    grid[ni][nj] = "0"
                    dfs(ni, nj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    dfs(i, j)
                    count += 1
                # for line in grid:
                #     print(line)
                # print()
        
        return count

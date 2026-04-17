class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j - 1] + grid[0][j]

        for line in grid:
            print(line)

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        
        for line in grid:
            print(line)

        return grid[m - 1][n - 1]


        # dirs = [(0, 1), (-1, 0)]
        # v = set()
        # heap = [(grid[0][0], 0, 0)]
        # v.add((0, 0))

        # while heap:
        #     w, i, j = heapq.heappop(heap)

        #     if (i, j) == (m - 1, n - 1):
        #         return w
            
        #     for di, dj in dirs:
        #         ni, nj = i + di, j + dj
        #         if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in v:
        #             nw = w + grid[ni][nj]
        #             v.add((ni, nj))
        #             heapq.heappush(heap, (nw, ni, nj))
        
        

            

            

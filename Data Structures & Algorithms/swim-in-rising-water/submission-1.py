class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        while heap:
            t, i, j = heapq.heappop(heap)
            if (i, j) == (m - 1, n - 1):
                return t
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in v:
                    v.add((ni, nj))
                    heapq.heappush(heap, (max(t, grid[ni][nj]), ni, nj))
    
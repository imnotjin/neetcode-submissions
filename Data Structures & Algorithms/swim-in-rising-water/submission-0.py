from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)] #(max_so_far, i, j)
        v = set()
        v.add((0, 0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while min_heap:
            max_so_far, i, j = heappop(min_heap)

            if (i, j) == (m - 1, n - 1):
                return max_so_far

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if (
                    ni < 0 or ni >= m or 
                    nj < 0 or nj >= n or
                    (ni, nj) in v
                ):
                    continue
                
                new_max = max(max_so_far, grid[ni][nj])
                heappush(min_heap, (new_max, ni, nj))
                v.add((ni, nj))


            
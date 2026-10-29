class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        n = len(grid)
        while heap:
            best, i, j = heapq.heappop(heap)
            if i == n - 1 and j == n - 1:
                return best
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    heapq.heappush(
                        heap,
                        (
                            max(best, grid[ni][nj]),
                            ni, nj
                        )
                    )




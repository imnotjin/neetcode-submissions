class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        heap = [(0, 0, 0)] # (diff, i, j)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        v = set()

        while heap:
            diff, i, j = heapq.heappop(heap)

            if (i, j) in v:
                continue
            
            v.add((i, j))

            if (i, j) == (ROWS - 1, COLS - 1):
                return diff

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    ni < 0 or ni >= ROWS or
                    nj < 0 or nj >= COLS or
                    (ni, nj) in v
                ):
                    continue

                newDiff = max(diff, abs(heights[ni][nj] - heights[i][j]))
                heapq.heappush(heap, (newDiff, ni, nj))
        
        return 0

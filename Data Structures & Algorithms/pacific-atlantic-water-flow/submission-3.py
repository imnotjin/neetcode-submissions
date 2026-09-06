from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac_q, atl_q = deque(), deque()
        pv, av = set(), set()

        # Step 1: Add all border cells to respective queues and visited sets
        for r in range(ROWS):
            pac_q.append((r, 0))
            pv.add((r, 0))
            atl_q.append((r, COLS - 1))
            av.add((r, COLS - 1))

        for c in range(COLS):
            if (0, c) not in pv:
                pac_q.append((0, c))
                pv.add((0, c))
            if (ROWS - 1, c) not in av:
                atl_q.append((ROWS - 1, c))
                av.add((ROWS - 1, c))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Step 2: Helper BFS function
        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    # Water flows upstream: neighbor height must be >= current height
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        bfs(pac_q, pv)
        bfs(atl_q, av)

        # Step 3: Result is the intersection of cells reachable by both oceans
        return list(pv & av)
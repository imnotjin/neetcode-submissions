class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(starts):
            seen = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and 0 <= nc < n
                        and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]   # uphill or level
                    ):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen

        pacific = [(0, c) for c in range(n)] + [(r, 0) for r in range(1, m)]
        atlantic = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m - 1)]

        both = bfs(pacific) & bfs(atlantic)
        return [[r, c] for r, c in both]
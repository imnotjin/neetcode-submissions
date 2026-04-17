class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            pacific = False
            atlantic = False

            v = set()
            q = deque([(r, c)])
            v.add((r, c))

            while q:
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0:
                        pacific = True
                    if nr >= ROWS or nc >= COLS:
                        atlantic = True 
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in v and heights[nr][nc] <= heights[r][c]:
                        q.append((nr, nc))
                        v.add((nr, nc))

            return pacific and atlantic


        for r in range(ROWS):
            for c in range(COLS):
                if bfs(r, c):
                    ans.append([r, c])

        return ans
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        ans = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pacific_q = deque([])
        pacific_v = set()

        for i in range(m):
            pacific_q.append((i, -1))
            pacific_v.add((i, -1))
        for j in range(n):
            pacific_q.append((-1, j))
            pacific_v.add((-1, j))
        
        print(pacific_q)

        atlantic_q = deque([])
        atlantic_v = set()

        for i in range(m):
            atlantic_q.append((i, n))
            atlantic_v.add((i, n))
        for j in range(n):
            atlantic_q.append((m, j))
            atlantic_v.add((m, j))

        print(atlantic_q)

        def bfs(q, v):
            while q:
                i, j = q.popleft()

                if i < 0 or i >= m or j < 0 or j >= n:
                    curr_val = float('-inf')
                else:
                    curr_val = heights[i][j]

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < m and
                        0 <= nj < n and
                        curr_val <= heights[ni][nj] and
                        (ni, nj) not in v
                    ):
                        v.add((ni, nj))
                        q.append((ni, nj))

        bfs(pacific_q, pacific_v)
        bfs(atlantic_q, atlantic_v)

        return [[i, j] for i, j in pacific_v & atlantic_v if 0 <= i < m and 0 <= j < n]

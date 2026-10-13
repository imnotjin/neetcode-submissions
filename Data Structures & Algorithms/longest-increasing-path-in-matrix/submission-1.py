class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            best = 1
            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and matrix[i][j] > matrix[ni][nj]:
                    best = max(best, 1 + dfs(ni, nj))
            cache[(i, j)] = best
            return best
        
        res = float('-inf')
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j))
        
        return res

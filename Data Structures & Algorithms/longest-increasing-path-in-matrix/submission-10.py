class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def open(i, j):
            return 0 <= i < m and 0 <= j < n

        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if open(ni, nj) and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            dp[(i, j)] = res
            return res
        
        res = 0
        for i in range(m):
            for j in range(n):
               res = max(res, dfs(i, j))
        return res 

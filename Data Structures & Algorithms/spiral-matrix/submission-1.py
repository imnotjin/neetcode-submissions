class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        def dfs(rows, cols, i, j, di, dj):
            if rows == 0 or cols == 0:
                return
            
            for _ in range(cols):
                i += di
                j += dj
                ans.append(matrix[i][j])
            
            dfs(cols, rows - 1, i, j, dj, -di)

        dfs(len(matrix), len(matrix[0]), 0, -1, 0, 1)
        return ans
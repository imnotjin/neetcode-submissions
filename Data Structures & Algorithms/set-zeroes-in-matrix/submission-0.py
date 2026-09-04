class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])

        row_flag, col_flag = False, False

        for i in range(m):
            if not matrix[i][0]:
                row_flag = True
                break
        
        for j in range(n):
            if not matrix[0][j]:
                col_flag = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if row_flag:
            for i in range(m):
                matrix[i][0] = 0
        if col_flag:
            for j in range(n):
                matrix[0][j] = 0
        
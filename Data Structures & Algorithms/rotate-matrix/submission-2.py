class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # 00 01 1 2
        # 10 11 3 4

        # 00 10 1 3
        # 01 11 2 4

        # 10 00 3 1
        # 11 01 4 2

        for r in range(m):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in matrix:
            print(row)
        print()

        for r in range(m):
            for c in range(n // 2):
                matrix[r][c], matrix[r][n - c - 1] = matrix[r][n - c - 1], matrix[r][c]

        for row in matrix:
            print(row)


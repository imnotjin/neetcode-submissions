class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        matrix.reverse()

        for r in range(m):
            for c in range(r + 1, m):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        up, down = -1, m
        left, right = -1, n
        count = 0

        ans = []
        i, j = 0, 0
        while len(ans) < m * n:
            # go right
            while j < right:
                ans.append(matrix[i][j])
                j += 1
            j -= 1
            up += 1
            i = up + 1
            if i == down:
                break

            # go down
            while i < down:
                ans.append(matrix[i][j])
                i += 1
            i -= 1
            right -= 1
            j = right - 1
            if j == left:
                break

            # go left
            while j > left:
                ans.append(matrix[i][j])
                j -= 1
            j += 1
            down -= 1
            i = down - 1
            if i == up:
                break

            # go up
            while i > up:
                ans.append(matrix[i][j])
                i -= 1
            i += 1
            left += 1
            j = left + 1
            if j == right:
                break

        return ans

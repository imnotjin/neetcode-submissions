class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

    #     2 3 4 5 6
    # 1   3 6 10 15 21
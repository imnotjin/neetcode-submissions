class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        one, two = 1, 2
        for _ in range(2, n):
            res = one + two
            one = two
            two = res
        return res
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        one, two = 1, 1
        for _ in range(n - 1):
            one, two = one + two, one
        
        return one

class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        @cache
        def dp(i):
            if i <= 1:
                return 1
            
            return dp(i-2) + dp(i-1)
        return dp(n)
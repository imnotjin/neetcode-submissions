class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        @cache
        def dfs(i):
            if i <= 1:
                return 1
            return dfs(i - 1) + dfs(i - 2)
        return dfs(n)
        # prev, curr = 1, 1
        # for i in range(n):
        #     prev, curr = curr, prev + curr
        # return prev

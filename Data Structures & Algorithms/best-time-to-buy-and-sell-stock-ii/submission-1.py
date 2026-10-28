from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache
        def dfs(i, holding):
            if i == n:
                return 0

            skip = dfs(i + 1, holding)

            if holding:
                act = prices[i] + dfs(i + 1, False) # sell
            else:
                act = -prices[i] + dfs(i + 1, True) # buy

            return max(skip, act)

        return dfs(0, False)

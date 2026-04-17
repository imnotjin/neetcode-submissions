from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ans = 0
        @lru_cache(maxsize=None)
        def recurse(i, holding):
            if i >= len(prices):
                return 0

            if holding:
                sell = prices[i] + recurse(i + 2, False)
                hold = recurse(i + 1, True)
                return max(sell, hold)
            else:
                buy = -prices[i] + recurse(i + 1, True)
                skip = recurse(i + 1, False)
                return max(buy, skip)
        
        return recurse(0, False)

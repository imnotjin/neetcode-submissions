from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def recurse(i, holding):
            if (i, holding) in memo:
                return memo[(i, holding)]
            if i >= len(prices):
                return 0

            if holding:
                sell = prices[i] + recurse(i + 2, False)
                hold = recurse(i + 1, True)
                memo[(i, holding)] = max(sell, hold)
                return max(sell, hold)
            else:
                buy = -prices[i] + recurse(i + 1, True)
                skip = recurse(i + 1, False)
                memo[(i, holding)] = max(buy, skip)
                return max(buy, skip)
        
        return recurse(0, False)

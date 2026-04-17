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
                result = max(sell, hold)
            else:
                buy = -prices[i] + recurse(i + 1, True)
                skip = recurse(i + 1, False)
                result = max(buy, skip)
            
            memo[(i, holding)] = result
            return result
        
        return recurse(0, False)

from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dp(i, rem):
            if rem == 0:
                return 0
            if i == n or rem < 0:
                return float('inf')
            return min(
                dp(i + 1, rem),
                1 + dp(i, rem - coins[i])
            )
        res = dp(0, amount)
        return res if res != float('inf') else -1 
            
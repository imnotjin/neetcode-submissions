class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(target):
            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            min_coins = float("inf")
            for coin in coins:
                if target - coin >= 0:
                    min_coins = min(min_coins, 1 + dp(target - coin))
            memo[target] = min_coins
            return memo[target]
        
        return dp(amount) if dp(amount) != float("inf") else -1

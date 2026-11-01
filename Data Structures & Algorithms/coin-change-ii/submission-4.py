class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}

        def dfs(i, target):
            if target == 0:
                return 1
            if i == n:
                return 0
            if (i, target) in cache:
                return cache[(i, target)]

            res = dfs(i + 1, target)  # skip this coin
            if target - coins[i] >= 0:
                res += dfs(i, target - coins[i])  # use it again
            cache[(i, target)] = res
            return res

        return dfs(0, amount)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # stoneSum = sum(stones)
        # target = stoneSum // 2
        # dp = {}

        # def dfs(i, total):
        #     if total >= target or i == len(stones):
        #         return abs(total - (stoneSum - total))
        #     if (i, total) in dp:
        #         return dp[(i, total)]
            
        #     dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
        #     return dp[(i, total)]
        
        # return dfs(0, 0)

        stone_sum = sum(stones)
        target = stone_sum // 2
        n = len(stones)

        dp = [0] * (target + 1)
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        
        return stone_sum - 2 * dp[target]

        # dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # for i in range(1, n + 1):
        #     for t in range(target + 1):
        #         stone = stones[i - 1]
        #         if t >= stone:
        #             dp[i][t] = max(dp[i - 1][t], dp[i - 1][t - stone] + stone)
        #         else:
        #             dp[i][t] = dp[i - 1][t]
        
        # return stone_sum - 2 * dp[n][target]

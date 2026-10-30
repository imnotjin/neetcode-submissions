class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= n - 1:
                return 0
            
            res = float('inf')
            for j in range(1, nums[i] + 1):
                res = min(res, 1 + dfs(i + j))
            dp[i] = res
            return dp[i]

        return dfs(0)
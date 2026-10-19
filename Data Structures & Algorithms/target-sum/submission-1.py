from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i, total):
            # Base case: processed every number
            if i == n:
                return 1 if total == target else 0

            # Choose +nums[i] or -nums[i]
            add = dp(i + 1, total + nums[i])
            subtract = dp(i + 1, total - nums[i])

            return add + subtract

        return dp(0, 0)
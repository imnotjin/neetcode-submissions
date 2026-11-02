from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(i, total):
            if i == n:
                if total == target:
                    return 1
                return 0
            
            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])
            return add + sub
        
        return dfs(0, 0)

        # -2          2
        # -4 0        0 4
        # -6 -2 -2 2  -2 2 2 6
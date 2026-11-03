from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return nums[0]

            return max(dfs(i-2) + nums[i-1], dfs(i-1))
        return dfs(n)
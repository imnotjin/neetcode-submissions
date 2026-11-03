from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i, prev_i):
            if i == len(nums):
                return 0
            
            res = dfs(i + 1, prev_i)

            if prev_i == -1 or nums[i] > nums[prev_i]:
                res = max(res, 1 + dfs(i + 1, i))
            
            return res
        
        return dfs(0, -1)

from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        def rob_range(start, end):
            @cache
            def dp(i):
                if i > end:
                    return 0    
                skip = dp(i + 1)
                take = nums[i] + dp(i + 2)
                return max(skip, take)
            return dp(start)
        
        return max(rob_range(0, n-2), rob_range(1, n-1))
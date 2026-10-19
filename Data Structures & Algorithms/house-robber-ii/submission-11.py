class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_lin(houses):
            from functools import cache
            @cache
            def dp(i):
                if i <= 0:
                    return 0
                return max(dp(i-1), dp(i-2) + houses[i-1])

            return dp(len(houses))
        
        return max(
            rob_lin(nums[1:]),
            rob_lin(nums[:-1])
        )
        
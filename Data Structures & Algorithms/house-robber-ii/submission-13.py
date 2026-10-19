from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_range(start, end):
            @lru_cache(None)
            def dp(i):
                # Base case: no houses left
                if i > end:
                    return 0

                # Option 1: Skip current house
                skip = dp(i + 1)

                # Option 2: Rob current house
                take = nums[i] + dp(i + 2)

                return max(take, skip)

            return dp(start)

        return max(
            rob_range(0, n - 2),  # Exclude last house
            rob_range(1, n - 1)   # Exclude first house
        )
        
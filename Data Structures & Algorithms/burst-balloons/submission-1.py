class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        from functools import cache
        @cache
        def dp(l, r):
            res = 0
            for k in range(l + 1, r):
                left = dp(l, k)
                mid = nums[l] * nums[k] * nums[r]
                right = dp(k, r)
                res = max(res, left + mid + right)
            return res

        return dp(0, n - 1)

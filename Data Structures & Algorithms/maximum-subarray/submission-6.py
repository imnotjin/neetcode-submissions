class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = max(dp[0], nums[0])

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
        return max(dp)

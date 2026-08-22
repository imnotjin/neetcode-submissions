class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            prev_max = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    prev_max = max(prev_max, dp[j])
                    dp[i] = 1 + prev_max
        return max(dp)

        
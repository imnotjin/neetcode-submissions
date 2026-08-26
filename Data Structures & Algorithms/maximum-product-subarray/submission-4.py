class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return nums[0], nums[0]
            
            if i in memo:
                return memo[i]

            prev_max, prev_min = dp(i - 1)

            curr_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            curr_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)

            memo[i] = curr_max, curr_min
            return memo[i]
        
        return max(max(dp(i) for i in range(len(nums))))

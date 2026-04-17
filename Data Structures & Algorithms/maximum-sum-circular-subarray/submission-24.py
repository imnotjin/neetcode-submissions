class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf')

        local_max = float('-inf')
        local_min = float('inf')

        for num in nums:
            local_max = max(local_max + num, num)
            local_min = min(local_min + num, num)

            max_sum = max(max_sum, local_max)
            min_sum = min(min_sum, local_min)
        
        total = sum(nums)
        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)

            total += num
        
        print(min_sum)

        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)

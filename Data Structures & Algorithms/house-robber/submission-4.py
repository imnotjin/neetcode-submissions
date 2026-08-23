class Solution:
    def rob(self, nums: List[int]) -> int:
        # def solve(i):
        #     if i >= len(nums):
        #         return 0
            
        #     rob = nums[i] + solve(i + 2)
        #     skip = solve(i + 1)

        #     return max(rob, skip)

        # return solve(0)

        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def solve(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            rob = nums[i] + solve(i + 2)
            skip = solve(i + 1)

            cache[i] = max(rob, skip)
            return cache[i]

        return solve(0)

        # rob1, rob2 = 0, 0

        # for num in nums:
        #     temp = max(num + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        
        # return rob2

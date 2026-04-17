class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = []

        def dfs(i, jump):
            if i >= n:
                return
            if i == n - 1:
                jumps.append(jump)
                return
            
            for j in range(1, nums[i] + 1):
                dfs(i + j, jump + 1)

        dfs(0, 0)
        # print(jumps)
        return min(jumps)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ss = []
        s = []

        def dfs(start):
            ss.append(s[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                s.append(nums[i])
                dfs(i + 1)
                s.pop()
        dfs(0)
        return ss
        
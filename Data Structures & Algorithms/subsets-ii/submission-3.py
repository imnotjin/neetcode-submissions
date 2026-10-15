class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def dfs(start, path):
            res.append(path.copy())

            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()



        
        dfs(0, [])
        return res

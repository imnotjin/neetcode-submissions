class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, path, total):
            if i >= n or total > target:
                return
            if total == target:
                res.append(path[:])
                return
            
            # include (+ backtrack)
            path.append(nums[i])
            dfs(i, path, total + nums[i])
            path.pop()

            # exclude
            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return res

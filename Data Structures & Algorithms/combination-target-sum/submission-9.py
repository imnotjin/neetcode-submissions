class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return

            for j in range(i, n):
                if total + nums[j] > target:
                    return
                path.append(nums[j])
                dfs(j, path, total + nums[j])
                path.pop()

        dfs(0, [], 0)
        return res

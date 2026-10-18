class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        c = []
        nums.sort()

        def dfs(start, target):
            if target == 0:
                combs.append(c[:])
            
            for i in range(start, len(nums)):
                val = nums[i]
                if target - val < 0:
                    break
                c.append(val)
                dfs(i, target - val)
                c.pop()

        dfs(0, target)
        return combs

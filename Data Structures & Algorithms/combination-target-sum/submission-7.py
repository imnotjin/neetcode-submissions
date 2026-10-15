class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        comb = []
        n = len(nums)

        def dfs(start, total):
            if total == target:
                combs.append(comb[:])
            
            for i in range(start, n):
                if total + nums[i] > target:
                    continue
                comb.append(nums[i])
                dfs(i, total + nums[i])
                comb.pop()
        
        dfs(0, 0)
        return combs

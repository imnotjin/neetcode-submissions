class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        comb = []

        def backtrack(start, curr_sum):
            if curr_sum == 0:
                combs.append(comb[:])
                return
            if curr_sum < 0:
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i, curr_sum - nums[i])
                comb.pop()

        backtrack(0, target)
        return combs
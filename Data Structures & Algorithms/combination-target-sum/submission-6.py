class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        comb = []
        nums.sort()

        def backtrack(start, target):
            if target == 0:
                combs.append(comb[:])
            
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break

                comb.append(nums[i])
                backtrack(i, target - nums[i])
                comb.pop()
        backtrack(0, target)
        return combs

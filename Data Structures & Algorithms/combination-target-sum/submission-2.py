class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        combs = []
        comb = []

        def backtrack(start, remain):
            if remain < 0:
                return
            
            if remain == 0:
                combs.append(comb[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                    
                comb.append(nums[i])
                backtrack(i, remain - nums[i])
                comb.pop()

        backtrack(0, target)
        return combs

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        v = set()

        def backtrack(start):
            if sorted(subset) in subsets:
                return

            subsets.append(sorted(subset))

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return subsets

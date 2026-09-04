class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in comp:
                return [comp[target - num], i]
            comp[num] = i
        
        return []
        
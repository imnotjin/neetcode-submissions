class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)

        for i in range(1, 100001):
            if i not in s:
                return i
        
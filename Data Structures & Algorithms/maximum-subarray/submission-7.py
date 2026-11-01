class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curr = 0
        for num in nums:
            curr = max(curr + num, num)
            best = max(curr, best)
        return best


            
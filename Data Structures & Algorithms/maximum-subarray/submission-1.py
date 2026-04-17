class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        ans = float('-inf')
        for num in nums:
            curr = max(num, curr + num)
            ans = max(ans, curr)
        return ans

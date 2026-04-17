class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = float('-inf')
        g = float('-inf')
        
        for num in nums:
            l = max(l + num, num)
            g = max(l, g)
        
        return g
        
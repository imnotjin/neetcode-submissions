class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1] + nums[:-1], nums[1:] + [1]
        for i in range(1, n):
            left[i] *= left[i - 1]
        
        for i in range(n - 2, -1, -1):
            right[i] *= right[i + 1]

        return [l * r for l, r in zip(left, right)]
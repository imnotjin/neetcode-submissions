class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                idx = val - 1
                if nums[idx] > 0:
                    nums[idx] *= -1
                elif nums[idx] == 0:
                    nums[idx] = -(n + 1)

        for i in range(1, n + 1):
            if nums[i-1] >= 0:
                return i

        return n + 1
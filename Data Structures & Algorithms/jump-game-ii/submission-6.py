class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = res = 0
        while r < n - 1:
            most = 0
            for i in range(l, r + 1):
                most = max(most, i + nums[i])
            
            l = r + 1
            r = most
            res += 1
        return res
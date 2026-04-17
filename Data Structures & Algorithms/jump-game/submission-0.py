class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_reachable = n - 1
        
        for i in range(n-2, -1, -1):
            if nums[i] + i >= last_reachable:
                last_reachable = i
        
        return True if last_reachable == 0 else False

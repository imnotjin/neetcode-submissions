class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        for i, num in enumerate(nums):
            for j in range(i + 1, min(len(nums), i+k+1)):
                if num == nums[j]:
                    return True
        return False

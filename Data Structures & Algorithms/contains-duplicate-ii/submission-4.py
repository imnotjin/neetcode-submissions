class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        for i, num in enumerate(nums):
            for j in range(1, k+1):
                if i + j > len(nums) - 1:
                    break
                # print(num, nums[i+j])
                if num == nums[i+j]:
                    return True
        return False

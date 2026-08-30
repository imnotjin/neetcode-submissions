class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left is sorted
            if nums[mid] > nums[r]:
                # search in left
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # search in right
                else:
                    l = mid + 1
            
            # right is sorted
            else:
                # search in left
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                # search in right
                else:
                    r = mid - 1
        
        return -1

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            if nums.pop() in nums:
                return True
        
        return False
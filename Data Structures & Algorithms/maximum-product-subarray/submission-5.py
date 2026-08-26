class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = global_max = nums[0]
        
        for num in nums[1:]:
            # If negative, max and min swap potential
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
                
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            
            global_max = max(global_max, cur_max)
            
        return global_max
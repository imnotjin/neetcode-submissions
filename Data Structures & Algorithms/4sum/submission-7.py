class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, curr = [], []
        
        def k_sum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    c, d = nums[l], nums[r]
                    if c + d == target:
                        res.append(curr + [c, d])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif c + d < target:
                        l += 1
                    else:
                        r -= 1
                return
            
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                k_sum(k - 1, i + 1, target - nums[i])
                curr.pop()
        
        k_sum(4, 0, target)
        return res

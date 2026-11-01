class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(l, r, target):
            twos = []
            while l < r:
                cand = nums[l] + nums[r]
                if cand == target:
                    twos.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif cand < target:
                    l += 1
                else:
                    r -= 1
            return twos

        n = len(nums)
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            
            twos = twoSum(i + 1, n - 1, -a)
            for b, c in twos:
                res.append([a, b, c])
        
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        # sort
        nums.sort()

        def twoSum(start, target):
            pairs = []
            l, r = start, n - 1

            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    pairs.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1

            return pairs

        # loop
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two sum
            pairs = twoSum(i + 1, -nums[i])
            for a, b in pairs:
                res.append([nums[i], a, b])
        
        return res
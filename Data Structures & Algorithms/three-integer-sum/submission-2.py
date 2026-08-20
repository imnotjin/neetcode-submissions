class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, start, target):
            couples = []
            l, r = start, len(nums) - 1

            while l < r:
                add = nums[l] + nums[r]
                if add == target:
                    couples.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif add < target:
                    l += 1
                else:
                    r -= 1

            return couples

        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            
            couples = twoSum(nums, i + 1, -nums[i])
            for c in couples:
                ans.append([nums[i]] + c)
        
        return ans
            
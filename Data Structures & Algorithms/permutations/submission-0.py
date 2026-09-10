class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        perm = []
        v = set()

        def backtrack():
            if len(perm) == len(nums):
                perms.append(perm[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in v:
                    continue

                perm.append(nums[i])
                v.add(nums[i])
                backtrack()
                perm.pop()
                v.remove(nums[i])
        
        backtrack()
        return perms

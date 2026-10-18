class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pms = []
        pm = []
        v = set()

        def dfs():
            if len(pm) == len(nums):
                pms.append(pm[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in v:
                    continue
                v.add(nums[i])
                pm.append(nums[i])
                dfs()
                v.remove(nums[i])
                pm.pop()

        dfs()
        return pms
            
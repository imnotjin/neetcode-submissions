class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        n = len(nums)

        def dfs(path, seen):
            if len(path) == n:
                perms.append(path.copy())
                return
            
            for i in range(n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    path.append(nums[i])
                    dfs(path, seen)
                    path.pop()
                    seen.remove(nums[i])
        
        dfs([], set())
        return perms
    

"""
[]
1           2   3
12 13
123      



"""
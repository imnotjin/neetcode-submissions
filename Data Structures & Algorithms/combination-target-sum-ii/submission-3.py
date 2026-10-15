class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        n = len(candidates)
        candidates.sort()

        def dfs(start, total, path):
            if total == target:
                combs.append(path.copy())
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    return
                path.append(candidates[i])
                dfs(i + 1, total + candidates[i], path)
                path.pop()
        
        dfs(0, 0, [])
        return combs

#         1 2 2 4 5 6 9
# 224569 

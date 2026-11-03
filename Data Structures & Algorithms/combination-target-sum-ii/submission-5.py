class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, total, path):
            if total == target:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    return

                path.append(candidates[i])
                dfs(i + 1, total + candidates[i], path)
                path.pop()
        
        dfs(0, 0, [])
        return res
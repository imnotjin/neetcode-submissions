class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        comb = []
        candidates.sort()

        def dfs(start, target):
            if target < 0:
                return
            if target == 0:
                combs.append(comb[:])
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                dfs(i + 1, target - candidates[i])
                comb.pop()
        
        dfs(0, target)
        return combs

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from functools import lru_cache
        @lru_cache
        def dfs(i, j, k):
            if k == len(s3) and (i < len(s1) or j < len(s2)):
                return False
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            use1 = use2 = False
            if i < len(s1) and s1[i] == s3[k]:
                use1 = dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                use2 = dfs(i, j + 1, k + 1)
            
            return use1 or use2

        return dfs(0, 0, 0)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i == m or j == n:
                return 0
            
            same = diff = 0
            if text1[i] == text2[j]:
                same = 1 + dfs(i + 1, j + 1)
            else:
                diff = max(dfs(i + 1, j), dfs(i, j + 1))
            cache[(i, j)] = same + diff
            return cache[(i, j)]
        
        return dfs(0, 0)

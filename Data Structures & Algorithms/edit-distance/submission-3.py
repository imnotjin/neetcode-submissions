from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @cache
        def dp(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            
            return 1 + min(
                dp(i + 1, j + 1),   # replace
                dp(i + 1, j),       # delete
                dp(i, j + 1)        # insert
            )
        
        return dp(0, 0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        from functools import cache
        @cache
        def dfs(i):
            if i == n:
                return True
            
            for w in wordDict:
                if s[i:i+len(w)] == w and dfs(i + len(w)):
                    return True

            return False
        
        return dfs(0)
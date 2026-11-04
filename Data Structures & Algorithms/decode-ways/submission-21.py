from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def dp(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            
            # one digit
            res = dp(i + 1)
            # two digit
            two = int(s[i:i+2])
            if i + 1 < n and 1 <= two <= 26:
                res += dp(i + 2)
            return res
        
        return dp(0)

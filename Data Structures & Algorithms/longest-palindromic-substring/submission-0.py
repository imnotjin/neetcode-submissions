class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i + 1)
            res = max(res, odd, even, key=len)

        return res
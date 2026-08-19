class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0

        def expand(l, r):
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(n):
            res1 = expand(i, i)
            res2 = expand(i, i + 1)

            res3 = max(res1, res2)

            if res3 > end - start + 1:
                start = i - (res3 - 1) // 2
                end = i + res3 // 2

        return s[start: end + 1]
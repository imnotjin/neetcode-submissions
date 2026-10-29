class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        ws = set()
        for r, c in enumerate(s):
            while c in ws:
                ws.remove(s[l])
                l += 1
            ws.add(c)
            res = max(res, r - l + 1)
        return res
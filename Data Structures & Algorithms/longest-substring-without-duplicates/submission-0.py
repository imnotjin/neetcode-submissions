class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = 0
        ans = 0
        for r, c in enumerate(s):
            while c in unique:
                unique.remove(s[l])
                l += 1
            
            unique.add(c)
            ans = max(ans, r - l + 1)
        return ans

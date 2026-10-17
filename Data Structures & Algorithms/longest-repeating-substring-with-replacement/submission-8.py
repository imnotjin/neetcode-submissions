class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_count = 0
        count = defaultdict(int)
        res = 0

        for r, c in enumerate(s):
            count[c] += 1
            max_count = max(max_count, count[c])

            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res    
            
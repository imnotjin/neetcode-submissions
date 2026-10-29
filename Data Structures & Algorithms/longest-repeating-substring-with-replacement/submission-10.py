class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most = 0
        window = defaultdict(int)
        res = 0
        l = 0
        for r, c in enumerate(s):
            window[c] += 1
            most = max(most, window[c])

            while (r - l + 1) - most > k:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # to_replace = window_length - max_count
        max_count = 0
        freq = defaultdict(int)
        ans = 0

        l = 0
        for r, c in enumerate(s):
            freq[c] += 1
            max_count = max(max_count, freq[c])

            while (r - l + 1) - max_count > k:
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans

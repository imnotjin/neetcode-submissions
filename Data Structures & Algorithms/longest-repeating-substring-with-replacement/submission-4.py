class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        max_freq, max_len = 0, 0
        
        for r, c in enumerate(s):
            freq[c] += 1        
            max_freq = max(max_freq, freq[c])
            curr_k = (r - l + 1) - max_freq

            if curr_k > k:
                freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, (r - l + 1))

        return max_len

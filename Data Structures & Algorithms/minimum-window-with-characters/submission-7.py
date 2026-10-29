class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_w = defaultdict(int)

        required = len(count_t)
        curr = 0

        l = 0
        min_start = 0
        min_len = float('inf')
        for r, c in enumerate(s):
            count_w[c] += 1

            if c in count_t and count_w[c] == count_t[c]:
                curr += 1
            
            while l <= r and curr == required:
                ch = s[l]
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_start = l

                count_w[ch] -= 1
                l += 1
                if count_w[ch] < count_t[ch]:
                    curr -= 1
            
        return "" if min_len == float('inf') else s[min_start: min_start + min_len]

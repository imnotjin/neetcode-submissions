class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = None
        min_len = float('inf')
        count = Counter(t)
        window = defaultdict(int)

        required = len(count)
        formed = 0

        l = 0
        for r, c in enumerate(s):
            window[c] += 1
            if c in count and window[c] == count[c]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                window[char] -= 1
                if char in count and window[char] < count[char]:
                    formed -= 1
                
                l += 1

        return "" if min_len == float('inf') else s[start: start + min_len]
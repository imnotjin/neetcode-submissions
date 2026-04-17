class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        window_f = defaultdict(int)
        l = 0

        for r, c in enumerate(s2):
            window_f[c] += 1

            if (r - l + 1) == len(s1):
                if count == window_f:
                    return True
                window_f[s2[l]] -= 1
                if window_f[s2[l]] == 0:
                    del window_f[s2[l]]
                l += 1

        return False

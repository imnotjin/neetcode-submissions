class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count = Counter(s1)
        window = defaultdict(int)
        for r, c in enumerate(s2):
            window[c] += 1
            print(window, count)
            if (r - l + 1) == len(s1):
                if window == count:
                    return True
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
        return False


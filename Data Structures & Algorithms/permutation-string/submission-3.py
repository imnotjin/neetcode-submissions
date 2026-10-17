class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        window = defaultdict(int)

        l = 0
        for r, c in enumerate(s2):
            window[c] += 1
            if (r - l + 1) == len(s1):
                if count == window:
                    return True
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
    
        return False

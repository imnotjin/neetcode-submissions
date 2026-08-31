class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        w_count = defaultdict(int)

        required = len(t_count)
        formed = 0
        ans = float("inf"), None, None

        l = 0
        for r, c in enumerate(s):
            w_count[c] += 1
            if c in t_count and w_count[c] == t_count[c]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                
                w_count[char] -= 1
                if char in t_count and w_count[char] < t_count[char]:
                    formed -= 1
                
                l += 1
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

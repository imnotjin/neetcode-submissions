class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        ans = 0
        n = len(s)
        def dfs(i):
            nonlocal ans
            if i >= n:
                ans += 1
                return
            if s[i] != '0':
                dfs(i + 1)
                if i <= n - 2 and s[i:i + 2] <= '26': 
                    dfs(i + 2)
            
        dfs(0)
        return ans

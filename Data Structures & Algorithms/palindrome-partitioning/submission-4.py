class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

        def dfs(start, path):
            if start == n:
                res.append(path[:])
            
            for end in range(start, n):
                string = s[start:end+1]
                if dp[start][end]:
                    path.append(string)
                    dfs(end + 1, path)
                    path.pop()
        
        dfs(0, [])
        return res

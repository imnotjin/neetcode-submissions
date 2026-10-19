class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                length = j - i + 1
                if s[i] == s[j]:
                    if length <= 2:
                        dp[i][j] = j - i + 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = dp[i+1][j-1] + 2
        
        max_len = 0
        start = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    start = i
        return s[start:start+max_len]

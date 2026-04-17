class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}        
        def dfs(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if k == len(s3):
                return i == len(s1) and j == len(s2)
            # if i == len(s1):
            #     return dfs(i, j + 1, k + 1)
            # if j == len(s2):
            #     return dfs(i + 1, j, k + 1)

            if i < len(s1) and s3[k] == s1[i]:
                res_one = dfs(i + 1, j, k + 1) 
            else:
                res_one = False

            if j < len(s2) and s3[k] == s2[j]:
                res_two = dfs(i, j + 1, k + 1) 
            else:
                res_two = False

            res = res_one or res_two
            memo[(i, j, k)] = res

            return res

        return dfs(0, 0, 0)

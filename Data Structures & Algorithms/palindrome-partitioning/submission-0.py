class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
            
            for end in range(start, len(s)):
                string = s[start : end + 1]
                if string == string[::-1]:
                    path.append(string)
                    dfs(end + 1, path)
                    path.pop()
        
        dfs(0, [])
        return res

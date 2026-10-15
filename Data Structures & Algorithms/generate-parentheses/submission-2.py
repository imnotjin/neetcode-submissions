class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(op, cl, path):
            if op == cl == n:
                res.append("".join(path))
                return
            
            if op < n:
                path.append('(')
                dfs(op + 1, cl, path)
                path.pop()
            if cl < op:
                path.append(')')
                dfs(op, cl + 1, path)
                path.pop()

        dfs(0, 0, [])
        return res


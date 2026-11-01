class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(op, cl):
            if op == cl == n:
                res.append(''.join(stack))
            
            if op < n:
                stack.append('(')
                dfs(op + 1, cl)
                stack.pop()

            if cl < op:
                stack.append(')')
                dfs(op, cl + 1)
                stack.pop()

        dfs(0, 0)
        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack = []
        res = []

        def bt(open_c, closed_c, stack):
            if open_c == closed_c == n:
                res.append("".join(stack))
                return
            
            if open_c < n:
                stack.append("(")
                bt(open_c + 1, closed_c, stack)
                stack.pop()
            if closed_c < open_c:
                stack.append(')')
                bt(open_c, closed_c + 1, stack)
                stack.pop()
        
        bt(0, 0, [])
        return res
        
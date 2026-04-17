class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        flag = False
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                rightmost = stack.pop()
                if rightmost == abs(ast):
                    flag = True
                    break
                if rightmost > abs(ast):
                    ast = rightmost
                # ast = max(rightmost, abs(ast))

            if not flag:
                stack.append(ast)
            flag = False

        
        return stack

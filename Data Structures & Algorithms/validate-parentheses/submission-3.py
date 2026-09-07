class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if stack and c in hashmap:
                # print(stack[-1], hashmap[c])
                if stack.pop() != hashmap[c]:
                    return False
                continue
            stack.append(c)

        return True if not stack else False

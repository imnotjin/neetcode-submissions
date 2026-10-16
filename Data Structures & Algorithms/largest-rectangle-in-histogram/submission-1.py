class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                res = max(res, height * (i - index))
            stack.append((start, h))
        
        return res

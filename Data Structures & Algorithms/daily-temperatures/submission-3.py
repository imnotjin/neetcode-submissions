class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, _ = stack.pop()
                res[idx] = i - idx
            stack.append((i, t))
        
        return res

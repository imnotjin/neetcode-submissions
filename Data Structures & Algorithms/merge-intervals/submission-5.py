class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in intervals:
            if merged and merged[-1][1] >= i[0]:
                merged[-1][1] = max(merged[-1][1], i[1])
                # print(merged)
            else:
                merged.append(i)
        return merged
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = merged[-1]
            start2, end2 = intervals[i]
            if start2 <= end:
                merged.pop()
                merged.append([start, max(end, end2)])
            else:
                merged.append(intervals[i])

        return merged

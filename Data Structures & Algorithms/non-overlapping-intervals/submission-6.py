class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last_end = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= last_end:
                last_end = end
            else:
                res += 1
                last_end = min(last_end, end)
        return res
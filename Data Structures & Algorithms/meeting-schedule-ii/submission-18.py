"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []
        for i in intervals:
            start,end = i.start, i.end
            if min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return len(min_heap)
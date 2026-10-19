from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []
        
    def addNum(self, num: int) -> None:
        l, r = self.l, self.r
        heappush(l, -num)
        heappush(r, -heappop(l))
        if len(r) > len(l):
            heappush(l, -heappop(r))

    def findMedian(self) -> float:
        l, r = self.l, self.r
        if len(l) == len(r):
            return (-l[0] + r[0]) / 2.0
        else:
            return -l[0] / 1.0
        
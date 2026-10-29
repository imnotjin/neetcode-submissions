from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        heappush(self.left, -num)
        heappush(self.right, -heappop(self.left))
        if len(self.right) - len(self.left) > 1:
            heappush(self.left, -heappop(self.right))
        
    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        if total % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return self.right[0]
        
        
class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_max, -heapq.heappushpop(self.right_min, num))

        if len(self.left_max) > 1 + len(self.right_min):
            heapq.heappush(self.right_min, -heapq.heappop(self.left_max))


    def findMedian(self) -> float:
        if len(self.left_max) > len(self.right_min):
            return float(-self.left_max[0])
        return (-self.left_max[0] + self.right_min[0]) / 2.0
        
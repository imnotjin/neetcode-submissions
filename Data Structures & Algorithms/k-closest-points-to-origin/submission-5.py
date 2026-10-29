class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            heapq.heappush(max_heap, (-(x*x + y*y), (x, y)))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [[b[0], b[1]] for a, b in max_heap]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a, b = -heapq.heappop(heap), -heapq.heappop(heap)
            if a - b:
                heapq.heappush(heap, b - a)
        
        return -heap[0] if heap else 0

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        from heapq import heappush, heappop
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]
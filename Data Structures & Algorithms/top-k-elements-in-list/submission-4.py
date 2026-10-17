class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        for num, c in Counter(nums).items():
            heapq.heappush(min_heap, (c, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for _,num in min_heap]

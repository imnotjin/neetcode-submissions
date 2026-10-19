class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        count = Counter(nums)
        for num in count:
            heapq.heappush(min_heap, (count[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [x for _,x in min_heap]

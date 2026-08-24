class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        # max_heap = [(-freq[n], n) for n in freq]
        # heapq.heapify(max_heap)

        # return [heapq.heappop(max_heap)[1] for i in range(k)]

        min_heap = []
        for n in freq:
            heapq.heappush(min_heap, (freq[n], n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [heapq.heappop(min_heap)[1] for i in range(k)]
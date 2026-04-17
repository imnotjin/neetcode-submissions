class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])
        min_heap = []
        curr_pass = 0
        print(trips)
        for num_pass, frm, to in trips:
            while min_heap and min_heap[0][0] <= frm:
                curr_pass -= min_heap[0][2]
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, (to, frm, num_pass))
            curr_pass += num_pass
            print(curr_pass)
            if curr_pass > capacity:
                return False
        
        return True

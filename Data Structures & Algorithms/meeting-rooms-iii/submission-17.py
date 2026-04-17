class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        meeting_heap = []
        available_heap = [i for i in range(n)]
        rooms_count = [0] * n

        for start, end in meetings:
            while meeting_heap and meeting_heap[0][0] <= start:
                end2, room2 = heapq.heappop(meeting_heap)
                heapq.heappush(available_heap, room2)

            if not available_heap:
                earliest_end, room_num = heapq.heappop(meeting_heap)
                heapq.heappush(available_heap, room_num)
                # delay
                end += earliest_end - start

            room = heapq.heappop(available_heap)
            heapq.heappush(meeting_heap, (end, room))
            rooms_count[room] += 1
        
        ans = 0
        most = float('-inf')

        for i, count in enumerate(rooms_count):
            if count > most:
                most = count
                ans = i

        return ans
            
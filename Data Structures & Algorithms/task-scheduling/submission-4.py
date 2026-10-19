class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [-freq for freq in Counter(tasks).values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0
        while max_heap or cooldown:
            time += 1
            if not max_heap:
                time = cooldown[0][1]
            else:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq:
                    cooldown.append((freq, time + n))
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])
        return time

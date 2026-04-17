class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)
        cd_q = deque([])
        time = 0

        while max_heap or cd_q:
            time += 1
            if max_heap:
                freq = -heapq.heappop(max_heap)
                freq -= 1
                if freq > 0:
                    cd_q.append((freq, time + n))
            if cd_q and cd_q[0][1] == time:
                heapq.heappush(max_heap, -cd_q.popleft()[0])

        return time

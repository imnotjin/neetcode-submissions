class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        times = {k: 0}
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if time > times[node]:
                continue
                
            for nei, nei_time in adj[node]:
                new_time = time + nei_time
                if new_time < times.get(nei, float('inf')):
                    times[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))

        return max(times.values()) if len(times) == n else -1

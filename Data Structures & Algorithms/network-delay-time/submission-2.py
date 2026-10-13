from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        pq = [(0, k)]
        time = {k: 0}

        while pq:
            t, u = heappop(pq)
            if t > time[u]:
                continue
            
            for v, w in graph[u]:
                nt = t + w
                if nt < time.get(v, float('inf')):
                    time[v] = nt
                    heappush(pq, (nt, v))

        return max(time.values()) if len(time) == n else -1

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = []

        adj = defaultdict(list)
        for source, dest, price in flights:
            adj[source].append((dest, price))
        
        q = deque([(src, 0, 0, set([src]))]) # (airport, stops, total, path)

        while q:
            print(q)
            airport, stops, total, path = q.popleft()

            if airport == dst:
                if stops <= k:
                    ans.append(total)
            elif airport != src:
                stops += 1

            for nei, price in adj[airport]:
                if nei not in path:
                    q.append((nei, stops, total + price, path | {nei}))
        
        return min(ans) if ans else -1

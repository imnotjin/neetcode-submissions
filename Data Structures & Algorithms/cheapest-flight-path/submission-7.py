class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()
            for u, v, p in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u] + p < temp[v]:
                    temp[v] = prices[u] + p
            prices = temp

        return -1 if prices[dst] == float("inf") else prices[dst]
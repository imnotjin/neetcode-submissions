class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        n = len(projects)

        available = []
        idx = 0

        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(available, -projects[idx][1])
                idx += 1
            
            if not available:
                break
            
            max_profit = -heapq.heappop(available)
            w += max_profit
        
        return w
        
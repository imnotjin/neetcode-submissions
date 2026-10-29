class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            adj[u].append(v)
        
        res = []
        def dfs(u):
            while adj[u]:
                dfs(adj[u].pop())
            res.append(u)
        dfs("JFK")
        return res[::-1]
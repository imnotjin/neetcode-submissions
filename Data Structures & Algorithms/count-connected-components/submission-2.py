class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        v = set()

        def dfs(node):
            for nei in adj[node]:
                if nei not in v:
                    v.add(nei)
                    dfs(nei)
        res = 0        
        for node in range(n):
            if node not in v:
                v.add(node)
                dfs(node)
                res += 1
        
        return res


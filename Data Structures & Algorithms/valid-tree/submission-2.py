class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set([0])
        q = deque([0])

        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return len(visited) == n

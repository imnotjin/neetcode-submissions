class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # one root
        # all nodes reachable (no cycles)
        if len(edges) != n - 1:
            return False

        adj = {node: [] for node in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        v = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)

        return len(v) == n

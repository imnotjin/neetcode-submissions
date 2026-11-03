from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(start):
            q = deque([start])
            visited.add(start)
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1

        return res
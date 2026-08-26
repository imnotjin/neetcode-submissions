class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        q = deque([0])

        while q:
            node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            count += 1

            for nei in adj[node]:
                if nei not in visited:
                    q.append(nei)
        
        return count == len(adj)

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            indegrees = [0] * (k + 1)
            adj = defaultdict(list)

            for u, v in edges:
                adj[u].append(v)
                indegrees[v] += 1
        
            order = []
            q = deque([i for i in range(1, k + 1) if not indegrees[i]])
            while q:
                v = q.popleft()
                order.append(v)

                for nei in adj[v]:
                    indegrees[nei] -= 1
                    if not indegrees[nei]:
                        q.append(nei)
            
            return order

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if len(row_order) != k or len(col_order) != k:
            return []
        
        col_pos = {val: idx for idx, val in enumerate(col_order)}
        ans = [[0] * k for _ in range(k)]

        for row, val in enumerate(row_order):
            col = col_pos[val]
            ans[row][col] = val
        print(col_pos)
        

        return ans
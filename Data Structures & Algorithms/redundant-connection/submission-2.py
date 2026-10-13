class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            rep_a, rep_b = find(a), find(b)
            if rep_a == rep_b:
                return False
            parent[rep_a] = rep_b
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return edges[-1]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = list(range(len(edges) + 1))

        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(a, b):
            rep_a, rep_b = find(a), find(b)
            if rep_a == rep_b:
                return False
            rep[rep_a] = rep_b
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return edges[-1]

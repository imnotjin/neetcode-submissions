class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)

        def dist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(points[i], points[j]), i, j))

        uf = UnionFind(n)
        edges.sort()
        res = 0
        count = 0
        for w, u, v in edges:
            if uf.union(u, v):
                res += w
                count += 1
                if count == n - 1:
                    break
        
        return res


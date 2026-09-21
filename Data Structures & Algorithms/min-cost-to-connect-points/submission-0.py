class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1] * size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)

        if rep_x != rep_y:
            if self.sizes[rep_x] > self.sizes[rep_y]:
                self.parents[rep_y] = rep_x
                self.sizes[rep_x] += self.sizes[rep_y]
            else:
                self.parents[rep_x] = rep_y
                self.sizes[rep_y] += self.sizes[rep_x]
            return True
        
        return False
        
    def get_size(self, x):
        return self.sizes[self.find(x)]

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def man_dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((man_dist(i, j), i, j))
        edges.sort()

        uf = UnionFind(n)
        total = 0
        used = 0

        for w, u, v in edges:
            if uf.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    break
        
        return total

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        self.parent[p1] = p2
        self.size[p2] += self.size[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        e_acc = {}
        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                if e in e_acc:
                    uf.union(i, e_acc[e])
                else:
                    e_acc[e] = i
        # print(e_acc)
        # print()

        e_group = defaultdict(list)
        for e, i in e_acc.items():
            rep = uf.find(i)
            e_group[rep].append(e)
        # print(e_group)
        # print()

        res = []
        for i, emails in e_group.items():
            res.append([accounts[i][0]] + sorted(emails))
        return res





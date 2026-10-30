class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        rset, cset, dset, adset = set(), set(), set(), set()
        def dfs(r, path):
            if r == n:
                sol = []
                for c in path:
                    qrow = '.' * c + 'Q' + '.' * (n - 1 - c)
                    sol.append(qrow)
                res.append(sol)
                return
            
            for c in range(n):
                if (
                    r in rset or
                    c in cset or
                    r + c in dset or
                    r - c in adset
                ):
                    continue
                rset.add(r)
                cset.add(c)
                dset.add(r + c)
                adset.add(r - c)
                path.append(c)

                dfs(r + 1, path)

                rset.remove(r)
                cset.remove(c)
                dset.remove(r + c)
                adset.remove(r - c)
                path.pop()
        
        dfs(0, [])
        return res


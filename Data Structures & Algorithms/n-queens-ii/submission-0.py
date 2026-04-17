class Solution:
    def totalNQueens(self, n: int) -> int:
        cset = set()
        dset = set()
        adset = set()
        ans = 0


        def backtrack(r):
            nonlocal ans
            if r == n:
                ans += 1
            
            for c in range(n):
                d = r - c
                ad = r + c
                if c not in cset and d not in dset and ad not in adset:
                    cset.add(c)
                    dset.add(d)
                    adset.add(ad)

                    backtrack(r + 1)

                    cset.remove(c)
                    dset.remove(d)
                    adset.remove(ad)

        backtrack(0)
        return ans

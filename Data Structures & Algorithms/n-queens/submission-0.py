class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cset, dset, adset = set(), set(), set()
        board = [-1] * n
        ans = []

        def bt(r):
            if r == n:
                sol = []
                for row in range(n):
                    row_str = ['.'] * n
                    row_str[board[row]] = 'Q'
                    sol.append(''.join(row_str))
                ans.append(sol)
                return
            
            for c in range(n):
                d = r - c
                ad = r + c
                if (
                    c not in cset and
                    d not in dset and
                    ad not in adset
                ):
                    board[r] = c
                    cset.add(c)
                    dset.add(d)
                    adset.add(ad)

                    bt(r + 1)

                    cset.remove(c)
                    dset.remove(d)
                    adset.remove(ad)
        
        bt(0)
        return ans

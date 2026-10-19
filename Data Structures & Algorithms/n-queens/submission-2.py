class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        r_set = set()
        c_set = set()
        d_set = set()
        ad_set = set()

        def dfs(row, path):
            if row == n:
                q_list = []
                for col in path:
                    q_str = '.' * col + 'Q' + '.' * (n - col - 1)
                    q_list.append(q_str)
                res.append(q_list)
                return
    
            for col in range(n):
                if row in r_set or col in c_set or row-col in d_set or row+col in ad_set:
                    continue
                r_set.add(row)
                c_set.add(col)
                d_set.add(row-col)
                ad_set.add(row+col)
                path.append(col)
                dfs(row + 1, path)
                r_set.remove(row)
                c_set.remove(col)
                d_set.remove(row-col)
                ad_set.remove(row+col)
                path.pop()

        dfs(0, [])
        return res

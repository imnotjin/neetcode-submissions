class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rset = [set() for _ in range(9)]
        cset = [set() for _ in range(9)]
        sset = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]
                if num == ".":
                    continue

                if num in rset[r] or num in cset[c] or num in sset[r//3][c//3]:
                    return False
                
                rset[r].add(num)
                cset[c].add(num)
                sset[r//3][c//3].add(num)
        
        return True

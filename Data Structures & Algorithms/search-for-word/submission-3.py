class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, offset):
            if offset == len(word):
                return True
            
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or 
                board[i][j] != word[offset] or
                board[i][j] == '#'):
                return False
            
            board[i][j] = '#'

            res = (dfs(i + 1, j, offset + 1) or 
                dfs(i - 1, j, offset + 1) or
                dfs(i, j + 1, offset + 1) or
                dfs(i, j - 1, offset + 1))
            
            board[i][j] = word[offset]

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
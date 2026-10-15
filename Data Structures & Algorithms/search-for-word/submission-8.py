class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, k, seen):
            if k == len(word):
                return True

            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and board[ni][nj] == word[k]:
                    seen.add((ni, nj))
                    if dfs(ni, nj, k + 1, seen):
                        return True
                    seen.remove((ni, nj))
            
            return False

        
        return any(
            board[i][j] == word[0] and dfs(i, j, 1, {(i, j)})
            for i in range(m) for j in range(n)
        )

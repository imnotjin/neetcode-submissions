class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = word
        
        def dfs(i, j, node):
            c = board[i][j]
            if c not in node.children:
                return
            nxt = node.children[c]
            
            if nxt.is_word:
                res.append(nxt.is_word)
                nxt.is_word = None
            
            board[i][j] = '#'
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, nxt)
            board[i][j] = c

            if not nxt.children:
                del node.children[c]

        res = []
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res
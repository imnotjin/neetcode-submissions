class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.children['@'] = w

        m, n = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            curr_node = node.children[char]
            matched_word = curr_node.children.pop('@', None)
            if matched_word:
                res.append(matched_word)

            board[r][c] = '#'  # mark visited
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)
            board[r][c] = char  # restore

            if not curr_node:
                parent_node.children.pop(char)

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)

        return list(res)


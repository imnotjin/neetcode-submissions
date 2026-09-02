class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node['@'] = w
        
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []

        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node[char]

            matched_word = curr_node.pop('@', None)
            if matched_word:
                res.append(matched_word)
            
            board[r][c] = '#'
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in curr_node:
                    dfs(nr, nc, curr_node)
            board[r][c] = char

            if not curr_node:
                parent_node.pop(char)

        for r in range(m):
            for c in range(n):
                if board[r][c] in root:
                    dfs(r, c, root)
        
        return res

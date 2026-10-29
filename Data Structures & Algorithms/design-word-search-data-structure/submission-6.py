class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_word

            ch = word[i]
            if ch == '.':
                for nei in node.children.values():
                    if dfs(i + 1, nei):
                        return True
                return False
            elif ch not in node.children:
                return False
            else:
                return dfs(i + 1, node.children[ch])

        return dfs(0, self.root)


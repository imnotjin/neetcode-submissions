class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        node = self.trie.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.isWord
            
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            elif c not in node.children:
                return False
            else:
                return dfs(i + 1, node.children[c])
            
        return dfs(0, self.trie.root)
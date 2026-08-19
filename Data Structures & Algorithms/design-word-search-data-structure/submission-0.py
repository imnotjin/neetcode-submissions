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
        def dfs(index, node):
            if index == len(word):
                return node.isWord
            
            c = word[index]
            if c == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(index + 1, node.children[c])

        return dfs(0, self.trie.root)
    

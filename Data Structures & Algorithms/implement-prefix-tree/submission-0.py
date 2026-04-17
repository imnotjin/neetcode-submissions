class PrefixTree:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = self.Node()
            node = node.children[c]
        node.is_word = True
            
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            if not self.is_sorted(word1, word2, order_map):
                return False
        
        return True
    
    def is_sorted(self, word1, word2, order_map):
        for i in range(min(len(word1), len(word2))):
            if order_map[word1[i]] < order_map[word2[i]]:
                return True
            elif order_map[word1[i]] > order_map[word2[i]]:
                return False
        
        return len(word1) <= len(word2)
